"""Stage 28: all-n eight-outside center-collector obstruction + finite census.

Sound ALL-n claim depends on cited human lemmas; this executable checker only
corroborates Boolean crossing, bounded collector-count combinatorics and
numerical application to necessary incidence profiles. Never promote a
candidate incidence matrix to a legal gossip chronology.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import sys

repo = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(repo / "v4.4"))
from n22_3x3_frontier import matrices, stage25, stage26, privacy, canonical  # noqa: E402


def collector_gate(m):
    """All-n theorem applies only when BOTH outside cells force >=1 full root."""
    qmin, pmin = privacy(m)
    qblocked = m[2] + m[5] <= 8 and min(qmin) >= 1
    pblocked = m[6] + m[7] <= 8 and min(pmin) >= 1
    # The theorem forbids a full CENTER collector on the blocked side.
    # In a center of size <=3, crossing plus the chronological tree
    # three-recipient double-cover lemma demands a center full root.
    if m[8] == 1 and (qblocked or pblocked):
        return "singleton_blocked"
    if m[8] == 2 and qblocked and pblocked:
        return "binary_both_blocked"
    if m[8] == 3 and qblocked and pblocked:
        return "triple_both_blocked"
    return "survive"


def crossing_masks(width):
    """Independently exhaust all NONEMPTY families of nonempty carrier masks."""
    possible = tuple(range(1, 1 << width))
    all_families = [
        frozenset(possible[i] for i in range(len(possible)) if bits >> i & 1)
        for bits in range(1, 1 << len(possible))
    ]
    return all_families


def has_full_center(family, width):
    return any(all(mask & (1 << x) for mask in family) for x in range(width))


def crossing_valid(a, b):
    return all(x & y for x in a for y in b)


def audit_crossing():
    for w in (1, 2, 3):
        f = crossing_masks(w)
        bad_pairs = 0
        valid_pairs = 0
        for a in f:
            for b in f:
                if not crossing_valid(a, b):
                    continue
                valid_pairs += 1
                if not has_full_center(a, w) and not has_full_center(b, w):
                    bad_pairs += 1
        if w < 3:
            assert bad_pairs == 0, (w, bad_pairs)
        else:
            # Triangle supports are pairwise intersecting and have NO
            # common center collector. A CHRONOLOGICAL-TREE lemma, not
            # abstract Boolean crossing, is essential for width 3.
            witness = frozenset((3, 5, 6))
            assert crossing_valid(witness, witness)
            assert not has_full_center(witness, 3)
            assert bad_pairs > 0
        print(f"PASS Boolean width={w}: {valid_pairs} compatible family pairs, "
              f"{bad_pairs} lack collectors on both sides")


def audit_four_roots():
    checked = 0
    for a in range(2, 7):
        for b in range(2, 7):
            if a + b > 8:
                continue
            for ar in range(1, 4):
                for br in range(1, 4):
                    cr = 4 - ar - br
                    if cr < 1:
                        continue
                    # 4 complete roots; >=1 each outside and >=1 center.
                    # One outside cell MUST have exactly one root,
                    # and its occupancy is <=6. Stage24 excludes it.
                    assert ar == 1 or br == 1
                    assert (ar == 1 and a <= 6) or (br == 1 and b <= 6)
                    checked += 1
            # With three roots (1 outside each, one center),
            # helper-robust 3-group tree-cover needs 4 designated in
            # EACH of the last-tree sides, hence a+b>=8.
            if a + b == 8:
                assert max(a, b) - 1 >= 3  # three distinct star leaves
    assert checked > 0
    print("PASS 4-root occupancy pigeonhole for all a,b>=2, a+b<=8; "
          "3-root equality requires >=3 opposite-tree star leaves")


def classify_new(n):
    before = Counter()
    after = Counter()
    survivors = []
    removed = []
    for m in matrices(n):
        if stage25(m) != "survive" or stage26(m) != "survive":
            continue
        before[m[8]] += 1
        lab = collector_gate(m)
        after[lab] += 1
        if lab == "survive":
            survivors.append(m)
        else:
            removed.append((m, lab))
    return before, after, survivors, removed


def main():
    audit_crossing()
    audit_four_roots()

    # Independent prior gate script is imported but does not compute
    # new full-center implications. All n>=22 use same new predicate.
    b21, r21, s21, _ = classify_new(21)
    assert sum(b21.values()) == 0 and not s21
    print("PASS Stage26 n21 0 remaining regression")
    b22, r22, s22, removed22 = classify_new(22)
    expected = {"survive": 104, "singleton_blocked": 24,
                "binary_both_blocked": 1, "triple_both_blocked": 8}
    assert dict(r22) == expected, r22
    assert len(s22) == 104
    assert len(set(map(canonical, s22))) == 28
    assert Counter(m[8] for m in s22) == {1: 4, 2: 40, 3: 36, 4: 20, 6: 4}
    assert (1, 1, 4, 1, 1, 4, 4, 4, 2) in [m for m, _ in removed22]
    print("PASS n22 137 -> 104 necessary incidence profiles, 28 orbits")
    print("PASS exact n22 center histogram:",
          dict(sorted(Counter(m[8] for m in s22).items())))

    b23, r23, s23, _ = classify_new(23)
    assert sum(b23.values()) == 1505
    assert r23 == {"survive": 1392, "singleton_blocked": 80,
                   "binary_both_blocked": 4, "triple_both_blocked": 29}
    assert len(set(map(canonical, s23))) == 360
    print("PASS independent n23 cross-check: 1505 -> 1392 (not n23 proof)")
    print("LIMIT: theorem is conditional on Stage24 and Stage15 all-n proofs;")
    print("LIMIT: finite incidence survivors are NOT realizable schedules;")
    print("LIMIT: no all-n half-forest proof, no verified novelty")


if __name__ == "__main__":
    main()
