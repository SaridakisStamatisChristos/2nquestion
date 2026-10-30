"""Stage 21: independently filter ALL 6,435 labelled positive n20 3x3 matrices.

Two cross-half collector directions:
  - a private prefix Pi recipient in Pi∩Q3 => full reversed Q3 collector.
  - a private reversed Qj recipient in P3∩Qj => full prefix P3 collector.
If four complete collectors outside the center occur on EITHER side, the
helper-tolerant Stage15 one-sided causal four-arm theorem forces center>=9.
Here all necessary Stage18 n20 centers are <9.

These are NECESSARY-condition incidence matrices, never complete schedules.
"""
from collections import Counter
from itertools import permutations

BASE = (1,1,2,1,1,2,2,2,1)
# Complete labelled chronological tree enumeration is independently
# performed by Stage19 Python + Stage21 C++ verifier. These minima
# are *not* extrapolated to arbitrary group sizes.
MIN_PRIVATE = {
 (1,1,2):2,(1,1,3):2,(1,1,4):1,(1,1,5):1,
 (2,1,2):2,(1,2,2):2,(2,1,3):2,(1,2,3):2,
 (1,2,4):1,(2,1,4):1,(1,3,2):2,(3,1,2):2,
 (1,3,3):2,(3,1,3):2,(2,2,2):2,(2,2,3):2,
}


def compositions(k,parts):
    if parts==1:
        yield (k,)
    else:
        for x in range(k+1):
            for tail in compositions(k-x,parts-1):
                yield (x,)+tail


def baseline_allowed(m):
    # Globally proved Stage18 necessary component sizes; plus Stage15.
    top_extra=(m[2]-2)+(m[5]-2)
    bottom_extra=(m[6]-2)+(m[7]-2)
    center_extra=m[8]-1
    if top_extra+center_extra<4 or bottom_extra+center_extra<4:
        return False
    if (top_extra==0 or bottom_extra==0) and center_extra<8:
        return False
    if top_extra==bottom_extra==0 and center_extra<63:
        return False
    return True


def minima(m):
    a=(MIN_PRIVATE[(m[0],m[1],m[2])]
       + MIN_PRIVATE[(m[3],m[4],m[5])])
    b=(MIN_PRIVATE[(m[0],m[3],m[6])]
       + MIN_PRIVATE[(m[1],m[4],m[7])])
    return a,b


def canonical(m):
    variants=[]
    for rr in permutations((0,1)):
        for cc in permutations((0,1)):
            out=list(m)
            for i in range(2):
                for j in range(2):
                    out[3*i+j]=m[3*rr[i]+cc[j]]
                out[3*i+2]=m[3*rr[i]+2]
            for j in range(2):
                out[6+j]=m[6+cc[j]]
            variants.append(tuple(out))
    return min(variants)


def main():
    stats=Counter()
    remain=[]
    for extra in compositions(20-13,9):
        m=tuple(x+y for x,y in zip(BASE,extra))
        stats["raw"]+=1
        if not baseline_allowed(m):
            continue
        stats["stage18"]+=1
        prefix,reverse=minima(m)
        stats[(prefix,reverse)]+=1
        if prefix>=4 or reverse>=4:
            stats["rejected_by_private"]+=1
        else:
            assert prefix==reverse==3,(m,prefix,reverse)
            remain.append(m)
    assert stats["raw"]==6435,stats
    assert stats["stage18"]==221,stats
    assert stats["rejected_by_private"]==169,stats
    assert len(remain)==52,stats
    assert {m[8] for m in remain}=={2,3,4}
    centers=Counter(m[8] for m in remain)
    assert centers=={2:16,3:32,4:4},centers
    orbits=Counter(canonical(m) for m in remain)
    assert len(orbits)==13,len(orbits)
    assert set(orbits.values())=={4},orbits
    assert stats[(4,4)]==85
    assert stats[(3,4)]==stats[(4,3)]==42
    assert stats[(3,3)]==52
    print("PASS all 6,435 positive labelled n20 3x3 matrices enumerated")
    print("PASS Stage18 all-n necessary size restrictions => 221 matrices")
    print("PASS Stage19/21 local private-collector minima reject 169 => 52")
    print("PASS remaining 52 matrices = 13 S2xS2 symmetry orbits, 4 per orbit")
    print("PASS center sizes distributed",dict(sorted(centers.items())))
    print("Canonical orbits:")
    for m in sorted(orbits, key=lambda v:(v[8],v)):
        print("   ",m[:3],m[3:6],m[6:],"labelled=",orbits[m])
    print("LIMIT: all 52 matrices are ONLY necessary structural profiles")
    print("The unrestricted original half-forest conjecture n>=20 remains OPEN")


if __name__=="__main__":
    main()
