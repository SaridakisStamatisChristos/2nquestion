# Stage 17 — Exact eight-person boundary and exclusion of the \(n=18\) original-half counterexample

**28 October 2026. Status: COMPLETE HUMAN MATHEMATICAL PROOF for \(n=18\), dependent on the historically sourced Bumby 1981 structural theorem, the Stage 14 causal four-arm theorem, and exact finite local enumerations.** This is **NOT a proof of the original chronological half-forest conjecture for all n**. No Lean/Coq verification or independent peer review is asserted. PR #1 stays **DRAFT, OPEN, UNMERGED**; manuscript submission HOLD.

## 1. Contract: EXACT original chronology

Let \(S=(e_1,\ldots,e_{2n-4})\) be a **successful**, pairwise-distinct, bidirectional telephone-gossip chronology. The target asserts that the **original** first or last \(n-2\) edges form a forest, with **no reordering**.

Assume for contradiction both original halves cyclic. By Richard T. Bumby, *A Problem with Telephones*, SIAM J. Algebraic Discrete Methods **2** (1981), 13–18, Theorem 3 and Case II, each half has exactly three components: two closed trees and one unicyclic component. Write prefix \(P_1,P_2\) (trees), \(P_3\) (unicyclic), and *fully time-reversed* suffix \(Q_1,Q_2\) (trees), \(Q_3\) (unicyclic), and \(m_{ij}=|P_i\cap Q_j|\).

Bumby's original last-prefix / first-suffix contact spine and exact local crossing yield the Stage 16 **two-fold off-corner secret coverage**, with local \(P_3\) final edge on its cycle between \(Q_1,Q_2\); equivalently for reversed \(Q_3\) between \(P_1,P_2\). Stage 16's exhaustive local theorem previously established \(|P_3|,|Q_3|\ge8\) unconditionally.

## 2. Exact eight-person local case classification (NEW)

### Theorem 17.1 (finite exact)

Consider a connected eight-person local *unicyclic* chronology of exactly eight distinct calls, with the **last** call closing the unique cycle and connecting groups \(A,B\) in a partition \(A\sqcup B\sqcup C\) of the eight people. Suppose every original secret has at least **two** terminal recipients in \(A\), at least **two** in \(B\), and at least **one** in \(C\). Then the **only possible group-size pattern**, up to interchanging \(A,B\), is

\[
\boxed{(|A|,|B|,|C|)=(2,2,4).}
\]

**Exact verification method.** First \(7\) contacts form a spanning labelled tree. Relabel the groups as contiguous intervals of lengths \(a,b,c\), and final endpoints as \((0,a)\). The first-seven tree cannot contain edge \((0,a)\). All \(8^{6}=262144\) labelled Prüfer strings yield every labelled tree once, and we enumerate every one of the \(7!=5040\) chronological orderings of its edges.

For efficiency, keep only one canonical *static tree* in each orbit under permutations of the labels **within groups and fixing the final endpoints**. For any such permutation, chronological call-order sequences and carrier counts are carried bijectively to those of the relabelled tree. Thus quotienting static tree topology only loses NO possible chronology. The canonical representative is the minimum 28-bit undirected-edge adjacency mask of the tree under this finite permutation group. Every chronological order of each surviving representative is still explicitly replayed. Endpoints update information via bitwise union, and all eight secrets' carrier multiplicities are checked independently.

Only four group-size triples are possible for \(8=a+b+c\) with \(a,b\ge2,c\ge1\), up to \(A,B\) interchange. Exact counts from [the standalone C++17 verifier](exact_eight_group_orbits.cpp):

| \(a,b,c\) | Trees avoiding the final edge | Canonical static-tree orbits | Exactly replayed chronological orderings | Valid local chronological orderings |
|---|---:|---:|---:|---:|
| (2,3,3) | 196,608 | 18,240 | 91,929,600 | **0** |
| (2,4,2) | 196,608 | 18,240 | 91,929,600 | **0** |
| (3,3,2) | 196,608 | 26,616 | 134,144,640 | **0** |
| (2,2,4) | 196,608 | 9,653 | 48,651,120 | **160** |

The three zero results and one nonempty result together are **a complete finite classification of possible size triples**, not a classification of all chronological graphs or global schedules. Total: **366,654,960** enumerated representative tree-order pairs. The previously replayed [eight-person witness](../v3.3/DUAL_DOUBLE_COVER_AND_LOCAL_MINIMUM.md) independently establishes feasibility of the local \((2,2,4)\) class.

### Corollary 17.2 — unconditional \(9\)-person lower bounds for BOTH cyclic components

