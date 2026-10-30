"""Independently check a concrete n=13 same-poset, different-midpoint pair.

The two schedules are hard-coded; this code does not import the generator.
It verifies every ordered-pair temporal journey by source-specific forward
reachability, not merely the combined gossip update routine.
"""
A=((12,0),(11,0),(10,0),(9,0),(8,0),(0,1),(4,5),(3,7),
   (2,6),(2,3),(1,5),(0,4),(1,2),(6,7),(4,6),(3,5),
   (0,7),(8,1),(9,1),(10,1),(11,1),(12,1))
B=((12,0),(11,0),(10,0),(9,0),(8,0),(0,1),(4,5),(3,7),
   (1,5),(2,6),(6,7),(0,4),(4,6),(2,3),(0,7),(1,2),
   (3,5),(8,1),(9,1),(10,1),(11,1),(12,1))


def verify_temporal(n,seq):
    for start in range(n):
        reached={start}
        for u,v in seq:
            prior_u=(u in reached)
            prior_v=(v in reached)
            if prior_u or prior_v:
                reached.update((u,v))
        if len(reached)!=n:
            raise AssertionError((start,len(reached)))


def cyc(n,seq):
    groups=[{i} for i in range(n)]
    rank=0
    for u,v in seq:
        a=next(i for i,x in enumerate(groups) if u in x)
        b=next(i for i,x in enumerate(groups) if v in x)
        if a==b:rank+=1
        else:
            groups[a]=groups[a]|groups[b]
            del groups[b]
    return rank


def signature(n,seq):
    return tuple(tuple(frozenset((u,v)) for u,v in seq if x in (u,v))
                 for x in range(n))


def run():
    n=13
    for s in (A,B):
        assert len(s)==22
        assert len({frozenset(e) for e in s})==22
        assert all(0<=u<n and 0<=v<n and u!=v for u,v in s)
        verify_temporal(n,s)
    assert {frozenset(e) for e in A}=={frozenset(e) for e in B}
    assert signature(n,A)==signature(n,B)
    assert (cyc(n,A[:11]),cyc(n,A[11:]))==(0,1)
    assert (cyc(n,B[:11]),cyc(n,B[11:]))==(0,0)
    print('PASS: independent all-pairs temporal n13 witness check')
    print('same incident-event order/induced minimal poset, different original midpoint geometry')


if __name__=='__main__':
    run()
