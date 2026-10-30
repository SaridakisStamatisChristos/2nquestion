# v1.5 — Labahn minimal-order bridge: constructive midpoint non-invariance

**Date:** 2026-10-25. **Status:** finite result, exact exhaustive linear-extension check, and scoped priority audit. **Originality:** UNRESOLVED. **Main 2n−3 temporal-clique conjecture:** OPEN.

## Research question and truth conditions

Does the known classification of optimal gossip *kernel posets* determine the chronological half-forest condition at n=13? More strongly, is the n=13 half-forest theorem an *immediate* corollary of Labahn (1995) without inspecting compatible total contact orders and extra non-kernel calls?

This checkpoint establishes **NO** to the claim that the **abstract minimal-order poset by itself** fixes the individual chronological midpoint component graphs. This does **not** answer whether all *admissible linear extensions* of all Labahn kernels satisfy the at-least-one-forest property, nor whether Labahn's full theory implies the n=13 result.

## Literary reconstruction actually available

Renken (2023), thesis *Algorithmic and Structural Aspects of Temporal Graphs*, Section 4, pp. 97–102 (PDF physical pp. 107–112):
https://d-nb.info/1289610584/34

Renken explicitly reconstructs the **minimal order** on edges (comparability by temporal event-to-event walk), its initial/final antichains, Labahn's Theorem 3.1 equality of their sizes, and Labahn's Section 6 kernel pattern for κ≥5:
- kernel has 4κ−4 contact-events in κ initial edges d_i, κ final edges c_i, κ−2 left-chain edges a_i and κ−2 right-chain edges b_i;
- the kernel footprint contains exactly 2κ vertices (Renken Lemma 4.37), with predecessor/successor covers specified in the thesis;
- the a/b cross-cover relations involve admissible permutations ρ,σ constrained by Labahn's original Section 6 (not fully reproduced);
- Theorem 6.3 counts admissible pairs, but **a count does not provide their predicate**;
- the *non-kernel* first/last contact trees must also be attached to reach 13 participants.

For **n=13**, κ≥5 could be κ=5 (10 kernel vertices, 16 kernel calls, 6 fringe calls) or κ=6 (12 kernel vertices, 20 kernel calls, 2 fringe calls). Exceptional κ=2,3,4 families also require treatment. Therefore direct exhaustive "all Labahn-compatible n13 schedules" **cannot responsibly be claimed from the available partial Section 6 reconstruction**.

Labahn 1995 primary publisher abstract: https://doi.org/10.1016/0012-365X(94)00031-D ;
Krumme 1996 reordering theorem abstract: https://doi.org/10.1016/0012-365X(94)00302-Y .
Full original papers were not accessible in this run.

## Constructive result: two linearly extended schedules on n=13

