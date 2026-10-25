"""Exact temporal gossip propagation and MILP minimum spanner solver for injectively labelled cliques."""
from __future__ import annotations
from itertools import combinations
import random, time
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix


def edges_complete(n):
    return list(combinations(range(n),2))

def temporal_reach(n, sequence, mask=None):
    """Return each vertex's bitmask of origins it learned, scanning strictly increasing events."""
    info = [1<<i for i in range(n)]
    if mask is None: mask=(1<<len(sequence))-1
    for i,(u,v) in enumerate(sequence):
        if mask>>i & 1:
            combined=info[u]|info[v]
            info[u]=combined
            info[v]=combined
    return info

def is_spanner(n, seq, mask=None):
    return all(z==(1<<n)-1 for z in temporal_reach(n,seq,mask))

def greedy(n,seq,seed=0):
    rng=random.Random(seed)
    order=list(range(len(seq)))
    rng.shuffle(order)
    mask=(1<<len(seq))-1
    for i in order:
        mask0=mask & ~(1<<i)
        if is_spanner(n,seq,mask0):mask=mask0
    return mask

def exact_milp(n, seq, time_limit=15, k_bound=None):
    """MILP exact boolean reachability encoding. Only optimal when status==0."""
    m=len(seq)
    # state r_{s,v,i}, after processing first i events
    total=m+n*n*(m+1)
    def r(s,v,i):return m+(s*n+v)*(m+1)+i
    lb=np.zeros(total);ub=np.ones(total); integ=np.ones(total,int)
    c=np.zeros(total);c[:m]=1
    for s in range(n):
        for v in range(n):
            lb[r(s,v,0)]=ub[r(s,v,0)]=int(s==v)
            lb[r(s,v,m)]=ub[r(s,v,m)]=1
    rows=[];cols=[];vals=[];lower=[];upper=[]
    def cons(terms,lo=-np.inf,hi=np.inf):
        j=len(lower)
        for idx,co in terms:
            rows.append(j);cols.append(idx);vals.append(co)
        lower.append(lo);upper.append(hi)
    if k_bound is not None: cons([(i,1) for i in range(m)],hi=k_bound)
    for i,(u,v) in enumerate(seq):
        for s in range(n):
            for z in range(n):
                if z!=u and z!=v:
                    cons([(r(s,z,i+1),1),(r(s,z,i),-1)],0,0)
            for a,b in [(u,v),(v,u)]:
                before=r(s,a,i);other=r(s,b,i);after=r(s,a,i+1)
                # after == before OR (x_i AND other)
                cons([(after,1),(before,-1)],0)
                cons([(after,1),(i,-1),(other,-1)],-1)
                cons([(after,1),(before,-1),(i,-1)],hi=0)
                cons([(after,1),(before,-1),(other,-1)],hi=0)
    M=coo_matrix((vals,(rows,cols)),shape=(len(lower),total)).tocsr()
    t=time.perf_counter()
    res=milp(c,integrality=integ,bounds=Bounds(lb,ub),constraints=LinearConstraint(M,lower,upper),options={"time_limit":time_limit})
    elapsed=time.perf_counter()-t
    ans={"n":n,"m":m,"time":round(elapsed,3),"status":res.status,"message":res.message,"best_bound":getattr(res,'mip_dual_bound',None),"gap":getattr(res,'mip_gap',None)}
    if res.x is not None:
        picked=[i for i in range(m) if res.x[i]>0.5]
        mask=sum(1<<i for i in picked)
        assert is_spanner(n,seq,mask), 'MILP encoding or solver invalid'
        ans.update(size=len(picked),indices=picked,mask=mask)
    return ans

if __name__=='__main__':
    for n in range(3,9):
        seq=edges_complete(n)
        random.Random(n+440).shuffle(seq)
        print('n',n,'greedy',min(greedy(n,seq,j).bit_count() for j in range(30)),end=' ',flush=True)
        print(exact_milp(n,seq,time_limit=20))
