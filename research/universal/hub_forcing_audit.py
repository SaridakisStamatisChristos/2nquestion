"""Finite falsification challenges for universal <=4-vertex crossed-cell hub forcing.

Tree model: original edge-once undirected contacts, knowledge exchange union.
No finite enumeration substitutes for the accompanying all-n proof.
"""
import heapq
import itertools


def prufer_edges(code):
    n = len(code) + 2
    deg = [1] * n
    for x in code:
        deg[x] += 1
    leaves = [x for x in range(n) if deg[x] == 1]
    heapq.heapify(leaves)
    out = []
    for x in code:
        v = heapq.heappop(leaves)
        out.append((v, x))
        deg[v] -= 1
        deg[x] -= 1
        if deg[x] == 1:
            heapq.heappush(leaves, x)
    out.append((heapq.heappop(leaves), heapq.heappop(leaves)))
    return out


def histories(n):
    for code in itertools.product(range(n), repeat=n - 2):
        edges = prufer_edges(code)
        for calls in itertools.permutations(edges):
            k = [1 << v for v in range(n)]
            for a, b in calls:
                new = k[a] | k[b]
                k[a] = k[b] = new
            yield calls, k


def full(k):
    n = len(k)
    return {i for i, v in enumerate(k) if v == (1 << n) - 1}


def supports(k, c):
    return tuple(frozenset(x for x in c if (k[x] >> a) & 1)
                 for a in range(len(k)))


def verify():
    checked_rooted = 0
    checked_opponent = 0
    for m in (3, 4):
        # A has m designated people and 1 outside full root.
        # Extra helper sizes are handled by the HUMAN proof, not this audit.
        n = m + 1
        E = set(range(m))
        for calls, k in histories(n):
            if n - 1 not in full(k):
                continue
            st = supports(k, E)
            if not all(len(s) >= 2 for s in st):
                continue
            checked_rooted += 1
            two = set(s for s in st if len(s) == 2)
            assert any(len(a & b) == 1
                       for a, b in itertools.combinations(two, 2))

        # B has m designated people and two outside final-call full roots.
        n = m + 2
        E = set(range(m))
        for calls, k in histories(n):
            a, b = calls[-1]
            if (a in E or b in E
                    or k[a] != (1 << n) - 1
                    or k[b] != (1 << n) - 1):
                continue
            checked_opponent += 1
            su = supports(k, E)
            # B crossing a path {0,1},{0,2} would require EVERY source
            # to reach 0, or BOTH 1 and 2.
            assert not all(0 in s or (1 in s and 2 in s) for s in su)

    print(f"PASS: {checked_rooted} rooted double-cover histories, "
          f"{checked_opponent} opponent histories challenged (n<=6)")


if __name__ == "__main__":
    verify()
