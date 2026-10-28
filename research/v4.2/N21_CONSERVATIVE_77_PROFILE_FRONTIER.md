# Stage 25 — Original fixed-chronology n=21 necessary-incidence frontier: 77 labelled profiles / 22 orbits

**28 October 2026. Conditional all-n logic plus independent complete finite enumeration of labelled positive 3×3 incidence vectors at n=21. The original chronological half-forest conjecture remains OPEN at n=21 and arbitrarily large n. These are NOT 77 feasible gossip schedules. No original contact is reordered.**

## Current historical and research status

The head of the draft PR now contains all-n structural consequences of Richard Bumby 1981 Theorem 3 and the original fixed-chronology first/last-contact spine, together with human proofs of foresthood for n=18,19,20 (Stages 18,20,23; **n20 Stage23 CI 40704093933 SUCCESS**). Stage 24 gives the original-order **three-star occupancy theorem**: in a k-arm causally sealed component with exactly one complete root in a B cell, the exact original-order crossing and twice-carried original arm secrets force |B|>=2k-1. Stage 24's theorem is CONDITIONAL on those premises and is not itself a universal solution.

This stage combines those proven gates with the independently stated [central-private root-cut lemma](../v3.7/CENTER_PRIVATE_ROOT_CUT_TEN_OUTSIDERS.md) and the precise central two-person support criterion from Stage 11. The result is an executable **candidate matrix shortlist**, not a proof for n21.

## Exact n21 model

For a successful shortest **distinct-call** 38-contact schedule on n=21 whose ORIGINAL first and last 19 calls were BOTH cyclic, Bumby forces prefix P1,P2 closed trees and P3 unicyclic, reversed original suffix Q1,Q2 closed trees and Q3 unicyclic. Define m_ij=|Pi∩Qj|. All nine entries are positive and all four off-corner entries m13,m23,m31,m32 are >=2. Parameterize the 12,870 positive labelled incidence vectors by the baseline

\[
M_0=\begin{pmatrix}1&1&2\\1&1&2\\2&2&1\end{pmatrix},\qquad
\sum m_{ij}=13+8=21.
\]

The following exact necessary gates are applied in original chronological orientation, with time reversal for symmetrical requirements. No published or repository theorem is treated as universally applicable beyond its hypotheses.

### Gate A: structural component sizes and pair saturation

[Stage16 dual local double-cover](../v3.3/DUAL_DOUBLE_COVER_AND_LOCAL_MINIMUM.md), strengthened by the later independent Stage18 global eight-person exclusion, forces **both** cyclic components to have >=9 vertices. In extra variables p=m13+m23-4, q=m31+m32-4, d=m33-1, these are p+d>=4 and q+d>=4. Count: **12,870 → 1,200**.

[Stage18 six-group 35-person obstruction](../v3.5/SIX_GROUP_35_PERSON_OBSTRUCTION.md) proves any off-corner (2,2) pair in a genuine both-cyclic original schedule requires n>=43, hence n=21 requires **p>=1 and q>=1**. Count: **1,200 → 850**.

The independent stars-and-bars count reparameterizes the 8 extra occupants into p,q,d and four free corner extras. Each triple contributes (p+1)(q+1)·C(8−p−q−d+3,3) labelled matrices, and independently produces counts 1,200 and 850 for these first two gates.

### Gate B: exact original-tree private recipient minima, without extrapolation

For a chronological TREE T with three collectively complete groups (corner1,corner2,off-corner), whose last actual call joins the corner groups, a recipient private within the off-corner group becomes a complete collector of the opposing unicyclic component under original source-target crossing.

Use **ONLY** exact privacy minima for the 16 six-/seven-person-or-smaller group triples independently exhausted in [Stage21](../v3.8/N20_PRIVACY_FRONTIER.md), [Stage19](../v3.6/SMALL_TREE_PRIVACY_N19_FRONTIER.md). For an unenumerated triple, use **ZERO** as a deliberately weak conservative bound, not a guessed estimate. Thus:
- complete reverse-Q3 outsiders forced in the two P1/P2 off-corner row cells: r1=f(m11,m12,m13), r2=f(m21,m22,m23);
- complete original P3 outsiders forced in the two Q1/Q2 off-corner column cells: c1=f(m11,m21,m31), c2=f(m12,m22,m32).

A unicyclic component can have **at most FOUR** full collectors, and if FOUR such collectors are OUTSIDE its common center X=P3∩Q3, the helper-tolerant one-sided causal four-arm theorem forces |X|>=9. None of the n21 structural survivors has |X|>=9, so reject if r1+r2>=4 or c1+c2>=4.

Count: **850 → 321**. The same implementation on n20 reproduces the previously independent exact Stage21 counts 221→52, providing a nontrivial regression.

### Gate C: Stage23 + Stage24 conditional three-outside-collector closure

On either U=P3 or reverse Q3, suppose the two outside-center cells have sizes A<=3 and B<=6, and the corresponding **verified finite** private lower bounds force at least TWO full U collectors in A and at least ONE in B. Also |X|<=5.

