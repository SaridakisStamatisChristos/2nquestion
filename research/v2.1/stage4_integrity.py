"""Fail-closed Stage-4 source/manuscript/certificate cross-consistency preflight.

This is an editorial integrity check, NOT a mathematical novelty certificate.
The existing v2.1 full verifier and independent Stage-3 workflow provide the
actual finite computation; this script checks the research text claims.
"""
import json
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parent
record=json.loads((ROOT/"N15_CERTIFICATE.json").read_text())
cases=record["orbits"]
assert len(cases)==20
assert [x["orbit"] for x in cases]==list(range(20))
assert record["structural"]=={
    "allocations":3003, "eligible":13680, "basic":4662,
    "strong":945, "orbits":20
}
assert sum(c["multiplicity"] for c in cases)==945
assert len({(tuple(map(tuple,c["matrix"])),c["cyclic_row"],c["cyclic_col"])
            for c in cases})==20

counts=Counter()
for case in cases:
    assert 0<=case["cyclic_row"]<3 and 0<=case["cyclic_col"]<3
    assert len(case["matrix"])==3
    assert all(len(row)==3 for row in case["matrix"])
    assert all(1<=v<=7 for row in case["matrix"] for v in row)
    assert sum(map(sum,case["matrix"]))==15
    assert len(case["row_domains"])==len(case["col_domains"])==3
    local=any(size==0 for size in
              case["row_domains"]+case["col_domains"])
    if case["result"]=="LOCAL_UNSAT":
        assert local
        counts["local"]+=1
    elif case["result"]=="PROFILE_UNSAT":
        assert not local
        counts["optimistic" if case["optimistic"] else "exact"]+=1
    else:
        raise AssertionError(("unknown or SAT case",case["orbit"]))
assert counts=={"local":6,"exact":10,"optimistic":4},counts

paper=(ROOT/"PAPER_DRAFT_STAGE4.md").read_text()
audit=(ROOT/"STAGE4_PRIORITY_AND_PUBLICATION_AUDIT.md").read_text()
review=(ROOT/"STAGE4_REVIEWER_REPORT.md").read_text()
status=(ROOT/"STATUS.md").read_text()
for title,text in (("paper",paper),("priority audit",audit),
                   ("review",review),("status",status)):
    assert ("n=15" in text or "15 vertices" in text or "n<=15" in text),(
        title,"missing fifteen-participant scope")
    for anchor in ("945","20"):
        assert anchor in text,(title,"missing",anchor)
    assert "unresolved" in text.lower(),title
for term in ("33","6","10","4","minimum","chronological",
             "original","Labahn","Krumme","Williams",
             "not submitted","N15_CERTIFICATE.json"):
    assert term.lower() in paper.lower(),("paper missing",term)
for required in ("PASS-CONDITIONAL","HOLD","MAJOR BLOCKERS"):
    assert required in audit or required in review,required
for name in (
    "stage3_independent_oracle.cpp",
    "stage3_adversarial_check.py",
    "stage3_exhaustive_stress.py",
    "N15_CERTIFICATE.json",
    "STAGE3_ADVERSARIAL_AUDIT.md",
    "STAGE4_PRIORITY_AND_PUBLICATION_AUDIT.md",
    "STAGE4_REVIEWER_REPORT.md",
):
    assert (ROOT/name).is_file(),name

# These are verifiable bibliographic identifiers, not evidence of mathematical
# non-derivability. Static checks deliberately do not assert scholarly novelty.
for doi in (
    "10.1016/0012-365X(91)90068-D",
    "10.1016/0012-365X(94)00031-D",
    "10.1016/0012-365X(94)00302-Y",
    "10.61091/cn238-05",
    "10.1016/j.jcss.2021.04.004",
):
    assert doi in paper,("bibliography missing DOI",doi)
assert "2n-3" in paper
print("PASS Stage4 integrity: 20 orbit records / 945 placements / 6+10+4 categories")
print("PASS Stage4 integrity: manuscript, literature, referee report, source paths, DOIs")
print("EDITORIAL VERDICT: AUDIT COMPLETE; NOVELTY UNRESOLVED; SUBMISSION HOLD")
