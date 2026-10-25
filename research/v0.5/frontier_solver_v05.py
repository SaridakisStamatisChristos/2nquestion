"""Global chronological-frontier cuts for minimum temporal clique spanners.

Exact when MILP returns a certified optimal feasible solution or a certified infeasibility.
Unknown solver limits remain UNKNOWN; never treat as mathematical disproof.
"""
from __future__ import annotations
import itertools,random,time
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix


def complete_edges(n): return list(itertools.combinations(range(n), 2))

def propagation(n,seq, mask):
    state=[1<<s for s in range(n)]
    for j,(u,v) in enumerate(seq):
        if (mask >> j)&1:
            t=state[u]|state[v];state[u]=state[v]=t
    return state

def is_connected(n,seq,mask):
    full=(1<<n)-1
    return all(x==full for x in propagation(n,seq,mask))

def temporal_frontier(n,seq,mask,s):
    """Cut: every valid superset of 'mask' must choose some edge from frontier.

    Frontier is defined using REACHABILITY under mask immediately before event j.
    """
    r=1<<s; cut=0
    for j,(u,v) in enumerate(seq):
        a=(r>>u)&1;b=(r>>v)&1
        if a ^ b:
            if (mask>>j)&1:
                r|=(1<<u)|(1<<v)
            else:
                cut|=1<<j
    assert r!=(1<<n)-1, 'only call for an infeasible source'
    assert cut !=0
    assert (cut & mask)==0
    return cut

def separate(n,seq,mask,both_directions=True):
    out=[]
    for reverse in ([False,True] if both_directions else [False]):
        events=seq[::-1] if reverse else seq
        xmask=int(f'{mask:0{len(seq)}b}'[::-1],2) if reverse else mask
        # encode reverse cut original indices
        for s in range(n):
            r=1<<s
            for j,(u,v) in enumerate(events):
                if ((xmask>>j)&1) and (((r>>u)&1) or ((r>>v)&1)):
                    r|=1<<u|1<<v
            if r==(1<<n)-1:continue
            cut=temporal_frontier(n,events,xmask,s)
            if reverse:
                y=0
                for j in range(len(seq)):
                    if (cut>>j)&1:y|=1<<(len(seq)-1-j)
                cut=y
            out.append(cut)
    return sorted(set(out),key=int.bit_count)

def solve(n,seq,upper=None,time_limit=15,max_rounds=90,verbose=False):
    m=len(seq);start=time.monotonic(); constraints=[];known=set(); rounds=0
    best=None;status='UNKNOWN'; last_result=None
    # all vertices must have some incident edge; basic static connectivity necessary
    for v in range(n):
        c=sum(1<<j for j,(u,w) in enumerate(seq) if u==v or w==v)
        constraints.append(c);known.add(c)
    while rounds<max_rounds:
        left=time_limit-(time.monotonic()-start)
        if left<=0:break
        A=lil_matrix((len(constraints),m),dtype=float)
        for i,c in enumerate(constraints):
            j=0
            while c:
                lsb=c&-c; j=lsb.bit_length()-1
                A[i,j]=1; c-=lsb
        cc=np.ones(m)
        lo=np.ones(len(constraints));hi=np.full(len(constraints),np.inf)
        if upper is not None:
            row=np.ones((1,m))
            from scipy.sparse import vstack,csr_matrix
            A=vstack([A.tocsr(),csr_matrix(row)])
            lo=np.r_[lo,-np.inf];hi=np.r_[hi,upper]
        res=milp(cc,integrality=np.ones(m),bounds=Bounds(np.zeros(m),np.ones(m)),constraints=LinearConstraint(A.tocsr(),lo,hi),options={'time_limit':min(left,5.0),'mip_rel_gap':0.0})
        last_result=res
        if res.x is None:
            if res.status==2:status='PROVED_INFEASIBLE';break
            status='UNKNOWN_MILP_LIMIT';break
        mask=sum((1<<j) for j in range(m) if res.x[j]>.5)
        rounds+=1
        if is_connected(n,seq,mask):
            best=mask
            if res.status==0:
                status='PROVED_OPTIMUM_UNDER_BOUND' if upper is not None else 'PROVED_OPTIMUM'
            else:
                status='FEASIBLE_NOT_CERTIFIED'
            break
        cuts=separate(n,seq,mask)
        fresh=[c for c in cuts if c not in known]
        if not fresh:
            status='BUG_NO_NEW_CUT';break
        for c in fresh:constraints.append(c);known.add(c)
        if verbose:print('round',rounds,'candidate_size',mask.bit_count(),'added',len(fresh),'constraints',len(constraints),flush=True)
    return {'n':n,'m':m,'status':status,'rounds':rounds,'constraints':len(constraints),
            'elapsed_sec':round(time.monotonic()-start,3),
            'best_size':best.bit_count() if best is not None else None,
            'mask':best, 'solver_status':None if last_result is None else last_result.status}

if __name__=='__main__':
    # Exhaustive semantic testing of cuts for K4 and random instances K5.
    for n in (3,4):
        for seq in itertools.permutations(complete_edges(n)):
            m=len(seq)
            for mask in range(1<<m):
                if is_connected(n,seq,mask):continue
                cuts=separate(n,seq,mask)
                if not cuts:raise AssertionError((n,seq,mask))
                for c in cuts:
                    # If ANY valid superset lacks a cut edge, the cut is invalid.
                    for ext in range(1<<m):
                        if ext&mask == mask and (ext&c)==0:
                            assert not is_connected(n,seq,ext),(n,seq,mask,c,ext)
        print('exhaustive frontier soundness',n, 'PASSED',flush=True)
    rng=random.Random(20261025)
    for n in (5,6,7,8,9):
        seq=complete_edges(n);rng.shuffle(seq)
        print(solve(n,seq,time_limit=12,verbose=False),flush=True)