Then U CANNOT have four complete collectors:
- four OUTSIDE X force |X|>=9 by the helper-tolerant causal four-arm theorem, contradiction;
- the only alternative distribution is exactly 2A complete, 1B complete and 1 X complete. The four-arm causal decomposition, B's twice-covered secrets, and Stage24's one-B-root occupancy theorem demand **B>=7**, contradicting B<=6.

Thus U has exactly THREE complete collectors and all three are outside X. This is a conservative B<=6 extension of the Stage23 B<=5 conditional argument, with its extra B=6 justification explicitly supplied by Stage24.

If **BOTH** unicyclic original/reversed components satisfy this collector-forcing condition, both have exactly three complete outsiders; by [Stage23 Lemma23.2](../v4.0/N20_ORIGINAL_FOREST_THEOREM.md), their unchanged center supports require |X|>=6. But n21 candidates from Gate B have |X|<=5. Therefore reject both-qualified matrices.

Count: **321 → 137**.

### Gate D: center of size one or two, original source/target support

A central singleton X={x} can carry all P3-to-Q3 source/target pairs only if x is a **complete original P3 collector** AND a **complete reverse-Q3 collector**. Hence if *either* unicyclic component qualifies under Gate C, that component would have its three forced complete outsiders PLUS x, contradicting Gate C's prohibition of a fourth complete collector. Reject.

A central two-person set X={x,y} obeys the exact two-point temporal crossing trichotomy: if one unicyclic side has **NO** complete central collector, both x,y must be COMPLETE collectors of the **other** unicyclic side. Gate C supplies this complete-central absence on the qualified side. Then the new [root-cut theorem](../v3.7/CENTER_PRIVATE_ROOT_CUT_TEN_OUTSIDERS.md) applies to the opposite unicyclic component: two full central collectors at its penultimate local tree call, coupled to universal off-corner double-carrier supports and the final cycle-closing contact outside X, force the TWO opposite outside-center cell sizes to **sum to at least 10**. Reject if they sum to <10.

The root-cut proof additionally needs that two complete center collectors occur **before** the final on-cycle call; because the final local call's endpoints are outside X, this follows automatically. Moreover the tree's penultimate complete centers are precisely the two last-tree endpoints. The root-cut proof does **not** require those full center collectors to have been generated by private singleton supports: its 10-person conclusion uses only their complete collector property and the universal two-fold exterior support. This broader quantifier is important to this Stage25 application.

Count: **137 → 77**, with exactly 12 singleton-center and 48 two-person-center rejections.

## Verified finite frontier, independently countable

| Gate | Labelled positive 3×3 necessary matrices | Remaining symmetry orbits |
|---|---:|---:|
| Raw all-positive n21 with four off-corners >=2 | 12,870 | not needed |
| Two cyclic components >=9 | 1,200 | not needed |
| Neither off-corner pair (2,2) | 850 | not needed |
| Exact known n<=7 tree-privacy minima | 321 | 86 |
| Both sides three-outside-collector forcing impossible | 137 | 40 |
| Central singleton/binary root-cut conditions | **77** | **22** |

The final 77 labelled matrices have central sizes: 9 with |X|=1, 4 with |X|=2, 48 with |X|=3 and 16 with |X|=4. A row/column symmetry orbit means only independent permutations of the two prefix TREE component indices and two reversed suffix TREE component indices, never exchanging actual chronological call order. The canonically minimized orbit size need not be 4 when a profile has a nontrivial stabilizer.

[Independent executable n20/n21 enumerator](n21_staged_frontier.py) produces this ledger from all nine-cell weak compositions, verifies the first two counts via a **separate p/q/d stars-and-bars** enumeration, checks Stage21's exactly known n20 221→52 count, and independently applies the same Stage23 conditional all-n logic to close n20 to zero without relabelling any local contact order. It checks that **UNKNOWN** tree-privacy group types are assigned a zero lower bound. This is a substantive fail-open-for-survivors, fail-closed-for-false-exclusion design, not a claim of exhaustive chronology enumeration.

## Remaining obligations / adversarial findings

The new final 22 n21 incidence orbits remain **necessary-condition survivors**, not valid 38-call schedules or a global counterexample. A universal forest proof at n21 would require eliminating all 77 labels (22 orbits) by exact original-order prefix/suffix supports, or discovering an actual completely replayable both-cyclic schedule.

The central size-1 survivors and four size-2 survivors are particularly promising targets for information-flow reasoning; neither is ruled out by the existing stated theorems. In particular, applying the older Stage14 strict-global-arm phase separation to arbitrarily large opposite groups is **invalid**, and applying small-tree privacy minima to unknown 8+ tree classes without verification would corrupt the candidate count. The new root-cut lemma is a strict conditional refinement, not a claimed universal bound of ten outsiders.

**Evidence state:** all-n conditional human proofs with independent small exact-tree checks; n21 count is exact for the declared necessary filters. No Lean/Coq formal certification, outside referee report or complete n21/full all-n theorem. PR #1 DRAFT / OPEN / UNMERGED; manuscript submission HOLD.
