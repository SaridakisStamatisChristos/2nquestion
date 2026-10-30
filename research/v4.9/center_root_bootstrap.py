"""Stage32 universal center-root capacity bootstrap, n22 necessary matrix reduction.

Lemma: In an edge-once unicyclic chronology whose FINAL edge joins exterior
cells A,B outside center X, >=2 complete terminal A collectors PLUS >=1
complete X collector FORCE the final edge B endpoint to be complete.
Combining the existing all-n Stage28 theorem and offcorner double-carrier
assumptions: A+B<=8 and >=2 full collectors in either exterior cell forbid
ANY complete center collector. No extrapolated privacy minima.

This is a conditional proof and sound necessary incidence classifier, never
a full global min-gossip schedule search or temporal-clique 2n-3 solution.
"""
from collections import Counter
from itertools import permutations, product, combinations
from pathlib import Path
import sys

RESEARCH = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RESEARCH / "v4.4"))
sys.path.insert(0, str(RESEARCH / "v4.5"))
from n22_3x3_frontier import matrices, privacy, canonical, stage25, stage26  # noqa: E402
from unbounded_eight_outside_audit import collector_gate  # noqa: E402


def center_blocked(cell_sizes, certified_roots):
    """ALL-n sufficient no-center-root rule (not a converse)."""
    if sum(cell_sizes) > 8:
        return False
    a, b = certified_roots
    return a >= 2 or b >= 2 or (a >= 1 and b >= 1)


def new_gate(m, inferred=None):
    """Optional custom minima for independent adversarial tests."""
    q, p = privacy(m) if inferred is None else inferred
    bq = center_blocked((m[2], m[5]), q)
    bp = center_blocked((m[6], m[7]), p)
    x = m[8]
    if x == 1 and (bq or bp):
        return "singleton_center"
    if x in (2, 3) and bq and bp:
        return "two_or_three_center"
    return "survive"


def prufer_edges(n, word):
    deg = [1] * n
    for i in word:
        deg[i] += 1
    edges = []
    for x in word:
        leaf = next(i for i, d in enumerate(deg) if d == 1)
        edges.append(tuple(sorted((leaf, x))))
        deg[leaf] -= 1
        deg[x] -= 1
    edges.append(tuple(i for i, d in enumerate(deg) if d == 1))
    return tuple(edges)


def replay(n, chronology):
    info = [1 << i for i in range(n)]
    for a, b in chronology:
        u = info[a] | info[b]
        info[a] = info[b] = u
    return {i for i, mask in enumerate(info) if mask == (1 << n) - 1}


def exhaustive_local_transfer():
    """Independent ALL n4,n5 labelled chronological tree+last cycle checks.

    Partitions include all A/B/X assignments with e in A×B,
    and A>=2,X>=1. Does NOT assume full-gossip crossing, double cover,
    fixed 3x3 geometry, or Stage28.
    """
    cases, triggering = Counter(), Counter()
    for n in (4, 5):
        verts = range(n)
        for prufer in product(verts, repeat=n-2):
            tree = prufer_edges(n, prufer)
            edgeset = set(tree)
            for e in combinations(verts, 2):
                if e in edgeset:
                    continue
                for order in permutations(tree):
                    full = replay(n, order + (e,))
                    # A,B,X partition: final edge a-b, X disjoint.
                    a, b = e
                    leftover = set(verts) - set(e)
                    for alloc in product(("A", "B", "X"), repeat=len(leftover)):
                        A, B, X = {a}, {b}, set()
                        for v, label in zip(sorted(leftover), alloc):
                            {"A": A, "B": B, "X": X}[label].add(v)
                        if len(A) < 2 or not X:
                            continue
                        cases[n] += 1
                        if len(A & full) >= 2 and X & full:
                            triggering[n] += 1
                            assert b in full, (n, order, e, A, B, X, full)
    assert cases == {4: 576, 5: 216000}, cases
    assert triggering == {4: 48, 5: 4320}, triggering
    print("PASS all n4/5 original local chronologies, cases", dict(cases),
          "antecedent-triggered", dict(triggering))


def census(n):
    earlier = [m for m in matrices(n) if
               stage25(m) == stage26(m) == collector_gate(m) == "survive"]
    by_reason = Counter(new_gate(m) for m in earlier)
    remain = [m for m in earlier if new_gate(m) == "survive"]
    return earlier, by_reason, remain


def main():
    assert center_blocked((3, 5), (2, 0))
    assert center_blocked((5, 3), (0, 2))
    assert not center_blocked((4, 5), (2, 0))
    assert not center_blocked((3, 5), (1, 0))
    assert center_blocked((4, 4), (1, 1))
    exhaustive_local_transfer()

    e21, a21, s21 = census(21)
    assert len(e21) == 0 and not s21
    print("PASS prior n21 necessary-incidence closure")

    e22, a22, s22 = census(22)
    assert len(e22) == 104
    assert a22 == {"two_or_three_center": 68,
                   "singleton_center": 4, "survive": 32}, a22
    assert len(s22) == 32
    assert len({canonical(m) for m in s22}) == 9
    assert Counter(m[8] for m in s22) == {3: 8, 4: 20, 6: 4}
    assert all(m[8] >= 3 for m in s22)
    assert all(m[8] != 2 for m in s22)
    print("PASS n22 104 -> 32 necessary profiles / 9 symmetry orbits")
    print("PASS NO center-width-1 or -2 necessary survivors")

    e23, a23, s23 = census(23)
    assert len(e23) == 1392
    assert a23 == {"survive": 804, "two_or_three_center": 504,
                   "singleton_center": 84}, a23
    assert len(s23) == 804
    assert len({canonical(m) for m in s23}) == 209
    print("PASS n23 1392 -> 804 necessary profiles / 209 orbits")

    # Monotonic dominance of previous all-n collector blocking.
    for n in (21, 22, 23):
        for m in matrices(n):
            if collector_gate(m) != "survive":
                assert new_gate(m) != "survive", m
    print("PASS new blocking condition subsumes prior Stage28 for n21..23")
    print("LIMIT: no n22 full original forest theorem, chronology SAT,")
    print("LIMIT: publication priority or direct 2n-3 temporal-spanner proof")


if __name__ == "__main__":
    main()
