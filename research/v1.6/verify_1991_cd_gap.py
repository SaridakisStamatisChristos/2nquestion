"""A reproducible 1991 static Cd-partition vs chronological halves distinction.

Source: F. Goebel, J. Orestes Cerdeira, H.J. Veldman (1991),
'Label-connected graphs and the gossip problem', Theorems 3, 9, 13.
https://doi.org/10.1016/0012-365X(91)90068-D

This verifies one example; it does NOT disprove any universal chronology claim.
"""
from itertools import combinations

W = ((0,1),(4,5),(3,7),(2,6),(2,3),(1,5),
     (0,4),(1,2),(6,7),(4,6),(3,5),(0,7))
FIRST = (0,1,2,3,4,9)
SECOND = tuple(i for i in range(12) if i not in FIRST)
CYCLE = (0,1,5,4)

def components(n, selected):
    parent = list(range(n))
    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v
    rank = 0
    for i in selected:
        x, y = map(root, W[i])
        if x == y:
            rank += 1
        else:
            parent[x] = y
    groups = tuple(root(i) for i in range(n))
    return groups, rank

def gossip(n, seq):
    for start in range(n):
        reach = {start}
        for u, v in seq:
            if u in reach or v in reach:
                reach.update((u,v))
        assert len(reach) == n, (start, reach)

def verify_cd(first, second):
    a, ca = components(8, first)
    b, cb = components(8, second)
    assert ca == cb == 0
    assert len(set(a)) == len(set(b)) == 2
    assert len(first) == len(second) == 6
    assert not (set(first) & set(second))
    edge_id = {frozenset(e): i for i,e in enumerate(W)}
    ids = [edge_id[frozenset((CYCLE[j], CYCLE[(j+1)%4]))] for j in range(4)]
    assert ids[0] in first and ids[2] in first
    assert ids[1] in second and ids[3] in second
    assert a[CYCLE[0]] != a[CYCLE[2]]
    assert b[CYCLE[1]] != b[CYCLE[3]]
    return ids

def run():
    gossip(8, W)
    assert len({frozenset(e) for e in W}) == len(W) == 12
    left_rank = components(8, range(6))[1]
    right_rank = components(8, range(6,12))[1]
    assert (left_rank, right_rank) == (0,1)
    cd_cycle_edges = verify_cd(FIRST, SECOND)

    forest_partitions = sum(
        components(8, choose)[1] == 0
        and components(8, tuple(i for i in range(12) if i not in choose))[1] == 0
        for choose in combinations(range(12), 6)
    )
    assert forest_partitions == 604
    print('PASS | ordered gossip: 8 vertices, 12 pairwise-distinct contacts')
    print('PASS | true chronological half cycle ranks: (0,1)')
    print('PASS | historical Cd partition: (0,0) with qualifying four-cycle')
    print('PASS | crossing four-cycle edge IDs:', cd_cycle_edges)
    print('PASS | forest/forest (ordered orientation) partitions:', forest_partitions)
    print('Cd first:', [W[i] for i in FIRST])
    print('Cd second:', [W[i] for i in SECOND])

if __name__ == "__main__":
    run()