If a hypothetical successful *original* both-cyclic midpoint had \(|P_3|=8\), Stage 16's two-fold cover would force
\[
(m_{31},m_{32},m_{33})=(2,2,4).
\]
But the one-sided Stage 15 theorem applied to the pair \(m_{31}=m_{32}=2\) forces \(m_{33}\ge9\), contradicting \(m_{33}=4\). Thus \(|P_3|\ne8\), and earlier Stage 16 proved \(|P_3|\ge8\). Apply the argument to the reversed original suffix for \(Q_3\):

\[
\boxed{
m_{31}+m_{32}+m_{33}\ge9,\qquad
m_{13}+m_{23}+m_{33}\ge9,
}
\]
**for all \(n\)**, under the hypothetical both-cyclic original schedule. This does NOT imply the center \(m_{33}\) alone is at least nine unless a Stage 15 size-two-pair condition holds.

## 3. Only one positive \(3\times3\) incidence orbit remains at \(n=18\)

The Stage 15–16 necessary conditions already require that all corners are \(\ge1\), all four off-corners are \(\ge2\), and neither pair of off-corners may be \((2,2)\) while the center is small. The new two size-\(\ge9\) conditions reduce the \(n=18\) labelled size matrices to **exactly four**: they differ only by permuting the two prefix tree rows and/or two suffix tree columns. This is independently checked by [the standalone Python verifier](check_five_person_and_n18.py).

One canonical matrix is
\[
\boxed{
M=\begin{pmatrix}
1&1&2\\
1&1&3\\
2&3&4
\end{pmatrix}.
}
\]

At \(n=18\), all corners are thus **singletons**, and (after harmless renaming of the tree *component indices*, not reordering calls) each of the two prefix trees \(P_1,P_2\) has 4 or 5 people, and each of the two reversed suffix trees \(Q_1,Q_2\) also has 4 or 5 people. In the tree with 4 participants, the three disjoint full-cover groups have sizes \((1,1,2)\); in the tree with 5 they have sizes \((1,1,3)\).

## 4. Five-person tree privacy theorem (NEW elementary lemma)

### Lemma 17.3 (two compulsory private recipients)

Let \(T\) be a connected five-person tree with its four edges each called once, in a fixed chronological order. Suppose the **last** call joins two designated singleton outside roots \(u,v\). Suppose the remaining three participants \(W=\{a,b,c\}\) **collectively** know all five original secrets after all calls.

Then **exactly TWO** different members of \(W\) have a *private* original secret relative to \(W\): for each of these two members there exists an original secret known to them and to **no other** member of \(W\).

**Proof independent of computation.** Remove the last edge \(uv\). Its two sides are chronological trees \(U\ni u\) and \(V\ni v\). Since the members of \(W\) are not endpoints of \(uv\), they cannot learn secrets across these sides at the last event. Both \(W\cap U\) and \(W\cap V\) must be nonempty for \(W\) collectively to cover both sides' original secrets. As \(|W|=3\), their sizes are \(1\) and \(2\). Relabel so \(U=\{u,a\}\), \(V=\{v,b,c\}\).

