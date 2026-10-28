# Universal chronological tree-cover theorem and exponential crossing/packing transfer

**28 October 2026. All quantifiers unrestricted in n, number of designated recipient groups, number of helpers, chronological edge order and common-center width. Human proofs below do NOT establish the original universal forest or exact 2n−3 temporal-clique spanner conjecture.**

## Theorem U.9 — general helper-robust disjoint-group cover lower bound

Let T be an undirected tree on N≥1 vertices, with exactly N−1 pairwise-distinct **bidirectional contacts**, one along each tree edge, in an arbitrary but FIXED chronological order. Each original person starts with an independent secret.

Let \(G_1,\ldots,G_s\) be **s≥1 pairwise disjoint, nonempty** designated recipient groups, possibly leaving any number of vertices unassigned as helpers. Assume each G_i terminally **collectively knows every original T secret**. Then

\[
\boxed{\sum_{i=1}^s |G_i|\ge 2^{s-1}.}
\]

This is a self-contained all-n proof of the helper-robust cover lemma previously imported from Stage11. No event reordering, time commutation, or assumption that an arbitrary chronological tree has a terminal full collector.

### Complete induction on (s,N)

For s=1 at least one designated recipient is required, so the bound is immediate. If T is a single vertex, only one pairwise disjoint nonempty group can exist, hence s≥2 is impossible.

For s≥2 and N≥2, delete T's ACTUAL final chronological contact xy. The N−2 preceding contacts separate into two independent original-order chronological subtrees A containing x and B containing y. Since no information from one side can reach the other before xy, after xy **x is the ONLY participant of A that can receive secrets originating in B**, and **y is the ONLY participant of B that can receive secrets originating in A**.

Consider original secrets originating in A. For ANY designated group G_i NOT containing the opposite final-edge endpoint y, its A-part \(G_i\cap A\) must already collectively cover EVERY original A secret: no other B participant can ever learn A secrets. Because groups are pairwise disjoint, at most ONE group contains y. Thus at least s−1 pairwise disjoint nonempty groups among \(G_i\cap A\) collectively cover all A-original secrets after the A-side chronological contacts. By induction on s (s−1<s), at least \(2^{s-2}\) distinct designated recipients must lie in A.

Symmetrically, at most one group contains x, so B has at least s−1 disjoint complete-cover recipient groups and therefore at least \(2^{s-2}\) designated recipients. Their side recipient sets are disjoint, yielding \(\sum|G_i|\ge2^{s-2}+2^{s-2}=2^{s-1}\). QED.

**Sharp for s=1,2,3:** s1 one singleton; s2 one call between two singleton collectors; s3 chronology (0,2),(1,3),(0,1) on four people, with groups {0},{1},{2,3}. Both 0,1 know all four secrets and {2,3} collectively covers. No sharpness assertion for general s is needed or made.

## Lemma U.10 — chronological rooted complete-collector / disjoint-support dichotomy

Let T be an edge-once chronological TREE with a **terminal complete root r∉C**, and let a designated C collectively cover every original T secret at least once (in particular any doubly or q-fold complete recipient group satisfies this).

**Exactly one of two cases holds:**

1. C contains a complete collector y. Necessarily y is T's actual final call endpoint opposite r; in this case EVERY original source's exact C-support contains y, so no two source supports are disjoint.
2. C contains NO complete collector. Then T's final call is r–y with y∉C. Removing it splits C into two NONEMPTY subsets C_A,C_B which separately support original secrets from two disjoint side trees, and any original source in A has C-support disjoint from any original source in B. In particular the family of exact C-supports contains **two disjoint nonempty members**.

**Proof.** A chronological tree with any terminally complete root r has precisely TWO complete people, the endpoints of its ACTUAL last contact. If the other endpoint y belongs to C, case1 holds. Otherwise neither last-call endpoint lies in C, no designated C recipient takes part in that call, and original side A secrets can be known only by C_A while B secrets only by C_B. Collective completeness of C forces C_A and C_B nonempty and each to cover its side's secrets. Their exact support families are disjoint. QED.

This is an **information-support Helly alternative specialized to chronological trees**, not a general statement about arbitrary hypergraphs.

