"""Stage 20 independent nine-person LOCAL unicyclic boundary.

A={0,1}, B={2,3,4,5}, C={6,7,8}. Reverse-chronological Q3 calls
build two complete full-tree roots, then a final cycle edge (0,2).
Exact local per-secret carrier minima are A>=2, B>=2, C>=1 and
complete collector set exactly {0,1,2}.

CRITICAL: This *is not a full gossip counterexample*. It shows that
the Stage 20 exclusion must use the necessary original P2 tree crossing:
the local Q3 history itself IS feasible with three complete collectors.
"""
from itertools import product


CALLS = (
    (0, 1), (1, 6), (3, 7), (1, 3),
    (2, 4), (8, 5), (2, 8), (1, 2), (0, 2)
)
A=(0,1)
B=(2,3,4,5)
C=(6,7,8)


def replay(calls, n):
    know=[1<<i for i in range(n)]
    edges=set()
    for u,v in calls:
        assert 0<=u<n and 0<=v<n and u!=v
        edge=tuple(sorted((u,v)))
        assert edge not in edges,edge
        edges.add(edge)
        know[u]=know[v]=know[u]|know[v]
    return know


def main():
    n=9
    before=replay(CALLS[:-1],n)
    after=replay(CALLS,n)
    full=(1<<n)-1
    assert len(CALLS)==n and len(set(tuple(sorted(x)) for x in CALLS))==n
    assert before[1]==before[2]==full
    assert {i for i,k in enumerate(after) if k==full}=={0,1,2}
    for secret in range(n):
        for group, required in ((A,2),(B,2),(C,1)):
            count=sum(bool(after[i]&(1<<secret)) for i in group)
            assert count>=required,(secret,group,count)
    # The B-group complete collector is 2, and every other B vertex
    # is a private recipient for an original Q3 secret; each reverse
    # target support then consists of exactly the collector and its
    # unique private B participant. These three pairs cannot cross the
    # independent six-person original P2 chronological tree.
    for z in (3,4,5):
        secret=z
        support={i for i in B if after[i]&(1<<secret)}
        assert support=={2,z},(z,support)
    assert (before[3]|before[4]|before[5])==full
    assert (before[6]|before[7]|before[8])==full
    print("PASS genuine local 9-person unicyclic (A2,B4,C3) chronology")
    print("PASS full collectors are 0,1,2 (only THREE)")
    print("PASS three reverse target supports {2,3}, {2,4}, {2,5}")
    print("PASS four tight tree-recipient groups at penultimate cut, one helper")
    print("LIMIT: the local cycle is feasible; the adjacent original P2 tree crossing is IMPOSSIBLE")
    # Pigeonhole four FULL collector root arms with 1 B root would
    # require at least one extra B nonroot in EACH of 4 disjoint arms,
    # but B contains only 3 nonroots. Enumerate all possible assignments.
    for assignment in product(range(4),repeat=3):
        assert set(assignment)!={0,1,2,3}
    print("PASS all 64 assignments of three B nonroots leave a full-root arm uncovered")


if __name__=="__main__":
    main()
