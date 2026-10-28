"""Stage 29: exact all-c privacy threshold for (1,1,c) chronological trees.

The all-n lower bound is proved in PRIVATE_THRESHOLD_THEOREM.md; bounded
enumeration is an independent regression, never a universal proof oracle.
"""
from collections import Counter
from itertools import permutations, product


def replay(n, calls, complete_tree=True):
    knowledge = [1 << i for i in range(n)]
    edges = set()
    parent = list(range(n))

    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x

    for a, b in calls:
        assert 0 <= a < n and 0 <= b < n and a != b
        edge = tuple(sorted((a, b)))
        assert edge not in edges
        edges.add(edge)
        ra, rb = root(a), root(b)
        assert ra != rb, "a chronology with a static cycle is not a tree"
        parent[ra] = rb
        new = knowledge[a] | knowledge[b]
        knowledge[a] = knowledge[b] = new
    if complete_tree:
        assert len(edges) == n - 1
        assert len({root(i) for i in range(n)}) == 1
    else:
        assert len(edges) == n - 2
    return knowledge


def privacy(knowledge, group):
    single = set()
    for secret in range(len(knowledge)):
        holders = [v for v in group if knowledge[v] & (1 << secret)]
        assert holders, ("not collectively complete", secret)
        if len(holders) == 1:
            single.add(holders[0])
    return single


def construction(c):
    """For EVERY c>=6: group {2,..,c+1}, two singleton full roots 0,1."""
    assert c >= 6
    # Add extra leaves FIRST, so their secrets join the base chronology.
    leaves = [(z, 3) for z in range(8, c + 2)]
    original = [(0, 3), (2, 4), (0, 2),
                (1, 6), (5, 7), (1, 5), (0, 1)]
    return leaves + original


def check_construction(c):
    n = c + 2
    calls = construction(c)
    assert calls[-1] == (0, 1)
    know = replay(n, calls)
    full = (1 << n) - 1
    assert know[0] == know[1] == full
    group = range(2, n)
    assert not privacy(know, group), c
    coverage = [sum(bool(know[x] & (1 << secret)) for x in group)
                for secret in range(n)]
    assert min(coverage) >= 2
    prior = replay(n, calls[:-1], complete_tree=False)
    assert all(prior[x] == know[x] for x in group)
    return min(coverage)


def independent_small_tree_enumeration():
    """Separate Prüfer/call-order enumerator; exact for n=3,4,5 only."""
    qualifying = Counter()
    for n in (3, 4, 5):
        for word in product(range(n), repeat=n-2):
            degree = [1] * n
            for v in word:
                degree[v] += 1
            edges = []
            for v in word:
                leaf = next(i for i in range(n) if degree[i] == 1)
                edges.append((leaf, v))
                degree[leaf] -= 1
                degree[v] -= 1
            edges.append(tuple(i for i in range(n) if degree[i] == 1))
            if (0, 1) not in {tuple(sorted(e)) for e in edges}:
                continue
            rest = [e for e in edges if tuple(sorted(e)) != (0, 1)]
            for order in permutations(rest):
                know = replay(n, list(order) + [(0, 1)])
                full = (1 << n) - 1
                if know[0] != full or know[1] != full:
                    continue
                group = range(2, n)
                try:
                    private = privacy(know, group)
                except AssertionError:
                    continue
                qualifying[n] += 1
                assert private, ("private-free small tree", n, order)
    assert qualifying[4] > 0 and qualifying[5] > 0
    return qualifying


def main():
    counts = independent_small_tree_enumeration()
    print("PASS independent chronological tree n=3..5 enumeration", dict(counts))
    for c in (6, 7, 8, 9, 10, 16, 24, 40):
        multiplicity = check_construction(c)
        print("PASS exact tree (1,1,%d): 0 private; minimum C support %d" %
              (c, multiplicity))
    print("PROVED IN TEXT: c<=5 forces >=1 private recipient by two-root cut")
    print("CONSTRUCTED: EVERY c>=6 allows zero private recipients")
    print("NOT a global both-cyclic gossip schedule or all-n forest proof")


if __name__ == "__main__":
    main()