## Theorem U.11 — universal exponential packing-to-crossing inequality

Let T,U be two edge-once original-order chronological trees with common designated cell X. Suppose their actual last contacts join two complete collectors **outside X**, and the exact all-pairs source-support crossing condition holds:
\[
\forall a\in V(T), b\in V(U),\quad S_a^T\cap S_b^U\ne\varnothing.
\]

Suppose T has **k≥1 PAIRWISE DISJOINT nonempty exact X-source supports**
\[
S_{a_1}^T,\ldots,S_{a_k}^T,
\qquad S_{a_i}^T\cap S_{a_j}^T=\varnothing\ \ (i\ne j).
\]
Then
\[
\boxed{
\sum_{j=1}^{k}|S_{a_j}^T|\ \ge\ 2^{k+1}-2,
\qquad
|X|\ge2^{k+1}-2.}
\]

No fixed limit on k, X, N, number of helpers, or source order is imposed.

### Human proof

Delete U's ACTUAL last chronological tree contact between its two complete outside collectors \(r_1,r_2\), leaving independent rooted chronological trees U1,U2 and an X partition \(X=X_1\uplus X_2\). For each i∈{1,2}, each j∈{1,...,k}, the set \(H_{ij}=S_{a_j}^T\cap X_i\) is a **collectively complete recipient group** for EVERY original U_i secret. Indeed all exact U_i source X supports lie in X_i and must intersect \(S_{a_j}^T\) by all-pairs crossing. In particular H_ij is nonempty.

For fixed i the k groups H_i1,...,H_ik are pairwise disjoint (since the original S groups are), and the single outside root singleton {r_i} is a further disjoint complete group. Apply the independently proved Theorem U.9 with s=k+1 on the genuine original-order side tree U_i:
\[
1+\sum_{j=1}^{k}|H_{ij}|\ge2^k,
\]
hence \(\sum_j |H_{ij}|\ge2^k−1\). Sum separately for i=1,2, recognizing that the X_i partition X and all S_j are subsets of X. This yields
\[
\sum_j |S_{a_j}^T|\ge2(2^k−1)=2^{k+1}−2.
\]
The supports are disjoint, so their sum is ≤|X|. QED.

### Consequences for the unresolved all-width problem

- k=2: |X|≥6, and more importantly **EVERY pair of disjoint exact source supports has combined size≥6**, the ingredient of the [stronger universal center≥14 theorem](CROSSED_TREE_COVER_TRANSFER.md).
- k=3: |X|≥14.
- k=4: |X|≥30.
- k=5: |X|≥62.
- For any crossed T/U, the exact support-packing number \(\nu(T)\) (maximum disjoint subfamily of T's nonempty source supports) obeys
  \[
  \nu(T)\le \left\lfloor\log_2(|X|+2)\right\rfloor-1,
  \]
  and symmetrically for U.

By Lemma U.10, if ONE of T's two rooted last-edge sides has no complete C collector, it contributes TWO disjoint source supports; the other side contributes one, hence \(\nu(T)\ge3\). If BOTH rooted sides have no complete C collector, \(\nu(T)\ge4\), so **|X|≥30** follows for ALL n under the original crossed-tree model.

**Not a global resolution:** having a full recipient inside EACH rooted side is consistent with many actual edge-once trees; in that case \(\nu(T)=2\) and the packing transfer does not diverge. The theorem improves the information-flow obstruction but does **not** prove that all widths are impossible or force exterior collectors in arbitrary original 3×3 both-cyclic structures.

## Reproducibility and claim gates

[Independent checker](general_group_cover_audit.py) replays genuine original-order tree histories, checks the q=3 exact construction, exhausts all group assignments on very small trees and tests disjoint hitting sets against original two-root chronological trees. Any finite script only challenges the bounded cases; the induction and support-cover proof carry ALL n and arbitrary k.

**States:** Theorems U.9/U.11 and Lemma U.10 = complete HUMAN_PROOFS, independent mathematical referee needed; FORMAL_CHECKER not run; historical novelty unchecked; universal original-half forest and 2n−3 spanner OPEN. PR #1 DRAFT/UNMERGED and manuscript submission HOLD.
