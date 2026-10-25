"""Deterministic validation: exhaustive K3/K4 frontier soundness and LP gap.
Run: python verify_v05.py. Python 3.10+, scipy, numpy.
"""
import itertools,random
import numpy as np
from scipy.optimize import linprog
from frontier_solver_v05 import is_connected,complete_edges,separate,solve
from baseline_time_expanded_milp import exact_milp


def independent_tc(n,seq,mask):
    origins=[1<<i for i in range(n)]
    for j,(u,v) in enumerate(seq):
        if mask>>j&1:
            a,b=origins[u],origins[v]
            origins[u]=origins[v]=a|b
    return all(z==(1<<n)-1 for z in origins)


def cut_properties_exhaustive():
    total=0
    for n in [3,4]:
        edges=complete_edges(n);m=len(edges)
        for seq in itertools.permutations(edges):
            for mask in range(1<<m):
                assert is_connected(n,seq,mask)==independent_tc(n,seq,mask)
                if is_connected(n,seq,mask):continue
                cuts=separate(n,seq,mask)
                assert cuts
                for c in cuts:
                    assert c&mask==0
                    for sup in range(1<<m):
                        if sup&mask==mask and sup&c==0:
                            assert not independent_tc(n,seq,sup)
                total+=1
        print('PASS exhaustive K'+str(n)+' schedules',flush=True)
    return total


def lp_gap_k4():
    seq=((0,1),(2,3),(0,2),(1,3),(0,3),(1,2))
    n,m=4,len(seq)
    cuts=set()
    for mask in range(1<<m):
        if not independent_tc(n,seq,mask):
            cuts.update(separate(n,seq,mask))
    pairs=[c for c in cuts if c.bit_count()==2]
    assert len(pairs)==12
    assert all(sum((c>>j)&1 for c in pairs)==4 for j in range(m))
    assert all(c.bit_count()>=2 for c in cuts)
    assert len(cuts)==26
    A=np.array([[-((c>>j)&1) for j in range(m)] for c in cuts],dtype=float)
    res=linprog(np.ones(m),A_ub=A,b_ub=-np.ones(len(cuts)),bounds=(0,1),method='highs')
    assert res.success and abs(res.fun-3)<1e-8
    assert all(sum((c>>j)&1 for j in range(m))>=2 for c in cuts)
    target=min(i for i in range(m+1) if any(independent_tc(n,seq,mask) for mask in range(1<<m) if mask.bit_count()==i))
    assert target==4
    print('PASS complete temporal frontier cut relaxation K4: fractional=3, integral=4, all 26 cuts',flush=True)


def global_cut_validity():
    import random
    rng=random.Random(8)
    for n in (3,4,5):
        edges=complete_edges(n)
        seqs=list(itertools.permutations(edges)) if n<=4 else [rng.sample(edges,len(edges)) for _ in range(50)]
        for seq in seqs:
            m=len(seq)
            connected=[x for x in range(1<<m) if independent_tc(n,seq,x)]
            for H in range(1<<m):
                if independent_tc(n,seq,H):continue
                for C in separate(n,seq,H):
                    assert all(X&C for X in connected), (n,seq,H,C)
        print('PASS unconditional global cut validity K'+str(n)+' schedules='+str(len(seqs)),flush=True)


def compare_exact_solvers():
    seqs=[(4,[(0,1),(0,2),(0,3),(1,3),(1,2),(2,3)]),
          (5,[(0,1),(0,2),(0,3),(0,4),(1,2),(1,4),(1,3),(2,4),(2,3),(3,4)]),
          (6,[(0,5),(0,4),(4,5),(0,3),(1,2),(1,3),(1,5),(3,4),(0,2),(1,4),(2,5),(2,4),(2,3),(0,1),(3,5)])]
    for n,seq in seqs:
        f=solve(n,seq,time_limit=10)
        b=exact_milp(n,seq,time_limit=10)
        assert f['status']=='PROVED_OPTIMUM' and b['status']==0
        assert f['best_size']==b['size']
        print('PASS exact solvers, K'+str(n)+':',f['best_size'],'edges',flush=True)

if __name__=='__main__':
    count=cut_properties_exhaustive();global_cut_validity();lp_gap_k4();compare_exact_solvers()
    print('ALL TESTS PASS; disconnected candidate-subgraph cases:',count)
