"""Exact local eight-vertex TWO-COLLECTOR TREE oracle for n16 orbit #10.

For M=((1,1,2),(1,1,2),(2,2,4)), cyclic row=column=0,
the large prefix tree row2 and the large suffix tree col2 both have
cell group sizes (2,2,4) and require the two vertices of the MIDDLE
cell to be complete collectors.

A tree's final call is between those two collectors. Removing it gives
two disjoint side trees. Full cellwise coverage by the *first* group,
which has exactly two vertices, forces one such vertex into each side
and forces both to be completely informed about their respective
side's secrets BEFORE the final edge. The last internal edge in each
side joins this group0 collector to the group1 collector.

A valid chronology also requires the four group2 vertices collectively
to cover all eight secrets. The search below exhausts all two-side
partitions satisfying the obvious necessary coverage, and enumerates
ALL side-tree chronological distinct-edge sequences on up to five
vertices, including their orders, without the C++ optimistic shortcut.
"""
from functools import lru_cache
from itertools import combinations,permutations

N=8
FULL=(1<<N)-1
GROUPS=((0,1),(2,3),(4,5,6,7))

@lru_cache(None)
def side_states(side,root,group0_collector):
    vertices=tuple(v for v in range(N) if side>>v&1)
    h=len(vertices)
    assert h>=3
    edges=tuple(combinations(vertices,2))
    states=set()
    for contacts in permutations(edges,h-1):
        parent=list(range(N))
        def root_of(v):
            while parent[v]!=v:v=parent[v]
            return v
        valid=True
        for u,v in contacts:
            a,b=root_of(u),root_of(v)
            if a==b:
                valid=False
                break
            parent[a]=b
        if not valid:continue
        knowledge=[1<<v for v in range(N)]
        for u,v in contacts:
            knowledge[u]=knowledge[v]=knowledge[u]|knowledge[v]
        if knowledge[root]!=side or knowledge[group0_collector]!=side:continue
        states.add(tuple(knowledge[v] for v in vertices))
    return tuple(sorted(states))

def profile(knowledge):
    B,D=[],[]
    for group in GROUPS:
        b=0
        for subset in range(1<<len(group)):
            seen=0
            for bit,v in enumerate(group):
                if subset>>bit&1:seen|=knowledge[v]
            if seen==FULL:b|=1<<subset
        B.append(b)
        d=0
        for secret in range(N):
            receivers=0
            for bit,v in enumerate(group):
                if knowledge[v]>>secret&1:receivers|=1<<bit
            d|=1<<receivers
        D.append(d)
    return tuple(B),tuple(D)

def exact_profiles():
    B,D=set(),set()
    count=0
    # Choose which of the two group0 collectors shares a final-edge side
    # with the first complete group1 collector. Each side must have
    # at least one group2 carrier; otherwise group2 cannot cover all
    # original secrets across the final bridge.
    for g0 in (0,1):
        for others in range(1,15):
            side=(1<<2)|(1<<g0)|(others<<4)
            other=FULL^side
            left=tuple(v for v in range(N) if side>>v&1)
            right=tuple(v for v in range(N) if other>>v&1)
            for x in side_states(side,2,g0):
                for y in side_states(other,3,1-g0):
                    knowledge=[0]*N
                    for v,k in zip(left,x):knowledge[v]=k
                    for v,k in zip(right,y):knowledge[v]=k
                    knowledge[2]=knowledge[3]=knowledge[2]|knowledge[3]
                    assert knowledge[2]==knowledge[3]==FULL
                    suff,ancestry=profile(knowledge)
                    # These are the exact collective coverage predicates.
                    if all(s & (1<<((1<<len(group))-1))
                           for s,group in zip(suff,GROUPS)):
                        B.add(suff)
                        D.add(ancestry)
                        count+=1
    return B,D,count

def main():
    B,D,count=exact_profiles()
    assert (B,D,count)==({(8,14,32768)},{(6,8,278)},48),(B,D,count)
    assert all((b[2]&d[2])!=d[2] for b in B for d in D)
    print("PASS exact n16 orbit 10: both large tree8 local groups "
          "(2,2,4) collectors (0,2,0) have B=",B,"D=",D,
          "terminal decompositions=",count,flush=True)
    print("PASS B[2] & D[2] != D[2]; orbit 10 impossible"
          " under necessary exact local profile compatibility",flush=True)

if __name__=="__main__":
    main()
