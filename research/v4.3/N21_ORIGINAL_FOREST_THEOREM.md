# Stage 26 — Original chronological half-forest at n=21

**28 October 2026. Complete HUMAN proof for n=21, conditional on the explicitly cited Bumby 1981 theorem, all-n information-flow/tree-cover lemmas and independently exhaustive small chronological-tree facts. The original chronological half-forest conjecture for all n≥22 is OPEN. No Lean/Coq or external referee/novelty verification. PR #1 stays DRAFT/UNMERGED.**

## The statement and historical reduction

**Theorem 26.1.** In every shortest successful bidirectional telephone-gossip schedule on **21 participants**, with **38 pairwise distinct telephone calls**, the **ORIGINAL first 19 calls OR the ORIGINAL last 19 calls** form an acyclic contact graph (a forest). This asserts nothing about a reordered schedule.

Suppose otherwise. By Richard T. Bumby's *A Problem with Telephones*, SIAM Journal on Algebraic and Discrete Methods **2** (1981) 13–18, Theorem 3 and proof, the original prefix component graphs are two closed trees \(P_1,P_2\) and one unicyclic component \(P_3\); the fully reversed original suffix components are two closed trees \(Q_1,Q_2\) and one unicyclic component \(Q_3\). Every cell \(C_{ij}=P_i\cap Q_j\) is nonempty. All four off-corner cells \(C_{13},C_{23},C_{31},C_{32}\) have at least two people. The last original prefix call of any \(P_i\) joins \(Q_1,Q_2\), and the first original suffix call of any \(Q_j\) joins \(P_1,P_2\). On either unicyclic component, this specific last chronological local call lies on the unique static cycle, and deleting it leaves the preceding chronological spanning tree. [Primary source audit](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md).

Write \(m_{ij}=|C_{ij}|\), \(X=C_{33}\). Original prefix source/reverse suffix target supports obey exact intersection \(A_a\cap B_b\ne\varnothing\) for EVERY source-target pair, cell by cell. This is the fixed chronological truth condition; it does not authorize exchanging events.

## Dependency A — independent exhaustive n21 incidence reduction

[Stage25 precise quantified filters](N21_CONSERVATIVE_77_PROFILE_FRONTIER.md) and [n20/n21 independent enumerator](n21_staged_frontier.py) enumerate all \(\binom{16}{8}=12,870\) labelled \(3\times3\) positive incidence matrices with four off-corners at least two. They only discard matrices when a *proved necessary* condition fails. The early filters are:

1. Both cyclic components have ≥9 people, proved for globally successful original both-cyclic schedules in [Stage18 global eight-person exclusion](../v3.5/FOUR_LEAF_STAR_GLOBAL_EIGHT_EXCLUSION.md): 12,870→1,200.
2. An off-corner \((2,2)\) pair would force \(n\ge43\) by the [all-n six-group exact chronological tree-cover theorem](../v3.5/SIX_GROUP_35_PERSON_OBSTRUCTION.md), so neither pair may be (2,2): 1,200→850.
3. Use **ONLY** exact previously exhaustively checked privacy lower bounds for the 16 chronological three-group TREE types of size at most seven, with all unenumerated larger types assigned **ZERO** (no unsupported extrapolation). Four full OUTSIDE-center collectors in either unicyclic component would force \(|X|\ge9\) by the helper-tolerant causal four-arm crossing, so discard: 850→321.
4. If each cyclic component has one exterior cell A≤3 with at least two forced full collectors and another cell B≤6 with at least one forced full collector, then Stage23/24 show it has **exactly three full collectors, all outside X**. Their joint absence of center full collectors implies both chronological cyclic center supports are twice-covered. Stage23's two-outside-root chronological spanning-tree lemma forces \(|X|\ge6\), contrary to each candidate's \(|X|\le5\). Discard: 321→137.
5. A singleton X must be complete in BOTH local cyclic components, so cannot coexist with even one Stage23/24-qualified three-outside-root component. For \(|X|=2\), if one component has no complete center collector, exact **two-point crossing** forces both central people to be complete collectors on the OPPOSITE component; [Stage25 generalized center-root-cut theorem](../v3.7/CENTER_PRIVATE_ROOT_CUT_TEN_OUTSIDERS.md) forces the opposite off-corner sizes to total ≥10. Discard: 137→77.

