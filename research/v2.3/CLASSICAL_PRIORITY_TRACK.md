# Stage 6 parallel track — Classical kernel implication and historical priority

**26 October 2026 | Result: claim-level comparison and an exact decision formulation; complete Labahn-to-half-forest implication remains OPEN.**

## Question being audited

Could the fixed **original chronological midpoint** forest property, verified by computer for n<=16, follow entirely from published classical results about shortest telephone-gossip schemes?

The relevant formal property is

\[
\forall S\text{ successful, } |S|=2n-4,\ E(S)\text{ pairwise distinct}:
\quad \big(\operatorname{cycrank}(S[1:n-2])=0\big)
\ \lor\
 \big(\operatorname{cycrank}(S[n-1:2n-4])=0\big).
\]

A proof of this property for *all* n is not in hand.

## Source-level priority facts (primary bibliography)

- Göbel, Cerdeira and Veldman (1991), *Label-connected graphs and the gossip problem*, Discrete Mathematics 87, 29-40, https://doi.org/10.1016/0012-365X(91)90068-D. Characterizes support graphs and forest decompositions; old results cannot be claimed as ours.
- Roger Labahn (1995), *Kernels of minimum size gossip schemes*, Discrete Mathematics 143, 99-139, https://doi.org/10.1016/0012-365X(94)00031-D. Its abstract **explicitly claims a complete classification of minimum-scheme kernel posets** and enumeration of their linear extensions. Hence the historical implication risk is material, not speculative.
- David W. Krumme (1996), *Reordered gossip schemes*, Discrete Mathematics 156, 113-140, https://doi.org/10.1016/0012-365X(94)00302-Y. An existential *rearrangement* theorem; this is not itself a universal statement about a fixed input chronology, though its full underlying machinery may yield additional consequences.
- West (1982), *A class of solutions to the gossip problem*, Parts I/II, Discrete Mathematics 39/40. NOHO is a restricted family.
- K. Williams (2026), *Greedy gossiping*, Congressus Numerantium 238, 113-121, https://doi.org/10.61091/cn238-05. Its earlier first n-2 prefix and adjacent commutations are NOT new techniques of ours; see [Stage 4 theorem comparison](../v2.1/STAGE4_PRIORITY_AND_PUBLICATION_AUDIT.md).

For actual original PDF page-by-page theorem attribution, retain the [existing v1.8 source-inspection audit](../v1.8/ORIGINAL_PRIMARY_SOURCE_PRIORITY_AUDIT.md) including provenance and the historical exceptional p=4 kernel warning. The complete copyrighted originals are not re-committed. Do not confuse minimum number of gossip *calls* with minimum number of *parallel rounds*: [Labahn–Pietsch on 16-vertex minimum-time graphs](../v2.2/PRIOR_ART_N16_UPDATE.md) addresses a different extremal objective.

## Exact new way to test *implication* using a fully realized classical event poset

The tested [balanced-ideal lemma](balanced_ideal_audit.py) says: for every realizable minimum successful full incident-event poset \(P\), every linear extension is successful and every balanced order ideal \(|I|=n-2\) occurs as a prefix of some linear extension. Therefore:

- A **counterexample** to the original-half forest property among schedules realizing \(P\) exists iff there is an ideal \(I\) of cardinality \(n-2\) with both edge sets \(I,P\setminus I\) cyclic.
- An absence of such an ideal certifies **all** linear extensions of that *one labeled full contact-poset*, not merely one chronological ordering.
- It is **not** enough to check the abstract inner kernel P alone when fringe contact events and their participant endpoints remain unspecified.
- To close historical implication one must realize *every* admissible kernel, every exceptional kernel, all fringe structures/contact labels and their full contact-event orders, then apply the order-ideal predicate. This exercise has **not** been completed.

The W8 example has only six balanced ideals although 51,200 linear extensions; two extensions of the identical full event-poset show differing individual prefix/suffix ranks, but neither is both-cyclic. Thus a kernel cannot determine *which* half is cyclic on its own, yet it is **still possible** that the classical classification implies the weaker at-least-one-forest conclusion.

## What has been checked from Labahn's 1995 Theorem 6.1

The previously committed [independent p-grid admissibility checker](../v1.8/verify_labahn61.py) constructs all 341 possible permutation pairs over p=3..7, checks an independently computed min-to-max reachability property against the published subset-union criterion, and confirms 121 valid pairs, with p-by-p counts 1,3,9,27,81. This is primary-theorem criterion corroboration, **NOT** a generative enumeration of all real successful gossip chronologies. The n=17 balanced ideal experiment supplies a distinct, sound exact decision route once a complete realizable event-poset is actually supplied.

## Unresolved requirements for a genuine priority decision

1. **Complete realization:** reconstruct actual event-to-participant incidence for Labahn's p-grid, exceptional κ=2..4 (including the 4-FFT exception), all fringe trees and allowed temporal precedence. Verify a generator against exhaustive successful n4/n5 schedules and against independent small instances before trusting it.
2. **Full quantitative scope:** prove there is no missed kernel family or fringe attachment, or restrict the historical claim to the model/parameter ranges genuinely covered.
3. **Implication computation/proof:** for all relevant generated realizations, compute the balanced ideal obstruction, using symbolic parameterized pruning for large n; either produce a real counterexample schedule or a complete general proof.
4. **Historical priority:** compare any final argument at theorem/lemma mechanism level to Labahn/Krumme and intervening literature, not just by phrase search or absence of the same paper title.

**Priority verdict:** Existing audited sources did not explicitly state the fixed-original-half theorem; complete *implicit* derivability remains **UNRESOLVED**. This is an epistemic and mathematical gap, not an assertion that the result is already known or that it is definitely novel.

**Novelty-safe contribution text:** "A computer-assisted finite classification through n=16 for a particular original-order midpoint invariant, supplemented by a verified 3x4 incidence obstruction through n=17 and an order-ideal formulation. Its derivability from classical complete kernel classifications and the unbounded case remain open."
