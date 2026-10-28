# Stage 27 — n=22 conservative original-half \(3\times3\) incidence frontier

**28 October 2026. Computational necessary-condition census only. No \(n=22\) forest theorem and no all-\(n\) theorem. Publication HOLD; PR #1 DRAFT/UNMERGED.**

## Exact contract and scope

Assume a successful, shortest, **pairwise-distinct**, bidirectional gossip chronology on \(n=22\) vertices (40 calls), both **original** 20-call halves cyclic, with **exactly three prefix components and three reversed-suffix components**. As in the [Stage 26 original-order analysis](../v4.3/N21_ORIGINAL_FOREST_THEOREM.md), label the two tree components and one unicyclic component on each side, form the nine positive intersection sizes \(m_{ij}\), and enforce four off-corner cells \(\ge2\).

**The restriction to \(3\times3\) is not exhaustive at \(n=22\)**. The Stage 9 exponential tree-cover bound still permits both-cyclic \(3\times4\) or \(4\times3\) configurations; these must be enumerated and eliminated (or realized) separately before any full \(n=22\) verdict. The same lower bound excludes \(4\times4\) at \(n=22\) (requires at least 24) and excludes \(\min(r,s)=3,\max(r,s)\ge5\).

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

The final **137 labelled 3×3 necessary-condition survivors** form **42 tree-row/tree-column swap orbits**, with center \(m_{33}\) distribution \(\{1:28,2:41,3:44,4:20,6:4\}\). These are **not** gossip schedules. A passing test establishes the enumerated arithmetic and faithful application of these predicates, **not** the published/earlier human lemmas independently and not actual satisfiability.

Differential regression: \(n=21\) baseline 12,870, Stage 25 remaining 77, Stage 26 remaining **zero** under the cited human lemmas. The special \((4,4,1)\) Stage 26 case sums to 21 and is intentionally **not** reused to eliminate an \(n=22\) matrix.

## Reproduction

From repository root:

~~~bash
python3 -B research/v4.4/n22_3x3_frontier.py
~~~

The matching [Stage 27 CI workflow](../../.github/workflows/research-v44.yml) must execute and succeed on the **latest commit** before labeling the GitHub run CI-VERIFIED. The script was run successfully in a local Python environment; that standalone run explicitly lacked its repository-import differential oracle, which CI will exercise.

## Proof frontier and adversarial obligations

1. **Missing component shapes:** enumerate \(3\times4\) and \(4\times3\) using the correct \(3\times4\) geometry and collector/tree-cover constraints, not the \(3\times3\) baseline.
2. **137 open 3×3 matrices:** build *sound original-chronology local information-profile oracles*; do not treat conservative incidence survival as feasible gossip.
3. **Large tree privacy:** compute certified privacy minima for newly needed 8-person+ corner-group triples; until then use zero (no extrapolation).
4. **Global proof:** seek a structural descent or an unbounded cell/crossing impossibility. Small-\(n\) success and extension/upward closure alone cannot establish the universal half-forest conjecture.
5. **Independent assurance:** audit the hypotheses of Stage 14, Stage 17, Stage 20, Stage 24 and Stage 26 before promoting any theorem. The historical priority status remains unresolved, especially against [Bumby 1981](https://doi.org/10.1137/0602002), [Labahn 1995](https://doi.org/10.1016/0012-365X(94)00031-D) and [Krumme 1996](https://doi.org/10.1016/0012-365X(94)00302-Y).

**Evidence ledger:** \(3\times3\) finite enumerator = locally EXECUTED; latest-head CI = UNVERIFIED pending observed completion; underlying all-\(n\) lemmas = HUMAN ARGUMENTS requiring independent mathematical review; \(3\times4/4\times3\) = UNCHECKED; \(n=22\) theorem = OPEN; full conjecture = OPEN. Preserve PR DRAFT/UNMERGED and manuscript HOLD.
