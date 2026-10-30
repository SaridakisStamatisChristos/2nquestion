# Stage 16 — universal two-fold off-corner coverage and an exact small local cycle exclusion

**28 October 2026.** The global fixed-original-midpoint half-forest conjecture remains **OPEN**. This stage supplies a new **all-\(n\) structural necessary condition** and a finite-exhaustion-certified local threshold, not a proof of global foresthood. Keep PR #1 **DRAFT / OPEN / UNMERGED**. Historical novelty is unknown.

## Problem and dependencies

Let \(S\) be a successful \(2n-4\)-call bidirectional gossip chronology with **distinct** edges, whose **original unreordered** first and last \(n-2\) calls are both cyclic. By Richard Bumby's 1981 Theorem 3 and case-II spine, the prefix components are two closed trees \(P_1,P_2\) and one unicyclic \(P_3\); the reverse-chronological suffix components are two closed trees \(Q_1,Q_2\) and one unicyclic \(Q_3\). Define \(m_{ij}=|P_i\cap Q_j|\), with all cells positive and all four off-corner cells at least two. See [the source-checked reduction](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md).

The **last original prefix call inside \(P_3\)**, say \(uv\), lies on the cycle and joins \(u\in Q_1\) to \(v\in Q_2\). Removing it leaves a chronological spanning tree on the SAME participants, with \(|P_3|-1\) distinct calls. This is crucial: arbitrary unicyclic chronologies need not have their final edge on the unique static cycle; **Bumby's Case II guarantees it here**.

## Lemma 16.1 — every secret is doubly covered in both tree-column cells (all n)

Let \(A=P_3\cap Q_1\), \(B=P_3\cap Q_2\), \(C=P_3\cap Q_3\). Every original secret originating in \(P_3\) is terminally held by **at least two distinct participants** of \(A\), and by **at least two distinct participants** of \(B\). Every such secret has at least one terminal carrier in \(C\).

**Proof.** Fix a \(P_3\) secret \(a\). Success requires the secret to reach every target participant in the original suffix component \(Q_1\), so its support \(A_a\subseteq P_3\cap Q_1\) at the midpoint is nonempty and intersects the reverse-time \(Q_1\) support of **every** \(Q_1\) target. If \(A_a=\{x\}\), then \(x\) would be a full reverse-time collector in \(Q_1\). But \(Q_1\) is a chronological tree when reversed; its only possible two full collectors are endpoints of its LAST reversed contact (FIRST original suffix contact), which by Bumby's first-contact spine joins \(P_1\) and \(P_2\), never \(P_3\). Thus \(|A_a|\ge2\). The identical argument applies to \(Q_2\). For \(C\), nonempty midpoint support follows from successful crossing to \(Q_3\). QED.

**Dual:** every reversed-\(Q_3\) secret has at least two terminal reversed carriers in each \(P_1\cap Q_3\), \(P_2\cap Q_3\), and at least one in \(P_3\cap Q_3\). This uses the last original prefix calls of the two prefix trees.

## Lemma 16.2 — the preceding spanning tree has three full recipient groups excluding two endpoints (all n)

Call \(e=uv\) the final chronological \(P_3\) edge, where \(u\in A\), \(v\in B\). The chronological spanning tree \(T=P_3-e\) has three **disjoint, nonempty, collectively complete** recipient groups

\[
H_A=A\setminus\{u\},\qquad H_B=B\setminus\{v\},\qquad H_C=C.
\]

Both \(u,v\) are unassigned **helpers** for this tree-cover problem.

**Proof.** At the last edge only endpoints \(u,v\) change information. After that edge each secret has at least two \(A\)-carriers, so at least one carrier in \(A\setminus\{u\}\), unchanged since the end of \(T\). Similarly, the two \(B\)-carriers guarantee one in \(B\setminus\{v\}\) before \(e\). All \(C\) carriers are unchanged because the final edge lies outside \(C\). Thus each \(H\) collectively covers every original \(P_3\) secret before \(e\). Applying Stage 11's helper-robust chronological tree-cover theorem gives

