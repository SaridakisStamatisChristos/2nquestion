"""Stage 26 independent finite 21-person original half-forest incidence closure.

Uses Stage 25's separately CI-tested all-positive 9-cell enumeration to
recover exactly 77 necessary candidate matrices. Each further rejection is
by a precisely documented all-n original-chronology lemma in
research/v4.3/N21_ORIGINAL_FOREST_THEOREM.md.

This is a NECESSARY-INCIDENCE census, NOT enumeration of global 38-call orders
and not formal proof assistant verification of the mathematical lemmas.
"""
from collections import Counter
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "v4.2"))
from n21_staged_frontier import direct, canonical, private, three_outside  # noqa: E402


def small_outside_pair(a, b):
    return (a == 2 or b == 2) and max(a, b) <= 6


def stage22_243(m):
    if m[8] != 3:
        return False
    qmins, pmins = private(m)
    for cells, minima in (((m[2], m[5]), qmins),
                          ((m[6], m[7]), pmins)):
        if sorted(cells) != [2, 4]:
            continue
        index2 = 0 if cells[0] == 2 else 1
        index4 = 1 - index2
        if minima[index2] >= 2 and minima[index4] >= 1:
            return True
    return False


def classify_final(m):
    upper = (m[2], m[5])
    lower = (m[6], m[7])
    center = m[8]
    qmins, pmins = private(m)
    q3 = three_outside(upper, qmins)
    p3 = three_outside(lower, pmins)

    # A singleton midpoint must be complete for BOTH cyclic components.
    # Four full collectors would contradict Stage24's singly-rooted
    # other-offcorner occupancy >=7.
    if center == 1 and (small_outside_pair(*upper) or
                        small_outside_pair(*lower)):
        return "singleton_center_four_root_contradiction"

    # Both cyclic sides lack center full collectors, which is incompatible
    # with the exact exhaustive 2-person midpoint-crossing trichotomy.
    if center == 2 and small_outside_pair(*upper) and small_outside_pair(*lower):
        return "binary_center_no_complete_collector"

    # Three-person double-cover in chronological spanning TREE forces
    # one full collector in center (Stage19), forbidden by Stage24.
    if center == 3 and q3 and small_outside_pair(*lower):
        return "triple_center_P_complete_contradiction"
    if center == 3 and p3 and small_outside_pair(*upper):
        return "triple_center_Q_complete_contradiction"

    # Both sides lack complete center collectors, so center secrets are
    # doubly covered. In the spanning tree of one U, two complete roots
    # remain OUTSIDE center, requiring center size >=6 (Stage13).
    if (center < 6 and small_outside_pair(*upper) and
            small_outside_pair(*lower)):
        return "two_root_double_cover_requires_center_six"

    if stage22_243(m):
        return "preexisting_three_star_243_exclusion"

    # Only last (4,4,1) matrix: one full collector in each offcorner
    # from the independently exhaustive tree (1,1,4) privacy minimum,
    # plus singleton center full. Four full roots prohibited by Stage24.
    # Three roots imply two tight last-edge chronological tree covers;
    # helper-robust equality makes 3 distinct outer private leaves,
    # all with support {complete_b,z_i}. These cannot cross the opposite
    # original tree whose final call has endpoints outside the outer cell.
    if m == (1, 1, 4, 1, 1, 4, 4, 4, 1):
        assert qmins == (1, 1) and pmins == (1, 1)
        return "final_441_three_star_contradiction"

    return "UNRESOLVED"


def main():
    counts20, old20 = direct(20)
    assert len(old20) == 0 and counts20["dual3"] == 52
    print("PASS Stage23 independent n20 original half-forest regression")

    old21_counts, candidates = direct(21)
    assert len(candidates) == 77
    assert len(set(map(canonical, candidates))) == 22
    assert old21_counts["privacy4"] == 529
    print("PASS Stage25 n21 initial 77 necessary matrices / 22 symmetry orbits")

    by_reason = Counter(classify_final(m) for m in candidates)
    expected = {
        "singleton_center_four_root_contradiction": 8,
        "binary_center_no_complete_collector": 4,
        "triple_center_P_complete_contradiction": 20,
        "triple_center_Q_complete_contradiction": 20,
        "two_root_double_cover_requires_center_six": 20,
        "preexisting_three_star_243_exclusion": 4,
        "final_441_three_star_contradiction": 1,
    }
    assert by_reason == expected, (by_reason, expected)

    # Independent audit: exactly one orbit representative is invariant
    # under both tree component row/column swaps.
    last = (1, 1, 4, 1, 1, 4, 4, 4, 1)
    assert canonical(last) == last
    assert len({canonical(m) for m in candidates}) == 22
    assert all(classify_final(m) != "UNRESOLVED" for m in candidates)

    prefix = 0
    for reason, n in by_reason.items():
        prefix += n
        print(f"PASS {reason}: excludes {n} labelled matrices")
    assert prefix == 77
    print("PASS exact original n21 necessary-incidence closure: 77 -> 0")
    print("LIMIT: human chronological proof, finite matrix census, "
          "not exhaustive enumeration of successful 38-call schedules")


if __name__ == "__main__":
    main()
