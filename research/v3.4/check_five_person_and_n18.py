"""Stage 17 independent finite four-corner private collector oracle.

Checks every ordered labelled tree on 5 participants (Prufer enumeration),
fixing two singleton corner roots and three off-corner participants; and
independently enumerates original 3x3 incidence matrices n=18..24.

This is NOT a full gossip schedule solver. The all-n implications use the
written crossing and causal four-arm lemmas.
"""
from collections import Counter
from itertools import permutations, product
from math import comb


def prufer_tree(seq, n):
    degree = [1] * n
    for value in seq:
        degree[value] += 1
    edges = []
    for value in seq:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((leaf, value))
        degree[leaf] -= 1
        degree[value] -= 1
    x,y=(i for i in range(n) if degree[i] == 1)
    return edges+[(x,y)]


def five_person_private():
    qualifying = Counter()
    witness = None
    for code in product(range(5), repeat=3):
        edges = prufer_tree(code, 5)
        for chronology in permutations(edges):
            if set(chronology[-1]) != {0,1}:
                continue
            known = [1<<i for i in range(5)]
            for a,b in chronology:
                known[a] = known[b] = known[a] | known[b]
            if known[0]!=31 or known[1]!=31:
                continue
            if (known[2]|known[3]|known[4])!=31:
                continue
            private = 0
            for i in (2,3,4):
                if any(
                    known[i]&(1<<secret) and
                    all(not(known[j]&(1<<secret)) for j in (2,3,4) if j!=i)
                    for secret in range(5)
                ):
                    private += 1
            qualifying[private] += 1
            if witness is None:
                witness = chronology
    assert qualifying == {2:72},qualifying
    print("PASS all chronological 5-person trees: 72 qualifying root-pair histories, each with exactly 2 private off-corner participants")
    print("EXAMPLE",witness)


def compositions(k,m):
    if m==1:
        yield (k,)
        return
    for x in range(k+1):
        for rest in compositions(k-x,m-1):
            yield (x,)+rest


BASE=(1,1,2,1,1,2,2,2,1)


def profile(m, stage):
    upper=(m[2]==m[5]==2)
    lower=(m[6]==m[7]==2)
    if (upper or lower) and m[8]<9:
        return False
    if upper and lower and m[8]<64:
        return False
    if stage>=16 and (m[2]+m[5]+m[8]<8 or m[6]+m[7]+m[8]<8):
        return False
    if stage>=17:
        # Adversarially repaired all-n disjunction: (2,5,1) IS feasible locally.
        if m[6]+m[7]+m[8]==8:
            if not(m[8]==1 and sorted((m[6],m[7]))==[2,5]):
                return False
        if m[2]+m[5]+m[8]==8:
            if not(m[8]==1 and sorted((m[2],m[5]))==[2,5]):
                return False
    return True


def orbit(m):
    # Independently relabel the two tree rows and two tree columns.
    transforms = []
    for rows in permutations((0,1)):
        for cols in permutations((0,1)):
            out = list(m)
            for i in range(2):
                for j in range(2):
                    out[3*i+j] = m[3*rows[i]+cols[j]]
                out[3*i+2] = m[3*rows[i]+2]
            for j in range(2):
                out[6+j] = m[6+cols[j]]
            transforms.append(tuple(out))
    return min(transforms)


def exact_counts():
    fixed={18:(489,41,4),19:(1365,221,45),20:(3333,825,257),
           21:(7359,2438,994),24:(52293,28205,17365)}
    for n in range(18,25):
        counts=Counter()
        survivor=[]
        for x in compositions(n-13,9):
            m=tuple(u+v for u,v in zip(BASE,x))
            for stage in (15,16,17):
                counts[stage]+=profile(m,stage)
            if n==18 and profile(m,17):
                survivor.append(m)
        print("PASS n=",n,"stage15=",counts[15],"stage16=",counts[16],
              "stage17=",counts[17])
        if n in fixed:
            assert tuple(counts[i] for i in (15,16,17)) == fixed[n],(n,counts)
        if n==18:
            assert len(survivor)==4
            assert len({orbit(m) for m in survivor})==1
            assert orbit(survivor[0]) == (1,1,2,1,1,3,2,3,4)
            print("PASS n18 four candidate labelled profiles, ONE S2xS2 orbit")
            for matrix in survivor:
                print("   ",matrix[:3],matrix[3:6],matrix[6:])
    print("LIMIT: Stage17 n18 forest proof also uses private-collector forcing and Stage14 cross-arm bound; incidence alone leaves four profiles.")


if __name__=="__main__":
    five_person_private()
    exact_counts()
