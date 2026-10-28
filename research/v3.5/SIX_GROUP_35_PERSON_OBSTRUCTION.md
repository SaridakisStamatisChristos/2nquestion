# Stage 18 — Six complete recipient groups force a 35-person unicyclic row

**28 October 2026. New all-\(n\) necessary condition for the ORIGINAL unreordered chronological midpoint.** The universal chronological half-forest conjecture remains OPEN. The result uses the all-n off-corner double-carrier theorem (Stage 17), exact helper-robust chronological tree-cover bound and equality rigidity (Stages 11/15), and the causal four-arm decomposition (Stage 14).

## Hypothetical both-cyclic fixed midpoint

Take a successful shortest schedule of \(2n-4\) **distinct** bidirectional calls, with \(n\ge4\). Suppose that both its actual original first and last \(n-2\) calls contain a cycle. As Bumby's 1981 Theorem 3 requires, partition the original prefix into closed tree components \(P_1,P_2\) and unicyclic \(P_3\); partition the **fully reversed actual suffix** into closed trees \(Q_1,Q_2\) and unicyclic \(Q_3\). Let \(m_{ij}=|P_i\cap Q_j|\), all positive.

By Bumby's original chronological spine, the last prefix call \(e\) **within \(P_3\)** is on its unique cycle and connects a participant \(a\in P_3\cap Q_1\) to a participant \(b\in P_3\cap Q_2\). Deleting **that actual final call** (without changing the order of anything else) leaves a spanning tree \(T\) on all of \(P_3\), whose \(v-1\) distinct edges were already contacted once.

## Lemma 1 — Two independent complete recipient groups survive the final cycle edge

For \(j\in\{1,2\}\), define the untouched off-corner recipients

\[
H_1=(P_3\cap Q_1)\setminus\{a\},\qquad
H_2=(P_3\cap Q_2)\setminus\{b\}.
\]

**Both nonempty sets \(H_1,H_2\), considered separately, collectively know every original \(P_3\) secret at the end of \(T\).**

**Proof.** The [Stage 17 universal off-corner double-carrier theorem](../v3.4/UNIVERSAL_OFFCORNER_DOUBLE_CARRIER.md) says that at the fixed midpoint **every** \(P_3\)-secret is held by at least **two distinct people in \(P_3\cap Q_1\)**, and also by at least two distinct people in \(P_3\cap Q_2\). The final original \(P_3\) contact changes the knowledge of **only** \(a,b\). Removing \(a\) from the first cell and \(b\) from the second leaves at least one unchanged carrier of each original \(P_3\) secret. These carriers already knew it before the final call, at the end of the tree \(T\). The groups are disjoint and respectively have \(m_{31}-1\) and \(m_{32}-1\) participants. QED.

This deduction does not require any specific off-corner cell to have **exactly** two people.

## Lemma 2 — Four central complete recipient groups from opposite causal arms

Assume \(m_{13}=m_{23}=2\). By the two-point crossing argument plus Bumby's prefix-tree collector spine (Stages 13/14/17), **all four people** in the two distinct cells \(P_1\cap Q_3\) and \(P_2\cap Q_3\) are complete in the fully reversed unicyclic \(Q_3\). Stage 14's original-chronology four-collector theorem then partitions \(Q_3\) into **four causally sealed rooted tree arms** \(B_1,\ldots,B_4\), one root per arm outside the center \(X=P_3\cap Q_3\), with all cross-arm calls exclusively between those roots.

For each arm set \(G_j=X\cap B_j\) for \(j=1,\ldots,4\). Full success requires every original \(P_3\)-source secret to reach every \(Q_3\) target. The causal-sealing condition ensures a reverse target label originating in arm \(B_j\) cannot enter an \(X\) member of any other arm. Therefore **each \(G_j\) is nonempty and collectively covers all \(P_3\) secrets at the original midpoint**, and hence already at the end of \(T\): the deleted final \(P_3\) call touched only \(a,b\notin X\).

