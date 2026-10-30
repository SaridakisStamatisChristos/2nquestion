# All-\(n\) receiver-multiplicity theorem and two-support crossed-tree rigidity

**28 October 2026. Mathematical statements quantified over EVERY finite edge-once chronological tree, EVERY positive multiplicity q, EVERY helper configuration, and arbitrary n. Human proofs below; finite independent audits are separate. This does NOT solve the unrestricted original fixed-half forest or direct 2n−3 temporal-clique spanner conjecture.**

## Canonical model: no reordered calls

An edge-once chronological tree T has exactly |V(T)|−1 *distinct undirected bidirectional calls*, one along each edge of a tree, ordered as they actually occurred. Initially every vertex carries one independent original secret. A designated group C is q-covering if **each** original T secret is possessed by **at least q DISTINCT C people** after the complete chronological history. A *root* r is terminally full if it knows every original T secret. Extra vertices not in C are allowed without restriction.

### Theorem U.4 — SHARP receiver-multiplicity lower bound, ALL q and n

For **every integer \(q\ge1\)** and **every** valid original-order edge-once chronological tree T with a terminal full collector r, one has

\[
\boxed{
|C|\ \ge\
\begin{cases}
2^{q-1},&r\in C,\\
2^q-1,&r\notin C.
\end{cases}}
\]

Both bounds are **attained** for **every** q by explicitly constructible genuine edge-once chronological trees with NO unassigned helpers. These are exact extremal numbers, not asymptotics or finite numerical guesses. In particular q=2 gives 2/3, q=3 gives 4/7, q=4 gives 8/15, q=5 gives 16/31, etc. The outsider result is stronger than the earlier ad hoc q=2 and q=3 special-case arguments.

### Human proof of the lower bounds, with a well-founded induction

Use double well-founded induction on (q, |V(T)|); when q stays unchanged, the recursive side tree is **strictly smaller**. The cases q=1 are immediate: C must be nonempty; the displayed lower bounds are both one. Define outsider bound f_out(0)=0 only for the bookkeeping of a non-coverage requirement.

For any q≥2 and T with more than one vertex, the full root r must be an endpoint of T's **actual final call r–y**. Indeed no participant can know secrets from both pre-final components before that call, while afterward only its endpoints could first become full. Remove that last call, giving *disjoint* chronological tree histories U∋r and V∋y. Both r and y must already know every original secret of **their own side** immediately before the final call. The last call changes information at r,y ONLY.

**Root r belongs to C.**
- If y also belongs to C, for each U secret at most one extra receiver across the final cut is y; for each V secret at most one extra C receiver outside V is r. Thus C∩U must (q−1)-cover U and C∩V must (q−1)-cover V, and both rooted subtrees' roots belong to their recipient sets. By induction
  \[
  |C|\ge2^{q-2}+2^{q-2}=2^{q-1}.
  \]
- If y does NOT belong to C, each U original secret must already have q C∩U receivers; root r∈C∩U is full on U. The **smaller** tree U therefore has |C∩U|≥2^{q−1} by induction on |V| with fixed q. Any other C members only increase |C|, proving the bound. This argument avoids circularity.

**Root r does NOT belong to C.**
- If y belongs to C, each U original secret must have at least q−1 carriers inside C∩U (only y can add one across the final cut), and every V original secret must have q carriers already inside C∩V (r is outside C, and no other U participant can receive V secrets at the final call). Root r is full within U and root y within V. Induction gives
  \[
  |C|\ge (2^{q-1}-1)+2^{q-1}=2^q-1.
  \]
- If y also does NOT belong to C, no C participant is affected by the final call. The smaller U chronological tree must already have q-fold coverage from C∩U and full outsider root r, so |C∩U|≥2^q−1 by the **strictly smaller tree** induction; again adding C∩V cannot lower |C|. This is well-founded even when U is a singleton (in that situation a positive-q U cover by C∩U would itself be impossible).

The one-vertex base case is compatible: if root r∈C then C={r} covers its only secret once, so q≤1; if root r∉C then no nonempty C exists. This closes all induction branches. QED.

### Explicit constructions attaining both bounds, EVERY q

The constructions are recursive, preserve the original chronological edge ordering, and **never reuse an edge**. Each combines *two disjoint trees whose local calls all occur before their single final joining call*.

- **IN(q):** root r∈C. Base IN(1) is one person, no calls, C={r}. For q>1 take two disjoint copies of IN(q−1), perform their internal chronological calls, then call their two roots once. Keep every participant in C, designate either of the joining roots as the complete root. Each original secret has its previous q−1 in-side receivers plus the complete root from the other side: ≥q recipients. Exactly 2^{q−1} C people.
- **OUT(q):** root r∉C. Base OUT(1) has two people r and z, C={z}, one call (r,z). For q>1 combine a copy of OUT(q−1) rooted at r with a disjoint copy of IN(q) rooted at y∈C. Perform both internal histories, then the final call (r,y). Original OUT-side secrets gain y in addition to their q−1 recipients; original IN-side secrets already have q recipients. The joined r is complete, remains outside C; recipient count is (2^{q−1}−1)+2^{q−1}=2^q−1.

For all q the resulting graph is a genuine tree with \(2^q\) vertices for OUT(q) and \(2^{q−1}\) vertices for IN(q), hence exact cardinality and chronological chronology both hold. QED.

