# Stage 27 — Conservative n=22 original chronological 3×3 frontier: 113 labelled profiles / 33 orbits

**28 October 2026. Exact census of original fixed-half necessary-component incidence sizes.** This note does NOT claim every survivor extends to a successful 40-contact gossip chronology or that the n22 half-forest conjecture is proved. The all-n conjecture is OPEN from n≥22. PR #1 stays DRAFT/UNMERGED; no reordering of any original contact.

## Proven baseline: n21 is already complete

[Stage26](../v4.3/N21_ORIGINAL_FOREST_THEOREM.md) gives a source-grounded human proof that every shortest successful distinct-call gossip schedule on n=21 has a forest in an original first or last 19-contact half. [Independent Stage26 CI 40745930756](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40745930756) succeeded in the exact 12,870-incidence-matrix closure, the original six-person three-leaf-star enumeration, n≤7 chronological tree privacy histograms and earlier supporting lemmas. This is not a formal proof assistant or priority certificate.

## The n22 enumeration and precise assumptions

Assume a hypothetical successful shortest **40-call** distinct-pair schedule on n=22 whose **original** first and last 20-contact halves are cyclic. By Bumby's historical Theorem 3 and proof, both prefix and fully reversed suffix component graphs have exactly two closed trees and one unicyclic component, and their positive 3×3 intersection matrix has all four off-corners at least two:

\[
M_0=\begin{pmatrix}1&1&2\\1&1&2\\2&2&1\end{pmatrix}.
\]

There are exactly \(\binom{17}{8}=24,310\) labelled positive matrices formed by distributing nine extra occupants across its nine fixed labelled cells.

Apply the n21 Stage25 **ALL-n necessary** filters, with exact small chronological-tree private-recipient minima only where previously exhaustively certified; any unenumerated tree class contributes a **ZERO** lower bound. The fixed original-cut gates include global cyclic-component size≥9, the Stage18 n≥43 consequence of an off-corner (2,2) pair, Stage20 helper-tolerant four-arm center≥9 if four full collectors lie outside center, Stage23/24 three-full-outside collector restriction with smaller exterior sizes, and Stage20 two-full-center root-cut if center size two.

| Gate | Number of labelled n22 candidate matrices remaining |
|---|---:|
| Initial all-positive 3×3 matrices (four off-corners ≥2) | 24,310 |
| Both unicyclic local components have ≥9 vertices | 3,396 |
| Neither off-corner pair remains (2,2) | 2,598 |
| Small-tree private-recipient lower bounds rule out 4 complete outsiders at small center | 1,389 |
| Dual three-full-outside-root obstruction at center ≤5 | 1,061 |
| Singleton center / binary center root-cut gates | **761** |

The original Stage25 all-n code, applied to n22 rather than just n20/21, yields exactly **761 labelled profiles / 198 row-column swap orbits**.

Next apply the all-n **Stage26 new local lemmas** to these 761:

- singleton center plus an off-corner size-two cell and companion cell≤6: 72 exclusions;
- two-person center with zero full collector on both local components: 40;
- three-person tree double-cover contradiction against zero-center-collector local component: 84 for each temporal orientation, 168 total;
- doubly covered center with two outside complete spanning-tree roots: 264;
- exact Stage22 globally incompatible (2,4,3) local three-star pattern with independently verified adjacent tree privacy minima: 80.

In total **624 exclusions**, leaving **137 labelled matrices / 42 orbits**. These are not full chronology certificates.

## New application of the n21 final (4,4,1) human lemma at arbitrary n

The [Stage26 final-case Lemma26.6](../v4.3/N21_ORIGINAL_FOREST_THEOREM.md) is an **ALL-n conditional local theorem**, not merely a fixed matrix computation. If either original prefix or fully reversed suffix unicyclic component has exactly two outside-center cell groups of size 4 each, a **singleton shared center**, and at least ONE terminal complete collector in each exterior group, the globally successful hypothetical both-cyclic chronology is impossible.

The reason is independent of the other corner sizes. The singleton center is a complete collector. Four terminal complete collectors would split into four causally sealed arms with a singly-rooted four-person exterior group, violating the Stage24 three-star occupancy lower bound |B|≥7. Thus exactly three complete collectors (one in each outside cell, one in center). The final unicyclic cycle edge joins the two outside collectors; the penultimate spanning-tree contact joins the center collector and one of those outsiders. Deleting these last two contacts gives two tree subproblems with disjoint complete recipient groups: each side's full root, and the untouched outside-cell recipients from each group. Exactly eight recipients spread across two sides, saturating the Stage11 3-group-per-side lower bound 4+4. Stage15 helper-robust equality rigidity makes the three untouched recipients in one exterior group PRIVATE, yielding three reverse-target supports {complete outsider,z_i}. These are incompatible with the adjacent opposite ORIGINAL chronological tree's last contact outside that cell, by the Stage20 all-n tree-versus-three-star lemma. Therefore no valid full original schedule exists under the local 4,4,1 collector hypotheses.

Adjacent original chronological **TREE** private-recipient minima for groups (1,1,4), (1,2,4), (2,1,4), etc., exactly enumerated by the n≤7 independent Stage21 verifier, supply the needed at-least-one collector on either 4-person cell for the relevant n22 matrices. For an unenumerated adjacency the checker uses minimum ZERO, therefore does not exclude.

This removes exactly **24** more of the 137 Stage26-level n22 profiles, leaving

\[
\boxed{113\text{ labelled NECESSARY n22 matrices in }33\text{ row/column orbits}.}
\]

The remaining center sizes are: **4** with center 1, **41** with center 2, **44** with center 3, **20** with center 4, and **4** with center 6.

A single representative of the remaining center-singleton orbit is

\[
\begin{pmatrix}1&1&3\\1&2&5\\3&5&1\end{pmatrix}.
\]

A representative with center six is

\[
\begin{pmatrix}1&1&2\\1&1&4\\2&4&6\end{pmatrix}.
\]

Both represent merely survivors of necessary restrictions; **neither is an actual successful 40-contact chronology**.

## Computational evidence and blockers

[Independent n22 frontier checker](n22_frontier.py) generates ALL 24,310 labelled positive matrices using the separately verified Stage25 enumerator, exact Stage26 all-n rejection predicates, and the newly generalized local 4,4,1 collector condition. It checks n21 remains zero, independently cross-checks the first two n22 stages with aggregated p/q/d stars-and-bars counts, validates reason counts and orbit sizes, and prints representative survivors. [CI workflow](../../.github/workflows/research-v44.yml) independently reruns the original six-person three-star chronological checker and seven-person tree privacy histograms.

**n22 original half-forest remains OPEN.** Closing 113 labelled incidence candidates requires stronger chronological source/target support incompatibilities and explicit checks of the remaining full-information components, or a genuine globally replayable successful both-cyclic counterexample. Neither is claimed. Human all-n local proofs and finite CI do NOT count as independent mathematical peer review, and no Lean/Coq certificate or historical novelty priority claim is made.

**PR #1: DRAFT, OPEN, UNMERGED. Submission HOLD.**
