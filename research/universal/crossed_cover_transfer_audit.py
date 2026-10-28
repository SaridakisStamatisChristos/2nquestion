"""Independent actual-chronology test of ALL-n crossed-tree cover transfer.

Human theorem (not a finite proof):
    If A,B disjoint subsets of a center X each collectively covering
    every original U secret, and U's last chronological tree call joins
    two fully informed roots OUTSIDE X, then |A|+|B|>=6.
    Combined with exact rooted q-cover bound gives crossed X>=14.

Tests use genuine edge-once bidirectional call histories, no stage-number
incidence filtering, no invented or approximate source-support families.
"""
from itertools import combinations
from pathlib import Path
import sys

sys.path.insert(0,str(Path(__file__).resolve().parent))
from exponential_multiplicity_audit import outside, joined_two_roots


def exact_hitting_sets(supports,C,topsize=4):
    return [frozenset(c) for k in range(1,min(topsize,len(C))+1)
            for c in combinations(sorted(C),k)
            if all(any(v in S for v in c) for S in supports)]


def challenge_lemma():
    for qa,qb in ((2,2),(2,3),(3,3)):
        n,seq,C,supports=joined_two_roots(outside(qa),outside(qb))
        hit=exact_hitting_sets(supports,C)
        overlapping=0
        disjoint=0
        min_union=999
        for S in hit:
            for T in hit:
                if S&T:
                    overlapping+=1
                    continue
                disjoint+=1
                m=len(S)+len(T)
                min_union=min(min_union,m)
                assert m>=6,(qa,qb,S,T,supports)
        assert disjoint>0
        assert min_union==6,(qa,qb,min_union)
        print("PASS actual original-order tree two-root group sizes",
              2**qa-1,2**qb-1,"terminal hitting sets",len(hit),
              "disjoint pairs",disjoint,"minimum combined size",min_union)


def integer_optimization():
    for a in range(2,32):
        for b in range(2,32):
            if a+b<6:
                continue
            assert (1<<a)+(1<<b)-2>=14,(a,b)
    assert min(((1<<a)+(1<<b)-2,a,b) for a in range(2,20)
               for b in range(2,20) if a+b>=6)==(14,3,3)
    print("PASS exact integer minimum (a,b)=(3,3), |X| lower=14")


def main():
    challenge_lemma()
    integer_optimization()
    print("UNBOUNDED proof in CROSSED_TREE_COVER_TRANSFER.md, finite tests separate")
    print("SCOPE: under outside-root/double-center/all-pairs crossing hypotheses")
    print("SCOPE: no claim all-width no-crossing, original forest or 2n-3 spanner")


if __name__=="__main__":
    main()
