"""Stage34: original n22 half-forest conditional HUMAN proof census.

All n22 positive 3x3 necessary incidence matrices (Bumby 1981) are filtered
by exact original-order lemmas from earlier stages plus two new ALL-n center
support obstructions. This script certifies finite reason partition,
NOT human lemma validity or full chronological schedule enumeration.

New all-n implications:
1. If neither U=P3 nor reversed V=Q3 has a complete shared-center collector,
   every U/V original secret has >=2 midpoint carriers in center C.
2. If U has >=2 complete terminal OUTSIDE collectors in the SAME exterior
   cell, the final cycle edge touches at most one of them. An untouched
   full outside collector is already full after preceding spanning tree T_U.
   Thus both endpoints of T_U's last tree contact are complete outside C.
3. Stage29 tree (1,1,c) zero-privacy threshold forces c>=6.
4. If BOTH U and V have the property and c==6, Stage30 distinct
   double-path support systems cannot cross for all original source-target
   pairs. Hence both-rooted case forces c>=7.

At n22, existing Stage33 filter leaves 24 profiles: 20 c4 with >=2
outside full roots on >=1 side, and 4 c6 with >=2 on BOTH sides.
This provides a complete finite incidence closure, CONDITIONAL on the
cited all-n human lemmas and original Bumby fixed-time spine.
"""
from collections import Counter, defaultdict
from pathlib import Path
import sys

R = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(R / "v4.4"), str(R / "v4.5"),
                str(R / "v4.9"), str(R / "v5.0")]
from n22_3x3_frontier import matrices, canonical, stage25, stage26  # noqa: E402
from unbounded_eight_outside_audit import collector_gate  # noqa: E402
from center_root_bootstrap import new_gate as gate32  # noqa: E402
from two_recipient_zero_privacy import (extended_gate as gate33,
                                        improved_privacy)  # noqa: E402


def blocked_u_sides(m):
    q, p = improved_privacy(m)
    up, dn = (m[2], m[5]), (m[6], m[7])

    def blocked(sz, minima):
        return (sum(sz) <= 8 and
                (max(minima) >= 2 or min(minima) >= 1))

    return blocked(up, q), blocked(dn, p), q, p


def center_support_gate(m):
    bq, bp, q, p = blocked_u_sides(m)
    center = m[8]
    # New lemma needs absence of complete center collectors on BOTH
    # original/reverse cyclic components. Never infer that merely from
    # a matrix unless both Stage32 closure predicates are proven.
    if not (bq and bp):
        return "survive"
    if center <= 5 and (max(q) >= 2 or max(p) >= 2):
        return "small_center_private"
    if center == 6 and max(q) >= 2 and max(p) >= 2:
        return "six_center_doublepath"
    return "survive"


def classify(m):
    if stage25(m) != "survive":
        return "Stage25_" + stage25(m)
    if stage26(m) != "survive":
        return "Stage26_" + stage26(m)
    if collector_gate(m) != "survive":
        return "Stage28_" + collector_gate(m)
    if gate32(m) != "survive":
        return "Stage32_" + gate32(m)
    if gate33(m) != "survive":
        return "Stage33_" + gate33(m)
    return "Stage34_" + center_support_gate(m)


def whole_census(n):
    counters = Counter()
    finalists = []
    last = []
    for m in matrices(n):
        name = classify(m)
        counters[name] += 1
        if name == "Stage34_survive":
            finalists.append(m)
        if name.startswith("Stage34_"):
            last.append((m, name))
    return counters, finalists, last


def main():
    c21, s21, f21 = whole_census(21)
    assert not s21 and not f21
    print("PASS n21 original-stage necessary-incidence zero-survivor regression")

    c22, s22, f22 = whole_census(22)
    assert sum(c22.values()) == 24310
    assert not s22
    assert len(f22) == 24
    assert Counter(label for _, label in f22) == {
        "Stage34_small_center_private": 20,
        "Stage34_six_center_doublepath": 4,
    }
    assert len({canonical(m) for m, _ in f22}) == 7
    assert all(blocked_u_sides(m)[0:2] == (True, True)
               for m, _ in f22)
    for m, label in f22:
        q, p = improved_privacy(m)
        if label == "Stage34_small_center_private":
            assert m[8] == 4
            assert max(q) >= 2 or max(p) >= 2
        else:
            assert label == "Stage34_six_center_doublepath"
            assert m[8] == 6
            assert max(q) >= 2 and max(p) >= 2
    print("PASS n22 exact 24 surviving Stage33 labelled matrices -> ZERO")
    print("PASS final reason partition: 20 private-small, 4 double-path-six")
    print("PASS 24 final Stage33 matrices = 7 S2xS2 symmetry orbits")
    print("PASS every excluded final n22 profile has both no-center premises")

    c23, s23, f23 = whole_census(23)
    assert len(f23) == 732
    assert Counter(label for _, label in f23) == {
        "Stage34_survive": 396,
        "Stage34_small_center_private": 288,
        "Stage34_six_center_doublepath": 48,
    }, Counter(label for _, label in f23)
    assert len(s23) == 396
    assert len({canonical(m) for m in s23}) == 104
    print("PASS n23 conditional necessary matrices 732 -> 396 / 104 orbits")
    print("LIMIT: finite incidence census is NOT a global schedule enumeration")
    print("LIMIT: all-n support lemmas are human proofs, not Lean/Coq-checked")
    print("LIMIT: any missing hypothesis in cited Stage14..33 invalidates")
    print("       the n22 proof and mandates automatic publication HOLD")
    print("LIMIT: n>=23 original-half conjecture and 2n-3 spanner remain OPEN")


if __name__ == "__main__":
    main()
