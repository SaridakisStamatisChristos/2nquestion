# Stage 22 — Universal conditional \((2,4,3)\) three-star exclusion; \(n=20\) reduced to 5 incidence orbits

**28 October 2026. New ALL-\(n\) necessary incompatibility with explicit collector hypotheses; new \(n=20\) exact incidence filter.** This does NOT complete the universal half-forest conjecture, nor the \(n=20\) case. Keep PR #1 DRAFT, OPEN and UNMERGED; publication HOLD.

## 1. Contract and precise hypotheses

Work with the **original fixed** shortest successful \(2n-4\)-call bidirectional chronology of distinct pairs; do not reorder events. By Bumby's 1981 Theorem 3, any both-cyclic midpoint is a 3×3 grid with original prefix \(P_1,P_2\) closed trees, \(P_3\) unicyclic, and reversed suffix \(Q_1,Q_2\) closed trees, \(Q_3\) unicyclic; the fixed last contact of each prefix component and the reverse-last contact of each suffix component join the opposite pair of tree components.

Let \(X=P_3\cap Q_3\). Suppose for one of the two unicyclic components, say the **reverse-time** Q3, its three cell groups satisfy
\[
A=P_1\cap Q_3,\ |A|=2;\qquad
B=P_2\cap Q_3,\ |B|=4;\qquad
C=P_3\cap Q_3,\ |C|=3,
\]
and the **two A members** are complete collectors of all Q3 reverse-time original secrets, while **at least one B member** is a complete Q3 reverse-time collector.

Stage 16's original chronology argument ensures every Q3 secret has at least two terminal B carriers and at least one C carrier. Bumby's spine ensures the final Q3 reverse call connects A to B, closes the unique cycle, and that the adjacent prefix P2 tree has its original final edge OUTSIDE B, joining the singleton or larger \(Q_1\)/\(Q_2\) corner groups.

### Theorem 22.1 (ALL n, proved under the explicit A/B collector hypotheses)

**Such a globally successful both-cyclic original chronology is IMPOSSIBLE.** The same holds when interchanging A,B, or under full time reversal for P3 instead of Q3.

This is exactly the [Stage 20 n19 three-leaf-star proof](../v3.7/N19_ORIGINAL_CHRONOLOGY_THEOREM.md), but note which assumptions it uses: it does **NOT** depend on the sizes of the other corner cells, the size of the adjacent original P2 tree, or on \(n=19\). Its only use of the adjacent tree is that its **last original contact has endpoints outside B**, it collectively covers all its secrets within B, and the chronological tree-versus-star lemma applies.

**Full proof without an \(n=19\)-specific step:**

