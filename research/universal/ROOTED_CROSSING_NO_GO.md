# Universal rooted-crossing no-go via two-type strict descent

**30 October 2026 — new candidate complete HUMAN PROOF for an UNRESTRICTED structural impossibility theorem.** Original-edge order and all source supports are preserved exactly. No bound is imposed on finite tree sizes, the shared-cell size, or unassigned helper participants. The argument uses no finite-n extrapolation or general group-cover bound.

> **Important scope:** This closes the **standalone crossed-tree obstruction P**, provided the two-type descent is independently accepted. It does NOT, on its own, prove the full original-half-forest conjecture (other exterior-collector cases remain), and does NOT establish the distinct general temporal-clique `2n-3` exact-spanner existence bound. Human proof only, not Lean/Coq-certified or externally refereed.

## Model and elementary chronological fact

A chronological tree is a finite undirected tree whose |V|-1 distinct tree edges are bidirectional full-information calls in their ACTUAL chronological order. Each original person starts with its own independent secret. For a source a and recipient cell E, its **exact support** is the set of E vertices that terminally know a's secret.

A *full collector* knows ALL original tree secrets. For every chronological tree with >=2 vertices, a terminal full collector must be one of the ACTUAL LAST call's endpoints. Indeed removing the actual last call separates two previously noncommunicating side trees, and only the two last-edge endpoints can know both sides' original secrets afterward. If one last endpoint is complete, then the other is complete too, because the bidirectional last call makes their final knowledge sets identical. Removing the last call then leaves two original-order chronological side trees, each with its own final-edge endpoint full for its own side's original secrets.

If both last-edge endpoints are outside designated E, the last call changes NO E-recipient's knowledge. A source originating in a pre-last component has all its exact E carriers in that component. These are facts about the exact ACTUAL order, not a license to reorder calls.

## Definition — rooted crossed pair of type R

Two nontrivial edge-once original-order chronological trees A,B have EXACT shared vertex set E=V(A) intersect V(B), E nonempty, and satisfy:

1. A has a terminal complete root r outside E.
2. B's **two ACTUAL last-call endpoints p,q** are complete and both lie outside E.
3. For EVERY original A source a and original B source b, their exact terminal E-supports intersect.

