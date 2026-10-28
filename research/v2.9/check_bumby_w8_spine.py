"""Independent Stage 12 Bumby (1981) theorem-3 consequence auditor.

Enumerate all 51,200 linear extensions of the minimal-order W8 event poset;
for every successful chronology verify the ORIGINAL chronological midpoint
component number is <=3 in both directions. For every prefix having three
components, check that the FIRST suffix call in EACH suffix component
joins the two prefix TREE components; apply the time-reversed last-call
dual independently for every suffix having three components.

The all-n statement is justified by Bumby's original 1981 Theorem 3,
NOT by this finite regression. No Labahn kernel or prior project oracle
is imported. The temporal rank pair histogram is pinned.
"""
from collections import Counter

W8 = ((0, 1), (4, 5), (3, 7), (2, 6), (2, 3), (1, 5),
      (0, 4), (1, 2), (6, 7), (4, 6), (3, 5), (0, 7))
N = 8


def components(edges):
    parent = list(range(N))

    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v

    for a, b in edges:
        parent[root(a)] = root(b)
    groups = {}
    for v in range(N):
        groups.setdefault(root(v), []).append(v)
    component = {
        v: index
        for index, vertices in enumerate(groups.values())
        for v in vertices
    }
    ecount = [0] * len(groups)
    for a, b in edges:
        ecount[component[a]] += 1
    cycle_ranks = [
        ecount[index] - len(vertices) + 1
        for index, vertices in enumerate(groups.values())
    ]
    return component, cycle_ranks


def check_original_chronology(schedule):
    half = N - 2
    prefix, suffix = schedule[:half], schedule[half:]
    p, pr = components(prefix)
    q, qr = components(suffix)
    r, s = len(pr), len(qr)
    assert r in (2, 3) and s in (2, 3)

    if r == 3:
        tree_rows = {index for index, cyc in enumerate(pr) if cyc == 0}
        assert len(tree_rows) == 2 and sum(pr) == 1
        component_id = next(i for i, v in enumerate(pr) if v == 1)
        final_edge = next(e for e in reversed(prefix) if p[e[0]] == component_id)
        vertices = {v for v in range(N) if p[v] == component_id}
        remaining = [e for e in prefix if p[e[0]] == component_id and e != final_edge]
        visited = {min(vertices)}
        for _ in range(N):
            for a, b in remaining:
                if a in visited:
                    visited.add(b)
                if b in visited:
                    visited.add(a)
        assert visited == vertices
        earliest_suffix_edge = {}
        for a, b in suffix:
            earliest_suffix_edge.setdefault(q[a], (a, b))
        assert len(earliest_suffix_edge) == s
        for edge in earliest_suffix_edge.values():
            assert {p[v] for v in edge} == tree_rows, (
                "Bumby closed-tree first-suffix contact falsified",
                schedule, edge
            )

    if s == 3:
        tree_columns = {index for index, cyc in enumerate(qr) if cyc == 0}
        assert len(tree_columns) == 2 and sum(qr) == 1
        latest_prefix_edge = {}
        for a, b in prefix:
            latest_prefix_edge[p[a]] = (a, b)
        assert len(latest_prefix_edge) == r
        for edge in latest_prefix_edge.values():
            assert {q[v] for v in edge} == tree_columns, (
                "Bumby reverse closed-tree last-prefix contact falsified",
                schedule, edge
            )

    return r - 2, s - 2


def main():
    last = [-1] * N
    predecessors = []
    for index, (a, b) in enumerate(W8):
        mask = 0
        for v in (a, b):
            if last[v] >= 0:
                mask |= 1 << last[v]
            last[v] = index
        predecessors.append(mask)
    histogram = Counter()
    def search(mask, order):
        if len(order) == len(W8):
            schedule = tuple(W8[index] for index in order)
            histogram[check_original_chronology(schedule)] += 1
            return
        for index in range(len(W8)):
            if (not (mask >> index & 1)
                    and predecessors[index] & mask == predecessors[index]):
                search(mask | (1 << index), order + (index,))

    search(0, ())
    assert histogram == {
        (0, 0): 12800, (0, 1): 19200, (1, 0): 19200
    }, histogram
    print("PASS all 51200 W8 event-poset linear extensions:"
          " original midpoint component counts r,s <=3;"
          " EVERY prefix-3 case obeys first-suffix closed-tree spine;"
          " EVERY suffix-3 case obeys last-prefix reversed spine",
          flush=True)
    print("PASS fixed all 51200 rank-pair histogram",
          dict(sorted(histogram.items())), flush=True)
    print("SOURCE: Bumby 1981 Theorem 3; finite check corroborates"
          " without proving all-n. General 3x3 half-forest remains OPEN",
          flush=True)


if __name__ == "__main__":
    main()
