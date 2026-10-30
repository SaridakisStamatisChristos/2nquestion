"""Exact root-free crossed UNICYCLIC core for every shared-center width >=4.

All calls are distinct even ACROSS the two component histories. This is a
local necessary-information construction, NOT a globally successful 2n-4
gossip schedule or a counterexample to the full forest conjecture.
"""


def build(k):
    assert isinstance(k, int) and k >= 0
    w = list(range(8, 8 + k))
    X = set(range(4)) | set(w)
    T = [(0, 6)] + [(0, x) for x in w] + [
        (1, 0), (3, 1), (0, 4), (2, 0), (4, 6)]
    U = [(0, 7)] + [(1, x) for x in w] + [
        (2, 1), (0, 5), (1, 5), (3, 0), (5, 7)]
    return X, T, U


def exact_history(vertices, calls):
    info = {v: {v} for v in vertices}
    for a, b in calls:
        merged = info[a] | info[b]
        info[a] = merged
        info[b] = merged
    return info


def is_tree_before_cycle(vertices, calls):
    prefix = calls[:-1]
    edges = [frozenset(e) for e in prefix]
    assert len(edges) == len(set(edges)) == len(vertices) - 1
    parent = {v: v for v in vertices}

    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v

    for a, b in prefix:
        ra, rb = root(a), root(b)
        assert ra != rb
        parent[ra] = rb
    assert len({root(v) for v in vertices}) == 1
    assert frozenset(calls[-1]) not in edges


def validate(k):
    X, T, U = build(k)
    VT, VU = X | {4, 6}, X | {5, 7}
    assert VT & VU == X
    assert len(T) == len(VT) and len(U) == len(VU)
    ET, EU = [frozenset(e) for e in T], [frozenset(e) for e in U]
    assert len(ET) == len(set(ET)) and len(EU) == len(set(EU))
    assert set(ET).isdisjoint(EU)
    assert T[-1] == (4, 6) and U[-1] == (5, 7)
    is_tree_before_cycle(VT, T)
    is_tree_before_cycle(VU, U)

    beforeT = exact_history(VT, T[:-1])
    beforeU = exact_history(VU, U[:-1])
    afterT = exact_history(VT, T)
    afterU = exact_history(VU, U)
    for x in X:
        assert beforeT[x] == afterT[x]
        assert beforeU[x] == afterU[x]

    for info, vertices in [(beforeT, VT), (beforeU, VU),
                           (afterT, VT), (afterU, VU)]:
        assert not any(len(info[v]) == len(vertices) for v in vertices)

    ST = {a: {x for x in X if a in afterT[x]} for a in VT}
    SU = {b: {x for x in X if b in afterU[x]} for b in VU}
    assert all(len(s) >= 2 for s in list(ST.values()) + list(SU.values()))
    assert all(a & b for a in ST.values() for b in SU.values())

    core = {0, 1, 2, 3}
    assert all(core <= ST[w] for w in range(8, 8 + k))
    assert all({1, 2} <= SU[w] for w in range(8, 8 + k))
    return len(X), len(VT) * len(VU)


if __name__ == "__main__":
    total = 0
    for k in [0, 1, 2, 3, 4, 8, 16, 32, 64]:
        width, pairs = validate(k)
        total += pairs
    print(f"PASS root-free unicyclic exact family at 9 widths; "
          f"all-pairs checks={total}, max shared center=68; "
          "no complete roots, all calls unique even across histories")
