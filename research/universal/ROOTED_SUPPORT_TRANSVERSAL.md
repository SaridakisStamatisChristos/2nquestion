# Universal crossed-tree two-carrier support theorem — every n

**28 October 2026. All-n mathematically quantified CONDITIONAL necessary theorem, not a full both-cyclic original-half forest proof. The purpose is to isolate the truly unbounded chronology-dependent obstruction, not increment n.**

## Exact chronological model

Let T be an edge-once bidirectional chronological TREE on a finite vertex set W, each original person having an independent secret and every tree edge called exactly once in some fixed original order. A terminal *complete collector* knows every original W-secret; a set C doubly covers W if every original W-secret is terminally known by at least two distinct C recipients. For each original source s define its exact C-carrier support \(S_s=\{x\in C:x\hbox{ knows s}\}\).

The following statements hold for **arbitrary** numbers of helper participants outside C.

## Lemma U.2 — rooted small recipient-support rigidity, ALL n

Suppose r∉C is a complete terminal collector of T and C doubly covers W. Then:

1. **|C|≥3.** For |C|≤2, every C participant would be complete, yielding ≥3 complete collectors including r, impossible for an edge-once tree.
2. If |C|=3 or4, the exact C-support family of W-original secrets contains **two DISTINCT two-element sets** \(\{y,z\},\{y,d\}\) sharing a vertex y. Thus the two supports are the edges of a three-vertex path.
3. If |C|=5, the exact C-support family contains **at least one** two-element set.

**Proof, preserving the original last contact and arbitrary helpers.** A chronological tree with a terminal full collector r has EXACTLY two full collectors, the endpoints of its final call, because no person could know secrets from both components before that call and its endpoints receive identical unions. Let the last contact be r–y. Delete it, leaving the preceding side trees U∋r and V∋y. The roots r,y were already complete for the original secrets of their respective sides before r–y.

If y were an unassigned helper outside C, every U-secret would need two C recipients **in U**, and every V-secret two **in V**. A side containing only two C recipients would make both complete for that side, **in addition to its outside complete root** r or y, contradicting the two-full-collectors limit. Therefore each side would require ≥3 C recipients, forcing |C|≥6. This rules out y outside C for all cases 3≤|C|≤5.

Hence y∈C. Put u=|C∩U| and v=|C∩V|. Every original U-secret has a terminal C-carrier only inside C∩U or at y, so u≥1; every V-secret has terminal C-carriers only within C∩V, so v≥2. Also u+v=|C|.

For |C|=3, (u,v)=(1,2). If C∩U={z} and C∩V={y,d}, the original r-secret has exact C-support {z,y} (double cover forces z), while the original y-secret has exact support {y,d}. Distinct edges share y.

For |C|=4, either (u,v)=(1,3) or (2,2). In the first case original r-secret has exact support {z,y}. Inside V, y is full and there are three C recipients; not all three can be complete (tree maximum two). Some original V-secret must therefore be absent from one of the three, and its C-support is **exactly two vertices** (double cover), **including y**, making a distinct pair {y,d}. In the second case, C∩V={y,d}; the original y-secret has exact support {y,d}. In U there are two C recipients and r is complete, so not both C∩U recipients can be complete; a U-secret carried by only one of those recipients has exact global C-support {y,z}, because y learns all U secrets at the final call. Distinct pairs again share y.

For |C|=5, possibilities (u,v)=(1,4),(2,3),(3,2). If u=1, the original r-secret has exact support {z,y}; if v=2, the original y-secret has exact support {y,d}; in the remaining case (2,3), the at-most-two-complete-collectors argument inside U produces a U-secret with exactly one C∩U carrier and thus exact global C-support {y,z}. This proves all cases. QED.

## Theorem U.3 — universal crossed-two-tree center obstruction

Let \(T_1,T_2\) be two edge-once chronological trees on finite vertex sets \(W_1,W_2\), sharing a cell \(X=W_1\cap W_2\) (their other vertices may be disjoint). In EACH tree assume:

- the terminal **T_i full collectors are the two distinct endpoints of its last call**, and **both endpoints lie OUTSIDE X**;
- X **doubly covers every original W_i secret**.

For original secrets \(a\in W_1,b\in W_2\), write \(S_a\subseteq X\) and \(R_b\subseteq X\) for their exact terminal carrier supports in the respective chronological trees. If the **all-pairs exact crossing condition** holds,

\[
\forall a\in W_1,\ \forall b\in W_2,\quad S_a\cap R_b\ne\varnothing,
\]

then necessarily

