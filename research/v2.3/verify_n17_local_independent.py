"""Independent last-edge brute-force tree oracle for n7/n8 local capacity.

This is deliberately not derived from the rooted-state DP. Every side
enumerates all distinct-edge ordered spanning-tree call sequences.
The final edge connects the two mandated full collectors (vertices 2,3).
"""
from functools import lru_cache
from itertools import combinations, permutations

@lru_cache(None)
def histories(side, root, n):
    vertices = tuple(i for i in range(n) if side >> i & 1)
    edges = tuple(combinations(vertices, 2))
    if len(vertices) == 1:
        return ((side,),)
    result = set()
    for seq in permutations(edges, len(vertices) - 1):
        parent = {v: v for v in vertices}
        def leader(v):
            while parent[v] != v:
                v = parent[v]
            return v
        k = {v: 1 << v for v in vertices}
        valid = True
        for u, v in seq:
            a, b = leader(u), leader(v)
            if a == b:
                valid = False
                break
            parent[a] = b
            k[u] = k[v] = k[u] | k[v]
        if valid and k[root] == side:
            result.add(tuple(k[i] for i in vertices))
    return tuple(result)

def audit(t):
    n = t + 4
    full = (1 << n) - 1
    groups = (tuple(range(2)), (2, 3), tuple(range(4, n)))
    B, D = set(), set()
    count = 0
    others = (0, 1, *range(4, n))
    for sub in range(1 << len(others)):
        U = (1 << 2) | sum(1 << i for j, i in enumerate(others) if sub >> j & 1)
        V = full ^ U
        au = tuple(i for i in range(n) if U >> i & 1)
        av = tuple(i for i in range(n) if V >> i & 1)
        # Neither group0 nor group2 has a last-bridge collector, so it
        # must collectively know both sides using members from each side.
        if any(not any(U >> i & 1 for i in g) or
               not any(V >> i & 1 for i in g)
               for g in (groups[0], groups[2])):
            continue
        for x in histories(U, 2, n):
            for y in histories(V, 3, n):
                k = [0] * n
                for i, v in zip(au, x):
                    k[i] = v
                for i, v in zip(av, y):
                    k[i] = v
                k[2] = k[3] = full
                if any(__import__("functools").reduce(int.__or__,
                          (k[i] for i in g), 0) != full for g in groups):
                    continue
                count += 1
                bb, dd = [], []
                for g in groups:
                    b = d = 0
                    for mask in range(1 << len(g)):
                        know = 0
                        for j, i in enumerate(g):
                            if mask >> j & 1:
                                know |= k[i]
                        if know == full:
                            b |= 1 << mask
                    for secret in range(n):
                        recipients = sum(1 << j for j, i in enumerate(g)
                                         if k[i] >> secret & 1)
                        d |= 1 << recipients
                    bb.append(b)
                    dd.append(d)
                B.add(tuple(bb))
                D.add(tuple(dd))
    return B, D, count

def main():
    assert audit(3) == (set(), set(), 0)
    assert audit(4) == ({(8, 14, 32768)}, {(6, 8, 278)}, 48)
    print("PASS independent ordered side-tree enumeration: n7 local"
          " (2,2,3) two-collector domain EMPTY; n8 (2,2,4)"
          " exact B/D and 48 histories regression")

if __name__ == "__main__":
    main()
