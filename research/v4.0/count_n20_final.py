"""Stage23 n20 original-chronology proof-obligation cross-check.

Independent weak-composition generator, local-tree privacy input table,
and exact five-orbit classification. This is NOT enumeration of all
successful 36-call schedules. The universal contradiction is established
by human lemmas in N20_ORIGINAL_FOREST_THEOREM.md; code checks finite data
and structural premises only.
"""
from collections import Counter
from itertools import combinations, permutations

BASE = (1, 1, 2, 1, 1, 2, 2, 2, 1)
PRIVATE = {
    (1,1,2):2, (1,1,3):2, (1,1,4):1, (1,1,5):1,
    (1,2,2):2, (2,1,2):2, (1,2,3):2, (2,1,3):2,
    (1,2,4):1, (2,1,4):1, (1,3,2):2, (3,1,2):2,
    (1,3,3):2, (3,1,3):2, (2,2,2):2, (2,2,3):2,
}
EXPECTED = {
    (1,1,2,1,1,4,2,4,4),
    (1,1,2,1,1,5,2,5,2),
    (1,1,2,1,1,5,3,4,2),
    (1,1,3,1,1,4,2,5,2),
    (1,1,3,1,1,4,3,4,2),
}


def weak_compositions_separators(stars=7, slots=9):
    """Separate exact combinatorial generator: stars/bars positions."""
    for bars in combinations(range(stars + slots - 1), slots - 1):
        marks = (-1,) + bars + (stars + slots - 1,)
        yield tuple(marks[j+1] - marks[j] - 1 for j in range(slots))


def is_structurally_allowed(m):
    up = m[2]+m[5]-4
    left = m[6]+m[7]-4
    central = m[8]-1
    return (up+central>=4 and left+central>=4
            and not ((up==0 or left==0) and central<8)
            and not (up==left==0 and central<63))


def required_collectors(m):
    prefix = PRIVATE[(m[0],m[1],m[2])] + PRIVATE[(m[3],m[4],m[5])]
    reversed_suffix = PRIVATE[(m[0],m[3],m[6])] + PRIVATE[(m[1],m[4],m[7])]
    return prefix, reversed_suffix


def excluded_three_star(m):
    return m[8]==3 and (
        sorted((m[2],m[5]))==[2,4]
        or sorted((m[6],m[7]))==[2,4])


def orbit(matrix):
    transforms=[]
    for rr in permutations((0,1)):
        for cc in permutations((0,1)):
            value=[0]*9
            for i in range(2):
                for j in range(2):
                    value[3*i+j]=matrix[3*rr[i]+cc[j]]
                value[3*i+2]=matrix[3*rr[i]+2]
            for j in range(2):
                value[6+j]=matrix[6+cc[j]]
            value[8]=matrix[8]
            transforms.append(tuple(value))
    return min(transforms)


def excluded_five_orbit(matrix):
    center=matrix[8]
    assert center in (2,4)
    # Prefix cyclic P3 uses opposite reversed-suffix trees Q1 and Q2,
    # reverse suffix cyclic Q3 uses original prefix trees P1 and P2.
    pairs=[(matrix[6],matrix[7]),(matrix[2],matrix[5])]
    for g1,g2 in pairs:
        small,large=sorted((g1,g2))
        assert small in (2,3) and large in (4,5)
        assert PRIVATE[(1,1,small)]>=2
        assert PRIVATE[(1,1,large)]>=1
        # Full roots are initially >= A2+B1, outside the center.
        # If four roots, all-outside => center >=9 (contradiction);
        # center-one-root => B >=6 (four-arm double-cover + 4-star).
        root_options=[]
        for a in range(2,small+1):
            for b in range(1,large+1):
                c=4-a-b
                if 0<=c<=center:
                    root_options.append((a,b,c))
                    if c==0:
                        assert center < 9
                    else:
                        assert (a,b,c)==(2,1,1)
                        assert large<=5
        assert root_options, (matrix,small,large)
        # Thus exactly three full collectors, all outside X.
        # They imply two outside-root full collectors in the earlier
        # chronological spanning tree. Absence of opposite center
        # collector forces each center source support size >=2.
    assert center < 6  # contradicts 2-outside-root tree double-cover lemma
    return True


def main():
    count=Counter()
    survivors=[]
    for extras in weak_compositions_separators():
        m=tuple(a+b for a,b in zip(BASE,extras))
        count["raw"]+=1
        if not is_structurally_allowed(m):
            continue
        count["stage18"]+=1
        p,q=required_collectors(m)
        if p>=4 or q>=4:
            continue
        count["stage21"]+=1
        if excluded_three_star(m):
            continue
        count["stage22"]+=1
        assert excluded_five_orbit(m),m
        survivors.append(m)
        count["stage23_excluded"]+=1
    assert count=={"raw":6435,"stage18":221,"stage21":52,
                   "stage22":20,"stage23_excluded":20},count
    pairs=Counter(orbit(m) for m in survivors)
    assert set(pairs)==EXPECTED,pairs
    assert set(pairs.values())=={4},pairs
    for m,k in sorted(pairs.items()):
        print("PASS n20 orbit:",m[:3],m[3:6],m[6:9],
              "labelled reps=",k,"excluded by 4-root / center-double-cover")
    print("PASS original n20 incidence closure: raw 6435; Stage21 52;"
          " Stage22 20; Stage23 0 remaining compatible with necessary lemmas")
    print("LIMIT: this oracle validates finite structural obligations; "
          "it does NOT brute-force 36-call schedules or constitute a formal proof.")


if __name__=="__main__":
    main()
