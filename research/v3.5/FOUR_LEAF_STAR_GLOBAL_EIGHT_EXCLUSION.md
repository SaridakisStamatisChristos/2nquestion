# Stage 18 — The four-leaf star obstruction closes the eight-person *global* loophole

**28 October 2026. New complete all-\(n\) conditional original-midpoint theorem: in any hypothetical successful both-cyclic fixed original half-schedule, BOTH unicyclic midpoint components have at least NINE participants.** This is **NOT** the unrestricted original-half forest conjecture. It uses an additional **global tree-versus-cycle crossing argument** missing from the earlier provisional Stage 17 local classification. PR #1 must remain DRAFT, OPEN, UNMERGED; publication HOLD; external referee/formal assistant not claimed.

## 1. Chronological contract and the adversarially discovered pitfall

The exact target is every successful sequence of \(2n-4\) pairwise-distinct bidirectional calls, with a forest in at least one of its **fixed original first/last \(n-2\)** calls. No permissible reordering substitutes for the original chronology.

Richard T. Bumby, *A Problem with Telephones*, SIAM J. Algebraic Discrete Methods **2** (1981), 13–18, Theorem 3 and case-II proof, confines a hypothetical both-cyclic original cut to \(P_1,P_2\) closed prefix trees, \(P_3\) unicyclic, and \(Q_1,Q_2\) closed reversed-suffix trees, \(Q_3\) unicyclic. Its first/last-contact spine says last original prefix call inside every \(P_i\) joins suffix tree columns \(Q_1,Q_2\), and last REVERSED suffix call inside every \(Q_j\) joins prefix tree rows \(P_1,P_2\). See [Bumby source audit](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md).

Stage 16 established **two distinct midpoint carriers** for every unicyclic secret in each off-corner tree-side cell, plus at least one carrier in center \(X=P_3\cap Q_3\), and exhaustively excluded unicyclic components smaller than 8.

An initial Stage 17 proof **incorrectly** claimed only the local eight-person pattern \((2,2,4)\) could occur; the omitted local pattern \((2,5,1)\) is a genuine local chronology. Stage 17 explicitly repaired the six-triple exact enumeration and withdrew its premature all-\(n\) size-nine assertion. **This stage proves the size-nine assertion for a DIFFERENT, logically sufficient reason**: the second local pattern cannot be glued to the mandatory adjacent original tree. Do not suppress this falsification history.

## 2. Lemma — chronological tree cannot cross a four-leaf star (ALL n)

Let \(T\) be a chronological connected tree with each edge called once, and let \(S=\{y,z_1,\ldots,z_r\}\) be \(r+1\) distinct designated participants **not** including the endpoints \(u,v\) of its last contact \(uv\). Suppose \(S\) collectively covers every original \(T\)-secret after the tree chronology.

Suppose another component's reversed-time target supports inside this same midpoint cell \(S\) contain, for each \(i=1,\ldots,r\), a distinct original target \(b_i\) whose support is **exactly** \(\{y,z_i\}\). Full original gossip would require, for each source \(a\) of \(T\), its midpoint carrier support in \(S\) to meet every pair \(\{y,z_i\}\).

**Claim:** this is **impossible whenever \(r\ge3\)**.

**Proof.** Remove the LAST original tree edge \(uv\), leaving subtrees \(U,V\) and all earlier calls internally confined to them. Since \(u,v\notin S\), no member of \(S\) receives information across \(U,V\) at the final call. Since \(S\) collectively knows every secret, both \(S\cap U\) and \(S\cap V\) are nonempty. Assume \(y\in U\). Choose an original secret \(a\) originating in \(V\). No member of \(S\cap U\), including \(y\), knows \(a\). For EVERY target support \(\{y,z_i\}\) to meet the source carrier set, **each** \(z_i\) must know \(a\), hence every \(z_i\in V\). The same reasoning works for **every** original \(V\)-secret \(a\), so all \(r\ge3\) distinct people \(z_i\) are complete collectors of the **chronological tree \(V\)**. But a connected tree with its \(|V|-1\) edges each called once can have at most TWO complete collectors (only the endpoints of its last internal contact can become complete). Contradiction. QED.

Note that the proof does **not** assume \(u,v\) are full tree collectors, that every tree arm ends before all root links, or that participants may be reordered. The exact binary crossing condition is necessary because all source-target temporal paths cross the original midpoint.

