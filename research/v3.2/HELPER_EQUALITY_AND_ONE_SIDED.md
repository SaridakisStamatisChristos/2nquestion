# Stage 15 — Steiner helper equality rigidity and the one-sided 3×3 obstruction

**28 October 2026. New ALL-n human proof, small exhaustive falsification and explicit local boundary construction.** The *unrestricted* original chronological half-forest conjecture is **OPEN**. PR #1 remains DRAFT/UNMERGED; historical originality is unverified.

## 0. Problem, source and what is NOT claimed

For a shortest successful bidirectional telephone-gossip schedule, consider the **original** fixed first/last \(n-2\) calls, without reordering. Bumby's 1981 Theorem 3 confines a hypothetical both-cyclic split to two closed tree components and one unicyclic component on each side; see [primary-source chronology audit](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md).

Index original prefix components \(P_1,P_2\) (trees) and \(P_3\) (unicyclic), fully reversed original suffix components \(Q_1,Q_2\) (trees) and \(Q_3\) (unicyclic), and \(m_{ij}=|P_i\cap Q_j|\). All nine cells must be nonempty for a successful scheme. Bumby's *actual* chronological spine says the last contact within \(P_3\) joins \(Q_1\) to \(Q_2\) and lies on its unique static cycle; the first original suffix contact within \(Q_3\), its last in reversed chronology, joins \(P_1\) to \(P_2\) and lies on its static cycle.

The new theorem applies when **one side**, not necessarily both sides, has a pair of size-two off-corner cells.

## 1. Strengthening the Stage 11 exact tree-cover equality theorem to UNUSED HELPERS

### Theorem H (ALL n, proved here)

Let \(T\) be any chronological tree on \(v\ge1\) distinct people, with each of its \(v-1\) edges called exactly once. Let \(G_1,\ldots,G_s\) be pairwise disjoint, nonempty designated recipient sets; participants outside their union are *helpers*. Suppose that after all tree calls, the members of **each** \(G_j\), collectively, know every original secret of \(T\). Stage 11's helper-robust lower bound gives

\[
R:=\sum_j |G_j|\ \ge\ 2^{s-1}.
\]

**New equality rigidity:** For **every \(s\ge2\)**, if \(R=2^{s-1}\), even with any number of unassigned helper vertices:

1. Both endpoints \(x,y\) of the last tree contact are designated recipients in **different** groups, and these are the *only* two terminal full collectors of \(T\).
2. Exactly two designated groups are singleton groups: \(G_a=\{x\}\), \(G_b=\{y\}\).
3. **Every** designated recipient \(z\in G_j\) has a *private original secret*: one secret known after the calls by \(z\) and by no other member of \(G_j\).

For \(s=1\), equality \(R=1\) simply makes the unique recipient a full collector and makes its group and private-secret assertion trivial.

### Complete induction

For \(s\ge2\), let the last edge \(xy\) partition the tree into \(U\ni x\) and \(V\ni y\). No earlier calls join \(U,V\). Write \(G_j^U=G_j\cap U\) and \(G_j^V=G_j\cap V\).

**Endpoints cannot be helpers under equality.** Suppose \(y\) is unassigned. For **every** \(j\), all \(U\)-secrets must be covered by \(G_j^U\), because the only terminal vertex in \(V\) potentially holding any \(U\)-secret is \(y\), and \(y\notin G_j\). These \(s\) nonempty recipient groups form a complete tree-cover instance inside \(U\), so \(R_U\ge2^{s-1}\). But \(R_V\ge1\): every \(V\)-secret must reach every \(G_j\); if all recipients were in \(U\), it could reach at most \(x\), which belongs to at most one group, impossible as \(s\ge2\). Thus \(R\ge2^{s-1}+1\), contradicting equality. Similarly \(x\) cannot be a helper.

**The endpoints must belong to different groups.** If both endpoints lie in \(G_a\), then each other group \(G_j\), \(j\ne a\), must have members on both sides and those members must collectively know all corresponding side secrets; the only recipients who could get other-side secrets at the last call are \(x,y\in G_a\). Applying the Stage 11 lower bound to these \(s-1\) groups in each side gives at least \(2^{s-2}+2^{s-2}=2^{s-1}\) designated recipients **outside \(G_a\)**, contradicting \(R=2^{s-1}\).

Thus \(x\in G_a\), \(y\in G_b\) with \(a\ne b\). For every \(j\ne b\), \(G_j^U\) covers all \(U\)-secrets; for every \(j\ne a\), \(G_j^V\) covers all \(V\)-secrets. Apply Stage 11 to the two \((s-1)\)-group instances:

\[
R_U^{(\ne b)}\ge2^{s-2},\qquad R_V^{(\ne a)}\ge2^{s-2}.
\]

The counted recipients are disjoint. **Equality** therefore requires (i) both subproblems attain equality, (ii) \(G_b^U=\varnothing\) and \(G_a^V=\varnothing\), and (iii) no designated recipients are omitted from either count.

Since \(G_b\) has no members in \(U\), all its members in \(V\) could learn \(U\)-secrets only through \(y\) at the last call. Hence \(x\) must already know **every** \(U\)-secret immediately before \(xy\). Symmetrically \(y\) knows every \(V\)-secret. Hence both become complete collectors, and no other vertex ever can (it never participates in the sole cross-edge).

Apply induction to the tight \((s-1)\)-group subinstances. When \(s=2\), both subproblems have one designated recipient (because each count equals 1), so \(G_a=\{x\}\), \(G_b=\{y\}\). When \(s\ge3\), the induction singleton-collector property says the complete side-root \(x\) (respectively \(y\)) is a singleton in its subproblem; since \(G_a\) has no V members, \(G_a=\{x\}\), and similarly \(G_b=\{y\}\). Every other group must have designated recipients in **both** sides (they have to cover each side's original secrets and cannot be touched at the last call), hence has size at least 2. Exactly two singleton groups result.

Finally, every designated recipient \(z\in G_j^U\), \(j\ne b\), has by induction a secret from \(U\) private within \(G_j^U\). No recipient of \(G_j^V\), \(j\ne b\), can receive that \(U\)-secret at the last contact (only \(y\in G_b\) could). Thus this same \(U\)-secret remains private within **all** \(G_j\). Apply the symmetric argument to \(V\); this also handles \(G_a,G_b\). The induction starts at \(s=1\). QED.

**Novelty caveat:** Stage 11 already proved the *lower bound* for helpers, and equality rigidity with **no** helpers. The above fills the previously unproved equality-rigidity-with-helpers case. The historical status of this special local theorem is not settled.

## 2. General one-sided crossed-arm obstruction (ALL n)

### Theorem C

Let \(A\) be a connected unicyclic original prefix component with \(v\) distinct chronological calls. Suppose its **last** call lies on its unique static cycle and has both endpoints outside \(X=A\cap B\); hence its preceding \(v-1\) calls form a spanning tree \(T\) and every \(X\) participant's knowledge is unchanged by the last call.

Let \(B\) be a connected reversed-suffix component with **\(k\ge3\)** causally sealed chronological tree arms \(B_1,\ldots,B_k\), each containing exactly one outside-\(X\) root (complete for its arm). Assume the complete **original** gossip schedule succeeds, and all information crossing between \(A\) and \(B\) at the midpoint is confined to \(X\).

Then

\[
\boxed{|X|\ge2^{k-1}+1.}
\]

**Proof.** For each arm \(B_j\), define \(G_j=A\cap B_j\cap X\). Successful original temporal information flow requires every original secret \(a\) of \(A\) to reach every original target \(b\) of the reversed suffix arm \(B_j\). Because \(X\) participants inside each \(B_j\) never receive secrets from other \(B\)-arms, for each pair \((a,b)\) their required midpoint carrier belongs to \(G_j\). Therefore every \(G_j\) is nonempty and collectively covers **all \(A\)-secrets at midpoint**. Since \(A\)'s final call has endpoints outside \(X\), this same covering already holds at the end of its earlier chronological spanning tree \(T\). The \(G_j\) are disjoint designated recipient groups of \(T\), with all other \(A\) vertices acting as arbitrary helpers.

Theorem H gives \(|X|\ge2^{k-1}\). If equality held, Theorem H(3) makes **every** \(x\in G_j\) private for an \(A\)-secret within \(G_j\). Exact crossing with *every* reversed \(B_j\) target then forces this \(x\) to know all original secrets of its \(B_j\) arm in reversed local chronology; it is a complete arm collector. But a chronological tree arm has at most two complete collectors, one already its designated outside-\(X\) root. Thus **each** \(G_j\) contains at most one vertex. Equality would imply \(|X|=k\), contradicting \(2^{k-1}>k\) for \(k\ge3\). Hence \(|X|\ge2^{k-1}+1\). QED.

This theorem uses the causal (per-root) sealing of Stage 14, **not** the false globally strict all-arm-before-core premise. Crucially, it does not assume a four-arm decomposition on the \(A\) side.

## 3. New universal necessary conditions within the unrestricted 3×3 family

By Bumby's spine, if the **original** suffix off-corner cell sizes obey

\[
m_{13}=m_{23}=2,
\]

then no participant in \(P_1\cap Q_3\) can be a complete prefix collector of tree \(P_1\), and no participant in \(P_2\cap Q_3\) can be a complete prefix collector of tree \(P_2\): Bumby's spine places the last contacts of these prefix trees across \(Q_1\) and \(Q_2\). The exact two-point crossing lemma therefore forces **both participants** of each size-two cell to be complete **reversed-suffix collectors of the unicyclic \(Q_3\)**. Thus Stage 14's collector decomposition makes \(Q_3\) a **causally sealed four-arm** component, with the four outsiders in \(P_1\cup P_2\).

The last chronological call inside original prefix \(P_3\) joins \(Q_1,Q_2\), hence lies outside \(X=P_3\cap Q_3\), and deleting it leaves a spanning tree (Bumby's Theorem 3, Case II). Apply Theorem C with \(A=P_3\), \(B=Q_3\), \(k=4\) to obtain

\[
\boxed{m_{13}=m_{23}=2\quad\Longrightarrow\quad m_{33}\ge9.}
\]

Reverse the original schedule for the symmetric implication:

\[
\boxed{m_{31}=m_{32}=2\quad\Longrightarrow\quad m_{33}\ge9.}
\]

**Immediate finite-size consequence:** Every corner cell is positive, and the two other off-corner cells are at least two by Bumby's first/last-contact spine. Therefore either one-sided size-two-pair condition already forces

\[
n=\sum_{i,j}m_{ij}\ge 4\text{ (corners)}+4\text{ (specified pair)}
 +4\text{ (opposite pair)}+9\text{ (center)}=21.
\]

Hence **for \(n=18,19,20\)**, any hypothetical both-cyclic original split must have *at least one entry of size at least three in EACH off-corner pair*, not merely in one. This is an all-n necessary restriction, **not** a certificate that the \(n=18,19,20\) cases are impossible.

Both statements require a **hypothetical successful both-cyclic original half-schedule** and make *no* assumptions on the remaining two off-corner sizes or on the four positive corner cell sizes. They are significantly broader than, but numerically weaker than, Stage 14's simultaneous size-two-pairs consequence \(m_{33}\ge64\).

**Check of cell indexing:** \(m_{13},m_{23}\) belong to suffix unicyclic column \(Q_3\), and \(m_{31},m_{32}\) belong to prefix unicyclic row \(P_3\). The precise outside-root argument is copied only with this orientation, avoiding any swap of original and reversed chronology.

## 4. Boundary: the unsaturated local tree-cover model can have only eight recipients

The weaker \(|X|\ge 2^{4-1}=8\) **without cross-arm private-secret compatibility** is sharp even if the last unicyclic call is outside \(X\). Start with the Stage 11 sharp eight-vertex chronological tree-cover of four recipient groups (group sizes 1,1,2,4). Introduce four unassigned outsider leaves, each with an early call to one designated vertex **before** any of the original tree contacts. Their secrets piggyback on this vertex's original secret, so every group still collectively covers all twelve secrets. Add a final distinct outsider-to-outsider contact forming one static cycle, with both endpoints outside \(X\). The designated recipients remain eight.

[Independent construction and assertions](equality_helper_probe.py) replay this precise 12-contact, 12-vertex unicyclic local chronology. This local object is **not a globally successful 3×3 two-half scheme**. It explains why the improved **nine** lower bound specifically requires the opposing causally sealed tree arms and private-secret contradiction, rather than only the one-sided temporal cover.

The same checker exhaustively enumerates **all** labelled chronological trees on \(n=2,3,4,5\), all tight 2/3-group assignments (including unassigned helpers), and independently tests private-secret, singleton-group and full-collector equality claims. It also constructs sharp helper-ending tree splits with \(2^s\) designated recipients for \(s=2,\ldots,6\), confirming an auxiliary exact last-edge count. These finite tests are falsifiers; the induction above supplies the all-n proof.

## 5. Open frontier and truth gate

The universal both-cyclic original-half conjecture remains **OPEN**. At least one off-corner pair may have entries larger than two, and Theorem C by itself cannot exclude it. The one-sided bound \(m_{33}\ge9\) does **not** supersede the stronger \(m_{33}\ge64\) when *both* pairs equal two. No theorem for arbitrary positive 3×3 entries, no global counterexample and no priority or formal proof-assistant certificate are claimed. PR #1 DRAFT/UNMERGED; publication HOLD.
