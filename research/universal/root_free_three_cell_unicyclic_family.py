"""All-width root-free UNICYCLIC local component, double-covering A,B,X.

Chronological edges are used once; final distinct edge closes a cycle A--B.
This is a LOCAL component, NOT a successful global gossip chronology.
"""


def equality_tree(s):
    if s == 1:
        return 1, [], 0, [set([0])]
    n, edges, root, groups = equality_tree(s - 1)
    groups_new = [{root}, {root + n}]
    groups_new.extend(groups[i] | {x + n for x in groups[i]}
                      for i in range(1, s - 1))
    return 2 * n, edges + [(a + n, b + n) for a, b in edges] + [
        (root, root + n)
    ], root, groups_new


def family(k):
    """For k>=0 construct 64+k vertex tree then final exterior cycle call."""
    assert isinstance(k, int) and k >= 0
    n, tree, r, groups = equality_tree(6)
    assert n == 32 and [len(x) for x in groups] == [1, 1, 2, 4, 8, 16]
    a0 = groups[0] | groups[2]
    b0 = groups[1] | groups[3]
    x0 = groups[4] | groups[5]
    L = set(range(n))
    R = set(range(n, 2 * n))
    extras = set(range(2 * n, 2 * n + k))
    A = a0 | {n + x for x in a0}
    B = b0 | {n + x for x in b0}
    X = x0 | {n + x for x in x0} | extras
    assert A | B | X == L | R | extras and not (A & B or A & X or B & X)
    # The new leaf's secret first joins r in L, so its future recipients
    # are all the people who get the old r secret, for every old group.
    leaves = [(r, w) for w in sorted(extras)]
    local = leaves + tree + [(a + n, b + n) for a, b in tree]
    e_l, e_r = min(x0), min(x0) + n
    d_a, d_b = min(groups[2]), min(groups[3]) + n
    assert e_l in X and e_r in X and d_a in A and d_b in B
    edges = local + [(e_l, e_r)] + [(d_a, d_b)]
    return A, B, X, edges


def replay(n, calls):
    masks = [1 << i for i in range(n)]
    for a, b in calls:
        x = masks[a] | masks[b]
        masks[a] = masks[b] = x
    return masks


def check(k):
    A, B, X, edges = family(k)
    n = 64 + k
    assert len(edges) == n and len(A) == 6 and len(B) == 10
    assert len(X) == 48 + k
    all_edges = [frozenset(x) for x in edges]
    assert len(set(all_edges)) == len(all_edges)
    parent = list(range(n))
    def root(i):
        while i != parent[i]:
            i = parent[i]
        return i
    for a, b in edges[:-1]:
        x, y = root(a), root(b)
        assert x != y
        parent[x] = y
    assert len({root(i) for i in range(n)}) == 1
    assert edges[-1][0] in A and edges[-1][1] in B
    pre = replay(n, edges[:-1])
    post = replay(n, edges)
    for x in X:
        assert pre[x] == post[x], "Exterior cycle closure changed X information"
    mask = (1 << n) - 1
    assert all(know != mask for know in pre)
    assert all(know != mask for know in post)
    for C in (A, B, X):
        for secret in range(n):
            count = sum((post[v] >> secret) & 1 for v in C)
            assert count >= 2, (k, secret, len(C), count)
    return n, len(A), len(B), len(X)


def main():
    vals = [0, 1, 2, 4, 8, 16, 32, 64]
    for k in vals:
        check(k)
    print("PASS: 8 root-free original-order unicyclic three-cell 2-cover histories;",
          "largest center", 48 + max(vals), "; all unordered contacts edge-once")


if __name__ == "__main__":
    main()