\[
|P_3|-2=|H_A|+|H_B|+|H_C|\ \ge\ 2^{3-1}=4,
\]
hence \(|P_3|\ge6\). The exact seven-vertex exhaustion below makes this stronger.

## Theorem 16.3 — no local terminal crossing with fewer than eight participants

**Claim (finite-exhaustion certified).** Consider any connected simple chronological unicyclic graph on \(v\) labelled people, using exactly \(v\) **distinct** bidirectional calls, with a final cycle-closing call joining a participant in group \(A\) to a participant in group \(B\). Suppose the participants are partitioned into nonempty \(A,B,C\) and **every secret has at least two terminal carriers in \(A\), at least two in \(B\), and at least one in \(C\)**. Then

\[
\boxed{v\ge8.}
\]

This is a finite theorem, proven by exhaustive exact enumeration of **all** admissible local chronologies for \(v=5,6,7\), combined with the trivial size bound \(v\ge2+2+1=5\). It is not claimed to have a shorter all-\(v\) symbolic proof. The certificate is an independently executable self-contained C++17 enumerator [exact_local_double_cover.cpp](exact_local_double_cover.cpp), whose implementation and CI evidence need to be checked independently.

**Completeness of finite enumeration:** By relabelling vertices within each designated group, any partition may be mapped to canonical contiguous labels
\[
A=\{0,\dots,a-1\},\quad B=\{a,\dots,a+b-1\},
\quad C=\{a+b,\dots,v-1\},
\]
with \(a,b\ge2,c=v-a-b\ge1\). The final call may be relabelled to \((0,a)\). Because it **closes** the unique cycle, the first \(v-1\) edges are a spanning labelled tree **not** containing \((0,a)\). Every such tree is generated by exactly one Prüfer word of length \(v-2\). Every chronological ordering is enumerated by the \((v-1)!\) permutations of its edges. Replay starts with \(v\) singleton bitset secrets and applies the exact union rule at every call, including the final \((0,a)\). For every secret, count distinct carriers within the three groups and reject unless counts are at least \((2,2,1)\). The checker exhausts all possible positive size triples \(a+b+c=v\) for \(v=5,6,7\), no probabilistic sampling or external SAT oracle.

| \(v\) | Ordered group-size triples tested | Labelled spanning trees without fixed final edge, per triple | Tree-call orders per triple | Valid triples and chronologies |
|---|---:|---:|---:|---:|
| 5 | 1 | 75 | 1,800 | 0 |
| 6 | 3 | 864 | 103,680 | 0 |
| 7 | 6 | 12,005 | 8,643,600 | 0 |

There are **52,174,440** chronological local replay cases across these ten size profiles (1,800 + 3·103,680 + 6·8,643,600). The finite test's logical coverage is fully specified; an executable result corroborates this proof of exhaustion, **not** universal foresthood.

**Sharp local example at \(v=8\).** Let the original chronological contacts be

\[
(0,4),(1,5),(0,1),(2,6),(3,7),(2,3),(0,2),(1,3).
\]

Assign \(A=\{0,1\}\), \(B=\{2,3\}\), \(C=\{4,5,6,7\}\). All eight static calls are distinct. Their union has one cycle and the final \((1,3)\) closes it across \(A,B\). After the last call each person in \(A\cup B\) knows all eight secrets; the four people in \(C\) jointly cover all secrets. Thus the respective per-secret carrier multiplicities are at least \((2,2,1)\). The example is local and **does not** yield a successful two-half \(2n-4\) counterexample. The threshold \(|P_3|\ge8\) cannot be improved from this local hypothesis alone.

## Corollary 16.4 — the unrestricted original 3×3 incidence geometry

