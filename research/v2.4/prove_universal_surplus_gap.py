"""Stage 7 universal collector-surplus lemma: independent boundary falsification.

For every hypothetical both-cyclic n=2n-4 successful distinct-call gossip
chronology with r prefix components and s suffix components (3<=r<=s),
the analytic necessary bound is n >= r*s + 2*s - 2.

Exhaustively test the only incidence matrices possible AT and ONE BELOW
this boundary, using only the earlier tree-collector and single-source
tree-entry necessary lemmas. Passing this test does not prove all n, and
the symbolic proof is in UNIVERSAL_SURPLUS_GAP.md.

Source independent of the existing 3x3/3x4 v2.3 generators.
"""
from itertools import combinations, combinations_with_replacement, product


def rank_vectors(k, total):
    if k == 1:
        yield (total,)
        return
    for value in range(total + 1):
        for rest in rank_vectors(k - 1, total - value):
            yield (value,) + rest


def necessary(M, tree_rows, tree_cols):
    r, s = len(M), len(M[0])
    # Singleton cells in a tree row are prescribed complete collectors.
    # A suffix-tree column with another singleton source additionally
    # requires a complete prefix collector in this row/column cell.
    for i in tree_rows:
        forced = {j for j in range(s) if M[i][j] == 1}
        for j in tree_cols:
            if any(i != k and M[k][j] == 1 for k in range(r)):
                forced.add(j)
        if len(forced) > 2:
            return False
    # Time-reversed singleton/tree-entry requirements.
    for j in tree_cols:
        forced = {i for i in range(r) if M[i][j] == 1}
        for i in tree_rows:
            if any(j != k and M[i][k] == 1 for k in range(s)):
                forced.add(i)
        if len(forced) > 2:
            return False
    return True


def boundary_scan(r, s, extra_budget=1):
    assert 3 <= r <= s
    min_extras = 2 * (s - 2)
    # The analytic proof forces exactly two tree prefix rows throughout
    # the closed budget window E <= min_extras+1. In r=s=3, cycle-rank
    # identity itself forces exactly two tree rows.
    assert extra_budget == 1
    singleton_pairs = tuple(combinations(range(s), 2))
    # Enumerate all possible suffix cycle rank vectors sum(s-2),
    # projected to their tree-column positions. Duplicate vectors
    # do not change the necessary collector constraints.
    possible_tree_columns = set()
    for ranks in rank_vectors(s, s - 2):
        possible_tree_columns.add(
            tuple(j for j, beta in enumerate(ranks) if beta == 0)
        )
    assert all(len(x) >= 2 for x in possible_tree_columns)
    matrices = marked = survivors = 0
    for tree_rows in combinations(range(r), 2):
        for pair_a, pair_b in product(singleton_pairs, repeat=2):
            M = [[1] * s for _ in range(r)]
            for i, singleton_cols in zip(tree_rows, (pair_a, pair_b)):
                for j in range(s):
                    M[i][j] = 1 if j in singleton_cols else 2
            # Exactly min_extras, or min_extras+1: any feasible tree row
            # with minimum extra has exactly two singleton cells, and
            # an additional surplus unit can be placed in ANY cell.
            for bonus in range(-1, r * s):
                if bonus >= 0:
                    M[bonus // s][bonus % s] += 1
                matrices += 1
                for tree_cols in possible_tree_columns:
                    marked += 1
                    if necessary(M, tree_rows, tree_cols):
                        survivors += 1
                if bonus >= 0:
                    M[bonus // s][bonus % s] -= 1
    return matrices, marked, survivors


def sharpness_probe_3xs(s):
    """Exhibit survivors at +2, proving the +2 gain is not vacuous."""
    r = 3
    possible_tree_columns = set(
        tuple(j for j, beta in enumerate(v) if beta == 0)
        for v in rank_vectors(s, s - 2)
    )
    survivors = 0
    for tree_rows in combinations(range(r), 2):
        for pair_a, pair_b in product(combinations(range(s), 2), repeat=2):
            M = [[1] * s for _ in range(r)]
            for i, singleton_cols in zip(tree_rows, (pair_a, pair_b)):
                for j in range(s):
                    M[i][j] = 1 if j in singleton_cols else 2
            for a, b in combinations_with_replacement(range(r * s), 2):
                M[a // s][a % s] += 1
                M[b // s][b % s] += 1
                for tree_cols in possible_tree_columns:
                    survivors += necessary(M, tree_rows, tree_cols)
                M[a // s][a % s] -= 1
                M[b // s][b % s] -= 1
    return survivors


def main():
    expected = {
        (3, 3): (270, 810, 0),
        (3, 4): (1404, 14040, 0),
        (3, 5): (4800, 120000, 0),
        (4, 4): (3672, 36720, 0),
        (4, 5): (12600, 315000, 0),
        (5, 5): (26000, 650000, 0),
    }
    for (r, s), counts in expected.items():
        got = boundary_scan(r, s)
        assert got == counts, (r, s, got, counts)
        print(f"PASS all-n lemma boundary r={r} s={s}: "
              f"{got[1]} marked necessary-profile instances; "
              f"zero survivors at E<=2(s-2)+1", flush=True)
    # Strictness: at E=2(s-2)+2 there are necessary-condition
    # survivors for each 3xs family; these are NOT gossip witnesses.
    assert [sharpness_probe_3xs(s) for s in (3, 4, 5)] == [81, 396, 1440]
    print("PASS sharpness adversarial probes r=3 s=3,4,5: "
          "81,396,1440 necessary-condition survivors at lower bound, "
          "not realizable-gossip witnesses", flush=True)
    print("VERDICT: independent finite falsification PASS; "
          "unbounded inequality depends on the accompanying human proof; "
          "original-half forest for arbitrary n remains OPEN", flush=True)


if __name__ == "__main__":
    main()
