"""Independent witness verifier for temporal K6 2-tree obstruction.

Run: python independent_verify.py. Python 3.10+, standard library only.
Enumerates 2-trees constructively (rather than via reverse-ear elimination),
checks temporal reachability separately for each source, and checks the minimum
retained edges and footprint treewidth by exhaustive enumeration.
"""
import itertools
from collections import Counter

N=6
TIMELINE = [(3,5),(0,5),(4,5),(0,2),(1,3),(2,3),(0,3),(1,2),(1,5),(0,4),(0,1),(2,5),(3,4),(2,4),(1,4)]
assert set(map(tuple,map(sorted,TIMELINE))) == set(itertools.combinations(range(N),2))
EDGES=list(itertools.combinations(range(N),2))
TIDX={e:i for i,e in enumerate(EDGES)}

def connected(mask):
    """Source-by-source earliest-arrival model."""
    for src in range(N):
        reachable={src}
        for a,b in TIMELINE:
            if not ((mask>>TIDX[tuple(sorted((a,b)))])&1):
                continue
            if a in reachable or b in reachable:
                reachable.add(a)
                reachable.add(b)
        if len(reachable)<N:return False
    return True

def constructive_two_trees(n):
    """All labelled 2-trees by starting on any triangle and adding vertices to an existing edge."""
    out=set()
    for init in itertools.combinations(range(n),3):
        base={tuple(sorted(x)) for x in itertools.combinations(init,2)}
        remaining=tuple(v for v in range(n) if v not in init)
        for order in itertools.permutations(remaining):
            states={frozenset(base)}
            for v in order:
                next_states=set()
                for state in states:
                    for a,b in state:
                        next_states.add(state|{tuple(sorted((v,a))),tuple(sorted((v,b)))})
                states=next_states
            for state in states:
                mask=sum(1<<TIDX[e] for e in state)
                out.add(mask)
    return out

def exact_treewidth(mask):
    nbr0=[0]*N
    for i,(a,b) in enumerate(EDGES):
        if mask>>i&1:
            nbr0[a]|=1<<b
            nbr0[b]|=1<<a
    best=N
    for order in itertools.permutations(range(N)):
        nbr=nbr0[:];live=(1<<N)-1; width=0
        for v in order:
            nei=nbr[v]&live&~(1<<v)
            width=max(width,nei.bit_count())
            if width>=best:break
            for u in range(N):
                if nei>>u&1:
                    nbr[u]|=(nei&~(1<<u))
            live^=1<<v
        else:
            best=min(best,width)
    return best

def main():
    trees=constructive_two_trees(N)
    assert len(trees)==1215, len(trees)
    hits=[m for m in trees if connected(m)]
    assert hits==[], f'Found an unexpected 2-tree spanner: {hits[:1]}'
    min_size=None; witness=None
    for size in range(0,16):
        for combo in itertools.combinations(range(len(EDGES)),size):
            mask=sum(1<<i for i in combo)
            if connected(mask):
                min_size=size;witness=mask;break
        if witness is not None:break
    assert min_size==8
    tw=exact_treewidth(witness)
    assert tw==3, (tw,witness)
    print('PASS 1215 distinct labelled 2-trees; none is a temporal spanner')
    print('PASS exact minimum temporal spanner size: 8')
    print('PASS verified eight-edge witness with treewidth exactly: ',tw)
    print('WITNESS edges (times):', [(i+1,e) for i,e in enumerate(TIMELINE) if witness>>TIDX[tuple(sorted(e))]&1])
    print('WITNESS mask:',witness)

if __name__=='__main__': main()
