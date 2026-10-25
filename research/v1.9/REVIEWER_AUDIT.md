# v1.9 adversarial research-paper review

**Artifact:** [working manuscript](PAPER_DRAFT.md). This is a structured adversarial audit, **not** an external referee report.

## Contribution preflight and stress test

Classical ingredients removed from originality claims: the 2n−4 lower bound, static two-forest partitions and vertex extension (Göbel et al., 1991), Labahn's p-grid kernels and linear extensions (1995), Krumme's reordering (1996), and contemporary prefix-tree/commuting-call methods (Williams, 2026).

**Surviving narrow contribution:** original-chronology finite n13 half-forest certificate plus a self-contained rectangular-grid cost bound n≥5s−4 and its n≤15 grid-confinement corollary. Scope is **BOUNDED**, novelty **CONDITIONAL**. We did not establish any universal n theorem nor the temporal-clique 2n−3 bound.

## Reviewer objections and dispositions

| Objection | Severity | Disposition |
| --- | --- | --- |
| A singleton tree has no final internal edge. | Moderate | Paper explicitly states *nontrivial tree*; in success with all component intersections, actual components have ≥2 vertices. |
| Forced bridge rule accidentally applied to singleton endpoints rather than a third source. | Major | Corrected since v1.4; v1.7 independent code applies third-source rule only. |
| Enumerating local orders might miss global interleavings. | Major | Distinct components of a half have disjoint vertex sets and their calls commute; all order-sensitive information resides inside local orders. |
| The residual-square suffix filter discards edge orders. | Major | It keeps every order that broadcasts unique prefix-triangle source information, a necessary condition of global success. |
| Independently written scripts may share a conceptual mistake. | Moderate | Separate implementations and CI green; external proof reviewer still desired. |
| n14/15 survivors might be read as realizable counterexamples. | Major | Paper table and code explicitly label survivors of **necessary** filters only. |
| Gossip schedules might be confused with fixed-label temporal clique spanners. | Major | Paper disclaims implication. |
| Historical novelty over Labahn/Krumme implicit corollaries. | Major / open | Full originals audited in v1.8, no exact explicit matches, but global originality and significance not certified. |
| Author information/venue not specified. | Minor | Working draft remains unsigned/unsubmitted. |

## Claim-to-evidence gate

- Information conservation, grid rank, collector and rectangular-grid inequalities: **human proof provided**.
- Finite n13 result: **independent exact enumeration/UNSAT with successful GitHub Actions** v1.4/v1.7; not machine-formally checked.
- n14/n15 necessary-grid counts: **reproducible standalone exact filter** v1.9; not an n14 theorem of impossibility.
- 5,000,000-mutation n14 null search: **exploratory only**, no significance without a successful independently verified witness.
- Literature DOI metadata: verified; historical *first-ever* claim not justified.
- Overall: **DRAFT COMPLETE; REFRAME / NOT YET SUBMISSION READY**. A stronger new theorem or expert novelty review would materially improve the case.

**Next mathematical bottleneck:** Exact chronological feasibility at n14 across 11 surviving matrix symmetry classes; a full solver must honor individual contacts, pairwise edge distinctness, information propagation, and unambiguous UNSAT certificates. Do not mistake necessary-condition pruning for a complete solver.
