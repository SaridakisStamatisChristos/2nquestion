"""Auditable n=13 two-cyclic-half reduction (stdlib, Python >=3.9).

This is a necessary-condition filter. It leaves ONE exceptional incidence
pattern for independent exact chronological-order enumeration.
"""
from collections import Counter
from itertools import combinations_with_replacement, permutations, product
import json

CELLS = tuple(product(range(3), repeat=2))
PERMS = tuple(permutations(range(3)))


def canonical(extras):
    """Orbit under S3(row) x S3(column) x time reversal."""
    return min(
        tuple(sorted((r[b], c[a]) if swap else (r[a], c[b])
                     for a, b in extras))
        for r in PERMS for c in PERMS for swap in (False, True)
    )


def matrix(extras):
    counts = Counter(extras)
    return tuple(tuple(1 + counts[i, j] for j in range(3)) for i in range(3))


def eligible_cycles(M):
    """Each tree component needs a nonsingleton opposite-side intersection."""
    rr = [i for i in range(3) if all(any(M[k][j] > 1 for j in range(3))
                                       for k in range(3) if k != i)]
    cc = [j for j in range(3) if all(any(M[i][k] > 1 for i in range(3))
                                       for k in range(3) if k != j)]
    return tuple(product(rr, cc))


def full_collector_demands(M, cyc_row, cyc_col):
    """Necessary collector demands from singleton and first-bridge covering.

    For suffix tree column with two singleton prefix-row intersections:
    third-row cell size=1 impossible, size=2 requires both row
    collectors, size=3 requires at least one row collector. Apply the
    symmetric statement to prefix tree rows and reverse-time collectors.
    Tree components have <=2 collectors. Cyclic size m>=5 components
    cannot gossip among all m vertices in m calls (2m-4 lower bound).
    """
    reasons = []
    for i in range(3):
        required = sum(M[i][j] == 1 for j in range(3))
        for j in range(3):
            if j == cyc_col:
                continue
            if sum(M[k][j] == 1 for k in range(3)) == 2:
                size = M[i][j]
                if size == 1:
                    # This is one of the TWO singleton bridge endpoints,
                    # not the third prefix source: no exclusion applies.
                    continue
                elif size == 2:
                    required += 2
                elif size == 3:
                    required += 1
        if i != cyc_row and required > 2:
            reasons.append(f'row {i}: >= {required} collectors required, tree maximum 2')
        elif i == cyc_row and required == sum(M[i]) and sum(M[i]) >= 5:
            reasons.append(f'row {i}: all {required} vertices must gossip in {sum(M[i])} calls, fewer than 2m-4')
    for j in range(3):
        required = sum(M[i][j] == 1 for i in range(3))
        for i in range(3):
            if i == cyc_row:
                continue
            if sum(M[i][k] == 1 for k in range(3)) == 2:
                size = M[i][j]
                if size == 1:
                    # One of the two forced prefix-bridge endpoints (dual).
                    continue
                elif size == 2:
                    required += 2
                elif size == 3:
                    required += 1
        if j != cyc_col and required > 2:
            reasons.append(f'column {j}: >= {required} reverse collectors required, tree maximum 2')
        elif j == cyc_col and required == sum(M[i][j] for i in range(3)) and required >= 5:
            reasons.append(f'column {j}: all {required} vertices must reverse gossip in {required} calls, fewer than 2m-4')
    return reasons


def enumerate_cases():
    reps = sorted({canonical(extras)
                   for extras in combinations_with_replacement(CELLS, 4)})
    cases = []
    for extras in reps:
        M = matrix(extras)
        for cr, cc in eligible_cycles(M):
            reasons = full_collector_demands(M, cr, cc)
            cases.append({'extras': [list(z) for z in extras],
                          'grid': [list(z) for z in M],
                          'cycle_row': cr, 'cycle_column': cc,
                          'collector_excluded': bool(reasons),
                          'reasons': reasons})
    return reps, cases


def main():
    reps, cases = enumerate_cases()
    remaining = [z for z in cases if not z['collector_excluded']]
    assert len(reps) == 16, len(reps)
    assert len(cases) == 44, len(cases)
    assert len(remaining) == 1, remaining
    # Regression: the singleton bridge endpoints must never be rejected
    # as third-source singleton cells. Earlier v1.4 emitted such invalid
    # explanatory reasons. All 43 exclusions survive this repair.
    raw_cases = 0
    raw_remaining = []
    for extras in combinations_with_replacement(CELLS, 4):
        M = matrix(extras)
        for cr, cc in eligible_cycles(M):
            raw_cases += 1
            if not full_collector_demands(M, cr, cc):
                raw_remaining.append((extras, cr, cc))
    assert raw_cases == 1278, raw_cases
    assert len(raw_remaining) == 9, raw_remaining
    assert {canonical(e) for e, _, _ in raw_remaining} == {((0,0),(0,1),(1,0),(1,1))}
    A = ((2, 2, 1), (2, 2, 1), (1, 1, 1))
    assert {tuple(map(tuple, z['grid'])) for z in remaining} == {A}
    for z in remaining:
        assert (z['cycle_row'], z['cycle_column']) == (2, 2)
    print(json.dumps({'n': 13, 'extras_orbits': len(reps),
                      'nominal_cycle_placements': len(cases),
                      'collector_excluded': sum(x['collector_excluded'] for x in cases),
                      'raw_eligible_placements': raw_cases,
                      'raw_remaining_placements': len(raw_remaining),
                      'survivors': remaining}, indent=2))
    return cases


if __name__ == '__main__':
    main()
