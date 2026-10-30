# Stage 30 — all-n six-recipient double-path rigidity and crossed-support obstruction

**28 October 2026. Human proof of a sharp, helper-robust original-order normal form plus a conditional all-n no-crossing theorem.** Not a full original-half-forest theorem; no general temporal clique \(2n-3\) spanner proof; historical priority unverified. PR #1 remains DRAFT/UNMERGED, publication HOLD.

## Problem contract

Work with an **edge-once chronological tree**, distinct bidirectional calls, initial independent vertex secrets, and terminal recipient knowledge. A set C *doubly covers* all original secrets if **every original secret has at least two distinct terminal C carriers**. This is equivalent to C collectively covering all secrets while **NO** member of C is private, in the precise sense of [Stage 29](../v4.6/PRIVATE_THRESHOLD_THEOREM.md).

All conclusions below refer to the **ACTUAL** chronological last contacts. No event reordering is used. Vertices outside the designated recipient sets can be **arbitrary helpers**.

## Theorem 30.1 — rooted 3-recipient normal form (all n, helpers allowed)

Let \(W\) be any chronological tree with a designated root \(r\) and disjoint recipient group \(D=\{w,z,d\}\) of cardinality **three**. Assume:

1. r terminally knows **every** original W-secret;
2. D **doubly covers every** original W-secret.

Then the **actual last W-call** must be \((r,w)\) for some \(w\in D\), and deleting it partitions W into independent chronological tree histories \(W_r\ni r\) and \(W_w\ni w\), such that \(D\cap W_r=\{z\}\) and \(D\cap W_w=\{w,d\}\). Moreover the **actual last** call inside \(W_r\) is \((r,z)\), and the **actual last** call inside \(W_w\) is \((w,d)\), with interleaving of the two independent histories allowed.

Exactly two W original secrets have the following **mandatory exact C-supports**, where the group D is fixed:
\[
\boxed{\operatorname{Supp}_D(r)=\{w,z\},\qquad
       \operatorname{Supp}_D(w)=\{w,d\}.}
\]
The two supports form a three-vertex path \(z-w-d\), and are NOT allowed to be replaced by larger support overapproximations when a stronger exact test is intended.

### Proof

Since r is full after W's calls, its **last actual call** must join r to some w (only the two endpoints of the last edge of an edge-once tree could possibly know all W-secrets). Both endpoints r,w are then terminally full.

Suppose w were an unassigned helper, not in D. Deleting \((r,w)\) separates W into \(W_r,W_w\). No D member participates in the last contact. Therefore at least TWO distinct D participants would be needed in **each** side to double-cover that side's own original secrets, forcing |D|≥4, contradiction. Hence w∈D.

No D vertex on the r-side can know an original \(W_w\)-secret at the terminal time because only r (not in D) receives secrets across the last edge. Therefore at least two D members lie in \(W_w\). Conversely, a W_r secret can reach only w among the W_w recipients, so at least one D vertex must lie in W_r. Since |D|=3, the distribution is precisely \(\{z\}\) in W_r and \(\{w,d\}\) in W_w.

For every W_r-secret, z must be a terminal carrier: it is the sole D recipient in W_r and at most w in W_w can carry it. Thus z is a **complete** collector of the ORIGINAL W_r tree. Likewise r is complete within W_r prior to the last W-call (otherwise r could not become globally complete afterward). In an edge-once tree the only two complete collectors are its **last-call endpoints**, so W_r's final local call is \((r,z)\).

For every W_w-secret, only w and d among D can carry it, and both must; therefore both are complete W_w collectors, forcing \((w,d)\) as the last W_w internal call. The original r-secret is known by z inside W_r and by w alone on the opposite side after \((r,w)\); d was not its recipient. Hence its D-support is exactly {z,w}. The original w-secret is known inside W_w by w,d and cannot reach z on the other side because only r receives it at the final W-call. Hence its D-support is exactly {w,d}. QED.

The marked three-contact skeleton \((r,z),(w,d),(r,w)\) connects all four designated vertices; helpers cannot lie on paths between these marked vertices without creating a static cycle, though helper branches may attach to them arbitrarily.

