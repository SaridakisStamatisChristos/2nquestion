"""Stage33: exact all-size zero-private threshold for recipient sizes (a,b,2).

Claim: a valid edge-once chronological tree with three disjoint collectively
complete groups G1,G2,C of sizes (a,b,2) and ZERO private C members exists
IFF a>=2,b>=2,a+b>=6, even when arbitrary helpers are permitted in the
NECESSITY direction. The constructed SUFFICIENCY has no helpers.

Only a conservative +1 private lower bound is derived for the impossible
zero-private parameter cells. No reordering of original gossip calls.
"""
from collections import Counter
from pathlib import Path
import sys

research = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(research / "v4.4"), str(research / "v4.5"),
                str(research / "v4.9")]
from n22_3x3_frontier import matrices, stage25, stage26, privacy, canonical  # noqa: E402
from unbounded_eight_outside_audit import collector_gate  # noqa: E402
from center_root_bootstrap import new_gate as stage32_gate  # noqa: E402


def private_two_lower_bound(a, b, c):
    if c == 2 and (a == 1 or b == 1 or a + b < 6):
        return 1
    return 0


def improved_privacy(m):
    original_q, original_p = privacy(m)
    q = tuple(max(original_q[i],
                  private_two_lower_bound(m[3*i], m[3*i+1], m[3*i+2]))
              for i in range(2))
    p = tuple(max(original_p[j],
                  private_two_lower_bound(m[j], m[3+j], m[6+j]))
              for j in range(2))
    return q, p


def extended_gate(m):
    return stage32_gate(m, inferred=improved_privacy(m))


def rooted_side(root, a_group, b_group):
    assert min(len(a_group), len(b_group)) >= 1
    assert len(a_group) + len(b_group) >= 3
    if len(a_group) >= 2:
        big, singleton = a_group, b_group
    else:
        big, singleton = b_group, a_group
    g = singleton[0]
    z1, z2 = big[:2]
    extra = big[2:] + singleton[1:]
    # New leaves send their own secrets toward the root before the base
    # three calls. Neither opposite designated group loses information.
    return [(z, root) for z in extra] + [
        (root, z1), (g, z2), (root, g)]


def sharp_construction(a, b):
    """For ALL a,b>=2,a+b>=6, both members C={0,1} complete and private-free."""
    assert a >= 2 and b >= 2 and a + b >= 6
    a1, b1 = (1, 2) if b >= 3 else (2, 1)
    a2, b2 = a - a1, b - b1
    assert min(a1, b1, a2, b2) >= 1
    assert a1 + b1 >= 3 and a2 + b2 >= 3
    A = list(range(2, 2 + a))
    B = list(range(2 + a, 2 + a + b))
    calls = rooted_side(0, A[:a1], B[:b1])
    calls += rooted_side(1, A[a1:], B[b1:])
    calls += [(0, 1)]
    return calls, (A, B, [0, 1])


def replay(a, b, calls, groups):
    n = a + b + 2
    knowledge = [1 << i for i in range(n)]
    parents = list(range(n))

    def root(x):
        while parents[x] != x:
            x = parents[x]
        return x

    edges = set()
    for x, y in calls:
        edge = tuple(sorted((x, y)))
        assert x != y and edge not in edges
        assert root(x) != root(y), "static cycle"
        parents[root(x)] = root(y)
        edges.add(edge)
        union = knowledge[x] | knowledge[y]
        knowledge[x] = knowledge[y] = union
    assert len(edges) == n - 1
    assert len({root(i) for i in range(n)}) == 1
    full = (1 << n) - 1
    assert knowledge[0] == knowledge[1] == full
    assert all(any(knowledge[v] & (1 << s) for v in G)
               for G in groups for s in range(n))
    assert all(sum(bool(knowledge[v] & (1 << s)) for v in groups[2]) == 2
               for s in range(n))


def independent_construction_audit():
    total = 0
    for a in range(2, 12):
        for b in range(2, 12):
            if a + b < 6:
                continue
            calls, groups = sharp_construction(a, b)
            replay(a, b, calls, groups)
            total += 1
    assert total == 97
    assert private_two_lower_bound(1, 1000, 2) == 1
    assert private_two_lower_bound(2, 3, 2) == 1
    assert private_two_lower_bound(2, 4, 2) == 0
    assert private_two_lower_bound(3, 3, 2) == 0
    assert private_two_lower_bound(3, 4, 3) == 0
    print("PASS 97 explicit tree chronologies across (a,b) up to 11")
    print("PASS unlimited singleton-side and <=5 opposite-recipient necessity")


def census(n):
    previous = [m for m in matrices(n)
                if stage25(m) == stage26(m) ==
                collector_gate(m) == stage32_gate(m) == "survive"]
    counts = Counter(extended_gate(m) for m in previous)
    survivors = [m for m in previous if extended_gate(m) == "survive"]
    return previous, counts, survivors


def main():
    independent_construction_audit()

    old21, c21, s21 = census(21)
    assert not old21 and not s21
    print("PASS prior n21 exact zero-survivor regression")

    old22, c22, s22 = census(22)
    assert len(old22) == 32
    assert c22 == {"survive": 24, "two_or_three_center": 8}, c22
    assert len(s22) == 24
    assert len({canonical(m) for m in s22}) == 7
    assert Counter(m[8] for m in s22) == {4: 20, 6: 4}
    assert not any(m[8] <= 3 for m in s22)
    print("PASS n22 32 -> 24 necessary matrices, 7 row/column orbits")
    print("PASS all centers n22 >=4 after all-n privacy extension")

    old23, c23, s23 = census(23)
    assert len(old23) == 804
    assert c23 == {"survive": 732, "two_or_three_center": 72}, c23
    assert len(s23) == 732
    assert len({canonical(m) for m in s23}) == 191
    print("PASS n23 804 -> 732 necessary matrices, 191 orbits")

    # Privacy extension never lowers an existing exact certified minimum.
    for n in (21, 22, 23):
        for m in matrices(n):
            q0, p0 = privacy(m)
            q1, p1 = improved_privacy(m)
            assert all(x >= y for x, y in zip(q1 + p1, q0 + p0))
            if stage32_gate(m) != "survive":
                assert extended_gate(m) != "survive", m
    print("PASS privacy minima and Stage32 necessary gate monotonicity")
    print("LIMIT: all-n human tree lemma and finite replay are separate;")
    print("LIMIT: n22 original-half forest and 2n-3 spanner conjecture OPEN")


if __name__ == "__main__":
    main()
