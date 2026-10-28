"""Stage 19: independent complete nine-cell n=19 incidence and private forcing.

The table below is NOT an all-n theorem about arbitrary trees. It consists
ONLY of exact finite chronological tree classes whose exhaustive underlying
histograms are separately checked by exact_small_tree_privacy.py.

A private prefix tree recipient in a Q3 cell must be a FULL reversed-Q3
collector under successful original midpoint temporal crossing; symmetrically
a private reversed suffix-tree recipient must be a FULL prefix-P3 collector.
FOUR such outside-center collectors on either unicyclic side invoke Stage15
one-sided causal four-arm theorem: center >=9. All n19 centers are <9.
"""
from collections import Counter
from itertools import permutations

BASE = (1,1,2,1,1,2,2,2,1)
# Minimum private recipients in the offcorner group (3rd argument).
# Label order of first two corner groups may be exchanged.
PRIVATE_MIN = {
    (1,1,2):2, (1,1,3):2, (1,1,4):1,
    (2,1,2):2, (1,2,2):2,
    (2,1,3):2, (1,2,3):2,
}


def compositions(k,m):
    if m == 1:
        yield (k,)
    else:
        for x in range(k+1):
            for rest in compositions(k-x,m-1):
                yield (x,)+rest


def stage18_allowed(m):
    p=(m[2]-2)+(m[5]-2)
    q=(m[6]-2)+(m[7]-2)
    d=m[8]-1
    if p+d<4 or q+d<4:return False
    if (p==0 or q==0) and d<8:return False
    if p==0 and q==0 and d<63:return False
    return True


def collector_lower_bounds(m):
    prefix_private = (PRIVATE_MIN[(m[0],m[1],m[2])]
                      +PRIVATE_MIN[(m[3],m[4],m[5])])
    reversed_suffix_private = (PRIVATE_MIN[(m[0],m[3],m[6])]
                               +PRIVATE_MIN[(m[1],m[4],m[7])])
    return prefix_private,reversed_suffix_private


def normalized_orbit(m):
    # Swap P1/P2 rows and/or Q1/Q2 columns; NEVER reorder contacts.
    transforms = []
    for rows in permutations((0,1)):
        for cols in permutations((0,1)):
            out = list(m)
            for i in range(2):
                for j in range(2):
                    out[3*i+j]=m[3*rows[i]+cols[j]]
                out[3*i+2]=m[3*rows[i]+2]
            for j in range(2):
                out[6+j]=m[6+cols[j]]
            transforms.append(tuple(out))
    return min(transforms)


def main():
    counter=Counter()
    allowed=[]
    survivors=[]
    for extra in compositions(19-13, 9):
        m=tuple(a+b for a,b in zip(BASE, extra))
        counter["raw"]+=1
        if not stage18_allowed(m):
            continue
        allowed.append(m)
        counter["stage18"]+=1
        p,q=collector_lower_bounds(m)
        counter["prefix>=4" if p>=4 else "prefix=3"]+=1
        counter["suffix>=4" if q>=4 else "suffix=3"]+=1
        if p>=4 or q>=4:
            counter["excluded by four full collectors"]+=1
        else:
            assert p==q==3, (m,p,q)
            survivors.append(m)
    assert counter == {
      "raw":3003,
      "stage18":41,
      "prefix>=4":31,
      "prefix=3":10,
      "suffix>=4":31,
      "suffix=3":10,
      "excluded by four full collectors":37,
    }, counter
    assert len(survivors)==4,survivors
    assert len({normalized_orbit(m) for m in survivors})==1
    canonical=(1,1,2,1,1,4,2,4,3)
    assert normalized_orbit(survivors[0])==canonical
    assert all(collector_lower_bounds(m)==(3,3) for m in survivors)
    print("PASS n19 complete 3003 raw labelled positive 3x3 incidence configurations")
    print("PASS Stage18 all-n size necessary filter => 41 labelled configurations")
    print("PASS exact local tree privacy forces >=4 outsiders on a cyclic side in 37")
    print("PASS FOUR remaining n19 matrices; ONE symmetry orbit, no schedule certified")
    print("Canonical matrix:")
    for i in range(0,9,3):
        print("   ",canonical[i:i+3])
    print("All four survivors are equivalent under tree component ROW/COLUMN relabeling.")
    print("LIMIT: n19 original-half theorem still OPEN; cannot exclude final four.")


if __name__=="__main__":
    main()
