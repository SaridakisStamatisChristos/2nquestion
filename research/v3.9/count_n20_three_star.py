"""Stage 22: independent finite original n20 incidence filtering.

The Stage20 three-leaf-star original chronological incompatibility applies
whenever a candidate unicyclic component has off-corner sizes (2,4),
center size 3 AND the adjacent chronological trees force both size-two
persons to be complete collectors and at least one in the size-four cell.

Those private collector minima are exactly verified by Stage19/Stage21.
The filter is necessary ONLY; it does not construct completed schedules.
"""
from itertools import permutations
from collections import Counter

BASE=(1,1,2,1,1,2,2,2,1)
PRIVATE={
 (1,1,2):2,(1,1,3):2,(1,1,4):1,(1,1,5):1,
 (2,1,2):2,(1,2,2):2,(2,1,3):2,(1,2,3):2,
 (1,2,4):1,(2,1,4):1,(1,3,2):2,(3,1,2):2,
 (1,3,3):2,(3,1,3):2,(2,2,2):2,(2,2,3):2,
}


def compositions(total,size):
    if size==1:
        yield (total,)
        return
    for x in range(total+1):
        for t in compositions(total-x,size-1):
            yield (x,)+t


def stage18(m):
    p=(m[2]-2)+(m[5]-2)
    q=(m[6]-2)+(m[7]-2)
    d=m[8]-1
    return (p+d>=4 and q+d>=4 and
            not((p==0 or q==0) and d<8) and
            not(p==q==0 and d<63))


def four_private(m):
    return (PRIVATE[(m[0],m[1],m[2])]+PRIVATE[(m[3],m[4],m[5])]>=4 or
            PRIVATE[(m[0],m[3],m[6])]+PRIVATE[(m[1],m[4],m[7])]>=4)


def forbidden_three_star(m):
    # Actual original prefix cyclic P3 and reversed original suffix Q3
    # possess the same all-n star incompatibility under either orientation.
    return (
      (m[8]==3 and sorted((m[2],m[5]))==[2,4]) or
      (m[8]==3 and sorted((m[6],m[7]))==[2,4])
    )


def orbit(m):
    seen=[]
    for rr in permutations((0,1)):
        for cc in permutations((0,1)):
            v=list(m)
            for i in range(2):
                for j in range(2):
                    v[3*i+j]=m[3*rr[i]+cc[j]]
                v[3*i+2]=m[3*rr[i]+2]
            for j in range(2):
                v[6+j]=m[6+cc[j]]
            seen.append(tuple(v))
    return min(seen)


def main():
    counts=Counter()
    survivors=[]
    eliminated=[]
    for extra in compositions(7,9):
        m=tuple(a+b for a,b in zip(BASE,extra))
        counts["raw"]+=1
        if not stage18(m):
            continue
        counts["stage18"]+=1
        if four_private(m):
            continue
        counts["stage21"]+=1
        if forbidden_three_star(m):
            eliminated.append(m)
        else:
            survivors.append(m)
    assert counts=={"raw":6435,"stage18":221,"stage21":52},counts
    assert len(eliminated)==32
    assert len(survivors)==20
    stage21_orbits={orbit(m) for m in eliminated+survivors}
    eliminated_orbits={orbit(m) for m in eliminated}
    remaining_orbits=Counter(orbit(m) for m in survivors)
    assert len(stage21_orbits)==13
    assert len(eliminated_orbits)==8
    assert len(remaining_orbits)==5
    assert set(remaining_orbits.values())=={4}
    assert Counter(m[8] for m in survivors)=={2:16,4:4}
    canonical_expected={
      (1,1,2,1,1,4,2,4,4),
      (1,1,2,1,1,5,2,5,2),
      (1,1,2,1,1,5,3,4,2),
      (1,1,3,1,1,4,2,5,2),
      (1,1,3,1,1,4,3,4,2),
    }
    assert set(remaining_orbits)==canonical_expected,(remaining_orbits,canonical_expected)
    print("PASS all n20 labelled positive matrices:",counts["raw"])
    print("PASS n20 Stage18 necessary structural matrices:",counts["stage18"])
    print("PASS n20 Stage19+21 private collector candidates:",counts["stage21"])
    print("PASS Stage22 original chronological three-star exclusion:",len(eliminated))
    print("PASS remaining 20 labelled matrices in exactly FIVE orbits")
    for m,count in sorted(remaining_orbits.items()):
        print("   ",m[:3],m[3:6],m[6:],"labelled",count)
    print("LIMIT: these are non-excluded incidence matrices; NOT full gossip schedules")
    print("OPEN: all-n original chronological half-forest conjecture, including n20")


if __name__=="__main__":
    main()
