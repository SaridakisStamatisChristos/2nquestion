"""Stage 27: exact but conservative ORIGINAL n22 necessary-incidence census.

Imports separately passing Stage25 (baseline 9-cell census) and Stage26
(original-order local collector rejection) filters. Adds the ALL-n Stage26
4/4/1 local three-star collector contradiction with only verified adjacent
chronological-tree privacy minima. No complete 40-call schedules enumerated.
"""
from collections import Counter
from pathlib import Path
import sys

here=Path(__file__).resolve().parent
sys.path.insert(0, str(here.parent / "v4.2"))
sys.path.insert(0, str(here.parent / "v4.3"))

from n21_staged_frontier import direct, canonical, private, independent_baseline # noqa: E402
from n21_final import classify_final # noqa: E402


def conditional_441(m):
    if m[8] != 1:
        return False
    qprivacy, pprivacy=private(m)
    return ((m[2],m[5])==(4,4) and min(qprivacy)>=1 or
            (m[6],m[7])==(4,4) and min(pprivacy)>=1)


def main():
    _, n21 = direct(21)
    assert n21 and len(n21) == 77
    assert all(classify_final(m) != "UNRESOLVED" for m in n21)
    print("PASS original n21 Stage26 proof finite closure remains ZERO")

    cnt, initial=direct(22)
    assert sum(cnt.values())==24310
    assert (sum(v for k,v in cnt.items() if k!="component"),
            sum(v for k,v in cnt.items() if k not in ("component","saturated"))) == (3396,2598)
    assert independent_baseline(22)==(3396,2598)
    expected_baseline = {
        "component":20914,"saturated":798,"privacy4":1209,
        "dual3":328,"binary_rootcut":244,
        "singleton4":56,"survive":761
    }
    assert cnt == Counter(expected_baseline),(cnt,expected_baseline)
    assert len({canonical(m) for m in initial})==198
    print("PASS initial n22 24310 labelled grids => 761 necessary => 198 orbits")

    by_stage26=Counter(classify_final(m) for m in initial)
    expected_stage26={
        "UNRESOLVED":137,
        "two_root_double_cover_requires_center_six":264,
        "preexisting_three_star_243_exclusion":80,
        "triple_center_P_complete_contradiction":84,
        "triple_center_Q_complete_contradiction":84,
        "binary_center_no_complete_collector":40,
        "singleton_center_four_root_contradiction":72,
    }
    assert by_stage26==Counter(expected_stage26),(by_stage26,expected_stage26)
    remaining=[m for m in initial if classify_final(m)=="UNRESOLVED"]
    assert len(remaining)==137
    assert len({canonical(m) for m in remaining})==42
    print("PASS Stage26 all-n necessary lemmas => 137 n22 profiles / 42 orbits")

    new_excluded=[m for m in remaining if conditional_441(m)]
    final=[m for m in remaining if not conditional_441(m)]
    assert len(new_excluded)==24,len(new_excluded)
    assert len(final)==113,len(final)
    assert len({canonical(m) for m in final})==33
    assert Counter(m[8] for m in final)==Counter({1:4,2:41,3:44,4:20,6:4})
    # Singleton four corner representative must be fully nontrivial,
    # not a successful schedule.
    assert (1,1,3,1,2,5,3,5,1) in {canonical(m) for m in final}
    assert (1,1,2,1,1,4,2,4,6) in {canonical(m) for m in final}
    print("PASS independently reuse Stage26 all-n (4,4,1) three-star: 24 exclusions")
    print("PASS exact n22 necessary frontier:",len(final),
          "labelled matrices /",len({canonical(m) for m in final}),"orbits")
    print("PASS center counts",dict(sorted(Counter(m[8] for m in final).items())))
    print("LIMIT: 113 are incidence survivors, NOT 40-call successful schedules")
    print("OPEN: n22 original chronological half-forest, all n>=22")


if __name__=="__main__":
    main()
