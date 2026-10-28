"""Stage 19: standalone replay of a locally admissible but globally blocked P3.

A P3-only ten-call unicyclic history has 2-fold offcorner coverage and
complete collective center coverage, but FOUR DISTINCT center singleton
secret carriers. Stage 19 proves an actual both-cyclic original split can
have at most two. A local example is NOT a global counterexample.
"""
from itertools import product


CALLS = ((5, 0), (1, 9), (7, 4), (0, 9), (8, 3),
         (4, 0), (6, 2), (3, 2), (2, 4), (0, 3))


def replay(n, calls):
    k = [1 << i for i in range(n)]
    edge_set = set()
    for u, v in calls:
        assert 0 <= u < n and 0 <= v < n and u != v
        edge = tuple(sorted((u, v)))
        assert edge not in edge_set
        edge_set.add(edge)
        k[u] = k[v] = k[u] | k[v]
    return k, edge_set


def connected(n, edges):
    p = list(range(n))

    def root(x):
        while p[x] != x:
            x = p[x]
        return x

    for a, b in edges:
        p[root(a)] = root(b)
    return len({root(i) for i in range(n)}) == 1


def check_local():
    n = 10
    k, edges = replay(n, CALLS)
    assert len(edges) == n and connected(n, edges)
    assert CALLS[-1] == (0, 3)
    assert len(edges - {tuple(sorted(CALLS[-1]))}) == n - 1
    assert connected(n, edges - {tuple(sorted(CALLS[-1]))})
    group1, group2, center = range(3), range(3, 6), range(6, 10)
    for secret in range(n):
        assert sum(bool(k[x] & (1 << secret)) for x in group1) >= 2
        assert sum(bool(k[x] & (1 << secret)) for x in group2) >= 2
        assert sum(bool(k[x] & (1 << secret)) for x in center) == 1
    assert [k[x] for x in center] == [
        (1 << 2) | (1 << 6),
        (1 << 4) | (1 << 7),
        (1 << 3) | (1 << 8),
        (1 << 0) | (1 << 1) | (1 << 5) | (1 << 9),
    ]
    d_a = {x for x in center if any(
        sum(bool(k[y] & (1 << secret)) for y in center) == 1
        and (k[x] & (1 << secret)) for secret in range(n))}
    assert d_a == set(center), d_a
    print("PASS 10-person connected unicyclic chronology: two complete"
          " offcorner two-fold covers, collective four-person center, "
          "FOUR singleton center positions")
    print("CERTIFIED LIMIT: not extendible to a successful both-cyclic original"
          " 3x3 chronology under the Stage 19 center collector-capacity theorem")


def all_families(width):
    choices = list(range(1, 1 << width))
    for length in (1, 2, 3):
        yield from product(choices, repeat=length)


def complete_points(supports, width):
    return {i for i in range(width) if
            all(mask & (1 << i) for mask in supports)}


def verify_boolean():
    for width in (2, 3):
        fs = list(all_families(width))
        checked = crossing = 0
        for a in fs:
            private_a = {
                mask.bit_length() - 1 for mask in a
                if mask.bit_count() == 1
            }
            for b in fs:
                checked += 1
                if not all(x & y for x in a for y in b):
                    continue
                crossing += 1
                assert private_a <= complete_points(b, width)
                private_b = {
                    mask.bit_length() - 1 for mask in b
                    if mask.bit_count() == 1
                }
                assert private_b <= complete_points(a, width)
                # Model the real chronological final-cycle argument by
                # restricting opposite complete CENTER points to <=2.
                if len(complete_points(b, width)) <= 2:
                    assert len(private_a) <= 2
                if len(complete_points(a, width)) <= 2:
                    assert len(private_b) <= 2
        print(f"PASS exhaustive width={width} support crossing:"
              f" {crossing}/{checked} exact pairs")


if __name__ == "__main__":
    check_local()
    verify_boolean()
    print("LIMIT: support enumeration corroborates a human all-n implication,"
          " not existence of a complete gossip schedule")