Apply the local theorem to \(P_3\) with \(A=P_3\cap Q_1\), \(B=P_3\cap Q_2\), \(C=P_3\cap Q_3\), using Lemmas 16.1–16.2 and Bumby's original chronology. Apply it again to \(Q_3\) in **fully reversed** local chronological order. Then **for every \(n\)**,

\[
\boxed{
m_{31}+m_{32}+m_{33}\ge8,\qquad
m_{13}+m_{23}+m_{33}\ge8.
}
\]

No off-corner-size-two-pair hypothesis is required. This is strictly broader than the one-sided \(\ge9\) center inequality in Stage 15, though it is only a bound on the two *component sizes* rather than on the central cell alone.

The inequalities can be inserted as **sound necessary prefilters** into any future full original-chronology search. They do not assert surviving incidence matrices admit an actual chronological schedule.

## Exact size-only frontier and independent count

Put \(k=n-13\), and introduce the additional nonnegative allocations
\[
p=(m_{13}-2)+(m_{23}-2),\quad
q=(m_{31}-2)+(m_{32}-2),\quad d=m_{33}-1,\quad
r=k-p-q-d.
\]

The four independent corner extras sum to \(r\). For fixed \(p,q,d\), there are \((p+1)(q+1)\binom{r+3}{3}\) *labelled* incidence matrices.

The new component-size conditions are \(p+d\ge3,\ q+d\ge3\). The existing Stage 15 one-sided rule is \((p=0\text{ or }q=0)\Rightarrow d\ge8\), and Stage 14's simultaneous rule is \((p=q=0)\Rightarrow d\ge63\). Thus the exact Stage 14–16 necessary-incidence count is

\[
\boxed{\displaystyle
N_{16}(n)=\sum_{\substack{p,q,d\ge0,\ p+q+d\le k\\
p+d\ge3,\ q+d\ge3\\
(p=0\lor q=0)\implies d\ge8\\
(p=q=0)\implies d\ge63}}
(p+1)(q+1)\binom{k-p-q-d+3}{3}.}
\]

An independent brute-force nine-cell integer-composition oracle in [count_stage16_incidence.py](count_stage16_incidence.py) cross-checks this triple-sum expression for \(13\le n\le25\).

| \(n\) | Raw labelled positive 3×3 matrices | Stage 15 survivors | Stage 16 survivors |
|---|---:|---:|---:|
| 18 | 1,287 | 489 | **41** |
| 19 | 3,003 | 1,365 | **221** |
| 20 | 6,435 | 3,333 | **825** |
| 21 | 12,870 | 7,359 | **2,438** |
| 24 | 75,582 | 52,293 | **28,205** |

For \(n=18\), every Stage 16 surviving matrix has \(m_{33}\in\{2,3,4\}\), a size-only consequence independent of any existence claim.

**Caveat:** These are counts of *labelled positive component-cell multiplicity matrices*, NOT valid global gossip chronologies or symmetry-orbit counts. In particular, 41 is a pool for future falsification; none is certified feasible.

## Research frontier and assurance gates

We have not excluded all 41 \(n=18\) profiles, nor all \(n\ge18\) possibilities. A useful next attack is a temporal-compatibility solver for these 41 matrices, integrating **both** tree contacts with Bumby's first/last spine; independent representation/oracle validation is mandatory. Earlier 3×3 incidence bounds and this stage's exact local finite enumeration are **necessary conditions only**.

- **All-n structural double-cover lemma:** human proof, source-dependent on Bumby's theorem.
- **All-n local \(\ge8\) size restriction:** follows from the exhaustive finite exclusion at \(v\le7\); tested code is not a formal proof assistant.
- **Counting formula:** exact algebra, independently enumerable.
- **Complete universal original-half forest claim:** **OPEN**.
- **Historically novel assertion:** **UNVERIFIED**.
- **PR / submission:** DRAFT, UNMERGED, HOLD.
