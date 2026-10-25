# Research v1.1 — Half-forest sharp threshold

This checkpoint proves a structural necessary condition for arbitrary gossip schedules and a sharp threshold: every shortest successful 2n−4 call protocol for 4≤n≤7 has acyclic chronological halves, but explicit shortest schedules with a cyclic half exist for all n≥8.

- Mathematical proof / novelty caveats: `RESEARCH_UPDATE_v1.1.md`
- Exact constructive witness and infinite extension: `sharp_half_forest.py`
- Independent reachability DFS and finite graph-structure check: `audit_threshold.py`
- Original K10 adversarial witness: `half_cycle_witness.json`

Run:
```
python research/v1.1/sharp_half_forest.py
python research/v1.1/audit_threshold.py
```
Neither the main 2n−3 conjecture nor POD is proved or disproved. Publication-level novelty is **unverified**.
