# Stage 12 — Bumby 1981 universal 3×3 confinement and closed-tree spine

**28 October 2026. MAJOR HISTORICAL SCOPE CORRECTION.** The component-count confinement below is **NOT OUR NEW THEOREM**. It follows directly from R. T. Bumby's refereed 1981 Theorem 3. The fixed-original-midpoint half-forest conjecture still **OPEN**. Priority for the final conjecture not established.

Primary source: Richard T. Bumby, *A Problem with Telephones*, SIAM J. Algebraic Discrete Methods **2** (1981), 13–18, [author-hosted complete six-page scan](https://sites.math.rutgers.edu/~bumby/telephone.pdf), DOI: https://doi.org/10.1137/0602002. Particularly pages **14** (definition of minimal-order splitting and closed components), **16–17** (proof and exact statement of Theorem 3). The PDF was visually checked page by page rather than relying on its abstract. Labahn 1995 and Krumme 1996 are later literature and may strengthen this statement.

## Precise scope mapping

Let S=(e_1,...,e_{2n-4}) be a **successful shortest** two-way telephone-gossip chronology on n>=4 people with pairwise-distinct calls. Let I be its first n−2 actual calls, F the remaining n−2. Bumby's 'pooling system' is the same successful full-information call model. His 'minimal partial order' takes transitive closure of chronological precedence among contacts sharing a participant. A chronological prefix I is necessarily an order ideal; therefore (I,F) is one of Bumby's 'splittings' (page 14).

The prefix graph on n people and n−2 edges with r connected components has aggregate cycle rank r−2. Thus r>=2. If r>=3, the rank r−2 distributed across r nonnegative component cycle ranks forces **at least two component trees**: otherwise the r−1 non-tree components would already contribute cycle rank ≥r−1>r−2. All n vertices participate before and after the cut (Stage 9 straddling theorem), so isolated components are absent, although this is not essential to invoking Bumby's theorem.

Bumby's Theorem 3 (page 17) applies to **any** splitting (I,F) with |I|≥n−2 and at least two tree components, in a successful 2n−4-call scheme. Its classification has THREE cases:

- Case I: exactly two components, both closed trees.
- Case II: exactly three components, two closed trees and one additional component.
- Case III: exactly two components, two non-closed trees.

In particular **NO SUCH SPLITTING HAS FOUR OR MORE COMPONENTS**. Since a half with n−2 edges has at least two trees, this applies to the original chronological midpoint. Therefore r∈{2,3} for **every n**. Bidirectional gossip success is invariant under reversing all calls (the temporal reachability matrix transposes). Apply the same 1981 theorem to the reversed original suffix to get s∈{2,3}.

**Historical corollary, all n.** Both original halves can be cyclic ONLY if r=s=3, with exactly ONE unicyclic component and TWO tree components in each half. Indeed r−2=s−2=1 and two zero-rank tree components force the remaining component to have rank one. The two tree components on both sides are CLOSED in Bumby's sense (Case II).

\[
 \boxed{\text{Any both-cyclic original split must be a 3×3 tree/tree/unicyclic grid, for ALL n.}}
\]

This is far stronger than the repo's earlier independently valid but historically REDUNDANT n=18,19 rectangular thresholds and bounds for 4×4 or higher component grids. **The earlier algebraic necessary-condition theorems are not disproved**: their hypotheses are unrealizable in optimal successful schedules whenever either dimension exceeds three. Their numerical boundary survivors were only **relaxed incidence patterns**, NEVER successful schedules. Any text suggesting 3×4 might first become genuinely possible at n=20 must be read as a bound of that insufficient relaxation, not as a real possibility.

## Additional universal closed-tree first/last-contact spine

Assume hypothetically **both halves cyclic**, so prefix components P_1,P_2 are closed trees, P_3 is unicyclic; suffix components Q_1,Q_2 are (reverse-time) closed trees, Q_3 unicyclic.

**Bumby's proof of Theorem 3, page 16, Case II** establishes more than the case list: whenever the two tree components X,Y in the splitting are closed, **every minimal contact in the future ideal F connects X to Y**. In our prefix case, this means each minimal suffix contact joins P_1 to P_2 (and cannot touch P_3).

In a suffix connected component Q_j, its chronological first call is a minimal element of F: the minimal call-poset order relates only contacts sharing a vertex, and any temporal predecessor chain of calls that ends in Q_j remains inside its own static suffix component. Therefore:

**(C1)** The FIRST original suffix call belonging to each Q_j, including the cyclic Q_3, is an edge connecting P_1 to P_2.

Reverse the entire schedule. In its split after n−2 calls, Q_1,Q_2 are the two closed trees, and all minimum contacts in the new F (old prefix in reverse order) join Q_1 to Q_2. The first reverse contact in each reversed-old-prefix connected component P_i is exactly the LAST original prefix contact in P_i. Therefore:

**(C2)** The LAST original prefix call belonging to each P_i, including cyclic P_3, is an edge connecting Q_1 to Q_2.

These are consequences of the specific **actual original chronology** and the 1981 case-II proof, not a license to reorder events. Together (C1),(C2) give four critical edge incidences in the 2×2 corner P_{1,2} × Q_{1,2}: the last calls in P_1,P_2 lie horizontally across the two suffix-tree columns, and the first suffix calls in Q_1,Q_2 lie vertically across the two prefix-tree rows. Endpoints of horizontal and vertical contacts within a common cell need NOT coincide, so this alone does not construct a literal four-cycle with four participants.

## Immediate necessary singleton exclusions

In a prefix TREE P_i (i=1,2), the endpoints of its last internal contact are its **only possible** complete midpoint collectors. By (C2), those endpoints lie in Q_1 and Q_2. If P_i∩Q_3 were singleton, its unique vertex would have to be a complete prefix collector to export every P_i secret to suffix component Q_3, contradiction. Therefore

\[
 M_{13},M_{23}\ge2.
\]

Reverse the argument using (C1) for suffix TREE components Q_j (j=1,2). Their last **reversed** internal contacts (first original suffix contacts) lie in P_1 and P_2. A singleton in P_3∩Q_j would force an impossible complete reverse collector in P_3. Hence

\[
 M_{31},M_{32}\ge2.
\]

The total number of participants is thus at least the nine mandatory positive cells plus four additional occupants: n>=13. This particular numerical n>=13 is already included in previous analyses; the **universal 3×3 geometry and first/last spine are the useful new reductions**, with explicit attribution to Bumby.

## What remains open

The full original-half-forest conjecture requires ruling out the **closed-tree 3×3** case for arbitrary cell multiplicities. Neither Bumby's Theorem 3, the four-corner first/last spine, nor Stage 9–12 exponential/private-secret local obstructions alone settles it. The fact Bumby could find a favorable balanced splitting by exchanging incomparable calls is **not a proof that the given original balanced splitting is favorable**. Stage 7's W8 example confirms individual midpoint cycle ranks can change under such reordering.

Next high-value proof task: derive full cross-half information compatibility constraints **conditioned on the mandatory first/last call spine**; determine whether this stronger global chronology law gives a universal contradiction or a valid counterexample. Never promote a 'local profile SAT' or a relaxed incidence pattern to a genuine chronology.

**Research gate:** all-n forest OPEN; source-level historical reduction VERIFIED in refereed source; full historical novelty UNRESOLVED; PR DRAFT and UNMERGED.
