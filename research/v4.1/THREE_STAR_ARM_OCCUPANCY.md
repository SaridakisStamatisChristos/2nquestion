# Stage 24 — Three-star occupancy barrier for a causally sealed arm interface

**28 October 2026. New conditional ALL-n necessary inequality.** Original chronological half-forest conjecture remains OPEN beyond the finite cases, including n>=21. Does not rearrange any call or infer global realizability from an incidence matrix. This generalizes Stage 23's B=4/5 pigeonhole/four-star reasoning.

## Precise conditional model

Consider one connected chronological local component U (original prefix, or fully reversed original suffix) that admits a **causally sealed k-arm decomposition**, k>=3, with exactly one COMPLETE collector/root in each rooted tree arm; all other vertices of an arm never receive secrets from another arm in the actual local chronology. Assume all non-arm-internal contacts join only roots, after their respective incident arms are sealed (but unrelated calls may interleave). Let B be a cell shared with a connected chronological TREE T in the opposite half, such that:

1. Among the k full U roots, **exactly one** is a vertex y of B. Every other B person is a nonroot belonging to one of U's k arms.
2. **Every original U-secret has at least TWO distinct terminal U carriers inside B.**
3. The global ORIGINAL (fixed-midpoint) telephone gossip is successful, so original U-source and opposite-tree T-target supports intersect in B for every source-target pair, with roles swapped under complete time reversal.
4. The original final chronological contact of T has endpoints **outside B**. Thus removing it splits T into independent chronological tree histories, and no B person changes knowledge on that last call.

### Theorem 24.1 — exterior recipient cell occupancy

Under these hypotheses,

\[
\boxed{|B|\ge2k-1.}
\]

For the four complete-collector arms of a unicyclic component (k=4), a singly-rooted cell B must contain at least **SEVEN** people, not merely five.

**Proof.** Let r_i be the complete U root of arm i. Its own original secret rho_i is carried in B by the unique full B root y. Since rho_i must have at least two B carriers, some additional B **nonroot** in the SAME arm i must carry it: a nonroot of any other arm cannot learn a secret originating in arm i. Thus every arm contains at least one B nonroot.

Write c_i>=1 for the number of B nonroots in arm i, so |B|=1+sum_i c_i. Call an arm a singleton-arm when c_i=1, and denote its unique B nonroot by z_i. For its root's secret rho_i, the B support is EXACTLY the two-person set {y,z_i}, because no other B nonroot can know rho_i and there is exactly one B complete root.

**No THREE different arms can be singleton-arms.** Otherwise there are three distinct original U root secrets with exact terminal B supports {y,z_1}, {y,z_2}, {y,z_3}. Consider the opposite chronological TREE T, deleting its last edge whose endpoints are outside B. This divides its previous calls into independent subtrees V,W. Put y in V. For EVERY secret of W, y cannot know that opposite-tree secret at the end, because it participates in no last-edge crossing and all earlier contacts stay within V. Exact original source-target compatibility with EACH of the three two-person supports forces z_1,z_2,z_3 each to know EVERY W-secret in the relevant orientation. Those three distinct z_i must lie in W and would each be complete collectors of the chronological W-tree. But an edge-once chronological tree has at most TWO complete terminal collectors. Contradiction.

Hence at most two arms have c_i=1, and the remaining at least k−2 arms have c_i>=2. Therefore

\[
\sum_i c_i \ge 2(k-2)+2=2k-2,
\quad\text{so }|B|\ge2k-1.
\]

For k=3 this gives |B|>=5; for k=4 gives |B|>=7. This is a **necessary** bound only, not a construction proving equality globally attainable. QED.

### Sharp occupancy of the abstract counting step

For k>=3, the occupancy vector (1,1,2,...,2) (two singleton-arms, k−2 double-occupancy arms) has exactly 2k−2 B nonroots, total |B|=2k−1. It evades only the *three-singleton-star* counting contradiction. It does NOT prove that the original contact chronology and opposite-tree crossing admit such an occupancy configuration.

The independent checker [check_three_star_occupancy.py](check_three_star_occupancy.py) enumerates every positive k-part composition for k=3,...,8 and total B nonroot counts through 2k−2, verifies that all smaller totals force at least three singleton arms, and independently checks each exact boundary construction. The earlier seven-person four-star tree regression (Stage 23) and original six-person three-star tree regression (Stage 20) are the independent chronological support checks. The all-n theorem is the preceding proof, not an inference from testing up to eight arms.

## Implications and boundaries

- Stage 23's mixed n20 **A2+B1+X1** fourth-root possibility, with B of size four or five, is ruled out by this single conditional theorem. The proof stays valid if B=6, improving the n20-specific four-root lemma's occupancy threshold from 5 to 6 **without requiring a new n=20 orbit calculation**.
- The theorem applies only when exactly ONE full U arm root belongs to B. If B has two complete arm roots, the argument that a root's B support has a single full hub y is not valid; use Stage20's four-outside-root obstruction instead where appropriate.
- It requires TWO carriers per secret in B (Stage 17 supplies this for genuine off-corner cells in a hypothetical both-cyclic split), and the adjacent opposite tree's original last contact must be outside B (Bumby's 1981 spine).
- It is false as an unconditional bound on a generic tree/cycle or on an arbitrary cell without causal sealing, original-midpoint crossing, and the unique B root. No claim of novel priority or all-n fixed-midpoint resolution is made.

**Research frontier:** use stronger occupancy barriers and exact original-tree local privacy constraints when adjacent off-corner cells grow to size six or seven, and further constrain the remaining unrestricted n>=21 possibilities. PR #1 remains DRAFT, OPEN, UNMERGED, publication HOLD.