There is one earlier edge \(ua\) on \(U\), and \(a\) is necessarily private in \(W\): it alone among \(W\) knows its original secret (and \(u\)'s) because the other two lie on \(V\) and cannot receive any \(U\)-secret at the final call.

The last \(uv\) contact makes the two roots \(u,v\) the only possible complete collectors of all five tree secrets. Because both singleton-root groups cover all five secrets, **both** are terminal complete collectors and were complete for their own sides before \(uv\). On the three-person side \(V\), the two earlier edges make \(v\) complete for \(V\). There are exactly two possible chronological tree shapes, up to relabelling \(b,c\):

- Star \(v-b,\ v-c\), called in that order: \(b\) has only \(\{v,b\}\), while \(c\) has \(\{v,b,c\}\). In group \(\{b,c\}\), exactly \(c\) is private, due to secret \(c\).
- Path \(b-c,\ c-v\), called in that order: \(b\) has only \(\{b,c\}\), while \(c\) has \(\{b,c,v\}\). In group \(\{b,c\}\), exactly \(c\) is private, due to secret \(v\).

All other orderings would leave \(v\) uninformed about one of its own side's secrets, violating the complete-singleton-root hypothesis. Hence exactly one of \(\{b,c\}\) is private within \(W\), and together with \(a\) there are exactly two. QED.

**Independent finite check:** [check_five_person_and_n18.py](check_five_person_and_n18.py) enumerates every \(5^3\) Prüfer-labelled tree and all \(4!\) edge orders, filters the fixed singleton-root last call and full-cover \(W\), and finds exactly **72** qualifying labelled ordered instances; **all 72** have two private \(W\) participants. This is corroboration of the human proof, not its substitute.

The corresponding four-person tree with group sizes \((1,1,2)\) has **both** off-corner members private by Stage 11's exact tight tree-cover equality rigidity.

## 5. THEOREM — the original chronological half-forest conjecture holds at \(n=18\)

**Theorem 17.4 (proved using the stated historic/Stage 14 and finite dependencies).** Every shortest successful **original fixed-order** bidirectional telephone gossip schedule of \(2\cdot18-4=32\) distinct calls has a forest among its original first or last \(18-2=16\) calls.

**Proof by contradiction.** Assume both original halves cyclic, giving the unique matrix \(M\) from Section 3.

- **Original prefix trees.** The four-person \(P_1\) has corner singleton collector groups in \(Q_1,Q_2\), plus a two-person group \(P_1\cap Q_3\). Its two off-corner recipients are private (Stage 11 tight equality). The five-person \(P_2\) likewise has two singleton corner collector groups and a three-person group \(P_2\cap Q_3\); **two** of these off-corner recipients are private by Lemma 17.3. In the exact original-midpoint crossing, a participant who is the *unique prefix carrier* of a \(P_i\)-secret inside its \(Q_3\) cell must be a **complete reverse-time collector of \(Q_3\)**, since this secret must reach every \(Q_3\) original target. Therefore **at least four distinct people in \(P_1\cup P_2\), outside \(X=P_3\cap Q_3\), are full collectors of reverse-chronological unicyclic \(Q_3\)**.
- **Reversed original suffix trees.** Apply the **same argument to the reversed original schedule**. The four-person \(Q_1\) and five-person \(Q_2\) force at least four *distinct* complete prefix \(P_3\) collectors in their \(P_3\) cells, again outside \(X\).

A connected unicyclic component with \(v\) distinct calls has **at most four** terminal complete collectors. Thus each of \(P_3,Q_3\) has **exactly four**, all outside \(X\); the Stage 14 [causal four-arm bridge](../v3.1/CAUSAL_FOUR_ARM_BRIDGE.md) applies to both local chronologies in their **actual original orientation**. Its rigorously corrected causal-sealing crossing theorem (NOT the false strict global-arm-order inference) forces
\[
\boxed{|X|=m_{33}\ge4\cdot2^4=64.}
\]
But the unique remaining incidence matrix has \(m_{33}=4\). Contradiction. Therefore at least one original chronological half is a forest. QED.

**Independence boundaries:** The n=18 theorem logically relies on (a) Bumby's published Theorem 3 and its closed-tree spine, (b) Stage 11 tree-cover rigidity, (c) the Stage 14 all-\(n\) causal four-arm bound, and (d) the Stage 16 and 17 complete finite local exclusion certificates. The Stage 17 Python five-person checker and exact matrix enumeration are separate from the n=8 C++ checker. These are human-checkable proofs plus reproducible exhaustive computation, **not** a formal proof-assistant theorem. At no point is the original chronology reordered.

## 6. Enlarged unconditional component-size frontier and exact counts

Define baseline \(\sum m_{ij}=13\), extras \(k=n-13\), and pair-extras \(p,q\) and center extra \(d\) as in Stage 16. Replace the old two thresholds \(p+d,q+d\ge3\) with **\(p+d,q+d\ge4\)**. Preserve the Stage 15 one-sided \((p=0\lor q=0)\Rightarrow d\ge8\), and Stage 14 simultaneous \((p=q=0)\Rightarrow d\ge63\).

The same compressed triple-sum incidence count becomes
\[
\boxed{
N_{17}(n)=\sum_{\substack{p,q,d\ge0,\ p+q+d\le k\\
p+d\ge4,\ q+d\ge4\\
(p=0\lor q=0)\Rightarrow d\ge8\\
(p=q=0)\Rightarrow d\ge63}}
(p+1)(q+1)\binom{k-p-q-d+3}{3}.
}
\]

| \(n\) | Stage 15 labelled incidence survivors | Stage 16B survivors | Stage 17 survivors **before final local privacy contradiction** |
|---|---:|---:|---:|
| 18 | 489 | 41 | **4** (one tree-row/column orbit, subsequently contradicted) |
| 19 | 1,365 | 221 | **41** |
| 20 | 3,333 | 825 | **221** |
| 21 | 7,359 | 2,438 | **850** |
| 24 | 52,293 | 28,205 | **15,517** |

These are *necessary-condition incidence counts*, not successful schedules. The final privacy argument eliminates the four Stage 17 \(n=18\) incidences completely, so at \(n=18\) **there is NO successful both-cyclic original-half schedule**. For \(n\ge19\) the unrestricted conjecture is **OPEN**; the finite component threshold is not an existence theorem.

## 7. Next research frontier

At \(n=19\), only **41** positive labelled incidence matrices satisfy the combined size filters. The next high-value task is the analogue of the four- and five-person tree privacy obstruction for slightly larger corner or off-corner groups, then an exact original chronology-compatible bidirectional check. Preserve literature and quantifier cautions, keep PR #1 DRAFT, and never call a relaxed incidence matrix a global witness.