No additional double-coverage assumption is imposed. The second complete endpoint of A, call it y (the endpoint opposite r in A's actual last call), may be either OUTSIDE E (type R0) or INSIDE E (type R1). Thus this class includes all previously defined admissibly crossed pairs P, but also includes one-inside/one-outside semi-crossed pairs.

### Theorem U.17 — NO rooted crossed pair of type R EXISTS, for ANY finite size

**Proof by minimal counterexample in |E|.**

Assume some type R pair exists. Choose one with minimum positive shared-center cardinality |E|. We construct a smaller type R pair in EVERY case, contradicting minimality. All subtrees inherit their own original relative order: we only delete actual final contacts.

**Case 0 — A's second full endpoint y is also outside E.**

Delete the ACTUAL last calls r-y of A and p-q of B, giving A0,A1 and B0,B1, each a genuine preceding chronological subtree. The four former last-edge endpoints are complete for their own component and all lie outside E.

Set E_ij=V(A_i) intersect V(B_j), for i,j in {0,1}. For every original source a in A_i and b in B_j, both deleted final calls had endpoints OUTSIDE E. Therefore their exact E supports were **unchanged** by either final call and are contained respectively within A_i and B_j. The parent all-pairs crossing yields a common E recipient necessarily lying in E_ij. Consequently each of the four (A_i,B_j) subpairs has exact original-source crossing on its own E_ij, and **all four E_ij are nonempty**. They are pairwise disjoint and partition E.

Each A_i has its inherited complete root (r or y) OUTSIDE E_ij; each B_j has its inherited complete root (p or q) OUTSIDE E_ij. Because its shared cell is nonempty and its root outside it, each side subtree has >=2 vertices, so its actual last edge has two complete endpoints. Write a_i for A_i's second terminal complete endpoint and b_j for B_j's second.

For (A_i,B_j) NOT to be a type R pair, **both** a_i and b_j would have to lie INSIDE E_ij: if either second endpoint lay outside, that side would have both its full last endpoints outside E_ij while the other side has at least one outside full root, and we could orient them as the two trees of type R.

But a_i lies in the single row component A_i and hence can belong to at most ONE of E_i0 and E_i1. In particular **a_0 cannot lie in both E_00 and E_01**. Therefore at least one of these two NONEMPTY cells is missing a_0. In that cell, the A0 subtree has BOTH full last-call endpoints OUTSIDE its center, while its B_j counterpart has an outside complete root, and exact crossing holds. After swapping the names A and B if needed, that cell is a type R pair.

Its center E_0j is strictly smaller than E because FOUR disjoint cells were nonempty. Contradiction.

**Case 1 — A's second full endpoint y lies INSIDE E.**

Delete the ACTUAL last call r-y of A, obtaining pre-last chronological side trees A0 (containing full root r) and A1 (containing full root y). Delete B's ACTUAL last call p-q into two pre-last side trees B0,B1, whose complete roots p,q are outside E.

Because y is a shared vertex in B, it belongs to exactly one B side. Let C be the OTHER B side, the one **not containing y**. Its inherited full root c is one of p,q and lies outside E.

Let E0=V(A0) intersect V(C) and E1=V(A1) intersect V(C). These cells are disjoint and both lie inside E minus {y}.

We verify **exact all-pairs crossing** in BOTH smaller cells. Take any original source a in A0 and any source b in C. In the original full A chronology, every E carrier of a lies in A0 OR is the endpoint y, which may acquire a's secret at A's final call. But y is outside C. In the original full B chronology, all E carriers of b lie in C, because B's last endpoints p,q are outside E and cannot transfer b's secret into any E person on the other side. Thus the nonempty intersection of the two parent exact supports must lie inside A0 intersect C = E0. That person's knowledge is unchanged when restricting to the two PRE-FINAL local chronologies, because the only possibly relevant deleted A call endpoints are r (outside E) and y (outside C), and deleted B call endpoints are outside E. Therefore A0 and C cross exactly on E0.

For a source a in A1, the original full A chronology adds no E carriers outside A1: its only newly informed outside-side endpoint is r, which is outside E, while y was already a full root of A1 before that last call. The same B argument makes every b in C have E support only in C. Their common exact recipient must therefore lie in A1 intersect C=E1, and this recipient's local chronology is unchanged. Hence A1 and C cross exactly on E1. Since these crossing properties hold for ALL nonempty source pairs, E0 and E1 are both NONEMPTY.

Both A0 and A1 have a complete root OUTSIDE their respective E cells: r is outside E globally, while y is outside C. The subtree C has its complete root c outside E and hence outside both cells.

Let w be the SECOND terminal complete collector of C, opposite c on C's own ACTUAL last contact. It exists because C contains at least one E0 or E1 recipient in addition to its outside root, and is therefore nontrivial. Since E0 and E1 are DISJOINT, **w cannot belong to both**.

Choose i in {0,1} such that w is OUTSIDE E_i. In the exact-crossed smaller pair (A_i,C), the C tree now has BOTH complete last-call endpoints c,w OUTSIDE E_i, while A_i has a complete root outside E_i. Hence (A_i,C) is a type R pair, with center E_i nonempty and STRICTLY SMALLER than E, since y belongs to E but not E_i.

Contradiction.

Both cases exhaust y's membership in E. Therefore no type R pair exists at any finite center cardinality, with arbitrarily many helpers. QED.

## Corollary U.18 — unconditional crossed-tree P impossibility at ALL widths

The canonical problem P from FOUR_HUB_MINIMAL_DESCENT.md asks for two original-order edge-once chronological trees whose **both actual last-call complete endpoints are outside their common center X**, whose X supports doubly cover all original secrets, and whose exact original-source support families fully cross.

Such a pair is automatically type R (indeed type R0). Theorem U.17 proves

 **THERE EXISTS NO admissibly crossed pair P FOR ANY finite X.**

In fact even dropping the double-coverage hypothesis cannot produce a pair: exact all-pairs crossing and both trees' outside complete endpoints are already impossible. The proof is not dependent on the numerical previous bounds (9,12,14,28) or a size upper limit. Those earlier conditional necessary bounds remain logically true but become vacuous when combined with U.17.

## Why earlier four-hub minimal descent did not close the problem

The prior U.14 descended only when BOTH local trees had their two final collectors OUTSIDE their smaller quadrant. This left a four-hub alternating pattern. The extra step above broadens the forbidden class to include a tree with one collector inside, and then chooses the other tree's prefinal component NOT CONTAINING that inside collector. The two resulting common cells are genuinely crossed in their original call orders. The other component has only one possible additional complete collector and cannot place it into both disjoint cells. This completes the infinite descent without any enumeration over n or |X|.

## Exact boundary counterexample: both trees with their second full collector INSIDE E

The requirement that at least one tree have BOTH terminal complete endpoints outside E is ESSENTIAL. It cannot be relaxed merely to one outside full root per tree.

Take E={0,1,2} and disjoint outside roots r and s. Let A have vertices {0,1,2,r}, with ACTUAL chronological contacts

 `(1,0), (2,r), (0,r)`.

Let B have vertices {0,1,2,s}, with ACTUAL chronological contacts

 `(0,1), (2,s), (1,s)`.

The two terminal complete collectors in A are r (outside E) and 0 (inside E), whereas in B they are s (outside E) and 1 (inside E). Exact replay gives the families of source E supports

 A: {0,1}, {0,1}, {0,2}, {0,2};

 B: {0,1}, {0,1}, {1,2}, {1,2}.

Every A support intersects every B support (including the cross pairs {0,2}∩{1,2}={2}), so the stronger **root-only** assertion would be FALSE. This positive chronological witness prevents claiming that U.17 establishes a prohibition when BOTH trees' opposite last-edge endpoints lie inside the shared center. It is excluded from type R as designed.

## Adversarial/falsification obligations and limits

1. **Inspect the carrier restriction in Case 1**: the potentially new A final-call recipient y is deliberately excluded by choosing C not containing y. No commutation of calls, root replacement or secret-source deletion occurs beyond legitimately restricting to original pre-last components.
2. **Inspect nonemptiness**: exact all-pairs crossing for the original source sets from every pre-last side forces each selected cell to be nonempty, even if outside helpers are present.
3. **Inspect the last-edge root fact**: complete endpoints of a tree are exactly its actual final-call endpoints for every nontrivial chronological tree, not all arbitrary spanning trees.
4. **Independent finite falsifier:** `rooted_crossing_descent_audit.py` separately replays original chronological trees and verifies the exact support locality identities in both cases across hundreds of thousands of source-pair checks. It is NOT a substitute for the human all-n descent proof.
5. **Epistemic boundary:** U.17/U.18 are presented as HUMAN PROOFS / independent mathematical referee pending. NOT FORMAL_CHECKER VERIFIED. Historical novelty UNCHECKED. The original gossip fixed-half forest problem, root-free exterior configurations, and main temporal clique 2n-3 question remain OPEN; do not promote these to solved.

**Citation dependencies:** self-contained elementary actual-last-contact fact; exact-support definition. No imported Stage11, Stage25-34, multiplicity, small-recipient-rigidity or finite-n computational conjecture is needed.