\[
\boxed{|X|\ge9.}
\]

This is valid for EVERY total number of original people and arbitrary helper vertices, not a finite n=22/23 induction.

### Proof

Remove the ACTUAL last contact of T_i. Its two full endpoints are outside X. The remaining histories are two independent chronological trees, each with a complete root outside X. Every original secret of a side has all its terminal X-carriers on the SAME side (no X participant touches the last contact). Hence X splits into two disjoint nonempty recipient sets of sizes k1,k2, each doubly covering every side-local secret. By Lemma U.2 each side must have at least three X recipients. Therefore |X|≥6.

Suppose |X|≤8. The only possible side-size distributions up to reversal are

- (3,3) at width 6;
- (3,4) at width 7;
- (3,5) or (4,4) at width 8.

From Lemma U.2, on a rooted side with 3 or4 X participants the ORIGINAL source-support family has two distinct exact 2-point supports forming a three-vertex path, and on a side with 5 X participants it has at least one exact 2-point support. The two sides use **disjoint X vertices**, so their forced small supports are disjoint across sides.

Let E be the forced 2-point support subfamily of T1. Every 2-point target support of T2 must meet **ALL** edges of E, because exact crossing holds for ALL source and target secrets.

For distributions (3,3),(3,4),(4,4), E contains the edges of TWO vertex-disjoint three-vertex paths. A two-person set intersects all four edges of E **only when it consists of the two path centers**; there is exactly **one** such 2-set.

For (3,5), E contains one 2-edge path on a three-vertex side and one 2-edge support from the disjoint five-vertex side. A two-person set intersecting all three edges must consist of the three-vertex path center and ONE of the two endpoints of the disjoint edge; there are at most **two** possible 2-set transversals.

Thus for all |X|≤8 the number of possible distinct two-point target supports compatible with T1 is ≤2. But applying Lemma U.2 independently to the two rooted sides of T2 produces **at least three distinct** terminal 2-point target supports: two from its 3/4 side and at least one from its 5 side, or four from its two 3/4 sides. This contradicts all-pairs crossing. Therefore |X|≥9. QED.

**Critical distinction:** It would be FALSE to assert that any chronological tree always has two full collectors. We invoke that fact only after the theorem explicitly assumes the two complete last-edge endpoints. Also, |X|≥9 is a necessary bound, NOT an existence theorem for 9 (or larger) compatible supports. The theorem must NOT be extrapolated to all widths from its bounded support subcases.

## Corollary for the ORIGINAL half-forest problem, ALL n

In a hypothetical successful shortest pairwise-distinct 2n−4-call schedule with BOTH ORIGINAL fixed halves cyclic, Bumby's original 3×3 structure gives the two unicyclic components U=P3 and V=Q3 in fully reversed suffix chronology, sharing center X. Their own last cycle-closing calls are between their exterior cells and DO NOT touch X, and each preceding spanning chronological tree preserves the center support sets.

If **neither U nor V has any complete center collector**, and **EACH** U,V has at least TWO terminal complete collectors within ONE SAME exterior cell, then each has an untouched exterior full collector before its last cycle-closing call. Its preceding spanning tree consequently has both last-tree-edge endpoints complete outside X. The absence of full collectors in the opposite cyclic component forces every original secret's center support to have size≥2 by exact original midpoint source-target crossing. Hence Theorem U.3 applies to the two preceding original-order trees and yields

\[
\boxed{|P_3\cap Q_3|\ge9.}
\]

This improves the earlier |X|≥7 *conditional structural bound* for EVERY n. Crucially it does **not** exclude hypothetical both-cyclic schemes with |X|≥9 or those lacking the outside-root hypotheses. It is NOT the desired all-n forest theorem, nor the separate 2n−3 temporal-clique spanner theorem.

## Reproducibility and falsification

[Independent bounded root/cover and abstract crossing tester](support_transversal_audit.py) exhausts all original labelled tree contact orders on 4,5,6 people with one outside full root and 3,4,5 designated recipients; checks the exact two-carrier path assertions and all abstract disjoint-path transversals for total center width 6,7,8. These computations challenge the local reasoning but do not establish all-n claims. The human proof above supplies the quantifiers for arbitrary helpers/total size.

**Historical originality:** no claim until comparing precisely to Bumby (1981), Labahn (1995), Krumme (1996). **Status:** all-n conditional lemma = human PROOF; complete all-n original-half forest theorem = OPEN; main 2n-3 spanner = OPEN; formal proof assistant check = NOT RUN. PR #1 DRAFT/UNMERGED, publication HOLD.
