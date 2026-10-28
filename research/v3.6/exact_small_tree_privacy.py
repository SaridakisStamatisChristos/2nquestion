"""Stage 19: independent exhaustive private-midpoint-recipient counts.

Complete labelled spanning trees via Prüfer codes; every chronological tree
edge ordering; fixed designated groups with sizes (a,b,c). Only count ordered
histories whose LAST call crosses the first two groups and EVERY group
collectively covers all original secrets. For the off-corner third group,
count how many recipients have a secret no other recipient in that group knows.

This is a finite local exhaustive theorem, not a global gossip solver.
"""
from collections import Counter
from functools import reduce
from itertools import permutations, product


def prufer_edges(code, n):
    degree = [1] * n
    for x in code:
        degree[x] += 1
    edges = []
    for x in code:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((leaf, x))
        degree[leaf] -= 1
        degree[x] -= 1
    a, b = (i for i in range(n) if degree[i] == 1)
    return edges + [(a, b)]


def history(n, calls):
    masks = [1 << i for i in range(n)]
    for a, b in calls:
        masks[a] = masks[b] = masks[a] | masks[b]
    return masks


def exact_private_histogram(a, b, c):
    n = a + b + c
    group0 = range(a)
    group1 = range(a, a+b)
    group2 = range(a+b, n)
    groups = (group0, group1, group2)
    full = (1 << n) - 1
    histogram = Counter()
    for code in product(range(n), repeat=n-2):
        edges = prufer_edges(code, n)
        # Fixed endpoint membership; no reordering of any tested history.
        for order in permutations(edges):
            u, v = order[-1]
            if not ((u in group0 and v in group1) or
                    (u in group1 and v in group0)):
                continue
            know = history(n, order)
            if any(reduce(int.__or__, (know[i] for i in group), 0) != full
                   for group in groups):
                continue
            private_count = 0
            for x in group2:
                if any((know[x] & (1 << secret)) and
                       all(not(know[y] & (1 << secret))
                           for y in group2 if y != x)
                       for secret in range(n)):
                    private_count += 1
            histogram[private_count] += 1
    return dict(sorted(histogram.items()))


EXPECTED = {
    (1, 1, 2): {2: 4},
    (1, 1, 3): {2: 72},
    (2, 1, 2): {2: 48},
    (1, 2, 2): {2: 48},
    (2, 1, 3): {2: 1728, 3: 192},
    (1, 2, 3): {2: 1728, 3: 192},
    (1, 1, 4): {1: 384, 2: 1344},
}


def main():
    for sizes, expected in EXPECTED.items():
        actual = exact_private_histogram(*sizes)
        assert actual == expected, (sizes, actual, expected)
        print("PASS tree", sizes,
              "complete covers by private offcorner count", actual)
    print("PASS all 7 local classes complete through 6 vertices")
    print("Boundary: (1,1,4) can have only ONE private recipient;"
          " do not assert at least two without further original crossing evidence")
    print("LIMIT: these are exact LOCAL tree counts, not full gossip schedules")


if __name__ == "__main__":
    main()