These gates all hold only for the ORIGINAL contact order and its total reverse, never for an optimized rearrangement. Independently count the first two gates using aggregated excess occupancy \(p,q,d\) and stars-and-bars coefficient \((p+1)(q+1)\binom{8-p-q-d+3}{3}\); the result exactly matches 1,200 and 850. Rerunning on n20 reproduces previously published-in-repository Stage21 exact 221→52 privacy count and Stage23 final zero.

### Lemma 26.2 — a size-two exterior cell plus a full center forces forbidden four-root occupancy

Consider either unicyclic original/reversed local component \(U\) of a hypothetical successful both-cyclic schedule. Let its outside-center cells be \(A,B\), with \(|A|=2\), \(|B|\le6\). Suppose **at least one complete U collector lies in X**.

Stage17's **exact original-order double-carrier** condition forces BOTH A residents to be complete U collectors at local termination. Let \(a\in A,b\in B\) be endpoints of U's actual last on-cycle contact, and \(a'\in A\setminus\{a\}\). The center collector \(x\) and untouched \(a'\) were already complete before this final call, i.e. at the end of U's preceding spanning tree \(T\). A chronological tree first acquires complete collectors only at its last call and has at most two, so \(x,a'\) are its **only** complete tree collectors; in particular \(a\) is not yet complete in T.