1. The unicyclic Q3 component has \(2+4+3=9\) participants and nine distinct calls. It has at least 3 full reverse collectors, two in A and one in B; it can have at most four.
2. If four full collectors, either (a) both A2 and two B roots are full, so all four roots lie OUTSIDE X. Stage 20's explicitly proven **helper-tolerant** four-arm one-sided crossing forces \(|X|\ge9\), contrary to \(|X|=3\); OR (b) the roots comprise A2, B1, C1. Four causally sealed rooted arms then require a different B nonroot in EACH of four arms to double-carry each arm root's original secret, but B has only 3 nonroot members. Contradiction.
3. Therefore exactly three terminal full collectors exist. Denote Q3's last reverse contact by \(a_0b_0\) with \(a_0\in A,b_0\in B\), the other complete A vertex \(a_1\). The first eight edges form a chronological spanning tree. Because \(a_1\) is complete before the final call, the two complete collectors of this tree are \(a_1,t\) with \(t\in\{a_0,b_0\}\). The partner \(b_0\) is necessarily the UNIQUE complete B collector after the final bidirectional call.
4. The preceding chronological tree T on nine participants already has FOUR disjoint, collectively complete recipient groups \(\{a_1\},\{t\}, B\setminus\{b_0\},C\), of sizes \((1,1,3,3)\). Two singleton groups contain terminal complete collectors; B minus b0 covers all secrets because every secret has two B carriers and only b0 participates in final call; C covers all and is unchanged. One other vertex among \(a_0,b_0\) is an unassigned helper. The eight designated recipients **exactly attain** the helper-robust four-group tree-cover lower bound \(2^{4-1}=8\). By Stage 15's **private-secret equality rigidity with unused helpers**, each of the three B non-b0 recipients \(z_i\) owns a different private original Q3 secret \(\sigma_i\) within B minus b0.
5. Complete reverse-time B root b0 additionally carries every \(\sigma_i\). Thus within the B crossing cell, the exact reversed-Q3 target support of \(\sigma_i\) is \(\{b_0,z_i\}\), for i=1,2,3. This is the correct support orientation for original-prefix-source to suffix-target compatibility, NOT the transposed matrix.
6. Let P2 be the ORIGINAL chronological prefix tree touching B. Its last edge joins Q1 to Q2 outside B (Bumby's spine). Full gossip requires the four B recipients to collectively cover all original P2 secrets and requires **every** P2 source secret to intersect each of these three Q3 reverse-target star supports at the fixed midpoint. But remove P2's last edge: B participants lie in the two independent pre-last chronological sides; with b0 in one side and every \(\sigma_i\)-pair requiring the other zi, all three distinct zi would need to be complete collectors of the opposite tree side, whereas an edge-once tree has at most TWO complete collectors. Contradiction.

The argument reverses symmetrically for original prefix P3 and reversed-suffix trees Q1/Q2. Therefore any positive 3×3 incidence matrix forcing such collector assumptions in a size-(2,4,3) cyclic row OR column is impossible globally.

**Important scope:** The numerical cell triple (2,4,3) alone, without the “A both complete / B at least one complete” hypotheses, is not asserted universally inconsistent. The collector hypotheses are supplied by exact private-secret tree tests in the \(n=20\) application below.

## 2. \(n=20\): 52 labelled Stage 21 candidate matrices → 20 / 5 orbits

[Stage 21's exact seven-person original chronological tree privacy enumeration](../v3.8/N20_PRIVACY_FRONTIER.md) establishes the complete needed lower bounds on off-corner private recipients for every one of the 52 \(n=20\) necessary-incidence candidates. In particular whenever a candidate cyclic Q3 column has cell sizes (2,4,3), the relevant prefix tree ending in Q3's two-person cell forces **BOTH** A recipients to be full Q3 reverse collectors, and the tree ending in its four-person cell forces **at least ONE** B recipient to be full Q3 reverse collector. These implications follow from private prefix source secrets and exact original-midpoint crossing. The same holds under time reversal for cyclic prefix P3 rows of sizes (2,4,3). Thus Theorem 22.1 excludes EVERY Stage 21 matrix whose cyclic row or column has this triple, regardless of remaining corners.

The independent [nine-cell full enumeration](count_n20_three_star.py) checks all 6435 baseline positive labelled 3×3 matrices at n20, Stage 18's all-n size requirements, Stage 15's one-sided size-two restrictions, Stage 19/21's exact privacy minima, and then the new (2,4,3) conditional theorem. It pins:

| Necessary-condition filter at \(n=20\) | Labelled positive matrices | Tree-row/column symmetry orbits |
|---|---:|---:|
| Stage 18 size requirements | 221 | not computed here |
| Stage 21 exact privacy | 52 | 13 |
| Stage 22 exact three-leaf-star exclusion | **20** | **5** |

All five remaining labelled orbits contain exactly four row/column representatives. Their canonical incidence matrices (each one still *necessary-condition-only*) are:

\[
\begin{aligned}
\begin{pmatrix}1&1&2\\1&1&4\\2&4&4\end{pmatrix},&
\quad
\begin{pmatrix}1&1&2\\1&1&5\\2&5&2\end{pmatrix},\\
\begin{pmatrix}1&1&2\\1&1&5\\3&4&2\end{pmatrix},&
\quad
\begin{pmatrix}1&1&3\\1&1&4\\2&5&2\end{pmatrix},\\
&
\begin{pmatrix}1&1&3\\1&1&4\\3&4&2\end{pmatrix}.
\end{aligned}
\]

The 20 labelled survivors have central sizes m33=2 (16 matrices) or m33=4 (4 matrices). **NO claim of successful global schedule or counterexample is made.**

## 3. Assurance and next bottleneck

This is an all-n conditional *three-star impossibility* with precise original source/target crossing, and an exact finite reduction at n20. It is NOT a proof of universal original chronological half-forest for every n or even n20. The Stage 20 direct original six-person tree/three-star exhaustive checker and local nine-person three-collector construction independently corroborate its mechanism. Small-tree Stage21 enumeration and the new independent n20 matrix count give reproducible finite evidence; no formal assistant / peer review / historical novelty determination has been achieved.

**Next falsifier:** examine the n20 remaining five orbit representatives in actual original chronology. The center size-two cases face the exact two-point crossing trichotomy, while the center-size-four case has positive equality slack. Independently replay any potential full 36-contact witness before elevating it beyond a relaxed incidence profile.

PR #1 DRAFT/UNMERGED, publication HOLD; original all-n half-forest conjecture OPEN.
