> **Stage 18 strengthening and final scope reconciliation (28 October 2026):** The local 8-vertex **(2,5,1)** survivor documented below is real, so it was correct to reject the local-only inference of a universal component-size-nine bound. But its mandatory FOUR reverse target supports `{y,z_i}` **cannot cross the opposite chronological tree**, as proved in [Stage 18 four-leaf star theorem](../v3.5/FOUR_LEAF_STAR_GLOBAL_EIGHT_EXCLUSION.md). This supplies the missing GLOBAL argument, so the all-n necessary bound `|P3|,|Q3|>=9` is now **proved with stronger hypotheses**; the full original half-forest conjecture remains OPEN. The stronger sound Stage 18 labelled necessary-incidence count is **41 at n=19**, not Stage 17's interim disjunctive 45. Preserve this audit history: the omitted local class was a genuine counterexample to the initial local classification, but is incompatible with an entire successful original midpoint schedule.

# Stage 17 — Exact eight-person boundary and exclusion of the \(n=18\) original-half counterexample

**28 October 2026. Status: COMPLETE HUMAN MATHEMATICAL PROOF for \(n=18\), dependent on the historically sourced Bumby 1981 structural theorem, the Stage 14 causal four-arm theorem, and exact finite local enumerations.** This is **NOT a proof of the original chronological half-forest conjecture for all n**. No Lean/Coq verification or independent peer review is asserted. PR #1 stays **DRAFT, OPEN, UNMERGED**; manuscript submission HOLD.

## 1. Contract: EXACT original chronology

Let \(S=(e_1,\ldots,e_{2n-4})\) be a **successful**, pairwise-distinct, bidirectional telephone-gossip chronology. The target asserts that the **original** first or last \(n-2\) edges form a forest, with **no reordering**.

Assume for contradiction both original halves cyclic. By Richard T. Bumby, *A Problem with Telephones*, SIAM J. Algebraic Discrete Methods **2** (1981), 13–18, Theorem 3 and Case II, each half has exactly three components: two closed trees and one unicyclic component. Write prefix \(P_1,P_2\) (trees), \(P_3\) (unicyclic), and *fully time-reversed* suffix \(Q_1,Q_2\) (trees), \(Q_3\) (unicyclic), and \(m_{ij}=|P_i\cap Q_j|\).

Bumby's original last-prefix / first-suffix contact spine and exact local crossing yield the Stage 16 **two-fold off-corner secret coverage**, with local \(P_3\) final edge on its cycle between \(Q_1,Q_2\); equivalently for reversed \(Q_3\) between \(P_1,P_2\). Stage 16's exhaustive local theorem previously established \(|P_3|,|Q_3|\ge8\) unconditionally.

## 2. Exact eight-person local case classification — adversarially corrected

### Theorem 17.1 (finite exact, corrected)

Consider a connected eight-person local *unicyclic* chronology of eight distinct calls with the **last** edge closing the cycle between groups \(A,B\) in a partition \(A\sqcup B\sqcup C\). Suppose every original secret has at least two terminal carriers in \(A\), at least two in \(B\), and at least one in \(C\). Then, up to interchanging \(A,B\), the only possible SIZE patterns are

\[
\boxed{(|A|,|B|,|C|)\in\{(2,2,4),(2,5,1)\}.}
\]

**Important adversarial correction:** An initial enumeration incorrectly omitted the two possible triples \((2,5,1)\) and \((3,4,1)\). The omitted \((2,5,1)\) class has **real local witnesses**. Consequently the earlier provisional claim that only \((2,2,4)\) survives, and the inferred **unconditional** \(|P_3|,|Q_3|\ge9\), were **false and must not be used**. This defect was caught before final certification, and every six-triple result below is now explicitly pinned in the executable.

**Complete exact verification.** Since \(a,b\ge2,c\ge1\), there are precisely SIX group-size triples up to swapping \(A,B\). Relabel each group into contiguous intervals, and the final endpoints as \((0,a)\). The first seven contacts are a labelled spanning tree not containing the final edge. Enumerate all \(8^6=262144\) labelled Prüfer codes; quotient only static *trees* by group-preserving vertex relabellings fixing \(0,a\), using the minimum encoded undirected adjacency mask. That quotient is exact: each tree's chronological orderings correspond bijectively, under label permutations, to those of its representative. Exhaust ALL \(7!\) chronological orders for each canonical tree and replay each bitset secret under the original union-call rule; test the \((2,2,1)\) minimum carrier counts for all eight original secrets.

| \((a,b,c)\) | Static trees without fixed final edge | Canonical tree orbits | Enumerated distinct chronological orders | Locally compatible |
|---|---:|---:|---:|---:|
| (2,2,4) | 196,608 | 9,653 | 48,651,120 | **160** |
| (2,3,3) | 196,608 | 18,240 | 91,929,600 | **0** |
| (2,4,2) | 196,608 | 18,240 | 91,929,600 | **0** |
| (3,3,2) | 196,608 | 26,616 | 134,144,640 | **0** |
| (2,5,1) | 196,608 | 9,653 | 48,651,120 | **160** |
| (3,4,1) | 196,608 | 18,240 | 91,929,600 | **0** |

**Total: 507,235,680 exact representative tree-call orderings**. The check is implemented independently in [exact_eight_group_orbits.cpp](exact_eight_group_orbits.cpp). The size-8 \((2,2,4)\) case has a separate explicit Stage 16 local witness, and the program obtains local \((2,5,1)\) witnesses too. Neither is a full two-half gossip scheme.

