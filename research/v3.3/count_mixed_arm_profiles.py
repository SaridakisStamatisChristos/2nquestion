"""Stage 16: independent incidence counting and rooted equality stress test.

Exhaustively enumerate every labelled positive 3x3 baseline occupancy for
n=13..26, and separately count by pair-category generating functions.
These are NECESSARY profiles, not complete chronological gossip schedules.
"""
from itertools import product
from math import comb


def bins(total, count):
    if count == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in bins(total - first, count - 1):
            yield (first,) + rest


def threshold(a, b):
    a0 = a == (0, 0)
    b0 = b == (0, 0)
    if a0 and b0:
        return 64
    if a0:
        return 16 if 0 in b else 9
    if b0:
        return 16 if 0 in a else 9
    return 1


def direct(n):
    count = 0
    for extra in bins(n - 13, 9):
        a = (extra[2], extra[5])
        b = (extra[6], extra[7])
        if extra[8] + 1 >= threshold(a, b):
            count += 1
    return count


def coefficients(category, k):
    if category == 0:
        return {0: 1}
    if category == 1:
        return {s: 2 for s in range(1, k + 1)}
    if category == 2:
        return {s: s - 1 for s in range(2, k + 1)}
    raise AssertionError(category)


def symbolic(n):
    k = n - 13
    if k < 0:
        return 0
    pair_series = [coefficients(i, k) for i in range(3)]
    total = 0
    for aclass in range(3):
        for bclass in range(3):
            lower = (64 if aclass == 0 and bclass == 0
                     else 16 if ((aclass == 0 and bclass == 1) or
                                  (aclass == 1 and bclass == 0))
                     else 9 if (aclass == 0 or bclass == 0)
                     else 1)
            for ea, ca in pair_series[aclass].items():
                for eb, cb in pair_series[bclass].items():
                    remaining = k - ea - eb - (lower - 1)
                    if remaining >= 0:
                        # Four unrestricted corners and one center variable.
                        total += ca * cb * comb(remaining + 4, 4)
    return total


def stage15_filter(n):
    k = n - 13
    if k < 0:
        return 0
    choose = lambda a, b: comb(a, b) if a >= b >= 0 else 0
    return (choose(k + 8, 8)
            - 2 * choose(k + 6, 6)
            + 2 * choose(k - 2, 6)
            + choose(k + 4, 4)
            - 2 * choose(k - 4, 4)
            + choose(k - 59, 4))


def tight_tree(labels, start=0):
    if len(labels) == 1:
        return [(start, labels[0])], [], start + 1, start
    if len(labels) == 2:
        return ([(start, labels[0]), (start + 1, labels[1])],
                [(start, start + 1)], start + 2, start)
    left, eleft, middle, u = tight_tree([labels[0]] + labels[2:], start)
    right, eright, finish, v = tight_tree([labels[1]] + labels[2:], middle)
    return left + right, eleft + eright + [(u, v)], finish, u


def check_root_group_equality():
    labels, calls, n, root = tight_tree(list(range(5)))
    assert n == 16 and len(calls) == 15
    assert len({tuple(sorted(e)) for e in calls}) == 15
    knowledge = [1 << i for i in range(n)]
    for u, v in calls:
        knowledge[u] = knowledge[v] = knowledge[u] | knowledge[v]
    full = (1 << n) - 1
    groups = [[v for v, label in labels if label == i] for i in range(5)]
    assert len(groups[0]) == 1 and groups[0] == [root]
    assert sorted(len(x) for x in groups) == [1, 1, 2, 4, 8]
    for group in groups:
        cover = 0
        for vertex in group:
            cover |= knowledge[vertex]
            assert any(knowledge[vertex] & (1 << s) and
                       all(not knowledge[w] & (1 << s)
                           for w in group if w != vertex)
                       for s in range(n)), (group, vertex)
        assert cover == full
    # Fifteen X recipients in 4 disjoint groups all private: a crossing
    # four-arm B tree with an outside full root cannot have such a group.
    assert sum(map(len, groups[1:])) == 15
    assert any(len(g) > 1 for g in groups[1:])
    print("PASS exact 16-person sharp tree: outside full root + 15 X recipients;",
          "all 16 designated recipients have in-group private secrets")


if __name__ == "__main__":
    check_root_group_equality()
    fixed = {18: 489, 19: 1365, 20: 3333, 21: 7359, 22: 15015,
             23: 28745, 24: 52209, 25: 90718, 26: 151774}
    for n in range(13, 27):
        brute = direct(n)
        fast = symbolic(n)
        assert brute == fast, (n, brute, fast)
        if n in fixed:
            assert fast == fixed[n], (n, fast, fixed[n])
        before = stage15_filter(n)
        assert 0 <= fast <= before <= comb(n - 13 + 8, 8)
        if n >= 18:
            print(f"PASS n={n}: Stage15={before}, Stage16={fast}, eliminated={before-fast}")
    for n in (28, 29, 40, 75, 76):
        print(f"PASS closed-form n={n}: Stage16 necessary profiles={symbolic(n)}")
    print("LIMIT: these are labelled incidence vectors only, not valid schedules")
