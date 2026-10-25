"""Exact incident-local chronological gossip MILP.

Binary variables only for retained edges; all information-flow state variables
are continuous in [0,1], yet become 0/1 automatically when edges are integral.
No other project solver imported. scipy>=1.9 required.
"""
from __future__ import annotations
import itertools
import time
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import coo_matrix


def complete_chronology(n, events):
    seq = [tuple(sorted(e)) for e in events]
    assert len(seq) == n * (n - 1) // 2
    assert set(seq) == set(itertools.combinations(range(n), 2))
    return seq


def check(n, events, selected):
    """Independent bitset temporal gossip verifier."""
    knowledge = [1 << v for v in range(n)]
    for t,(u,v) in enumerate(events):
        if t in selected:
            w=knowledge[u]|knowledge[v]
            knowledge[u]=knowledge[v]=w
    return all(x==(1<<n)-1 for x in knowledge)


def build(n, events, upper=None):
    seq=complete_chronology(n, events)
    m=len(seq)
    # Incident-local states q[s,v,r] after r incident events of v.
    def q(s,v,r):return m + s * n * n + v * n + r
    nv=m+n**3
    low=np.zeros(nv);high=np.ones(nv)
    integ=np.zeros(nv,dtype=np.int32);integ[:m]=1
    for s in range(n):
        for v in range(n):
            low[q(s,v,0)]=high[q(s,v,0)]=float(s==v)
            low[q(s,v,n-1)]=high[q(s,v,n-1)]=1.0
    rows=[]; cols=[]; vals=[]; lbs=[];ubs=[]
    def row(coeffs,lower=-np.inf,upper=np.inf):
        rid=len(lbs)
        for j,c in coeffs.items():
            if c: rows.append(rid);cols.append(j);vals.append(float(c))
        lbs.append(lower);ubs.append(upper)
    incident=[0]*n
    for t,(u,v) in enumerate(seq):
        ru=incident[u];rv=incident[v]
        for s in range(n):
            p=q(s,u,ru);z=q(s,v,rv)
            a=q(s,u,ru+1);b=q(s,v,rv+1)
            # a = p OR (x_t AND z); b = z OR (x_t AND p)
            row({a:1,p:-1},lower=0)
            row({a:1,z:-1,t:-1},lower=-1)
            row({a:1,p:-1,t:-1},upper=0)
            row({a:1,p:-1,z:-1},upper=0)
            row({b:1,z:-1},lower=0)
            row({b:1,p:-1,t:-1},lower=-1)
            row({b:1,z:-1,t:-1},upper=0)
            row({b:1,z:-1,p:-1},upper=0)
        incident[u]+=1;incident[v]+=1
    assert incident==[n-1]*n
    if upper is not None:
        row({t:1 for t in range(m)},upper=upper)
    A=coo_matrix((vals,(rows,cols)),shape=(len(lbs),nv)).tocsr()
    objective=np.zeros(nv);objective[:m]=1.0
    return objective,integ,Bounds(low,high),LinearConstraint(A,np.array(lbs),np.array(ubs))


def solve(n,events,upper=None,seconds=30):
    seq=complete_chronology(n,events)
    c,integrality,bounds,constraints=build(n,seq,upper)
    tick=time.monotonic()
    result=milp(c,integrality=integrality,bounds=bounds,constraints=constraints,
                options={'time_limit':float(seconds),'mip_rel_gap':0.0})
    output={'n':n,'time_sec':round(time.monotonic()-tick,4),'solver_status':int(result.status),
            'status':'UNKNOWN','selected_1based':None,'cardinality':None,
            'variables':len(c),'binary_variables':n*(n-1)//2,
            'constraints':len(constraints.lb),'message':str(result.message)}
    if result.x is not None:
        chosen=[j for j in range(len(seq)) if result.x[j]>.5]
        if not check(n,seq,set(chosen)):
            output['status']='INVALID_SOLVER_WITNESS'
            return output
        output['selected_1based']=[j+1 for j in chosen]
        output['cardinality']=len(chosen)
        output['status']='OPTIMAL' if result.status==0 else 'FEASIBLE_UNCERTIFIED'
    elif result.status==2:
        output['status']='INFEASIBLE_SOLVER_CERTIFIED'
    return output

if __name__=='__main__':
    import argparse,json,random
    p=argparse.ArgumentParser();p.add_argument('--n',type=int,default=6)
    p.add_argument('--seed',type=int,default=1);p.add_argument('--upper',type=int,default=None)
    p.add_argument('--seconds',type=float,default=20)
    a=p.parse_args()
    seq=list(itertools.combinations(range(a.n),2));random.Random(a.seed).shuffle(seq)
    print(json.dumps(solve(a.n,seq,a.upper,a.seconds),indent=2))