## 3. Lemma — an eight-person local \((2,5,1)\) cycle forces this star (ALL chronological local histories)

Consider a connected eight-person unicyclic component \(C\) with eight distinct chronological calls, the **last** edge closing its unique cycle between two disjoint recipient groups \(A,B\), and a three-group partition
\[
|A|=2,\qquad |B|=5,\qquad |D|=1.
\]
Suppose **every** original \(C\)-secret has at least two terminal carriers in each of \(A\) and \(B\), and at least one in \(D\).

Write \(A=\{a_0,a_1\}\), \(D=\{x\}\). The two \(A\) members must individually know **all eight** secrets, as each secret has TWO \(A\)-carriers. The singleton \(x\) must also know all eight. Thus at least THREE terminal complete collectors exist.

Before the eighth call at most two collectors can be complete: at least seven distinct edges are required before even one collector can know all eight secrets, and a single contact makes at most two newly complete. The final contact joins \(A\) to \(B\), not \(x\). Hence \(x\) and the \(A\)-member **not** participating in the final contact are the two complete collectors just before the last edge. The other \(A\)-member must become complete *at* the last call, so its partner \(y\in B\) becomes complete at the same moment. We have **exactly four** complete terminal collectors: \(a_0,a_1,x,y\), with ONE in the five-person group \(B\).

Apply Stage 14's **causally sealed four-arm decomposition** to this original local chronology. All four complete collectors serve as four arm roots, and the other four participants of \(B\), call them \(z_1,\ldots,z_4\), are the **only** non-root vertices anywhere in \(C\).

Every original secret has at least two \(B\)-carriers. Since \(y\) is already a complete \(B\)-collector, for a secret originating in each arm there must be **another** \(B\)-carrier in that arm. Causal sealing prevents a non-root from receiving secrets from other arms. Therefore *each* of the four arms contains at least one of \(z_1,\ldots,z_4\), hence exactly one. Each arm is a root–nonroot pair; no nonroot ever learns another arm's secret. For each \(z_i\), consider its own original secret as a reverse-time target support. Among the five members of \(B\), this secret is known by exactly \(z_i\) and the complete root \(y\):

\[
\boxed{\forall i=1,\ldots,4,\qquad\mathrm{Supp}_{B}(z_i)=\{y,z_i\}.}
\]

This is **the four-leaf star**. The conclusion is based on exact chronology and complete collector rigidity, not heuristic support generation. The [independent eight-person C++ enumeration](../v3.4/exact_eight_group_orbits.cpp) also checks this four-full-collector and four support-pair assertion for **every** locally compatible \((2,5,1)\) candidate (160 representative chronological orders).

## 4. Universal all-n theorem — neither original unicyclic component can have size eight

**Theorem 18.1 (ALL n, proved, conditional on a hypothetical both-cyclic original schedule).** If BOTH fixed original chronological halves are cyclic in a successful shortest pairwise-distinct telephone gossip schedule, then

\[
\boxed{
|P_3|=m_{31}+m_{32}+m_{33}\ge9,\qquad
|Q_3|=m_{13}+m_{23}+m_{33}\ge9.
}
\]

**Proof.** Stage 16 established both component sizes at least 8. Suppose the reversed-suffix unicyclic component \(Q_3\) has size exactly 8. The exact complete Stage 17 six-pattern classification says its only possible off-corner/center size triples, up to exchanging \(P_1,P_2\), are **\((2,2,4)\)** or **\((2,5,1)\)**.

The \((2,2,4)\) pattern is excluded by Stage 15: when the two off-corner cells \(m_{13}=m_{23}=2\), success requires center \(m_{33}\ge9\), contradicting 4.

For the \((2,5,1)\) pattern, relabel \(A=P_1\cap Q_3\) (size two), \(B=P_2\cap Q_3\) (size five), \(D=P_3\cap Q_3\) (singleton). The reversed chronology of \(Q_3\) meets Lemma 3 and forces within \(B\) four reverse-target support pairs \(\{y,z_i\}\). The ORIGINAL prefix tree \(P_2\) has its last contact joining \(Q_1\) and \(Q_2\) by Bumby's **actual** last-prefix-contact spine. Its last endpoints therefore lie **outside** \(B=P_2\cap Q_3\). Full gossip implies \(B\) collectively covers every original \(P_2\)-secret and every original \(P_2\) source must cross each of the four reverse-target support pairs inside \(B\). The all-n tree-versus-star Lemma 2 forbids this. Contradiction.

