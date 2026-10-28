"""Exact labelled chronological-tree rigidity falsification and sharp constructions.

No external solver. Each tested call is a distinct edge of a labelled tree.
Tests equality for disjoint designated recipient groups with unused helpers.
Finite verification does not prove the all-n induction.
"""
from itertools import combinations, permutations, product
from functools import reduce
from collections import Counter


def prufer_edges(seq, n):
    deg = [1] * n
    for v in seq:
        deg[v] += 1
    edges = []
    for v in seq:
        leaf = next(i for i in range(n) if deg[i] == 1)
        edges.append((leaf, v))
        deg[leaf] -= 1
        deg[v] -= 1
    a, b = [i for i in range(n) if deg[i] == 1]
    return edges + [(a, b)]


def replay(n, calls):
    know = [1 << i for i in range(n)]
    for u, v in calls:
        know[u] = know[v] = know[u] | know[v]
    return know


def exhaustive(nmax=5):
    counts = Counter()
    for n in range(2, nmax + 1):
        for code in product(range(n), repeat=n - 2):
            edges = prufer_edges(code, n)
            for chronology in permutations(edges):
                know = replay(n, chronology)
                full = (1 << n) - 1
                for s in (2, 3):
                    minimum = 1 << (s - 1)
                    if n < minimum:
                        continue
                    for chosen in combinations(range(n), minimum):
                        for assignment in product(range(s), repeat=minimum):
                            if len(set(assignment)) != s:
                                continue
                            groups = [[chosen[i] for i, j in enumerate(assignment) if j == g]
                                      for g in range(s)]
                            if any(reduce(int.__or__, (know[v] for v in group), 0) != full
                                   for group in groups):
                                continue
                            counts[(n, s)] += 1
                            for group in groups:
                                for v in group:
                                    private = any(
                                        ((know[v] >> secret) & 1)
                                        and all(not ((know[w] >> secret) & 1)
                                                for w in group if w != v)
                                        for secret in range(n)
                                    )
                                    assert private, (n, chronology, groups, know, v)
                            assert sum(len(group) == 1 for group in groups) == 2
                            singles = {group[0] for group in groups if len(group) == 1}
                            actual_full = {v for v in range(n) if know[v] == full}
                            assert singles == actual_full, (n, chronology, groups, know)
    assert counts == {
        (2, 2): 2, (3, 2): 12,
        (4, 2): 144, (4, 3): 144,
        (5, 2): 2880, (5, 3): 4320,
    }, counts
    return counts


def tight_groups(labels, offset=0):
    if len(labels) == 1:
        return [(offset, labels[0])], [], offset + 1, offset
    if len(labels) == 2:
        return [(offset, labels[0]), (offset + 1, labels[1])], [(offset, offset + 1)], offset + 2, offset
    left, e_left, middle, r_left = tight_groups([labels[0]] + labels[2:], offset)
    right, e_right, stop, r_right = tight_groups([labels[1]] + labels[2:], middle)
    return left + right, e_left + e_right + [(r_left, r_right)], stop, r_left


def sharp_two_helper_cut(s):
    p1, e1, m1, _ = tight_groups(list(range(s)))
    p2, e2, m2, _ = tight_groups(list(range(s)), m1)
    h1, h2 = m2, m2 + 1
    calls = [(h1, p1[0][0])] + e1 + [(h2, p2[0][0])] + e2 + [(h1, h2)]
    know = replay(m2 + 2, calls)
    groups = {g: [v for v, label in p1 + p2 if label == g] for g in range(s)}
    full = (1 << (m2 + 2)) - 1
    assert all(reduce(int.__or__, (know[v] for v in group), 0) == full
               for group in groups.values())
    assert sum(len(group) for group in groups.values()) == 2 ** s
    return len(calls)


def one_sided_local_boundary():
    # Exactly eight designated recipients in four groups, and four helpers.
    # Last cycle edge joins helpers; local group cover still complete.
    assigned, tree, n, _ = tight_groups([0, 1, 2, 3])
    outsiders = list(range(n, n + 4))
    calls = [(v, assigned[0][0]) for v in outsiders] + tree + [(outsiders[0], outsiders[1])]
    assert len(calls) == n + 4
    assert len({tuple(sorted(e)) for e in calls}) == len(calls)
    know = replay(n + 4, calls)
    full = (1 << (n + 4)) - 1
    groups = [[v for v, g in assigned if g == j] for j in range(4)]
    assert [len(g) for g in groups] == [1, 1, 2, 4]
    assert all(reduce(int.__or__, (know[v] for v in group), 0) == full
               for group in groups)
    return len(calls)


if __name__ == "__main__":
    print("PASS exhaustive helper equality:", dict(sorted(exhaustive().items())))
    for s in range(2, 7):
        calls = sharp_two_helper_cut(s)
        print(f"PASS terminal helper cut: groups={s} recipients={1<<s} calls={calls}")
    print("PASS local one-sided 4-group / 8-recipient unicyclic boundary:",
          one_sided_local_boundary(), "distinct calls")
    print("LIMIT: no global gossip counterexample; all-n claims rely on the human induction")