## Theorem U.5 — UNIQUE two-carrier support in any crossed two-root trees, ALL n

Let T1 and T2 each be an original-order edge-once chronological TREE with a shared participant cell \(X=V(T_1)\cap V(T_2)\) (and arbitrary non-shared helper vertices). Suppose each tree's two terminal complete collectors are its ACTUAL final-tree-call endpoints **outside X**; suppose X doubly covers **every** local original secret in each tree; suppose every exact original T1 source support S_a in X intersects every exact original T2 source support R_b in X.

**Then T1 has at most ONE DISTINCT two-person original-secret support \(S_a\subseteq X\), and symmetrically T2 has at most one.** Different original secrets may legitimately share the same two-person support; the theorem counts distinct SUPPORT SETS, not source multiplicity.

### Complete human proof

Remove the actual last T2 tree call between its two outside full collectors. It leaves two independent preceding rooted chronological side trees \(V_1,V_2\), each with a terminal complete root OUTSIDE X, and partitions X into disjoint sets \(X_1,X_2\). Each original V_i secret has all of its terminal X carriers inside X_i, because only the outside roots participate in the final T2 contact.

Suppose T1 has a two-person source support S={x,y}. Exact all-pairs crossing forces S to intersect a nonempty X support for EVERY original secret from **each** V_i. It follows that S MUST contain exactly one point in each X_i. Write x∈X1,y∈X2. For EVERY original V1 secret b, its support R_b is included in X1 and must intersect S, hence contains x. Thus x alone knows **ALL original V1 secrets**, i.e. x is a terminal FULL collector of the V1 rooted side tree. Likewise y is a full collector of V2.

But the root r_i of V_i is ALREADY terminally full and lies OUTSIDE X. An edge-once chronological tree can have **at most two** complete collectors, so each V_i can contain at most ONE additional full collector in X_i. For any second two-person T1 support S', exactly the same argument forces its unique X1 point to be that SAME x, and its unique X2 point the SAME y. Therefore S'=S. QED.

### Corollary U.6 — improved original-order all-n center lower bound 12

For either T_i remove its actual last tree call outside X. The two preceding side trees have full outside roots, and X splits into C1,C2, each of which doubly covers the original secrets on its own side. These are disjoint support universes.

By Theorem U.5, the **entire T_i** has at most one *distinct* 2-person X support. A rooted side with |C_j|≤4 necessarily has **at least TWO DISTINCT** two-person support sets, by the earlier proven [rooted 3/4 recipient exact-support normal form](ROOTED_SUPPORT_TRANSVERSAL.md). Thus **each** rooted side has |C_j|≥5.

If a rooted side has |C_j|=5 or6, and all its original secrets had at least **three** carriers in C_j, Theorem U.4 (q=3, root outside C_j) would force |C_j|≥7, contradiction. Hence every side with size 5 or6 has at least ONE 2-person X support. The **other** disjoint rooted side therefore has **ZERO** two-person supports by Theorem U.5, so every original secret there has at least THREE carriers, and Theorem U.4 forces its size≥7.

If neither rooted side has size 5 or6, both have size≥7. In all cases

\[
\boxed{|X|=|C_1|+|C_2|\ge5+7=12.}
\]

This holds for ALL total n and arbitrary helpers; it is an exact new **NECESSARY** bound, not a claim that width12 is feasible. If neither side has ANY two-person supports, the stronger |X|≥14 follows. QED.

### Conditional corollary for the original half-forest question

In the previous both-original-cyclic shortest-gossip 3×3 setting, IF the two unicyclic sides have no complete center collectors and each has ≥2 complete terminal collectors in a single exterior cell, then each preceding spanning chronological tree has two full last-edge endpoints outside X; each original source/target X support is double-carried because a singleton would force a complete opposite center collector. The last unicyclic calls are OUTSIDE X so the exact X supports are unchanged. Apply Theorem U.5 and Corollary U.6 to obtain:

\[
\boxed{\forall n,\quad |P_3\cap Q_3|\ge12.}
\]

This strengthens the prior conditional |X|≥9 bound and requires **NO n-specific incidence census or assumption that every tree has full collectors**. HOWEVER the all-n forest conjecture itself is not proved: X≥12 is not ruled out, and exterior-cell full-collector forcing is not universal (sharp private-free constructions exist at large cells).

## Independent numerical falsification, not finite-to-infinite sleight of hand

Run from repository root:
  python3 -B research/universal/exponential_multiplicity_audit.py

The audit constructs and REPLAYS exact IN(q), OUT(q) chronological trees for q=1..7 (up to 128 vertices), independently enumerates ALL labelled original chronological trees and arbitrary designated subsets up to n=6 to challenge the exponential lower bound with omitted helpers, and checks size-two support transversals on independently built two-root 3+3,3+5,5+7,7+7 chronological trees.

Evidence states: **HUMAN_PROVED** for the displayed exact induction and two-point support lemma; **EXECUTED CI only after confirmed matching run**; **NOT FORMALLY VERIFIED**; historical novelty **UNCHECKED**; full all-n original-half forest and primary exact 2n−3 temporal-clique spanner **OPEN**. Maintain PR #1 DRAFT/UNMERGED, publication HOLD.
