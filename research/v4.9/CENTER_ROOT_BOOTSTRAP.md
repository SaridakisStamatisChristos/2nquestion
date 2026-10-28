# Stage 32 — all-n center-root bootstrap from two exterior collectors

**28 October 2026. Generalization of Stage31, for ALL n in fixed-original-order both-cyclic minimum gossip. The original half-forest conjecture for n≥22 and direct exact temporal-clique spanner bound 2n−3 remain OPEN. PR #1 DRAFT/UNMERGED; manuscript HOLD.**

## Theorem 32.1 — universal 2+1 complete-root transfer

Let U be any connected edge-once chronological unicyclic component whose actual LAST local call e=ab closes its static cycle, with a∈A, b∈B and a designated center X disjoint from A∪B. Suppose **at least two distinct A participants and at least one X participant are terminally complete U collectors**. Then the B endpoint b of e is also a terminal complete U collector, even when |A|>2. Symmetrically swap A/B.

**Proof.** Removing the final e leaves a spanning chronological tree T with |V(U)|−1 distinct calls. In an edge-once chronological tree on at least two vertices, at most TWO participants can be complete after all tree calls, since no one can know every original U secret before the actual last T call and only its endpoints can become complete at that call. The complete X collector never takes part in e, hence was already complete at the end of T. The at least two complete A collectors together with it give at least THREE distinct terminal full participants, so at least one of those A collectors was NOT complete just before e. Only a∈A takes part in e, so a must be terminally complete. A bidirectional call gives its two endpoints identical final knowledge. Therefore b is complete. QED.

The extra X-full premise is essential when A has more than two participants. The Stage31 explicit five-person original unicyclic counterexample has two full A participants, no full B participant, and a nonfull center: e bypasses both full A participants. No step moves the original chronological contact.

### Theorem 32.2 — strong center-complete exclusion when exterior occupancy ≤8

Add the ACTUAL minimum-gossip original-order assumptions of [Stage28](../v4.5/ALL_N_EIGHT_OUTSIDE_COLLECTOR_THEOREM.md): every U-secret has ≥2 terminal carriers in each exterior cell A,B, the opposing closed TREE's last contact lies outside the crossing exterior cell, all four offcorner cells have ≥2 participants, and the earlier conditional Stage28 proof is valid.

If |A|+|B|≤8 and EITHER (i) each of A and B already contains ≥1 full U collector, OR (ii) one of the two exterior cells contains ≥2 full U collectors (with no assumption of full collectors in the other cell), then

\[
\boxed{\text{NO participant of }X\text{ can be a complete U collector.}}
\]

**Proof.** Case (i) is exactly Stage28 Theorem28.1. In case (ii), assume for contradiction that some x∈X is complete. Theorem32.1, applied to the side containing two full collectors, transfers full status to the opposite exterior cell. Both exterior cells therefore contain full U collectors. Stage28 prohibits a center full collector when exterior sum≤8, contradicting x. QED.

This is a genuinely **all-n conditional** structural result; the bound is on exterior occupancy, not on total n or |X|. It does not extrapolate unknown privacy minima. Its use on an incidence profile still depends on certifying the two outside collectors by exact original/reversed TREE private-secret support.

### Corollary 32.3 — low-width center obstruction

Apply Theorem32.2 independently to the original P3 and the **fully reversed actual** Q3. For center |X|=1, at least one blocked cyclic side contradicts exact midpoint crossing. For |X|=2, if both sides are blocked, exact pairwise-intersecting support families on TWO center participants force a complete collector on at least one side, contradiction. For |X|=3, if both sides are blocked, the Stage19 all-n three-recipient doubly-covering edge-once-tree lemma plus absence of opposite center collectors forces a center complete collector, contradiction. Do **not** use the same argument for center≥4.

## Reproducible exact necessary-incidence consequences

[Stage32 independent checker](center_root_bootstrap.py) enumerates the nine positive cells using Stage27's stars-and-bars oracle, applies prior Stage25+Stage26+Stage28 necessary filters without modification, and then implements precisely
\[
\operatorname{blocked}((a,b),(u,v))\iff
a+b\le8\land((u\ge2)\lor(v\ge2)\lor(u\ge1\land v\ge1)).
\]

Here (u,v) are **certified lower bounds on number of complete U collectors** supplied by *opposite-chronology original-tree private-recipient minima*. Unknown classes are assigned ZERO and therefore cannot trigger a new rejection.

| n | Prior Stage28 survivors | Stage32 survivors | newly removed | S2×S2 symmetry orbits |
|---:|---:|---:|---:|---:|
| 21 | 0 | **0** | 0 | 0 |
| 22 | 104 | **32** | **72** | **9** |
| 23 | 1392 | **804** | **588** | **209** |

For n22 the 72 newly rejected comprise 4 center-width-one matrices and 68 center-width-two/three matrices. **No** center-width-one or -two n22 necessary profiles remain. The 32 survivors comprise center-size 3:8, 4:20, 6:4. These are *positive labelled nine-cell incidence matrices*, NOT full successful 40-call gossip histories. Stage32 includes all Stage31 transfer exclusions and is strictly stronger.

Independently, the checker enumerates ALL Prüfer-labelled chronological trees plus a final distinct cycle-closing contact for n=4,5 and **ALL A/B/X partitions** with final call a∈A,b∈B, |A|≥2 and X nonempty. The n4/n5 audit checks **576 / 216,000** local partition-history cases, including **48 / 4,320** cases satisfying the two A full plus one X full antecedent, and finds **zero** failures of the forced-B-full conclusion. This finite check supports and challenges Theorem32.1; the explicit full proof provides the unbounded quantifier.

## Precise scientific gate

- **PROVED human (conditional):** Theorem32.1 all-n spanning tree two-complete property and last-contact identity. Theorem32.2 combines it with previously human-proved Stage28 collector theorem; source/historical assumptions need independent audit.
- **EXECUTABLE finite verification:** Stage32 checker and previous Stages25–28; regressions checked in CI workflow [Stage32](../../.github/workflows/research-v49.yml), latest-head status requires fresh observation.
- **OPEN:** all-n original-half forest property; n22 minimum-gossip chronology feasibility; direct temporal clique exact 2n−3 reachability spanner conjecture; literature novelty; formal Lean/Coq/Isabelle or independent referee.
- **NEXT:** attack the remaining 32 n22 profiles, especially center width3, using a new all-n root/private transfer when another tree recipient cell has exactly two people and a singleton external group, instead of forcing an expensive exact chronology CSP prematurely. Preserve PR DRAFT/UNMERGED and publication HOLD.