## Theorem 30.2 — global six-recipient tree-cover double-path normal form

Let T be any edge-once chronological tree with two terminal complete singleton collectors u,v and an **exactly six-person group C** that doubly covers every original T-secret. Unassigned helpers are allowed.

By [Stage 29](../v4.6/PRIVATE_THRESHOLD_THEOREM.md), T's last call must be (u,v) and its deletion yields two independent tree histories rooted at u and v, each containing at least THREE designated C recipients. Since |C|=6, each side contains **exactly three**. Apply Theorem 30.1 to each side. Thus eight marked participants \(\{u,v\}\cup C\) span the **mandatory seven actual contacts** comprising the two rooted three-contact skeletons plus (u,v). The seven marked edges connect all eight marked vertices, so helpers form pendant trees off this marked skeleton, never intermediary paths between marked vertices.

Most importantly, among the exact carrier supports **within C** of T's original source secrets lie **four distinct 2-person sets** whose edge graph is precisely two vertex-disjoint length-two paths:
\[
\boxed{
E_T=
\bigl\{\{z_1,w_1\},\{w_1,d_1\},
       \{z_2,w_2\},\{w_2,d_2\}\bigr\},
}
\]
with all six z_i,w_i,d_i pairwise distinct. In each side they are exact supports of the respective rooted-tree labels r_i and w_i.

This is a universal **fixed original chronology and exact information-support** statement, not just a cardinality count. The construction from Stage 29 realizes the configuration and all its helper extensions, so the structural conclusion is nonvacuous.

## Lemma 30.3 — unique two-person transversal of two disjoint paths

Let \(E\) consist of the four edges of two disjoint three-vertex paths, with centers \(w_1,w_2\). A two-element set \(H\) meets every edge in E **iff** \(H=\{w_1,w_2\}\).

**Proof.** Each disjoint path requires at least one vertex of H. A single vertex hits both edges of a three-vertex path only when it is its center. Since H contains exactly two vertices to cover both vertex-disjoint paths, it must contain the center of each. Conversely their two centers hit all four edges. QED.

The statement is checked independently for all **90** distinct labelled \(2P_3\) edge families on six vertices and all 15 candidate two-person hitting sets per family.

## Theorem 30.4 — two sharp privacy-free trees cannot cross (all n, helpers allowed)

Let T be one original-prefix chronological tree and T' be a fully reversed original-suffix chronological tree, with an identical designated intersection cell C of **six** participants. Assume both local chronologies separately meet all Theorem 30.2 hypotheses: two fully complete singleton recipient groups outside C, each tree's own secrets doubly covered in C, and zero C-private recipients. Assume exact **all-pairs midpoint compatibility** across C:

\[
\forall a\in V(T),\ \forall b\in V(T'),\quad
  \operatorname{Supp}^{T}_{C}(a)
  \cap\operatorname{Supp}^{T'}_{C}(b)\ne\varnothing.
\]

**Claim:** This is IMPOSSIBLE for every choice of helper vertices and every number of original participants.

**Proof.** Theorem 30.2 forces four exact two-person source-support sets E_T forming two disjoint 3-vertex paths. It separately forces four **distinct** exact two-person target-support sets E_T' forming two disjoint paths. All-pairs compatibility would make *each* two-element target set in E_T' intersect *every* of the four source edges E_T. By Lemma 30.3 each target set would have to equal the **same unique pair** \(\{w_1,w_2\}\), contradicting the fact that the four target sets are distinct. Therefore the two tree chronologies cannot cross. QED.

### Direct consequence for the original half-forest frontier

In a hypothetical both-cyclic original **3×3** prefix/suffix split, an adjacent prefix tree \(P_i\) with its two singleton corner recipient cells and a six-person off-corner group \(C=P_i\cap Q_3\) can have zero private recipients, as Stage 29 shows. When it does, Theorem 30.2 forces its **four exact two-person P_i source-supports** in C. Therefore **every** reversed-Q3 target-support in C must hit the corresponding \(2P_3\) family. In particular **any target secret with exactly two C carriers must have those carriers precisely at the two path centers**. If two different target secrets have distinct two-carrier supports in C, that local pair cannot be globally compatible.

Theorem 30.4's full **two-tree** contradiction cannot be automatically applied to the opposite **unicyclic** Q3, and we do **not** infer that all (1,1,6) off-corner configurations are impossible. This is a strict new sound **source-target support filter** to integrate into an exact original-chronology CSP for the current remaining n22 matrices.

## Corollary 30.5 — exact 25-of-63 opposite support domain (all n)

Suppose the sharp six-recipient zero-private tree produces the four exact source supports of the two disjoint paths as in Theorem 30.2. A nonempty opposing reverse target-support set \(H\subseteq C\) satisfies midpoint crossing for **all four mandatory source secrets** if and only if it meets every edge in \(E_T\). Equivalently,

\[
\boxed{
  \bigl(w_1\in H\ \lor\ \{z_1,d_1\}\subseteq H\bigr)
  \quad\land\quad
  \bigl(w_2\in H\ \lor\ \{z_2,d_2\}\subseteq H\bigr).
}
\]

The **four inclusion-minimal** admissible support sets are exactly
\[
\begin{aligned}
&\{w_1,w_2\},\\
&\{w_1,z_2,d_2\},\\
&\{z_1,d_1,w_2\},\\
&\{z_1,d_1,z_2,d_2\}.
\end{aligned}
\]

Taking their upward closure inside the six-vertex cell gives **exactly 25 admissible nonempty support masks**, out of all \(2^6-1=63\). The cardinality histogram of admissible masks is
\[
 |H|=2:1,\quad 3:6,\quad 4:11,\quad 5:6,\quad 6:1.
\]
Thus **38** other nonempty target-support masks are rigorously incompatible with a privacy-free sharp (1,1,6) tree under exact original-order midpoint crossing. This is a universal **local-support-domain restriction**, not elimination of an entire n22 incidence matrix: an opposing unicyclic component might legitimately realize only compatible masks.

For an exact CSP/SAT chronology solver the implementation is particularly simple: add the four *binary* requirements
\[
 (w_1\lor z_1),\ (w_1\lor d_1),\
 (w_2\lor z_2),\ (w_2\lor d_2)
\]
for each opposite target's six carrier-indicator Booleans. Their conjunction is equivalent to the displayed domain. These clauses are valid **only after** independently establishing the six-person tree's **zero-private** condition and the associated marked path centers. If any C recipient is private, a different branch must be used and the present clauses cannot be silently imposed.

The Stage 30 independent enumerator now checks all 90 labelled path-pair systems against all 63 possible support masks, confirms the same 25-member upward-closed domain and 2,3,3,4 minimal sizes for each, and preserves the 8,100-pair all-crossing no-go test. **This is a finite combinatorial representation of an all-n conditional information-flow theorem** because the support-domain size is fixed at six independently of the number of helper participants.


## Independent adversarial evidence

[Stage 30 checker](double_path_rigidity.py):

- independently enumerates EVERY labelled chronological tree on n=4,5,6 via Prüfer words plus ALL edge orders; among instances with an outside full root and three designated double-cover recipients, tests the forced final-marked-edge structure and exact source-support pairs. Qualifying case totals are **12,72,864**, respectively (includes n=5,6 extra helper participants);
- independently exhausts all 90 labelled two-disjoint-path edge families, all 15 candidate two-element transversals per family, and **all 8,100 ordered pairs** of two-path families; zero pairs satisfy full cross-intersection;
- replays the exact eight-marked-participant chronology with 0,1,2,3,4,8,16 unassigned helpers, checking full singleton roots, double cover in C, and all four specified exact support pairs.

The computation is independent falsification support; the unbounded claims are established only by the displayed human last-edge arguments. No proof-assistant or outside referee certificate. Global original-half forest and the main \(2n-3\) spanner conjecture remain OPEN. Historical novelty unverified, manuscript submission HOLD, PR DRAFT/UNMERGED.