### Corollary 17.2 — universal DISJUNCTIVE size-eight constraint (corrected)

Stage 16 already proved \(|P_3|,|Q_3|\ge8\). If \(|P_3|=8\), the above local classification allows only \((m_{31},m_{32},m_{33})=(2,2,4)\) or \((2,5,1)\) up to swapping the first two columns. But the former is globally excluded by Stage 15: \(m_{31}=m_{32}=2\Rightarrow m_{33}\ge9\). Therefore any **hypothetical original both-cyclic** split satisfies the sharp necessary dichotomy

\[
\boxed{
|P_3|\ge9\ \ \text{OR}\ \
(m_{33}=1,\ \{m_{31},m_{32}\}=\{2,5\}).
}
\]

By exact time reversal,

\[
\boxed{
|Q_3|\ge9\ \ \text{OR}\ \
(m_{33}=1,\ \{m_{13},m_{23}\}=\{2,5\}).
}
\]

In particular **if the center has at least two participants**, \(|P_3|,|Q_3|\ge9\). There is **no global all-\(n\) claim** that both components always have size at least nine.

### Why the \(n=18\) size reduction still holds

Let \(p=(m_{13}-2)+(m_{23}-2)\), \(q=(m_{31}-2)+(m_{32}-2)\), \(d=m_{33}-1\), and \(r\ge0\) denote extra occupants in the four positive corner cells. Then \(p+q+d+r=n-13\). Stage 16's size-eight lower bounds give \(p+d\ge3\), \(q+d\ge3\).

When \(n=18\), \(p+q+d+r=5\). **If \(d=0\)**, those two inequalities force \(p,q\ge3\), contradicting \(p+q\le5\). Thus \(m_{33}=d+1\ge2\) at \(n=18\). By the corrected universal disjunction, both unicyclic components must then have size \(\ge9\), giving **\(p+d\ge4,\ q+d\ge4\) for \(n=18\) only**. These and the prior Stage 14–15 restrictions leave precisely four labelled matrices, as established in Section 3.

## 3. Only one positive \(3\times3\) incidence orbit remains at \(n=18\)

The Stage 15–16 necessary conditions already require that all corners are \(\ge1\), all four off-corners are \(\ge2\), and neither pair of off-corners may be \((2,2)\) while the center is small. The two size-\(\ge9\) conditions **now justified specifically at \(n=18\)** reduce the \(n=18\) labelled size matrices to **exactly four**: they differ only by permuting the two prefix tree rows and/or two suffix tree columns. This is independently checked by [the standalone Python verifier](check_five_person_and_n18.py).

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

Let \(T\) be a connected five-person tree with its four edges each called once, in a fixed chronological order. Suppose the **last** call joins two designated singleton outside roots \(u,v\), **each of which is a complete collector of all five secrets after that call**. Suppose the remaining three participants \(W=\{a,b,c\}\) **collectively** know all five original secrets after all calls.

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

## 6. Correct all-n disjunctive size frontier and count

It would be **wrong** to require \(|P_3|,|Q_3|\ge9\) for arbitrary \(n\): the genuine local \((2,5,1)\) size-eight case survives the currently proved conditions. The valid universal necessary filter is Stage 15 plus:

- always \(p+d\ge3\) and \(q+d\ge3\) (Stage 16);
- if \(q+d=3\) (equivalently \(|P_3|=8\)), then necessarily \(d=0,\ q=3\), with \((m_{31}-2,m_{32}-2)=(0,3)\) or \((3,0)\);
- if \(p+d=3\) (equivalently \(|Q_3|=8\)), then necessarily \(d=0,\ p=3\), with analogous \(P_1/P_2\) off-corner distribution.

Retain Stage 15's \((p=0\lor q=0)\Rightarrow d\ge8\) and Stage 14's \((p=q=0)\Rightarrow d\ge63\). The extra free corner-cell occupants contribute \(\binom{r+3}{3}\), where \(r=n-13-p-q-d\). Enumerate the \(p+1\) and \(q+1\) pair splits *separately*, retaining only the two extreme splits when the corresponding component size equals eight.

| \(n\) | Stage 15 relaxed profiles | Stage 16 local ≥8 survivors | Stage 17 exact eight-person disjunctive survivors **before further chronology** |
|---|---:|---:|---:|
| 18 | 489 | 41 | **4** (then all four contradicted in Section 5) |
| 19 | 1,365 | 221 | **45** |
| 20 | 3,333 | 825 | **257** |
| 21 | 7,359 | 2,438 | **994** |
| 24 | 52,293 | 28,205 | **17,365** |

[check_five_person_and_n18.py](check_five_person_and_n18.py) independently cross-checks these disjunctive size-filter counts against every labelled positive nine-cell integer composition, and checks that the four \(n=18\) profiles form a single row/column-swap orbit. **Do not reuse the previously proposed unsound all-\(n\) \(\ge9\) incidence count of 41 at \(n=19\); the correct count is 45.** None of these size-only survivors is automatically a completed successful schedule.

## 7. Next research frontier

At \(n=19\), **45** positive labelled incidence matrices satisfy the combined size filters. The next high-value task is the analogue of the four- and five-person tree privacy obstruction for slightly larger corner or off-corner groups, then an exact original chronology-compatible bidirectional check. Preserve literature and quantifier cautions, keep PR #1 DRAFT, and never call a relaxed incidence matrix a global witness.
