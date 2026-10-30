# Stage 27 — n=22 conservative original-half \(3\times3\) incidence frontier

**28 October 2026. Computational necessary-condition census only. No \(n=22\) forest theorem and no all-\(n\) theorem. Publication HOLD; PR #1 DRAFT/UNMERGED.**

## Exact contract and scope

Assume a successful, shortest, **pairwise-distinct**, bidirectional gossip chronology on \(n=22\) vertices (40 calls), both **original** 20-call halves cyclic, with **exactly three prefix components and three reversed-suffix components**. As in the [Stage 26 original-order analysis](../v4.3/N21_ORIGINAL_FOREST_THEOREM.md), label the two tree components and one unicyclic component on each side, form the nine positive intersection sizes \(m_{ij}\), and enforce four off-corner cells \(\ge2\).

**Universal shape closure (already classical):** Bumby's 1981 Theorem 3, as audited with the source-level closed-tree spine in [Stage 12](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md), excludes FOUR or more components from EITHER chronological half in any successful minimum-call schedule. Since a cyclic half with n−2 contacts must have at least three components, **both cyclic forces r=s=3 for all n**. Thus this Stage 27 census covers every admissible both-cyclic **incidence shape** at n=22, although it does NOT enumerate legal chronologies or prove the conjecture. Earlier Stage 9 numerical r×s thresholds for r>=4 apply to relaxed impossible combinatorial grids, not realizable shortest gossip splits.

The 3×3 baseline is
\[
M_0=\begin{pmatrix}1&1&2\\1&1&2\\2&2&1\end{pmatrix}
\quad\text{(sum 13)}.
\]
Distributing nine extra occupants among the nine labelled cells produces exactly \(\binom{17}{8}=24,310\) labelled matrices.

## Executed independent finite audit

[Stage 27 checker](n22_3x3_frontier.py) enumerates weak compositions via separator positions, **not** Stage 25's recursive generator. It implements all applicable earlier necessary conditions independently, using the exact 16 previously exhausted chronological tree-privacy minima. **Unknown privacy types default to zero** so they cannot cause unjustified rejection. It checks each classified matrix against the prior Stage 25 and Stage 26 code when run in the repository, including all positive \(n=21\) matrices, and checks row/column tree-component swap orbits.

| Sound necessary-filter stage, conditional on cited proofs | n22 3×3 labelled survivors |
|---|---:|
| All positive off-corner-constrained matrices | 24,310 |
| Cyclic components each have \(\ge9\) vertices | 3,396 |
| Off-corner \((2,2)\) pairs excluded for \(n<43\) | 2,598 |
| Known exact private-recipient minima and four-collector cap | 1,389 |
| Both three-outside-collector qualifications contradictory | 1,061 |
| Stage 25 singleton and binary center/root-cut filters | **761** |
| Stage 26 singleton center with a \((2,\le6)\) exterior pair | 689 |
| Stage 26 binary center with two such exterior pairs | 649 |
| Stage 26 triple-center collector contradiction | 481 |
| Stage 26 two-outside-root double-cover | 217 |
| Stage 22 universal \((2,4,3)\) conditional three-star exclusion | **137** |

The final **137 labelled necessary-condition survivors (within the universal 3×3 shape)** form **42 tree-row/tree-column swap orbits**, with center \(m_{33}\) distribution \(\{1:28,2:41,3:44,4:20,6:4\}\). These are **not** gossip schedules. A passing test establishes the enumerated arithmetic and faithful application of these predicates, **not** the published/earlier human lemmas independently and not actual satisfiability.

Differential regression: \(n=21\) baseline 12,870, Stage 25 remaining 77, Stage 26 remaining **zero** under the cited human lemmas. The special \((4,4,1)\) Stage 26 case sums to 21 and is intentionally **not** reused to eliminate an \(n=22\) matrix.

## Reproduction

From repository root:

~~~bash
python3 -B research/v4.4/n22_3x3_frontier.py
~~~

The matching [Stage 27 CI workflow](../../.github/workflows/research-v44.yml) must execute and succeed on the **latest commit** before labeling the GitHub run CI-VERIFIED. The script was run successfully in a local Python environment; that standalone run explicitly lacked its repository-import differential oracle, which CI will exercise.

## Proof frontier and adversarial obligations

1. **Historical shape prerequisite:** independently re-audit Bumby's Theorem 3 as applied to the ORIGINAL split, especially its order-ideal and closed-tree hypotheses. The [Stage 12 primary-source analysis](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md) already establishes r=s=3 universally for both-cyclic shortest schedules. Do NOT resurrect 3×4/4×3 as open genuine shapes merely because older relaxed counting bounds permit them.
2. **137 open 3×3 matrices:** build *sound original-chronology local information-profile oracles*; do not treat conservative incidence survival as feasible gossip.
3. **Large tree privacy:** compute certified privacy minima for newly needed 8-person+ corner-group triples; until then use zero (no extrapolation).
4. **Global proof:** seek a structural descent or an unbounded cell/crossing impossibility. Small-\(n\) success and extension/upward closure alone cannot establish the universal half-forest conjecture.
5. **Independent assurance:** audit the hypotheses of Stage 14, Stage 17, Stage 20, Stage 24 and Stage 26 before promoting any theorem. The historical priority status remains unresolved, especially against [Bumby 1981](https://doi.org/10.1137/0602002), [Labahn 1995](https://doi.org/10.1016/0012-365X(94)00031-D) and [Krumme 1996](https://doi.org/10.1016/0012-365X(94)00302-Y).

**Evidence ledger:** \(3\times3\) finite enumerator = locally EXECUTED; latest-head CI = UNVERIFIED pending observed completion; underlying all-\(n\) lemmas = HUMAN ARGUMENTS requiring independent mathematical review; r>=4 or s>=4 = classically EXCLUDED by Bumby Theorem 3; \(n=22\) theorem = OPEN; full conjecture = OPEN. Preserve PR DRAFT/UNMERGED and manuscript HOLD.
