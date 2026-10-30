> **28 October 2026 dominant universal geometry correction:** Bumby's 1981 Theorem 3 already forces r,s≤3 at every original balanced midpoint of a shortest successful gossip schedule. Thus any hypothetical both-cyclic schedule has exactly r=s=3 for *all n*, and the only live universal proof frontier is a 3×3 positive incidence with two closed trees and one unicyclic component on each side. Its exact first/last contact spine and the dual one-event forest reordering are proved in [Stage 12 audit](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md). Older rectangular n-threshold claims remain valid but are strictly weaker and historically redundant. **Universal original-chronology forest: OPEN.**

> **27 October 2026 Stage 11 continuation:** The exact recipient-count bound now holds even with unassigned helper vertices; its equality cases force exactly two singleton groups and a private secret for every assigned recipient. The [symmetric k-arm crossing theorem](../v2.8/STEINER_COVER_RIGIDITY.md) strengthens four-arm t≥60 to **t≥63**, and the [binary temporal crossing trichotomy](../v2.8/TWO_VERTEX_CROSSING.md) constrains all size-1/2 shared arm subcells. These are conditional component obstructions. The unrestricted chronological half-forest conjecture **remains OPEN**; a mandatory crossed-arm decomposition or sound reduction still has not been proved.

> **27 October 2026 Stage 10 continuation:** New conditional all-n [four-arm crossing theorem](../v2.7/FOUR_ARM_CROSSING_THEOREM.md) forces a shared cell to contain at least **60** participants for rigid 4-by-4 rooted-arm interfaces. This eliminates the marked (2,2,t) tree/tree and four-collector cyclic subfamilies with t≤59. The central universal step—showing *every* both-cyclic schedule contains an obstruction or descends to one—is **still missing**. Earlier status below is retained as a historical checkpoint.

# Stage 9 — All-n full-proof campaign, adversarial outcome ledger

**27 October 2026. Status: universal chronological half-forest conjecture OPEN. Do not promote this campaign into a claimed full proof.** PR #1 DRAFT/UNMERGED, publication HOLD, classical originality UNRESOLVED.

## Exact statement under attack

Given a shortest \(2n-4\)-contact bidirectional distinct-contact telephone gossip chronology, for every n>=4, one of the two ORIGINAL contiguous chronological blocks of n-2 calls induces a static forest. Every contact and position stays unchanged. Reordering, graph-only forest decomposition, a relaxed information CSP, or finite verification alone would not establish this statement.

## Attacks and established intermediate results

1. **Exact exponential tree-cover theorem.** A connected m-vertex tree using its m-1 unique contacts and partitioned into s nonempty recipient groups, each collectively covering all m secrets at the end, requires \(m\ge2^{s-1}\). Last-contact induction proves it for all s and a recursive tree construction attains equality for all s. See [the complete proof](EXPONENTIAL_TREE_COVER.md). An independent exhaustive C++ verifier checked 12,259,656 ordered labelled tree chronologies on 4–7 vertices for the four-group obstruction; a separate construction verifier checked s=1..8.

2. **Global all-n necessary information-cover inequality.** Any hypothetical both-cyclic optimum on an r×s component-intersection grid must obey

   \[
   n\ge\max\{rs+2(r+s)-8,\;2rs-4\min(r,s)+4,\;
     2^s+(r-2)s,\;2^r+(s-2)r\}.
   \]

   The exponential terms use only elementary component incidence, cellwise information coverage and time reversal—not the more delicate single-source entry lemma. In particular r,s are O(log n). This is NOT a contradiction for arbitrarily large n.

3. **All-n midpoint straddling.** Every participant makes at least one call in each original half: no vertex can know all n secrets after n-2 calls, while a secret untouched by the prefix cannot reach all n vertices through only n-2 suffix calls. Every degree-two participant therefore has exactly one call in each half. Any successful new-participant insertion consisting of two calls (at ANY chronological slots) must straddle the new midpoint and preserves BOTH static half-cycle ranks. Exact proof and independent exhaustive all-valid-insertion test in [straddling theorem](STRADDLING_AND_FRINGE_INVARIANCE.md).

4. **A real induction obstacle.** An existing degree-two participant is NOT necessarily deletable to a successful optimal shorter scheme, even if its contacts are first and last. The prior Stage 8 n5 counterexample and 360/1800 failed marked deletions remain genuine. Thus upward invariance does NOT imply a valid downward induction.

5. **Adversarial 3×3 n18 all-2-cell test.** [Independent exact small-component profile program](probe_n18_uniform_two.cpp) enumerated 360,360 ordered five-contact six-participant component histories, and 3,603,600 six-contact histories. Among them 4,992 and 369,312 respectively satisfy connectedness and three pairwise-group coverage. There are 13 vs 48 unique exact B profile types and 15 vs 69 exact D types. Across all 48×13×13=8,112 row-profile triples, NOT ONE is compatible with an exact suffix-column profile under the relaxed B/D necessary condition. By row/column permutation symmetry this excludes all marked cycle positions for the single n18 matrix M with every one of its nine cells equal to 2. This is a **single matrix family only**, not all n18.

6. **Historical comparison sharpened.** Bumby's 1981 *A Problem with Telephones* establishes the classical 2n-4 call bound and the four-cycle structure, and discusses minimal-event-order splittings and closed tree components. Labahn (1995) reports a complete classification of minimum gossip scheme kernels, and Krumme (1996) proves an existence-of-*reordering* theorem. Their existence statements are not on their own the fixed-midpoint all-chronology theorem. However no complete full-text kernel implication audit has been done: the theorem might be an unstated corollary of a stronger classical result. Novelty is NOT established. Primary sources: Bumby https://sites.math.rutgers.edu/~bumby/telephone.pdf ; Labahn https://doi.org/10.1016/0012-365X(94)00031-D ; Krumme https://doi.org/10.1016/0012-365X(94)00302-Y.

## Reduced but unresolved universal proof obligation

The n≤17 finite certificate in [Stage 6](../v2.3/N17_CLOSURE_CERTIFICATE.md) and the new exponential lower bound imply that for n=18 or n=19 any hypothetical both-cyclic chronology must have a **3×3 component intersection**. The targeted all-two-cells n18 instance is impossible, but many other 3×3 matrices remain unchecked.

For arbitrary n, three fundamentally different routes remain:

- **Universal cross-half profile lemma:** Prove no arrangement of prefix/suffix temporal trees and the requisite cyclic components can satisfy the fixed-intersection B/D information compatibility. Local tree-cover bounds alone cannot discharge this, because n can grow with fixed 3×3.
- **Sound irreducible-kernel descent:** Establish a reduction of every hypothetical both-cyclic minimum scheme to a *smaller successful* both-cyclic scheme, or prove all irreducible kernel posets forbid balanced ideals with cycles in both sides. Deleting a degree-two participant without checking gossip is **UNSOUND**.
- **Construct a genuine counterexample:** Any relaxed-SAT profile must be lifted into a pairwise-distinct, temporally correct, fully successful complete schedule with both original half cycle ranks >=1 and all secret-state transitions independently replayed.

**Evidence decision:** exact tree-cover theorem and generalized straddling lemma PROVED by written mathematical arguments, CI independently corroborated; universal half-forest conjecture STILL OPEN, no verified counterexample, historical originality UNRESOLVED. Keep the research PR draft and do not merge as a universal proof.
