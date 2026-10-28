# Universal minimal-crossing descent: the four-corner hub-cycle reduction

**28 October 2026. A genuinely UNBOUNDED structural reduction. Every assertion is quantified over arbitrarily large finite chronological trees and center sizes. It is NOT a proof that a crossing pair exists or cannot exist, and NOT the complete original-half-forest or 2n−3 temporal-spanner theorem.**

## Canonical crossed-tree problem P

Take two edge-once original-order chronological trees T,U, with common vertex set \(X=V(T)\cap V(U)\) (outside vertices arbitrary). Suppose the **actual last contact** of T joins two terminal full collectors outside X, and similarly for U. Suppose every original source secret of either tree is terminally known by at least TWO different recipients in X, and EVERY exact T source X-carrier set intersects EVERY exact U source X-carrier set.

Call such a pair *admissibly crossed*. The conjecture that **NO** admissibly crossed pair exists, for arbitrary X, remains OPEN (and is stronger than the conditional original-half-forest reductions).

## Lemma U.12 — four nonempty temporal quadrants (ALL n)

Delete the actual last T contact, giving preceding chronological rooted trees \(T_0,T_1\) with full outside roots r0,r1. Delete the actual last U contact, giving rooted trees \(U_0,U_1\) with full outside roots s0,s1. For each i,j∈{0,1}, set
\[
Q_{ij}=V(T_i)\cap V(U_j)\subseteq X.
\]

Then **ALL FOUR Q_ij are nonempty**. Each pair \((T_i,U_j)\) satisfies exact all-pairs source-carrier crossing **inside Q_ij** under its unchanged original local chronological histories.

**Proof.** Every original T_i secret has X support contained entirely in \(T_i\cap X\): the deleted T final contact changes knowledge only at r0,r1, outside X. Likewise U_j support lies in \(U_j\cap X\). Choose any original source a∈T_i and b∈U_j. The global crossing condition gives at least one common carrier, necessarily in \(Q_{ij}\). All source pairs in that quadrant therefore cross, and Q_ij cannot be empty. QED.

## Lemma U.13 — a collector-free quadrant produces a STRICT descent (ALL n)

In each rooted T_i, the outside complete root r_i is an endpoint of its own ACTUAL last local tree contact r_i–y_i, and y_i is also complete for all original T_i secrets. Similarly the last local contact of U_j is s_j–z_j with both complete for U_j.

If for some quadrant \(Q_{ij}\) we have
\[
y_i\notin Q_{ij}\quad\land\quad z_j\notin Q_{ij},
\]
then the two STRICTLY SMALLER chronological trees \(T_i,U_j\), with shared set Q_ij, **themselves constitute an admissibly crossed pair** satisfying ALL hypotheses of P, and \(|Q_{ij}|<|X|\).

**Proof.** Lemma U.12 gives all-pairs source crossing inside Q_ij. In T_i, its last local endpoints r_i,y_i are both outside Q_ij (r_i is outside all X); likewise s_j,z_j are outside Q_ij in U_j. Thus each side has its two terminal full collectors outside its shared set. To establish DOUBLE coverage, suppose some original T_i secret has a singleton Q_ij support {w}. Crossing with every U_j source forces every U_j source to occur in the terminal knowledge of w; i.e. w is a complete U_j collector. But U_j is an edge-once tree whose ONLY possible complete terminal collectors are its actual last-contact endpoints s_j,z_j, both outside Q_ij. Contradiction. The same argument applies with T_i/U_j exchanged. Therefore Q_ij double-covers every original local source secret on each side. Finally all four Q_ij were nonempty, so any single Q_ij is a strict subset of X. No call has been reordered or relabelled. QED.

## Theorem U.14 — a minimal crossed pair MUST have a deranged four-hub cycle

**UNBOUNDED reduction theorem.** If any admissibly crossed pair P exists at any finite shared-center width, then there exists an admissibly crossed pair with MINIMUM possible center size whose four rooted-side last-edge second collectors \(y_0,y_1,z_0,z_1\) satisfy ALL of:

1. All four lie **inside** X.
2. They occupy **four DISTINCT quadrants**, exactly one collector in EACH \(Q_{ij}\).
3. The two T collectors y0,y1 occupy **opposite quadrants** (one in each row and in different columns).
4. The two U collectors z0,z1 occupy the **complementary opposite pair** (one in each column and different rows).

Equivalently, up to interchanging labels of the two T and U halves:
\[
\begin{pmatrix}
Q_{00}:\ y_0\text{ complete for }T_0&
Q_{01}:\ z_1\text{ complete for }U_1\\
Q_{10}:\ z_0\text{ complete for }U_0&
Q_{11}:\ y_1\text{ complete for }T_1
\end{pmatrix}.
\]

Thus the only possible MINIMAL obstruction to a universal crossed-tree impossibility proof has an **alternating four-corner complete-collector pattern**, regardless of total n or |X|.

### Proof (no finite-n enumeration)

If any admissible pair exists, choose one minimizing the POSITIVE INTEGER \(|X|\). By Lemma U.13, **no** quadrant can avoid both corresponding second last-edge full endpoints. Each T hub y_i, being a single participant of T_i, can lie in **at most ONE** of the two quadrants in row i; if outside X, it lies in none. Similarly each U hub z_j can lie in at most ONE quadrant of column j. Therefore these FOUR hubs can cover at most FOUR different quadrants.

But all FOUR quadrants MUST contain a hub of one of the two sides, otherwise that hub-free quadrant produces a smaller admissible crossed pair, contradicting minimality. Hence all four hubs lie in X, occupy four DISTICT quadrant cells, and their occupied cells are pairwise different. The two T hubs are in distinct rows by definition and must now be in different columns; otherwise a U column would have to cover TWO unoccupied cells with its ONE hub, impossible. Therefore the T hubs form one diagonal; the U hubs, which occupy the other two cells and are in distinct columns, form the complementary diagonal. The displayed arrangement follows by relabelling side indices only; **no original chronological call is reordered**. QED.

### Logical consequence and precise missing lemma

Existence of an unrestricted admissible crossed pair is EQUIVALENT to existence of an admissible crossed pair with the four-corner deranged hub arrangement: one direction is Theorem U.14; the reverse is trivial since a four-hub pair is still an admissible pair.

This converts the **ALL-WIDTH** subproblem into one STRUCTURAL configuration, **not** into a bounded number of participants. It does NOT establish impossibility of the remaining 4-hub cycle; constructing a real example would disprove the stronger crossed-tree no-go but NOT automatically disprove the full original-half-forest conjecture. A new acyclic information-flow or chronological private-support invariant must now eliminate this exact deranged pattern, or an actual chronological witness must be exhibited.

The user's PRIMARY exact 2n−3 temporal-clique spanner conjecture is a separate existence problem; even resolving the crossed-tree subproblem would leave root-free both-cyclic configurations unaddressed.

## Adversarial evidence / status

The independent [symbolic quadrant-coverage checker](four_hub_descent_audit.py) enumerates all possibilities for the four final local hub positions (each may lie in one of its two row/column quadrants or outside X) and confirms that avoiding every hub-free quadrant **forces** exactly the two complementary-matching assignments. This is a finite COMBINATORIAL check of the hub placement reduction, not a substitute for Lemma U.13's original chronology and double-coverage proof. All-n mathematical induction/descent above is HUMAN CHECKABLE, not formally Lean/Coq certified, and novelty against historical gossip structural theory remains UNVERIFIED. No unrestricted all-n original half-forest or 2n−3 spanner proof has been claimed. Keep PR DRAFT and publication HOLD.
