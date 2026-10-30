"""Independent chronology brute-force for Stage 8 collector-budget theorem.

This is a falsification regression, NOT a substitute for the all-n proof.
Exhaustively enumerate all ordered distinct undirected calls on m=3,4,5
participants of lengths m-1+k, for k=0,...,min(3, C(m,2)-(m-1)).
Check every *connected* graph and compute the exact maximum count of
fully informed participants using per-participant knowledge bitmasks.
No reliance on earlier rooted-tree or optimistic profile oracles.
"""
from itertools import combinations, permutations

EXPECTED = {
    (3, 0): (6, 2),
    (3, 1): (6, 3),
    (4, 0): (96, 2),
    (4, 1): (360, 4),
    (4, 2): (720, 4),
    (4, 3): (720, 4),
    (5, 0): (3000, 2),
    (5, 1): (26640, 4),
    (5, 2): (147600, 5),
    (5, 3): (604800, 5),
}


def classify(m, k):
    edges = tuple(combinations(range(m), 2))
    length = m - 1 + k
    full = (1 << m) - 1
    complete_graph_count = 0
    maximum_collectors = 0
    witness = None
    for schedule in permutations(edges, length):
        info = [1 << v for v in range(m)]
        parent = list(range(m))

        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v

        for u, v in schedule:
            a, b = root(u), root(v)
            if a != b:
                parent[a] = b
            info[u] = info[v] = info[u] | info[v]

        if len({root(v) for v in range(m)}) != 1:
            continue
        complete_graph_count += 1
        count = sum(bits == full for bits in info)
        assert count <= 2 * (k + 1), (
            "universal collector bound falsified", m, k, schedule, info
        )
        if count > maximum_collectors:
            maximum_collectors = count
            witness = schedule

    return complete_graph_count, maximum_collectors, witness


def main():
    assert len(EXPECTED) == 10
    for (m, k), (total, collectors) in EXPECTED.items():
        observed, maximum, witness = classify(m, k)
        assert (observed, maximum) == (total, collectors), (
            m, k, (observed, maximum), (total, collectors)
        )
        assert witness is not None
        print(
            f"PASS m={m} rank={k}: {observed} connected ordered "
            f"distinct-call schedules; exact max collectors={maximum}; "
            f"universal bound=2({k}+1)={2 * (k + 1)}",
            flush=True,
        )

    # Independent arithmetic sanity checks of the new and old all-n
    # inequalities; these are necessary bounds, NOT attainability.
    for r, s, old, new in (
        (3, 3, 13, 10),
        (3, 4, 18, 16),
        (3, 5, 23, 22),
        (3, 6, 28, 28),
        (3, 7, 33, 34),
        (4, 4, 24, 20),
        (4, 6, 36, 36),
        (5, 5, 37, 34),
        (6, 6, 52, 52),
        (8, 8, 88, 100),
        (10, 10, 132, 164),
    ):
        assert old == r * s + 2 * (r + s) - 8
        assert new == 2 * r * s - 4 * min(r, s) + 4
        assert max(old, new) >= old
    print("PASS eleven exact combined all-n grid thresholds", flush=True)
    print("SCOPE: checks finite component chronologies; "
          "the original-half forest conjecture remains OPEN", flush=True)


if __name__ == "__main__":
    main()