The four \(G_j\) partition \(X\). Together with \(H_1,H_2\) they are **six disjoint, nonempty, completely covering designated recipient groups of the same original chronological spanning tree \(T\)**. All other tree vertices (including \(a,b\)) are permissible unused helpers.

## Theorem — One saturated off-corner PAIR requires a 35-person opposite unicyclic component

The helper-robust exact chronological tree-cover theorem ([Stage 11](../v2.8/STEINER_COVER_RIGIDITY.md), [Stage 15 equality with helpers](../v3.2/HELPER_EQUALITY_AND_ONE_SIDED.md)) for **six** complete-cover groups yields

\[
R=|H_1|+|H_2|+\sum_{j=1}^4|G_j|
=(m_{31}-1)+(m_{32}-1)+m_{33}
=|P_3|-2\ge2^{6-1}=32.
\]

**Equality \(R=32\) is impossible.** Stage 15 equality rigidity, valid with *arbitrary unused helpers*, says **every** designated recipient \(x\in G_j\) owns an original \(P_3\)-secret that no other person in \(G_j\) knows (a private cell secret). Exact temporal crossing with every reversed \(B_j\)-arm target would then force \(x\) to be a complete reversed collector of that **tree arm**. But each \(B_j\) tree has at most two complete collectors, and one is its outside-\(X\) root. Thus **\(|G_j|\le1\)**. Since each \(G_j\ne\varnothing\), all four would be singletons, and their four distinct vertices would individually know every \(P_3\)-secret (they are complete recipient groups). But a chronological spanning tree has at most **two** terminal complete collectors, contradiction.

Thus \(R\ge33\) and

\[
\boxed{
m_{13}=m_{23}=2\quad\Longrightarrow\quad
|P_3|=m_{31}+m_{32}+m_{33}\ge35.
}
\]

The prefix trees \(P_1,P_2\) contain at least \(1+1+2=4\) people each (positive corners and the two indicated off-corner cells). Therefore

\[
\boxed{
m_{13}=m_{23}=2\quad\Longrightarrow\quad n\ge43.
}
\]

Reverse the entire **original schedule** and apply the same proof to obtain

\[
\boxed{
m_{31}=m_{32}=2\quad\Longrightarrow\quad
m_{13}+m_{23}+m_{33}\ge35\quad\Longrightarrow\quad n\ge43.
}
\]

**Consequently, for every \(n\le42\), a hypothetical both-cyclic original midpoint must have at least one entry \(\ge3\) in each off-corner pair.** This improves the Stage 15/16 frontier from \(n\le22\) to \(n\le42\), WITHOUT proving that such remaining \(3\times3\) possibilities are chronologically realizable or impossible.

The stronger Stage 14 \(m_{33}\ge64\) still applies when **all four** off-corner entries equal 2. Stage 16's mixed \(m_{33}\ge16\) remains a valid, sharper *center-specific* inequality; this stage instead gives a stronger **component-total** inequality that does not bound \(m_{33}\) alone independent of the opposite off-corner sizes.

### General \(k\)-arm double-carrier / last-edge principle

The same proof is not specific to four arms. Let \(A\) be an original chronological unicyclic component with **\(A\setminus X=D_1\sqcup D_2\)**, whose last on-cycle call connects one vertex of each of these two **distinct outside-\(X\)** recipient cells. Suppose **every original \(A\)-secret has at least two terminal carriers in each \(D_i\)**. Let the reversed opposite component \(B\) admit \(k\ge3\) causally sealed rooted tree arms with one complete outside-\(X\) collector per arm, and assume successful original source-target midpoint crossing.

Removing the final \(A\) call leaves \(k+2\) disjoint, nonempty, collectively complete designated recipient groups of its chronological spanning tree \(T\): the two outside groups \(D_1\setminus\{a\}\), \(D_2\setminus\{b\}\), and \(k\) central arm cells. They cover **all but exactly two** \(A\) vertices, namely \(a,b\). Hence the exact tree-cover theorem gives \(|A|-2\ge2^{k+1}\). Equality would make every central group recipient private within their group; crossing forces each to be a full collector of its \(B\) arm. Because each \(B\) arm already has its outside complete root, each central group would be a singleton. Those \(k\ge3\) singleton complete-cover groups would provide **at least three** full collectors in the tree \(T\), contradicting the tree maximum of two. Therefore:

\[
\boxed{|A|\ge2^{k+1}+3\qquad(k\ge3).}
\]

This is a general **conditional** all-n structural lemma. At \(k=4\), it yields the 35-person theorem above. The direct six-group equality witness shows why the crossing argument, not group count alone, supplies the final \(+1\).

### Sharpness boundary of the recipient-count method

The unweighted six-group tree-cover bound \(R\ge32\) is attained abstractly by a 32-person original chronological tree with group sizes \((1,1,2,4,8,16)\). Its 32 designated recipients all have private secrets, exactly two singleton complete groups, and only two complete terminal collectors. This demonstrates that **simply counting six complete recipient groups cannot prove \(R>32\)**; the strengthened \(R\ge33\) uses the *actual opposing causal tree-arm* compatibility to rule out the equality case. The 32-person construction is not a full gossip schedule, and does not realize a counterexample.

[Independent 32-person equality witness and exact profile check](six_group_bridge_check.py) replay the chronological tree and verify each group covers every original secret and every recipient is private, then reproduce the \(n\le42\) size-only incidence counts using a completely independent enumeration and a stars-and-bars formula. No solver-assisted all-n certificate is claimed.

## Exact n≤42 SIZE-ONLY incidence filter

Let \(k=n-13\), and distribute \(k\) extra occupants across the \(3\times3\) baseline

\[
\begin{pmatrix}1&1&2\\1&1&2\\2&2&1\end{pmatrix}.
\]

For **\(n\le42\)**, the new theorem forbids EITHER off-corner pair from remaining \((2,2)\). The exact number of labelled positive cell-size matrices surviving this **necessary size-only** filter is

\[
\boxed{
N_{18}(n)=\binom{k+8}{8}-2\binom{k+6}{6}+\binom{k+4}{4},
\qquad k=n-13,
}
\]

where \(\binom ab=0\) for \(a<b\). This is inclusion–exclusion for the two events in which a specified pair receives no extra occupant. The formula is a **size-only overapproximation**: it is not a count of successful schedules, feasible local knowledge histories, isomorphism classes, or proof of the universal conjecture.

| n | Raw positive labelled matrices | Stage 18 size-only survivors |
|---|---:|---:|
| 18 | 1,287 | 489 |
| 19 | 3,003 | 1,365 |
| 20 | 6,435 | 3,333 |
| 22 | 24,310 | 15,015 |
| 23 | 43,758 | 28,743 |
| 24 | 75,582 | 52,195 |
| 25 | 125,970 | 90,662 |
| 40 | 23,535,820 | 21,352,149 |
| 42 | 38,608,020 | 35,402,620 |

The independent regression enumerates all compositions at \(n=13,\ldots,26\) and matches the formula, then checks the formula itself at \(n=28,32,40,42\). For \(n\ge43\) the new theorem does **not** ban every \((2,2)\) pair, and this simplified formula must **NOT** be used as an exhaustive necessary profile count without reinstating the conditional component-total inequality and Stages 14–16.

## Proof dependencies and limitations

Bumby 1981 original chronological split and last cycle edge -> Stage 17 double carriers in each off-corner -> two disjoint post-last-edge-removed complete covers -> Stage 14 causal four-arm decomposition (only when opposite off-corner pair=2,2) -> four additional central full covers -> Stage 11/15 helper-robust tree-cover lower bound and equality private-secret rigidity -> \(R\ge33\).

The all-n argument is **human written and adversarially scoped**, not machine formalized. Historical priority versus Labahn (1995) and Krumme (1996) remains unverified. **Universal original-half forest conjecture: OPEN. Independent genuine counterexample: NONE. PR #1: DRAFT/UNMERGED.**