Fix the n=8 sequence S from the earlier v1.1 witness:
\`\`\`
01 45 37 26 23 15 04 12 67 46 35 07
\`\`\`
Here two-digit tokens are undirected vertex contacts; the script has canonical tuples.

Define the event-order poset P by transitive closure of all incident-event precedence orders: if two calls share a vertex, their original chronology is preserved. Incomparable events have disjoint endpoints. Any adjacent swap of incomparable events preserves gossip knowledge and event reachability. Accordingly **every linear extension of P** has the same static event set, the same per-vertex chronological subsequences, the same event-to-event reachability poset, and the same Labahn kernel extracted from that poset.

An exact depth-first enumeration of **ALL 51,200 labelled linear extensions** of this single 12-event poset gave the following first-half and second-half cycle rank distribution (six events in each):
| Cycles in prefix | Cycles in suffix | Number of extensions |
| --- | --- | ---: |
| 0 | 0 | 12,800 |
| 0 | 1 | 19,200 |
| 1 | 0 | 19,200 |
| other | any | 0 |

We select one of the 19,200 (0,1) extensions, A8, and one of the 12,800 (0,0) extensions, B8. Both are valid 12-call gossip schemes on 8 vertices and have identical original event-poset relations. In particular the **poset does not determine whether the second half is cyclic**.

Extend each n-schedule S to (n+1) participants by inserting contact (n,0) before S and contact (n,1) after S. All information from the new participant enters the old optimal schedule through vertex 0, and the new participant obtains the old participants' complete knowledge at the last contact with vertex 1. These two edges are distinct and give 2(n+1)−4 calls. The construction preserves each old participant's incident-event order in both A and B; it adds the **same** new events at both ends.

Applying this identical construction five times yields two explicit successful, 22-call, distinct-edge **n=13** schedules **A13 and B13**, both with precisely the same per-vertex contact orders, event-to-event reachability poset, and kernel statistics:
- **A13:** midpoint prefix is a forest, suffix has one cycle, i.e. (0,1).
- **B13:** both midpoint halves are forests, i.e. (0,0).
- Across n=8..13, script verifies full gossip, unique contacts, event-poset signature equality, equal kernel statistics and expected cycle ranks.

**Formal logical implication:** From *a given abstract kernel P alone*, one cannot deduce the separate original midpoint cycle ranks; both are realized by legal linear extensions of the same stronger full minimal event-poset. To test the weaker statement "at least one half is a forest for every extension", one MUST either analyze *all extensions* or prove a stronger ordering-invariant obstruction. This finite pair does not contradict the n=13 half-forest theorem (both schedules have a forest half), and does not disprove a deep corollary of Labahn.

## Independent finite equality checks

The script independently reconstructs (using event-to-event temporal reachability) the maximal initial antichain, minimal final antichain, and induced kernel; it verifies the **necessary** Labahn cardinality invariants on every successful distinct-contact minimal K4/K5 scheme:
- K4: 360 candidate orders, **24** successful, 24 pass;
- K5: 151,200 candidate orders, **3,240** successful, 3,240 pass;
- for each successful scheme: κ_initial=κ_final and kernel size = 4κ−4.

This test is **not** verification of all Labahn's sufficient kernel-cover constraints, or of κ≥5 cases. Treat it as a cross-check of the extraction code.

## v1.4 classifier correction / independent assurance note

The previous v1.4 \`half_forest13_reduction.py\` emitted two logically **invalid reasons**: while scanning a suffix tree column with **two singleton intersections**, it wrongly flagged each of those singleton bridge endpoints as if it were the *third* prefix source, whereas the first-bridge covering condition concerns only the **third** prefix source. The same error appeared in the time-reversed dual.

**Repaired:** skip the two bridge-endpoint cells rather than attributing impossibility to them. Local independent recomputation on the 44 nominal eligible cycle placements found that **43 placements** had at least one spurious rejection reason, but **none** was excluded solely by a spurious reason: after removing every such reason, 43 are still excluded and exactly the previous square pattern remains. Re-run the corrected script in GitHub CI. The original finite verdict survives **this** correction; the result still requires a wholly independent completeness audit.

## Code and reproduce

\`\`\`sh
python3 research/v1.5/minimal_order_bridge.py
python3 research/v1.4/half_forest13_reduction.py
python3 research/v1.4/verify_square.py
\`\`\`

The n8 extension enumeration and n13 pair are executed in local Python 3.13.5, and verified by the \`research-v15.yml\` GitHub CI workflow from committed source. The v1.4 classifier is rerun. This is exact *finite* evidence, not Lean/Coq formal verification or external peer review.

## Independent assurance status

| Audit gate | Status |
| --- | --- |
| Actual source/branch reconstruction | PASS |
| Explicit n13 same-poset witness pair | PASS (finite executable, elementary induction) |
| Exhaustive n8 event-poset linear extensions | PASS (51,200, finite enumeration) |
| Labahn necessary kernel-size regression K4/K5 | PASS |
| Fixed v1.4 invalid exclusion reasons | PASS (finite residual classification unchanged) |
| **All Labahn-compatible n13 kernel/linear extensions** | **UNVERIFIED — missing full admissible permutations + fringe rules; not executed** |
| v1.4 finite theorem independent completeness audit | PARTIAL |
| Equivalence or non-equivalence to Labahn's full theorem | UNRESOLVED |
| Novelty claim | BLOCKED |
| Main fixed-chronology 2n−3 conjecture | OPEN |

## Next decisive mathematical program

Obtain full Labahn (1995) Section 6, including κ=2..4 exceptional classifications, precise ρ/σ admissibility, all kernel-to-graph footprints and fringe attachment constraints. Implement their exact generative model, independently compare its *image* with full shortest-schedule enumerations for n<=6, and only then explore n=13 with symbolic/constraint methods. The correct question becomes whether **every admissible extension** has at least one forest half, not whether the poset records each midpoint structure by itself.

**Keep PR in draft; do not claim historical priority or universal discovery.**