Yet \(a\) becomes complete at the final bidirectional \(ab\) contact. Since both endpoints finish with IDENTICAL knowledge, \(b\) also becomes complete. U therefore has exactly FOUR complete collectors \(a,a',b,x\), distributed **two in A, exactly one in B, exactly one in X**. By Stage14, a four-full-collector U admits four original-order CAUSALLY sealed tree arms rooted at those persons. Since every U-secret has at least two carriers in B and exactly one B root is complete there, Stage24's **all-n three-star occupancy theorem** requires \(|B|\ge2·4-1=7\), contrary to \(|B|\le6\). QED.

**Corollary:** Whenever one of the two U off-corner cells has size 2 and the other has size ≤6, **U has no complete central collector whatsoever**. This holds for ALL n under the stated original globally successful both-cyclic hypothesis, not just n21. This strengthens the earlier Stage25 root-cut numerical test.

### Lemma 26.3 — the three small-center contradictions

Use Lemma 26.2 on any side satisfying the off-corner size condition \((2,\le6)\).

- **Center size one:** Its sole participant must be a full collector in both cyclic components by all-pairs midpoint crossing. If either component has an off-corner size-two cell with other size ≤6, Lemma 26.2 contradicts this.
- **Center size two:** If **both** unicyclic components satisfy that off-corner condition, neither can have a complete center collector. The exact two-person crossing lemma (Stage11) says any two-point family of nonempty prefix source supports and reversed suffix target supports that intersect for **all pairs** must have a complete central collector on at least one side (in fact both on one side or a common collector). Contradiction.
- **Center size three:** Suppose Q3 satisfies the Stage23/24 qualified *three-complete-outsiders* condition, so Q3 has **no** complete center collector. Then every original \(P_3\) secret must have **at least two** of the three center carriers, because a singleton P3 support would force a complete reversed-Q3 center collector. The final original P3 on-cycle contact is outside X, hence these same three participants doubly cover every P3 secret already in P3's earlier chronological spanning tree T. The [Stage19 exact three-person tree double-cover lemma](../v3.6/CENTRAL_PRIVATE_CAPACITY.md) forces at least ONE of them to be a complete collector of T, and hence P3 has a complete center collector. If P3's own exterior cells have sizes (2,≤6), Lemma 26.2 forbids this. Swap roles for the other direction.

Applying these precisely quantified gates to the 77 Stage25 matrices independently excludes **8** with a single center person, **4** with two center people, and **40** with three center people (20 per orientation). There remain **25 labelled matrices in eight row/column-swap symmetry orbits**. Every exclusion is an all-n human implication, not a new computational axiom.

### Lemma 26.4 — dual absence of full center collectors excludes twenty more

If **both** unicyclic P3 and reverse-Q3 have \((2,\le6)\) exterior cell pairs and the center \(|X|<6\), Lemma 26.2 leaves NO complete central collector on EITHER side.

Then no original P3 secret can have singleton center support (else the supporting center point would be a complete reversed-Q3 collector), so **each** P3 secret has ≥2 carriers in X. The original P3 final unicyclic call touches no center point, so its preceding chronological spanning tree \(T_P\) has the same two-fold X coverage.

Because one P3 exterior cell has exactly two people, both are complete at terminal P3 by Stage17. One of them is UNTOUCHED by the final P3 on-cycle call; hence it was already a complete collector at \(T_P\). A tree with one complete collector has **two**: the endpoints of its last chronological call. Neither can be in X, since no P3 center participant is complete at terminal time. Therefore \(T_P\) has **TWO complete collectors outside X** and **every original P3 secret known by at least two people in X**.

The [Stage13 all-n two-outside-complete-roots double-cover tree lemma](../v3.0/CENTER_SATURATION_THEOREM.md) gives \(|X|\ge6\): remove the last tree edge between the two full outsiders; each independent side has its own complete outside root and requires at least three double-cover X recipients. Contradiction to \(|X|<6\).

This excludes **20 more labelled matrices** among the 25, all with center three or four, leaving **five labelled matrices in three orbits**.

### Lemma 26.5 — four \((2,4,3)\) matrices are historically excluded by our Stage22 three-star theorem

Four of the five remaining matrices have a unicyclic component with exterior sizes \((2,4)\) and center size 3. The exact adjacent chronological tree privacy minima (especially \((1,1,2)\mapsto2\) and \((1,1,4)\mapsto1\)) force **both** size-two residents and at least one size-four resident to be complete original/reverse U collectors.

[Stage22 all-n conditional \((2,4,3)\) exclusion](../v3.9/N20_THREE_STAR_FRONTIER.md) proves that a globally successful both-cyclic ORIGINAL chronology with these exact collector hypotheses is IMPOSSIBLE. Its proof either rules out four collectors by the causal four-arm obstruction or rules out three by a **three-leaf support star** incompatible with the adjacent original chronological tree whose last call lies outside the size-four cell. No new finite oracle assumption is introduced.

Thus **only one labelled matrix remains**, invariant under tree-row/tree-column swaps:

\[
\boxed{M=\begin{pmatrix}
1&1&4\\
1&1&4\\
4&4&1
\end{pmatrix}.}
\]

### Lemma 26.6 — exact last \((4,4,1)\) unicyclic pattern is impossible with one complete exterior collector per side

Consider a unicyclic local component U of the ORIGINAL hypothetical both-cyclic fixed split with three disjoint cell groups \(A,B,X\), with

\[
|A|=4,\qquad |B|=4,\qquad X=\{x\}.
\]

Suppose the global original chronology succeeds and **at least one person in A and one in B are complete U collectors**. This hypothesis is forced in the final matrix by the adjacent original TREE private-recipient minimum for **(1,1,4)**: every fully covering chronological such tree with its last edge across its two singleton corner groups has at least one private off-corner recipient, who becomes a complete collector of U by exact midpoint crossing (Stage21). The central singleton x is independently COMPLETE for U: success from every source to every target in the other cyclic component must cross X={x}.

**Step 1: U has exactly THREE complete terminal collectors, one each in A,B,X.** U has at least these three and at most four. Suppose it had four. Since only one person belongs to X, the four are distributed (2,1,1) among A,B,X in some order: two in one exterior group and one in the other, plus x. The four-collector causal-arm decomposition holds in the ORIGINAL local chronology (Stage14). Its opposite exterior cell has exactly ONE complete root and size 4, and all its original U secrets must have at least TWO carriers there by Stage17. Stage24's all-n three-star occupancy theorem forces that singly rooted exterior cell to have size **at least 7**. Contradiction. Hence exactly three complete collectors exist, call them \(a\in A,b\in B,x\in X\).

**Step 2: The last two original local contacts split the preceding spanning tree into two exactly tight tree-cover instances.** U's actual last call, say \(e=a_0b_0\), lies on its static cycle and joins A to B, outside X, by Bumby's chronological spine. Its \(v-1=8\) preceding distinct calls form a spanning chronological tree \(T\).

Since x is complete at the end of U and e does not touch x, x is already complete at the end of T. A chronological tree has at most two complete collectors, who first appear at its last contact. U has three terminal complete collectors, so e MUST create at least one new complete collector. Both endpoints of a bidirectional call leave with identical knowledge; therefore **both e endpoints are terminal complete**. They must be the unique exterior terminal collectors \(a,b\), hence e=ab.

Precisely ONE of a,b was already complete in T, alongside x. Write that previously complete exterior person as \(t\in\{a,b\}\). The LAST chronological tree contact in T is necessarily **xt** (the only possible two full T collectors are the last-call endpoints); its deletion splits the first seven chronological calls into disjoint tree histories \(U_x\ni x\) and \(U_t\ni t\). Immediately before xt, x knows every original U_x secret, t knows every original U_t secret.

Let \(H_A=A\setminus\{a\}\), \(H_B=B\setminus\{b\}\). Both have size 3. By Stage17's universal double-carrier condition and because e touched only a,b, **H_A and H_B each individually collectively cover EVERY U secret already at the end of T**. Moreover neither H group participates in xt (its endpoints x,t are excluded). Thus, for each side W∈{U_x,U_t}, the three disjoint recipient groups
\(\{\text{full side root }r_W\},H_A\cap W,H_B\cap W\)
are nonempty and individually collectively cover EVERY original W-secret.

The all-n exact helper-robust tree-cover theorem (Stage11) for THREE complete-cover groups gives ≥\(2^{3-1}=4\) designated recipients on EACH side. Across the two sides, the designated vertices are exactly the eight people \(x,t\) and all six members of \(H_A,H_B\), so total recipient count is EXACTLY 8. Therefore **both** tree-cover subinstances attain exact equality. By the [Stage15 equality theorem, valid even with unassigned helper vertices](../v3.2/HELPER_EQUALITY_AND_ONE_SIDED.md), **every** designated recipient is private within their own recipient group in their side tree.

**Step 3: Three distinct B private support pairs are forced.** In each of the two tree subinstances, every \(z\in H_B\cap W\) owns some original W-secret \(\sigma_z\) which is known by no other member of \(H_B\cap W\). Members of \(H_B\) in the opposite W-side never receive W-secrets at the contact xt, since only x,t are endpoints, and nobody in H_B participates in the final unicyclic e=ab either. Thus \(\sigma_z\) is private within the **entire THREE-person H_B group** in the final U chronology. These three \(\sigma_z\), indexed by distinct z, are themselves distinct (otherwise one secret could not be private to two people).

The final B endpoint b is a COMPLETE terminal U collector, so each \(\sigma_z\) is held within B=H_B∪{b} **exactly by the two people \(\{b,z\}\)**. Label the three distinct H_B members \(z_1,z_2,z_3\); then the exact fixed-original-midpoint reverse-target support sets in the B intersection cell contain three **distinct TWO-point STAR leaves**

\[
\{b,z_1\},\quad\{b,z_2\},\quad\{b,z_3\}.
\]

**Step 4: contradiction with the ACTUAL opposite chronological tree.** If U is the reversed-suffix Q3 and B is one of its prefix-tree row cells, the adjacent ORIGINAL prefix tree P_i has its ACTUAL last contact joining suffix-tree columns Q1,Q2, and hence both last endpoints are outside B⊂Q3. Its original secrets must each intersect ALL three reverse-Q3 support pairs above, by exact source-target midpoint compatibility. But the [Stage20 all-n tree-versus-three-star lemma](../v3.7/N19_ORIGINAL_CHRONOLOGY_THEOREM.md) proves this impossible: delete the actual last P_i tree contact, splitting earlier chronological information into two tree sides. Place b in one side. To reach the other side's original secrets, each distinct z_i would have to become a COMPLETE collector of that opposite tree side. A chronological tree with each edge contacted once has at most TWO complete collectors. Three is impossible.

Time reversal gives the same contradiction if U=P3 rather than reversed Q3. **Therefore no globally successful hypothetical original both-cyclic chronology contains this (4,4,1) unicyclic pattern with one complete exterior collector per side.** QED.

The exact six-person chronological P_i tree of the final n21 incidence case has group sizes (1,1,4) and a last contact outside B. [Stage20 independent exhaustive three-star chronology checker](../v3.7/exact_three_leaf_star.py) tests every fixed-last-edge labelled six-person tree order (10,368 histories, 1,728 complete group covers), and reports ZERO compatible three-star crossings. This corroborates but does not substitute for the all-n original-order proof.

## Theorem 26.7 — original n21 fixed-half forest

Returning to the hypothetical shortest successful 38-contact n21 schedule with BOTH original 19-contact halves cyclic, the initial source-grounded Bumby classification plus **complete exact labelled incidence enumeration** and successive proved original-order necessary conditions reduce 12,870 matrices through 1,200, 850, 321, 137, 77, 25 and 5 to the four \((2,4,3)\) cases and one \((4,4,1)\) case. Lemmas 26.5–26.6 exclude the final five. **Zero necessary incidence matrices remain.**

Therefore our initial both-cyclic assumption contradicts a combination of individually human-checkable all-n contact-order lemmas and exhaustively checked small-tree facts. Hence every successful shortest DISTINCT-contact bidirectional gossip schedule on n=21 has a FOREST among its **ORIGINAL first 19 calls or its ORIGINAL last 19 calls**. QED.

## Computational proof obligations and independent assurance

- [Initial independently parameterized n20/n21 9-cell census and 77-profile bound](n21_staged_frontier.py) enumerates all \(\binom{16}{8}=12,870\) labelled n21 positive matrices and separately verifies first two reductions with exact stars-and-bars enumeration, while rechecking n20 closure.
- [Final staged original n21 zero-survivor enumerator](n21_final.py) applies the all-n Stage24 center-occupancy lemma, Stage19 tree-three-person doublecover, Stage13 two-outside-root doublecover and Stage22 universal \((2,4,3)\) three-star exclusion to finish 77→0. It is an incidence necessary-condition checker, **not** exhaustive enumeration of 38-call gossip histories.
- [Independent Stage20 original six-person three-star tree checker](../v3.7/exact_three_leaf_star.py), [Stage21 original chronological privacy histograms](../v3.8/exact_seven_tree_privacy.cpp), and [Stage24 occupancy enumerator](../v4.1/check_three_star_occupancy.py) are independent regressions.
- The new Stage26 GitHub Actions workflow executes all above separate programs and refuses to report success until their assertions pass. These are computational checks of the finite inputs and local lemmas; the all-n logical implications rest on the displayed mathematical proofs, NOT on CI or an unverified solver.

**Research truth/priority ledger:** fixed-original-half forest proved by human arguments and computational finite support through n=21; universal all-n n≥22 OPEN; no genuine globally successful both-cyclic counterexample; no Lean/Coq machine formalization; no independent peer review or historical novelty certificate. PR #1 remains DRAFT/OPEN/UNMERGED; manuscript publication HOLD.
