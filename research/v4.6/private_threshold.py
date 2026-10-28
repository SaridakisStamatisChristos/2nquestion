"""Stage 29: exact all-c minimum private recipients for (1,1,c) tree covers.

Full proof in PRIVATE_THRESHOLD_THEOREM.md:
c=2,3: 2 private; c=4,5: 1 private; c>=6: 0 private.
Independent Prüfer small-tree regression and universal explicit family constructor.
"""
from collections import Counter
from itertools import permutations, product


def replay(n, contacts):
    knowledge = [1 << i for i in range(n)]
    seen = set()
    parent = list(range(n))

    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i

    for a, b in contacts:
        assert 0 <= a < n and 0 <= b < n and a != b
        edge = tuple(sorted((a, b)))
        assert edge not in seen
        seen.add(edge)
        ra, rb = root(a), root(b)
        assert ra != rb, "static cycle"
        parent[ra] = rb
        mask = knowledge[a] | knowledge[b]
        knowledge[a] = knowledge[b] = mask
    assert len(seen) == n - 1
    assert len({root(i) for i in range(n)}) == 1
    return knowledge


def private_vertices(knowledge, C):
    private = set()
    for secret in range(len(knowledge)):
        holders = [v for v in C if (knowledge[v] >> secret) & 1]
        assert holders, ("not a collective cover", secret)
        if len(holders) == 1:
            private.add(holders[0])
    return private


def minimum(c):
    assert c >= 2
    return 2 if c <= 3 else 1 if c <= 5 else 0


def root_side(root, recipients):
    """Root full; group private minima 1,1,0 for lengths 1,2,>=3."""
    a = recipients[0]
    if len(recipients) == 1:
        return [(root, a)]
    b = recipients[1]
    if len(recipients) == 2:
        return [(a, b), (root, a)]
    d = recipients[2]
    return ([(z, a) for z in recipients[3:]] +
            [(root, a), (b, d), (root, b)])


def sharp_history(c):
    """Two rooted chronological trees then their single final connecting edge."""
    assert c >= 2
    left_size = 1 if c <= 4 else 2 if c == 5 else 3
    left = list(range(2, 2 + left_size))
    right = list(range(2 + left_size, c + 2))
    history = root_side(0, left) + root_side(1, right) + [(0, 1)]
    assert len(history) == c + 1
    return history


def test_construction(c):
    n = c + 2
    history = sharp_history(c)
    k = replay(n, history)
    complete = (1 << n) - 1
    assert k[0] == k[1] == complete
    C = range(2, n)
    priv = private_vertices(k, C)
    assert len(priv) == minimum(c), (c, priv)
    if c >= 6:
        assert all(sum((k[v] >> s) & 1 for v in C) >= 2
                   for s in range(n))
    return len(priv)


def independent_small_enumeration():
    """All labelled trees and original chronological orders, n=3..5."""
    checked = Counter()
    for n in (3, 4, 5):
        for word in product(range(n), repeat=n-2):
            degree = [1] * n
            for x in word:
                degree[x] += 1
            edges = []
            for x in word:
                leaf = next(i for i in range(n) if degree[i] == 1)
                edges.append((leaf, x))
                degree[leaf] -= 1
                degree[x] -= 1
            edges.append(tuple(i for i, v in enumerate(degree) if v == 1))
            if (0, 1) not in {tuple(sorted(e)) for e in edges}:
                continue
            rest = [e for e in edges if tuple(sorted(e)) != (0, 1)]
            for order in permutations(rest):
                k = replay(n, list(order) + [(0, 1)])
                full = (1 << n) - 1
                if k[0] != full or k[1] != full:
                    continue
                try:
                    priv = private_vertices(k, range(2, n))
                except AssertionError:
                    continue
                checked[n] += 1
                if n >= 4:
                    assert len(priv) >= minimum(n-2), (n, order, priv)
    assert checked[4] > 0 and checked[5] > 0
    return checked


def main():
    print("PASS Prüfer independent n=3..5 eligible census",
          dict(independent_small_enumeration()))
    for c in list(range(2, 22)) + [24, 40]:
        p = test_construction(c)
        print("PASS exact group sizes (1,1,%d): private_minimum=%d" % (c, p))
    print("PASS sharp all-c construction, zero-private exactly when c>=6")
    print("LIMIT: all-c lower bound rests on last-edge human proof, not finite tests")
    print("LIMIT: no global both-cyclic chronology, no 2n-3 temporal-spanner proof")


if __name__ == "__main__":
    main()
