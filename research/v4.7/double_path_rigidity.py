"""Stage 30: sharp six-recipient double-path information-support rigidity.

All-n theorem is a human proof in DOUBLE_PATH_RIGIDITY.md.
This script independently enumerates every chronological labelled tree on n=4..6
with root 0, group C={1,2,3}, and arbitrary other helper nodes, verifying the
forced last-call normal form. It exhausts all 90 labelled 2P3 structures on
six recipients, all 8100 pairs, and all 15 two-point transversals per structure.
"""
from collections import Counter
from itertools import combinations, permutations, product


def replay(n, seq):
    k = [1 << i for i in range(n)]
    for a, b in seq:
        union = k[a] | k[b]
        k[a] = k[b] = union
    return k


def components(n, seq):
    parents = list(range(n))

    def root(v):
        while parents[v] != v:
            v = parents[v]
        return v

    for a, b in seq:
        ra, rb = root(a), root(b)
        assert ra != rb
        parents[ra] = rb
    return [root(i) for i in range(n)]


def prove_local_shape(n, seq):
    """Check only genuine rooted double-cover instances, not arbitrary trees."""
    k = replay(n, seq)
    C = (1, 2, 3)
    if k[0] != (1 << n) - 1:
        return False
    if any(sum((k[v] >> s) & 1 for v in C) < 2 for s in range(n)):
        return False
    assert len(seq) == n - 1
    assert 0 in seq[-1]
    w = seq[-1][0] if seq[-1][1] == 0 else seq[-1][1]
    assert w in C
    component = components(n, seq[:-1])
    assert component[0] != component[w]
    rootC = [x for x in C if component[x] == component[0]]
    otherC = [x for x in C if component[x] == component[w] and x != w]
    assert len(rootC) == len(otherC) == 1
    z, d = rootC[0], otherC[0]
    side_r = [e for e in seq[:-1] if component[e[0]] == component[0]]
    side_w = [e for e in seq[:-1] if component[e[0]] == component[w]]
    assert side_r and side_w
    assert set(side_r[-1]) == {0, z}
    assert set(side_w[-1]) == {w, d}
    assert {v for v in C if k[v] & 1} == {z, w}
    assert {v for v in C if k[v] & (1 << w)} == {w, d}
    return True


def prufer_edges(n, word):
    degree = [1] * n
    for v in word:
        degree[v] += 1
    out = []
    for v in word:
        leaf = next(i for i, x in enumerate(degree) if x == 1)
        out.append((leaf, v))
        degree[leaf] -= 1
        degree[v] -= 1
    out.append(tuple(i for i, x in enumerate(degree) if x == 1))
    return out


def exact_rooted_regression():
    observed = Counter()
    for n in (4, 5, 6):
        for word in product(range(n), repeat=n - 2):
            edges = prufer_edges(n, word)
            for order in permutations(edges):
                observed[n] += int(prove_local_shape(n, order))
        assert observed[n] > 0
    assert observed == {4: 12, 5: 72, 6: 864}, observed
    return observed


def two_paths():
    vertices = set(range(6))
    shapes = set()
    for left_tuple in combinations(range(6), 3):
        left = set(left_tuple)
        right = vertices - left
        if min(left) > min(right):
            continue
        for a in left:
            for b in right:
                edges = frozenset(
                    [frozenset((a, v)) for v in left if v != a] +
                    [frozenset((b, v)) for v in right if v != b]
                )
                shapes.add(edges)
    assert len(shapes) == 90

    # Exact minimal and upward-closed opposite target-support domain.
    for E in shapes:
        allowed = [frozenset(v for v in range(6) if (mask >> v) & 1)
                   for mask in range(1, 1 << 6)
                   if all(any((mask >> v) & 1 for v in edge) for edge in E)]
        assert len(allowed) == 25, (E, len(allowed))
        minimal = [h for h in allowed if not any(g < h for g in allowed)]
        assert sorted(map(len, minimal)) == [2, 3, 3, 4]
        assert Counter(map(len, allowed)) == {2: 1, 3: 6, 4: 11, 5: 6, 6: 1}
        assert sum(len(h) == 2 for h in allowed) == 1
        assert all(any(base <= h for base in minimal) for h in allowed)
        assert all(any(base <= h for base in minimal) ==
                   all(h & edge for edge in E)
                   for h in [frozenset(v for v in range(6)
                                       if (mask >> v) & 1)
                             for mask in range(1, 1 << 6)])

    compatible = sum(
        all(a & b for a in E for b in F)
        for E in shapes for F in shapes
    )
    assert compatible == 0
    return len(shapes), len(shapes) ** 2, compatible


def check_marked_outer(extra_helpers):
    """Actual 8 marked original vertices, arbitrary helper leaves."""
    n = 8 + extra_helpers
    calls = ([(z, 3) for z in range(8, n)] +
             [(0, 3), (2, 4), (0, 2),
              (1, 6), (5, 7), (1, 5), (0, 1)])
    assert len(calls) == n - 1
    know = replay(n, calls)
    assert know[0] == know[1] == (1 << n) - 1
    C = tuple(range(2, 8))
    assert all(sum((know[v] >> s) & 1 for v in C) >= 2
               for s in range(n))
    expected = {
        0: {2, 3}, 2: {2, 4},
        1: {5, 6}, 5: {5, 7},
    }
    for secret, holders in expected.items():
        actual = {v for v in C if (know[v] >> secret) & 1}
        assert actual == holders, (extra_helpers, secret, actual)
    return True


def main():
    counts = exact_rooted_regression()
    print("PASS local rooted three-recipient double-cover shape:", dict(counts))
    n, pairs, zero = two_paths()
    print("PASS 2P3 families:", n, "ordered pairs:", pairs,
          "all-cross compatible:", zero)
    print("PASS exact target support domain: 25/63 nonempty masks; "
          "4 minimal transversals of sizes 2,3,3,4")
    for helpers in (0, 1, 2, 3, 4, 8, 16):
        assert check_marked_outer(helpers)
        print("PASS marked eight-recipient normal form with helpers", helpers)
    print("LIMIT: exact local proof, not full 2n-4 global gossip chronology")
    print("LIMIT: midpoint no-go assumes TWO six-cell zero-private TREES")
    print("LIMIT: main temporal-clique 2n-3 conjecture remains OPEN")


if __name__ == "__main__":
    main()
