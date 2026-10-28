"""Independent seven-orbit certificate for Stage34 n22 final 24 profiles.

Hard-coded mathematical seven-orbit inputs, NOT generated from Stage34 code.
Checks full S2xS2 orbit closure, multiplicities, original certified
privacy roots, both no-center conditions and 20/4 analytic reason split.
The separate Stage34 census supplies upstream 24310->24 completeness;
this checker challenges its FINAL stage with an independently fixed oracle.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import sys

RESEARCH = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(RESEARCH / "v4.4"), str(RESEARCH / "v5.0")]
from n22_3x3_frontier import canonical  # noqa: E402
from two_recipient_zero_privacy import improved_privacy, census  # noqa: E402


# Explicit orbit representative, expected orbit size, certified lower
# bounds of complete collectors in upper Q3 and lower P3 exterior cells,
# and the exact human lemma used for LAST-step contradiction.
CERTIFICATE = (
    ((1,1,2,1,1,4,2,4,6), 4, (2,1), (2,1), "six_double_path"),
    ((1,1,2,1,1,4,4,4,4), 2, (2,1), (1,1), "small_private"),
    ((1,1,2,1,4,3,3,3,4), 4, (2,0), (2,0), "small_private"),
    ((1,1,3,1,4,2,3,3,4), 4, (2,1), (2,0), "small_private"),
    ((1,1,3,1,4,3,2,3,4), 4, (2,0), (2,0), "small_private"),
    ((1,1,3,1,4,3,3,2,4), 4, (2,0), (2,1), "small_private"),
    ((1,1,4,1,1,4,2,4,4), 2, (1,1), (2,1), "small_private"),
)


def orbit(m):
    return {tuple(m[3*r+c] for r in rows for c in cols)
            for rows in ((0,1,2), (1,0,2))
            for cols in ((0,1,2), (1,0,2))}


def center_blocked(m, q, p):
    def blocked(sizes, roots):
        return sum(sizes) <= 8 and (max(roots) >= 2 or min(roots) >= 1)
    return (blocked((m[2],m[5]),q), blocked((m[6],m[7]),p))


def independently_certify(m):
    q, p = improved_privacy(m)
    bq, bp = center_blocked(m, q, p)
    assert bq and bp, ("no-center premise failed", m, q, p)
    c = m[8]
    if c <= 5 and (max(q) >= 2 or max(p) >= 2):
        return "small_private"
    if c == 6 and max(q) >= 2 and max(p) >= 2:
        return "six_double_path"
    raise AssertionError(("unclosed necessary orbit", m, q, p))


def main():
    fixtures = set()
    counters = Counter()
    for rep, multiplicity, roots_q, roots_p, reason in CERTIFICATE:
        assert canonical(rep) == rep
        q,p = improved_privacy(rep)
        assert (q,p) == (roots_q,roots_p), (rep, q,p)
        members = orbit(rep)
        assert len(members) == multiplicity
        assert not fixtures.intersection(members)
        fixtures.update(members)
        for m in members:
            assert independently_certify(m) == reason, (m, reason)
            counters[reason] += 1
        print("PASS orbit representative", rep, "members", multiplicity,
              "outside certified minima", q,p,"closure",reason)

    assert len(fixtures) == 24
    assert counters == {"small_private":20,"six_double_path":4}
    assert Counter(m[8] for m in fixtures) == {4:20,6:4}
    assert len({canonical(m) for m in fixtures}) == 7

    # Different evidence lineage: Stage33 is the EARLIER finite necessary
    # profile oracle. Stage34's decision code is NOT imported.
    prior, _, final = census(22)
    assert len(prior) == 32
    assert set(final) == fixtures, (
        "Stage33 24-profile frontier differs from immutable orbit fixture",
        set(final).symmetric_difference(fixtures))
    print("PASS independent immutable 7-orbit certificate covers EXACT Stage33 24")
    print("PASS all 24 direct source/target crossing blockers; 20 + 4 partition")
    print("LIMIT: imports earlier private-minimum HUMAN lemmas, not formal proof")
    print("LIMIT: not a test of all 40-call successful gossip histories")


if __name__ == "__main__":
    main()