Thus \(|Q_3|\ne8\) and \(|Q_3|\ge9\). Apply the **exact time-reversed** argument to exclude \(|P_3|=8\), obtaining both inequalities. QED.

**The lower bound of 9 is now genuinely universal in the hypothetical both-cyclic setting.** This is NOT inferred solely from the finite local eight-person classification (which has a real \((2,5,1)\) survivor); it additionally uses the global, mandatory crossing of a prefix TREE.

## 5. Verified finite frontier: \(n=18\) theorem, \(n=19\) reduction

Use baseline matrix \(M_0=[[1,1,2],[1,1,2],[2,2,1]]\) and extras
\[
p=(m_{13}-2)+(m_{23}-2),\quad
q=(m_{31}-2)+(m_{32}-2),\quad d=m_{33}-1,\quad
r=n-13-p-q-d.
\]

The new all-n inequalities are \(p+d\ge4\), \(q+d\ge4\). Retain the older Stage 15 one-sided center condition \((p=0\text{ or }q=0)\implies d\ge8\) and Stage 14 simultaneous condition \((p=q=0)\implies d\ge63\). Exact labelled necessary-incidence matrices are counted by
\[
\boxed{
N_{18}(n)=
\sum_{\substack{p,q,d\ge0,\ p+q+d\le n-13\\
p+d\ge4,\ q+d\ge4\\
(p=0\lor q=0)\Rightarrow d\ge8\\
(p=q=0)\Rightarrow d\ge63}}
(p+1)(q+1)\binom{n-13-p-q-d+3}{3}.
}
\]

| \(n\) | Stage 15 necessary incidence survivors | Stage 16B local ≥8 survivors | Stage 18 **new all-n** size-filter survivors |
|---|---:|---:|---:|
| 18 | 489 | 41 | **4** |
| 19 | 1,365 | 221 | **41** |
| 20 | 3,333 | 825 | **221** |
| 21 | 7,359 | 2,438 | **850** |
| 24 | 52,293 | 28,205 | **15,517** |

The four surviving \(n=18\) labelled matrices are all the ONE orbit of \(M=[[1,1,2],[1,1,3],[2,3,4]]\). Stage 17B's [five-person privacy proof](../v3.4/N18_ORIGINAL_CHRONOLOGY_THEOREM.md) eliminates this final orbit by forcing four **outside-center** complete collectors in both unicyclic halves, giving \(m_{33}\ge64\) versus \(m_{33}=4\). Thus **the original half-forest conjecture is proved at n=18**, dependent on the explicit human and finite-exhaustive lemmas. This finite result does NOT settle arbitrary n.

The four center-singleton profiles at \(n=19\) are now also excluded as a special case of Theorem 18.1; only 41 labelled size-necessary profiles remain. These are **NOT** completed original gossip schedules or symmetry orbits.

## 6. Independent computational falsification and limitations

[exact_tree_star_crossing.cpp](exact_tree_star_crossing.cpp) independently enumerates every labelled seven-person chronological tree whose last edge joins the two fixed corner roots, checks that these roots individually know all original local secrets and that five other group members collectively cover them, and directly tests all four \(\{y,z_i\}\) crossing constraints:

- 4,802 labelled trees with the prescribed last corner-root edge;
- 576,240 complete original chronological orderings of such trees;
- **57,600** satisfying the singleton-root and five-person collective-cover conditions;
- **zero** satisfying all four star-crossing target pairs.

This exact finite test independently corroborates, but does NOT replace, the all-n last-edge proof. The Stage 17B [eight-person exhaustive verifier](../v3.4/exact_eight_group_orbits.cpp) additionally asserts four terminal full collectors and the four pair supports in every locally compatible \((2,5,1)\) history; older software paths are not used as the oracle.

**Assurance and status:** The all-n **necessary** size-nine theorem has a complete human proof with explicit Bumby 1981, Stage 14 and Stage 15 prerequisites, and finite local exclusion evidence. It has no formal proof assistant certification and no independent refereeing or historic novelty certificate. The unrestricted all-n **chronological half-forest conjecture remains OPEN**. PR #1 remains DRAFT / UNMERGED. Next high-value task: exploit extra corner-tree privacy/poset constraints against the remaining \(n=19\) 41 necessary matrices, without mistaking a relaxed incidence matrix for a schedule.
