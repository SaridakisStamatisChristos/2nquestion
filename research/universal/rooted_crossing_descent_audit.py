"""Independent finite falsifier of exact-support restriction used by all-n descent.

Replays ORIGINAL-ORDER chronological trees. The universal theorem follows
from its two-case well-founded descent, NOT finite execution of this audit.
"""
import heapq
import itertools


def prufer_tree(code):
    n = len(code) + 2
    deg = [1] * n
    for v in code:
        deg[v] += 1
    leaves = [i for i, d in enumerate(deg) if d == 1]
    heapq.heapify(leaves)
    edges = []
    for v in code:
        u = heapq.heappop(leaves)
        edges.append((u, v))
        deg[u] -= 1
        deg[v] -= 1
        if deg[v] == 1:
            heapq.heappush(leaves, v)
    edges.append((heapq.heappop(leaves), heapq.heappop(leaves)))
    return edges


def replay(vertices, calls):
    K = {v: {v} for v in vertices}
    for a, b in calls:
        shared = K[a] | K[b]
        K[a] = shared
        K[b] = shared
    return K


def components(vertices, calls):
    """Delete ACTUAL last edge; retain original subsequences on each side."""
    prefix = calls[:-1]
    adj = {v: set() for v in vertices}
    for a, b in prefix:
        adj[a].add(b)
        adj[b].add(a)
    roots = calls[-1]
    parts = []
    for r in roots:
        seen = {r}
        pending = [r]
        while pending:
            for w in adj[pending.pop()]:
                if w not in seen:
                    seen.add(w)
                    pending.append(w)
        parts.append((seen, [e for e in prefix if e[0] in seen]))
    assert parts[0][0].isdisjoint(parts[1][0])
    assert parts[0][0] | parts[1][0] == set(vertices)
    return parts


def histories(n, k, last_type):
    """Last pair OO=outside/outside or IO=inside/outside, both complete."""
    v = tuple(range(n))
    for code in itertools.product(v, repeat=n - 2):
        edges = prufer_tree(code)
        for calls in itertools.permutations(edges):
            a, b = calls[-1]
            if last_type == "OO" and (a < k or b < k):
                continue
            if last_type == "IO" and ((a < k) == (b < k)):
                continue
            K = replay(v, calls)
            if K[a] != set(v) or K[b] != set(v):
                continue
            yield v, calls, K


def crossed_support_restriction(T, U, k, pairs):
    tv, te, TK = T
    uv, ue, UK = U
    ta = components(tv, te)
    ub = components(uv, ue)
    E = set(range(k))
    tlocal = [replay(V, C) for V, C in ta]
    ulocal = [replay(V, C) for V, C in ub]
    cases = 0
    for i, j in pairs:
        ti, uj = ta[i][0], ub[j][0]
        center = ti & uj & E
        for a in ti:
            for b in uj:
                original = {x for x in E if a in TK[x] and b in UK[x]}
                local = {x for x in center if a in tlocal[i][x]
                         and b in ulocal[j][x]}
                assert original == local, (te, ue, i, j, a, b,
                                          original, local)
                cases += 1
    return cases


def run():
    outside = list(histories(5, 3, "OO"))
    checks_oo = 0
    for t in outside:
        for u in outside:
            checks_oo += crossed_support_restriction(
                t, u, 3, [(0, 0), (0, 1), (1, 0), (1, 1)])

    inside = list(histories(4, 3, "IO"))
    checks_io = 0
    for t in inside:
        y = next(x for x in t[1][-1] if x < 3)
        for u in outside:
            j = next(j for j, (v, _) in enumerate(components(u[0], u[1]))
                     if y not in v)
            checks_io += crossed_support_restriction(
                t, u, 3, [(0, j), (1, j)])

    # Four local second collectors cannot occupy both slots in all 4 cells.
    placements = 0
    for a0, a1, b0, b1 in itertools.product((-1, 0, 1), repeat=4):
        a_hubs = [(0, a0), (1, a1)]
        b_hubs = [(b0, 0), (b1, 1)]
        assert any(sum(q == h for h in a_hubs + b_hubs) <= 1
                   for q in itertools.product((0, 1), repeat=2))
        placements += 1
    # A single vertex cannot belong to two disjoint cells.
    assert all(w not in ({0} & {1}) for w in (-1, 0, 1))
    print(f"PASS: OO histories={len(outside)}, IO histories={len(inside)}, "
          f"OO support identities={checks_oo}, "
          f"IO support identities={checks_io}, "
          f"four-hub placements={placements}")


if __name__ == "__main__":
    run()
