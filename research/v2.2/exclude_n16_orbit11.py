"""Independent exact finite exclusion of n16 marked 3x3 orbit #11.

Representative: ((1,1,2),(1,1,2),(2,2,4)), cyclic row=2,
cyclic column=2. Both cyclic 8-vertex components have three local
cell sizes (2,2,4) and mandated complete collectors (2,2,0).

We enumerate every *admissible* connected unicyclic 8-contact history
using a last-two-contact structural decomposition, NOT the v2.1
optimistic envelope. Every such history with FOUR final distinct full
collectors must have (i) two tree components after six calls,
(ii) two disjoint cross-tree final contacts, and (iii) exactly two
complete collectors in each of the pre-six-call trees. Their final
internal calls join these respective collectors.

An independent side-tree exhaustive DFS, with all collector branch
requirements, constructs complete B/D profile sets. The cell coverage
constraint is exact. Successful check proves the two exact cyclic
profile domains cannot communicate the third group's secrets.
"""
from functools import lru_cache
from itertools import combinations,permutations
from pathlib import Path

N=8
FULL=(1<<N)-1
COLLECTORS=(0,1,2,3)
GROUPS=((0,1),(2,3),(4,5,6,7))

@lru_cache(None)
def side_histories(side,pair):
    members=tuple(i for i in range(N) if side>>i&1)
    a,b=pair
    assert a in members and b in members
    h=len(members)
    assert h>=2
    other_edges=tuple(e for e in combinations(members,2) if e!=(a,b))
    states=set()
    for before in permutations(other_edges,h-2):
        parent=list(range(N))
        def root(v):
            while parent[v]!=v:v=parent[v]
            return v
        valid=True
        for u,v in before:
            x,y=root(u),root(v)
            if x==y:valid=False;break
            parent[x]=y
        if not valid or root(a)==root(b):continue
        # The pre-last-contact forest is made of two trees and last
        # edge a-b is its only bridge, so this is a connected tree.
        k=[1<<v for v in range(N)]
        for u,v in before:
            k[u]=k[v]=k[u]|k[v]
        k[a]=k[b]=k[a]|k[b]
        if k[a]!=side:continue
        states.add(tuple(k[v] for v in members))
    return tuple(sorted(states))

def profile(knowledge):
    B=[];D=[]
    for cells in GROUPS:
        b=0
        for subset in range(1<<len(cells)):
            union=0
            for j,v in enumerate(cells):
                if subset>>j&1:union|=knowledge[v]
            if union==FULL:b|=1<<subset
        d=0
        for secret in range(N):
            mask=0
            for j,v in enumerate(cells):
                if knowledge[v]>>secret&1:mask|=1<<j
            d|=1<<mask
        B.append(b);D.append(d)
    return tuple(B),tuple(D)

def exact_profiles():
    B,D=set(),set()
    terminal=0
    for other_collector in (1,2,3):
        for extra in range(1<<4):
            side=(1<<0)|(1<<other_collector)|(extra<<4)
            other=FULL^side
            left=tuple(i for i in COLLECTORS if side>>i&1)
            right=tuple(i for i in COLLECTORS if other>>i&1)
            assert len(left)==len(right)==2
            LM=tuple(i for i in range(N) if side>>i&1)
            RM=tuple(i for i in range(N) if other>>i&1)
            for l in side_histories(side,left):
                for r in side_histories(other,right):
                    k=[0]*N
                    for v,x in zip(LM,l):k[v]=x
                    for v,x in zip(RM,r):k[v]=x
                    # Two choices of crossing perfect matching between
                    # the four prescribed full collectors. Their order
                    # does not alter the midpoint final knowledge.
                    for flip in (0,1):
                        state=k.copy()
                        for j in range(2):
                            a,b=left[j],right[j^flip]
                            state[a]=state[b]=state[a]|state[b]
                        assert all(state[c]==FULL for c in COLLECTORS)
                        suff,anc=profile(state)
                        # Cellwise union coverage is mandatory for all
                        # three local groups, particularly the four
                        # remaining vertices.
                        if not all(s & (1<<((1<<len(g))-1))
                                   for s,g in zip(suff,GROUPS)):
                            continue
                        B.add(suff);D.add(anc);terminal+=1
    return B,D,terminal

def main():
    B,D,n=exact_profiles()
    assert (B,D,n)==({(14,14,32768)},{(8,8,278)},144),(B,D,n)
    # The first two suffix cells have at least one full collector
    # each; the third (size-four) intersection cannot jointly
    # broadcast ALL secrets from the prefix cyclic row:
    assert all((b[2]&d[2])!=d[2] for b in B for d in D)
    print("PASS orbit 11: exact four-collector unicyclic eight-vertex"
          " local B domains",B,"D domains",D,"terminal pairs",n)
    print("PASS local mutual incompatibility: B[2] & D[2] != D[2]")
    print("PASS global n16 orbit 11 excluded by a necessary cell"
          " profile condition, independent of optimistic domains")
    print("LIMIT: orbit 10 remains RELAXED_SAT; no n16 general theorem.")

if __name__=="__main__":main()
