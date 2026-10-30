"""Exact necessary-incidence counts, NOT full chronological schedule checks."""
from math import comb


def choose(n, r):
    return comb(n, r) if n >= r >= 0 else 0


def profile_count(n):
    # Nine positive cells; mandatory off-corners >=2, center >=1.
    # Extra occupancy k=n-13 is distributed among nine cells.
    k = n - 13
    if k < 0:
        return (0, 0)
    all_matrices = choose(k + 8, 8)
    # Inclusion-exclusion, with either size-two off-corner pair forcing
    # center >=9 and both such pairs forcing center >=64.
    survivors = (all_matrices - 2 * choose(k + 6, 6)
                 + 2 * choose(k - 2, 6)
                 + choose(k + 4, 4)
                 - 2 * choose(k - 4, 4)
                 + choose(k - 59, 4))
    return (all_matrices, survivors)


def compositions(k, width):
    if width == 1:
        yield (k,)
    else:
        for first in range(k + 1):
            for tail in compositions(k - first, width - 1):
                yield (first,) + tail


def independent_enumeration(n):
    # Row-major extra occupancy over base matrix
    # [[1,1,2],[1,1,2],[2,2,1]].
    k = n - 13
    total = kept = 0
    for x in compositions(k, 9):
        total += 1
        upper_pair_tight = x[2] == x[5] == 0
        lower_pair_tight = x[6] == x[7] == 0
        center = x[8] + 1
        if (upper_pair_tight or lower_pair_tight) and center < 9:
            continue
        if upper_pair_tight and lower_pair_tight and center < 64:
            continue
        kept += 1
    return total, kept


if __name__ == "__main__":
    print("n raw-positive-incidence remaining-necessary-incidence")
    for n in range(18, 26):
        predicted = profile_count(n)
        actual = independent_enumeration(n)
        assert actual == predicted, (n, actual, predicted)
        print(n, *actual)
    for n in (26, 30, 40, 75, 76):
        raw, kept = profile_count(n)
        assert 0 <= kept <= raw
        print(n, raw, kept, "(closed-form only)")
    assert profile_count(18) == (1287, 489)
    assert profile_count(19) == (3003, 1365)
    assert profile_count(20) == (6435, 3333)
    print("PASS inclusion-exclusion vs independent exhaustive integer compositions")
    print("NOT verified full gossip schedules; survivors are overapproximations")
