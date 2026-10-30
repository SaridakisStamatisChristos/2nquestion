# Unrestricted crossed-tree receiver-cover transfer: center at least fourteen

**28 October 2026. Human proof with \(\forall n\), with NO n-specific incidence composition or bound on the total number of participants. This is a CONDITIONAL theorem about original edge-once chronological trees; it is NOT yet a solution of the all-n fixed-half forest conjecture or the 2n−3 temporal-clique reachability conjecture.**

## Definitions and hypotheses (no reordering)

Let \(T\) and \(U\) be two distinct edge-once chronological undirected trees with original independent vertex secrets. Their common designated recipient set is \(X=V(T)\cap V(U)\), with potentially arbitrarily many vertices outside X and without requiring their outside vertices to agree.

Each chronological tree has its **actual last-call endpoints fully informed and outside X**. Consequently its earlier calls form **two disjoint rooted chronological side trees**, each with a full collector outside X. Assume that the final recipient knowledge of X **doubly covers** each tree's original local secrets. Assume exact all-pairs center crossing:
\[
\forall a\in V(T),\ \forall b\in V(U),\
\operatorname{Supp}^{T}_{X}(a)\cap\operatorname{Supp}^{U}_{X}(b)\ne\varnothing.
\]
No original contact event may be reordered. Each source support must be the exact set of X participants terminally knowing that original source secret.

## Lemma U.7 — two disjoint transverse information covers cannot have total size below six

Let U be a chronological tree whose two complete last-call endpoints are OUTSIDE X; delete its last edge, producing two disjoint rooted trees \(U_1,U_2\) with full outside roots \(r_1,r_2\), and partition \(X=X_1\uplus X_2\).

Let A,B⊆X be **disjoint** subsets, such that EVERY original U secret has at least one recipient in A and at least one in B. Then

\[
\boxed{|A|+|B|\ge6.}
\]

**Human proof, no imported general tree-cover theorem.** In each rooted chronological side \(U_i\), its original secrets can reach only members of \(X_i\) among X, because the final U contact involves only \(r_1,r_2\), neither belonging to X. The two disjoint groups \(A_i=A\cap X_i\) and \(B_i=B\cap X_i\) therefore each collectively cover EVERY original secret on \(U_i\). Both are nonempty. Since \(r_i\notin X_i\) is ALREADY a complete U_i collector, if \(|A_i|+|B_i|=2\) both disjoint groups must be singletons. Each singleton would individually know all original \(U_i\) secrets, yielding **three distinct complete collectors** \(\{r_i\},A_i,B_i\). This is impossible for any chronological edge-once tree: only the two actual last-edge endpoints can ever be globally complete. Hence \(|A_i|+|B_i|\ge3\) separately for i=1,2, and summing gives |A|+|B|≥6. QED.

This uses only the elementary at-most-two-complete-collectors tree fact. It is independent of any previous helper-robust higher-arity tree-cover theorem.

## Theorem U.8 — all-n crossed-tree quantitative transfer

In the precise crossed T/U model above, remove T's own actual last contact outside X, splitting its original sources into two independent rooted sides \(T_A,T_B\), and X into disjoint groups \(X_A,X_B\).

Define the **minimum exact X-support multiplicities** of original sources within those sides:
\[
a=\min_{s\in V(T_A)}|\operatorname{Supp}^T_X(s)|,\qquad
b=\min_{t\in V(T_B)}|\operatorname{Supp}^T_X(t)|.
\]
The doubly covering hypothesis guarantees \(a,b\ge2\), and the minimum supports lie respectively entirely inside \(X_A\) and \(X_B\).

Choose source secrets s,t attaining these minima, and write A=Supp(s), B=Supp(t). The two sets A,B are disjoint. **Exact cross compatibility** says A and B each intersects the U-support of EVERY original U secret. Therefore A,B are two disjoint, collectively complete recipient groups for the other tree U, and Lemma U.7 applies:

\[
\boxed{a+b=|A|+|B|\ge6.}
\]

Now each rooted T_A side has a complete collector outside its recipient group \(X_A\), and each original side secret has at least a recipients in \(X_A\); likewise T_B with b. The sharp [all-q rooted multiplicity theorem](EXPONENTIAL_MULTIPLICITY_AND_PAIR_RIGIDITY.md) (proved by a full well-founded chronological last-edge induction, independently of this result) yields:
\[
|X_A|\ge 2^a-1,\qquad |X_B|\ge2^b-1.
\]

The function \(2^a+2^b-2\) over integers a,b≥2 with a+b≥6 attains its absolute minimum **14**, at (a,b)=(3,3); the next allowed pair (2,4) already gives 18. Hence:

\[
\boxed{\forall n,\quad |X|\ge14.}
\]

The proof is symmetric in T and U and allows any number of outside helper participants. **No global forest property has been assumed.** QED.

### Stronger conditional profile observations

The previous [unique two-carrier support theorem](EXPONENTIAL_MULTIPLICITY_AND_PAIR_RIGIDITY.md) further states that **each entire crossed tree permits at most ONE DISTINCT two-person source support**. If a side of T has a=2, its opposite side must have b≥4 and |X|≥18 by the argument above. If both sides have a,b≥3, then |X|≥14. In particular |X|=14 (if possible at all) would force both rooted sides to have exactly seven X participants and **every** local source to have exactly three carriers; these are extreme configurations, not established realizable crossed pairs. An exact MILP test of two fixed recursive sharp constructions was infeasible, but those tests are not an all-width no-go.

### Corollary for original half-forest research, EVERY n

For a hypothetical shortest successful distinct-call gossip chronology with BOTH ORIGINAL fixed halves cyclic, write U=P3, V=fully reversed Q3, and X=P3∩Q3. Whenever:
- neither cyclic component has any full terminal center collector;
- each cyclic component has ≥2 terminal full collectors within a SINGLE exterior cell;

an untouched exterior full collector makes the preceding chronological spanning TREE of each cyclic component have TWO complete original last-edge endpoints OUTSIDE X. The cyclic last contacts lie outside X, so center information supports are unchanged. Since a singleton P3 source X-support would force a reversed Q3 center complete collector (and vice versa), both trees' original-secret center supports are ≥2. Exact all-pairs crossing holds for successful gossip.

Therefore the crossed-tree theorem applies to the ACTUAL unreordered histories:
\[
\boxed{\forall n,\quad |P_3\cap Q_3|\ge14.}
\]
This is stronger than the earlier conditional nine- and twelve-center lower bounds, and **the same hypotheses are STILL ESSENTIAL**. We have **not proved the universal original half-forest property**, since width≥14 and cases lacking exterior full collectors remain unrestricted. Nor does a structural claim about an already-existing optimum establish the independently open 2n−3 arbitrary temporal clique spanner existence bound.

## Adversarial and independent evidence

[Executable independent cover-transfer audit](crossed_cover_transfer_audit.py) enumerates genuine original chronological rooted trees constructed via the all-q recurrence, computes all small terminal X hitting sets and checks that no two disjoint collectively complete X recipient groups have combined size below six. This is a finite falsification check of Lemma U.7. It additionally checks exact rooted multiplicity construction families and the integer optimization \(a+b\ge6\implies 2^a+2^b−2\ge14\) across sample ranges.

**Epistemic label:** human PROVED (the statements shown with explicit all-n quantifiers); not FORMALLY_VERIFIED in Lean/Coq, no external referee, scholarly novelty UNCHECKED, original all-n half-forest OPEN, primary exact 2n−3 temporal clique spanner OPEN. Draft PR #1 remains open/unmerged; manuscript submission HOLD.
