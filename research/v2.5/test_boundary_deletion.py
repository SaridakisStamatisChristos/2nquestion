"""Independent exhaustive n5 test of exact boundary-vertex deletion criterion.

Every ordered 6-call schedule with distinct undirected edges is checked;
every successful schedule and every vertex used only at times 0 and 5
is evaluated. The test is a falsifier, not all-n proof.
"""
from itertools import combinations, permutations


def process(n, calls):
    k = [1 << i for i in range(n)]
    for a, b in calls:
        k[a] = k[b] = k[a] | k[b]
    return k


def rank(n, calls):
    p = list(range(n))
    cycles = 0

    def root(v):
        while p[v] != v:
            v = p[v]
        return v

    for a, b in calls:
        u, v = root(a), root(b)
        if u == v:
            cycles += 1
        else:
            p[u] = v
    return cycles


def analyse(n, schedule, v):
    assert v in schedule[0] and v in schedule[-1]
    assert all(v not in e for e in schedule[1:-1])
    a = next(x for x in schedule[0] if x != v)
    b = next(x for x in schedule[-1] if x != v)
    assert a != b
    middle = schedule[1:-1]
    old = [w for w in range(n) if w != v]
    relabel = {w: i for i, w in enumerate(old)}
    reduced = tuple((relabel[u], relabel[w]) for u, w in middle)
    k = process(n - 1, reduced)
    success = all(x == (1 << (n - 1)) - 1 for x in k)
    delivered = bool(k[relabel[b]] & (1 << relabel[a]))
    assert success == delivered, (
        "exact boundary deletion criterion failed",
        n, schedule, v, a, b, k,
    )
    assert (
        rank(n, schedule[: n - 2]),
        rank(n, schedule[n - 2 :]),
    ) == (
        rank(n - 1, reduced[: n - 3]),
        rank(n - 1, reduced[n - 3 :]),
    )
    return success, reduced


def main():
    n = 5
    witness = ((0, 1), (2, 3), (2, 4), (0, 2), (0, 3), (1, 4))
    assert all(v == (1 << n) - 1 for v in process(n, witness))
    ok, reduced = analyse(n, witness, 1)
    assert not ok, "pinned nondeletable witness unexpectedly passes"
    assert reduced == ((1, 2), (1, 3), (0, 1), (0, 2))
    print("PASS explicit optimal n5 nondeletable boundary-fringe witness", flush=True)

    valid = marked = deletable = blocked = 0
    edges = tuple(combinations(range(n), 2))
    for calls in permutations(edges, 2 * n - 4):
        if not all(x == (1 << n) - 1 for x in process(n, calls)):
            continue
        valid += 1
        for v in range(n):
            indices = [i for i, e in enumerate(calls) if v in e]
            if indices != [0, len(calls) - 1]:
                continue
            marked += 1
            success, _ = analyse(n, calls, v)
            if success:
                deletable += 1
            else:
                blocked += 1

    assert valid == 3240, valid
    assert (marked, deletable, blocked) == (1800, 1440, 360), (
        marked, deletable, blocked
    )
    print("PASS all 3240 optimal n5 gossip schedules: 1800 marked "
          "first/last-only vertex cases, 1440 deletable, 360 "
          "nondeletable; exact iff criterion and two cycle ranks "
          "independently verified", flush=True)
    print("VERDICT: unconditional downward deletion REFUTED; "
          "half-forest conjecture for all n OPEN", flush=True)


if __name__ == "__main__":
    main()
