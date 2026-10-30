"""Fail-closed orbit identity check for Stage 6 final n17 closure.

The eight records excluded by exclude_n17_residual_eight.cpp MUST match
the independently generated sorted canonical 3x3 orbit map. A stale orbit
index, matrix, cyclic placement, or multiplicity invalidates the closure.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "v2.0"))
from half_forest14_grid import run

A = ((1, 1, 2), (1, 1, 2), (2, 3, 4))
B = ((1, 1, 2), (1, 1, 2), (2, 4, 3))
C = ((1, 1, 2), (1, 2, 2), (2, 2, 4))
EXPECTED = {
    32: (A, 0, 0, 72),
    33: (A, 0, 1, 72),
    34: (A, 2, 2, 36),
    35: (B, 0, 0, 72),
    72: (C, 0, 0, 36),
    73: (C, 0, 1, 72),
    74: (C, 1, 1, 36),
    75: (C, 2, 2, 36),
}

def main():
    eligible, basic, strong, orbits = run(17)
    assert (eligible, basic, strong, len(orbits)) == (75933, 45783, 15777, 256)
    ordered = sorted(orbits.items())
    for idx, (matrix, cr, cc, mult) in EXPECTED.items():
        (actual_matrix, actual_cr, actual_cc), actual_mult = ordered[idx]
        assert (actual_matrix, actual_cr, actual_cc, actual_mult) == (
            matrix, cr, cc, mult
        ), (idx, actual_matrix, actual_cr, actual_cc, actual_mult)
    assert sum(x[3] for x in EXPECTED.values()) == 432
    print("PASS exact canonical identity and weights for final eight n17"
          " classes: indices 32–35, 72–75; 432 marked placements")

if __name__ == "__main__":
    main()
