"""Independent fixed-chronology upward closure check (not a proof of the all-n conjecture)."""
from itertools import combinations, permutations


def gossip(n, schedule):
    knowledge = [1 << i for i in range(n)]
    for u, v in schedule:
        knowledge[u] = knowledge[v] = knowledge[u] | knowledge[v]
    return all(x == (1 << n) - 1 for x in knowledge)


def rank(n, schedule):
    parent = list(range(n))
    cycles = 0

    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v

    for u, v in schedule:
        ru, rv = root(u), root(v)
        if ru == rv:
            cycles += 1
        else:
            parent[ru] = rv
    return cycles


def main():
    for n, expected_successes in ((4, 24), (5, 3240)):
        successes = 0
        edges = tuple(combinations(range(n), 2))
        for schedule in permutations(edges, 2 * n - 4):
            if not gossip(n, schedule):
                continue
            successes += 1
            before = (
                rank(n, schedule[: n - 2]),
                rank(n, schedule[n - 2 :]),
            )
            for a, b in ((0, 1), (1, 0), (0, n - 1)):
                assert a != b
                extended = ((n, a),) + schedule + ((n, b),)
                assert len(extended) == 2 * (n + 1) - 4
                assert len(set(tuple(sorted(x)) for x in extended)) == len(extended)
                assert gossip(n + 1, extended), (n, a, b, schedule)
                after = (
                    rank(n + 1, extended[: n - 1]),
                    rank(n + 1, extended[n - 1 :]),
                )
                assert before == after, (n, a, b, schedule, before, after)
        assert successes == expected_successes, (n, successes)
        print(
            f"PASS n={n}: all {successes} successful ordered distinct "
            f"minimum gossip schedules, all three extension choices, "
            "both original chronological cycle ranks preserved",
            flush=True,
        )
    print("SCOPE: this proves no downward/minimal-counterexample reduction", flush=True)


if __name__ == "__main__":
    main()
