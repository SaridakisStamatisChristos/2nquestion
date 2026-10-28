"""Stage 31: last-edge full-collector transfer across a two-person cell.

All-n conditional lemma: when U's last cycle-closing contact joins two exterior
cells A,B and |A|=2 with both A people complete, B's final-call endpoint
is complete. DO NOT transfer if |A|>=3 even with >=2 known full collectors.

Combines only earlier necessary incidence rules and Stage28 conditional theorem.
Does NOT produce legal global gossip schedules or prove original-half forest.
"""
from collections import Counter
from pathlib import Path
import sys

research = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(research / "v4.4"))
sys.path.insert(0, str(research / "v4.5"))
from n22_3x3_frontier import matrices, stage25, stage26, privacy, canonical  # noqa: E402
from unbounded_eight_outside_audit import collector_gate  # noqa: E402


def replay(n, contacts):
    k = [1 << i for i in range(n)]
    used = set()
    parents = list(range(n))

    def root(x):
        while parents[x] != x:
            x = parents[x]
        return x

    for i, (a, b) in enumerate(contacts):
        e = tuple(sorted((a, b)))
        assert a != b and 0 <= a < n and 0 <= b < n and e not in used
        used.add(e)
        if i < len(contacts) - 1:
            u, v = root(a), root(b)
            assert u != v, "first n-1 contacts must form spanning tree"
            parents[u] = v
        else:
            assert root(a) == root(b), "final call must close unique cycle"
        k[a] = k[b] = k[a] | k[b]
    assert len(used) == n
    return k


def transfer(cells, known):
    """Sound transfer ONLY when the entire opposite cell has size exactly 2."""
    full = [known[0] > 0, known[1] > 0]
    if cells[0] == 2 and known[0] >= 2:
        full[1] = True
    if cells[1] == 2 and known[1] >= 2:
        full[0] = True
    return tuple(full)


def transfer_gate(m):
    qmin, pmin = privacy(m)
    up, down = (m[2], m[5]), (m[6], m[7])
    qblocked = sum(up) <= 8 and all(transfer(up, qmin))
    pblocked = sum(down) <= 8 and all(transfer(down, pmin))
    x = m[8]
    if x == 1 and (qblocked or pblocked):
        return "singleton"
    if x == 2 and qblocked and pblocked:
        return "binary"
    if x == 3 and qblocked and pblocked:
        return "triple"
    return "survive"


def eligible_six_tree_cells(m):
    return any((
        m[0] == m[1] == 1 and m[2] == 6,
        m[3] == m[4] == 1 and m[5] == 6,
        m[0] == m[3] == 1 and m[6] == 6,
        m[1] == m[4] == 1 and m[7] == 6,
    ))


def prior_frontier(n):
    return [m for m in matrices(n)
            if stage25(m) == stage26(m) == collector_gate(m) == "survive"]


def new_frontier(n):
    prior = prior_frontier(n)
    labels = Counter(transfer_gate(m) for m in prior)
    survivors = [m for m in prior if transfer_gate(m) == "survive"]
    return prior, labels, survivors


def validate_boundary():
    # Distinct edges; chronological 4-edge spanning tree, 5th edge closes
    # 4-cycle. TWO full people 0,1 in a 3-person exterior A={0,1,2},
    # yet NO full person in exterior B={3}. Endpoint 2 was not full.
    k = replay(5, [(2, 0), (4, 0), (3, 1), (0, 1), (2, 3)])
    full = (1 << 5) - 1
    assert [v for v in range(5) if k[v] == full] == [0, 1]
    assert k[3] != full and k[2] != full
    assert transfer((3, 2), (2, 0)) == (True, False)
    assert transfer((2, 6), (2, 0)) == (True, True)
    assert transfer((6, 2), (0, 2)) == (True, True)
    print("PASS sharp boundary: two complete in size-three A DO NOT force B full")


def main():
    validate_boundary()
    old21, c21, s21 = new_frontier(21)
    assert len(old21) == 0 and not s21
    print("PASS n21 exact prior incidence closure regression")

    old22, c22, s22 = new_frontier(22)
    assert len(old22) == 104
    assert c22 == {"survive": 92, "binary": 12}, c22
    assert len(s22) == 92
    assert len({canonical(m) for m in s22}) == 24
    assert Counter(m[8] for m in s22) == {1: 4, 2: 28, 3: 36,
                                         4: 20, 6: 4}
    assert sum(eligible_six_tree_cells(m) for m in old22) == 4
    assert not any(eligible_six_tree_cells(m) for m in s22)
    assert (1, 1, 2, 1, 1, 6, 4, 4, 2) in old22
    assert (1, 1, 2, 1, 1, 6, 4, 4, 2) not in s22
    print("PASS n22 104 -> 92 necessary profiles / 24 symmetry orbits")
    print("PASS all 4 previously eligible n22 sharp six-cell targets excluded")
    print("PASS n22 center histogram", dict(sorted(Counter(m[8] for m in s22).items())))

    old23, c23, s23 = new_frontier(23)
    assert len(old23) == 1392
    assert c23 == {"survive": 1348, "binary": 28, "triple": 16}, c23
    assert len({canonical(m) for m in s23}) == 346
    assert sum(eligible_six_tree_cells(m) for m in old23) == 140
    assert sum(eligible_six_tree_cells(m) for m in s23) == 128
    assert len({canonical(m) for m in s23 if eligible_six_tree_cells(m)}) == 33
    print("PASS n23 1392 -> 1348 necessary profiles / 346 symmetry orbits")
    print("PASS n23 eligible six-cell CSP targets 140 -> 128, in 33 orbits")

    # Strictly sound monotonicity: a transfer may never REJECT a matrix
    # already classified by the previous Stage28 collector gate.
    for n in (21, 22, 23):
        for m in matrices(n):
            if collector_gate(m) != "survive":
                assert transfer_gate(m) != "survive", (
                    "new gate does not subsume prior gate", m)
    print("PASS Stage31 transfer gate subsumes Stage28 on all raw n21..23")
    print("LIMIT: bound conditional on source-local privacy collector forcing and")
    print("LIMIT: prior Stage28 all-n HUMAN proof; no global schedule enumeration")
    print("LIMIT: main 2n-3 temporal clique spanner conjecture remains OPEN")


if __name__ == "__main__":
    main()
