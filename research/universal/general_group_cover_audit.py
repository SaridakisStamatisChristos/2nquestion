"""Independent all-n tree-group cover and support-packing regression suite.

UNBOUNDED statements proved in GENERAL_COVER_PACKING.md; this script
enumerates finite original call orders, exact group memberships, and
helper vertices solely as an adversarial correctness check.
"""
from itertools import product,permutations,combinations
from collections import Counter
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parent))
from exponential_multiplicity_audit import outside,joined_two_roots,replay,support_masks


def prufer(n,word):
    deg=[1]*n
    for v in word:deg[v]+=1
    E=[]
    for v in word:
        leaf=next(i for i,d in enumerate(deg) if d==1)
        E.append((leaf,v))
        deg[leaf]-=1
        deg[v]-=1
    E.append(tuple(i for i,d in enumerate(deg) if d==1))
    return tuple(E)


def test_tree_cover_groups(n):
    counts=Counter()
    for word in product(range(n),repeat=n-2):
        E=prufer(n,word)
        for order in permutations(E):
            know=replay(n,order)
            complete=(1<<n)-1
            for s in range(1,min(n,4)+1):
                for assign in product(range(s+1),repeat=n):
                    # code 0=unused helper; 1..s group IDs
                    groups=[tuple(i for i,g in enumerate(assign) if g==j)
                            for j in range(1,s+1)]
                    if not all(groups):continue
                    if not all(
                        all(any(know[v]&(1<<secret) for v in G)
                            for secret in range(n))
                        for G in groups
                    ):continue
                    total=sum(map(len,groups))
                    assert total>=2**(s-1),(n,order,groups)
                    counts[(s,total)]+=1
            # Adversarial rooted Helly dichotomy on ALL C subsets,
            # including unassigned helper vertices.
            if know[0]!=complete:continue
            for mask in range(1,1<<(n-1)):
                C=frozenset(i+1 for i in range(n-1) if mask>>i&1)
                S=support_masks(n,know,C)
                if any(not ss for ss in S):continue
                full=any(know[x]==complete for x in C)
                disjoint=any(not a&b for a,b in combinations(S,2))
                assert full or disjoint,(n,order,C,S)
    assert counts, n
    print("PASS ALL labelled chronological trees and ALL disjoint group"
          " assignments n=",n,"cover distributions",dict(counts))


def witness_s3():
    info=replay(4,[(0,2),(1,3),(0,1)])
    groups=({0},{1},{2,3})
    for G in groups:
        assert all(any(info[x]&(1<<secret) for x in G)
                   for secret in range(4))
    assert sum(map(len,groups))==4
    print("PASS sharp 3 recipient groups at exactly 4 designated people")


def test_two_root_cover_transfer():
    for qa,qb in ((2,2),(2,3),(3,3)):
        n,contacts,C,S=joined_two_roots(outside(qa),outside(qb))
        groups=[]
        for z in range(1,5):
            groups.extend(frozenset(c) for c in combinations(sorted(C),z)
                          if all(any(v in t for v in c) for t in S))
        for A in groups:
            for B in groups:
                if A&B:continue
                assert len(A)+len(B)>=6
        print("PASS all small disjoint complete hitting groups in true"
              " two-root tree q=",qa,qb)


def sharp_all_s_groups(s):
    """Construct a genuine edge-once chronological equality tree for EVERY s."""
    if s==1:
        return 1, (), 0, (frozenset((0,)),)
    n1,e1,r1,G1=sharp_all_s_groups(s-1)
    n2,e2,r2,G2=sharp_all_s_groups(s-1)
    assert n1==n2
    # Singletons containing the two new terminal complete collectors,
    # then pair every remaining previous complete group across both sides.
    groups=[frozenset((r1,)),frozenset((r2+n1,))]
    groups.extend(G1[i]|frozenset(v+n1 for v in G2[i])
                  for i in range(1,s-1))
    return (n1+n2, tuple(e1)+tuple((a+n1,b+n1) for a,b in e2)
            +((r1,r2+n1),),r1,tuple(groups))


def verify_exact_all_s_equality():
    for s in range(1,9):
        n,edges,root,groups=sharp_all_s_groups(s)
        assert n==2**(s-1)
        assert len(groups)==s
        assert sum(map(len,groups))==n
        assert set().union(*(set(G) for G in groups))==set(range(n))
        assert all(not set(a)&set(b)
                   for a,b in combinations(groups,2))
        if s==1:
            assert list(map(len,groups))==[1]
        else:
            assert list(map(len,groups))==[1,1]+[2**j for j in range(1,s-1)]
        know=replay(n,edges)
        assert know[root]==(1<<n)-1
        for G in groups:
            assert all(any(know[v]>>sec&1 for v in G)
                       for sec in range(n)), (s,G)
        print("PASS SHARP recipient-group cover s=",s,"vertices=",n,
              "group sizes=",list(map(len,groups)))


def main():
    for n in (2,3,4):
        test_tree_cover_groups(n)
    witness_s3()
    verify_exact_all_s_equality()
    test_two_root_cover_transfer()
    print("UNBOUNDED HUMAN PROOF: s disjoint cover groups require EXACT minimum 2^(s-1)")
    print("UNBOUNDED HUMAN PROOF: k disjoint source supports require center >=2^(k+1)-2")
    print("SCOPE: no all-width crossing impossibility or all-n half forest proof")


if __name__=="__main__":
    main()
