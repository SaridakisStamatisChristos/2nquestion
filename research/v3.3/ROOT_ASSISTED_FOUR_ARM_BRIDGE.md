# Stage 16 — A pre-terminal collector forces a 16-person center

**28 October 2026. All-\(n\) conditional theorem for the ORIGINAL fixed chronological midpoint.** The universal chronological half-forest conjecture is OPEN. The result is a strict mixed-off-corner strengthening of [Stage 15](../v3.2/HELPER_EQUALITY_AND_ONE_SIDED.md), does not reorder any calls, and is not a global impossibility theorem.

## Source-checked setup

Suppose a shortest successful \(2n-4\)-call distinct-edge telephone-gossip schedule has **both original chronological halves cyclic**. By R. T. Bumby's *A Problem with Telephones*, 1981, Theorem 3, the original prefix components \(P_1,P_2\) are closed trees and \(P_3\) is unicyclic. In the reversed original suffix \(Q_1,Q_2\) are closed trees and \(Q_3\) is unicyclic. Let \(m_{ij}=|P_i\cap Q_j|\). All nine cells are nonempty, and the four off-corner cells \(m_{13},m_{23},m_{31},m_{32}\) are at least 2 (Bumby original first/last-contact spine).

Bumby's case II proof also shows the **actual last original prefix call** in \(P_3\) connects suffix-tree columns \(Q_1\) and \(Q_2\) and lies on the unique static cycle of \(P_3\). Removing that call leaves a spanning tree with its **original earlier call order**. The corresponding reverse-time assertion holds for \(Q_3\). These facts are source-scoped in [Stage 12](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md).

## Lemma A — Root-assisted causal crossing with unused helpers

Let \(A\) be a connected unicyclic component of the original prefix, with exactly \(v\) distinct chronological calls on its \(v\) people. Suppose its final call is on its unique static cycle and has both endpoints outside \(X=A\cap B\). Write \(T\) for the chronological spanning tree given by the first \(v-1\) calls.

Suppose that **some outside-\(X\) vertex \(u\) is already a complete collector of all \(A\) original secrets at the end of \(T\)**.

Let \(B\) be a reverse-time suffix component admitting \(k\ge3\) **causally sealed** chronological rooted tree arms \(B_1,\ldots,B_k\), each with exactly one outside-\(X\) root that is complete for its own arm. All root-to-root calls touch only the roots, and every internal arm call precedes all core calls incident to its own root; unrelated root calls may interleave.

Assume the full original fixed-order schedule succeeds. Then

\[
\boxed{|X|\ge2^k.}
\]

**Proof.** Let \(G_j=A\cap B_j\cap X\), \(j=1,\ldots,k\). By causal sealing and full temporal source-target compatibility at the **original midpoint**, each \(G_j\) is nonempty and collectively receives every \(A\)-secret. No \(X\) participant is touched by the final \(A\) cycle call, so those covers already hold at the end of the tree \(T\).

Adjoin the **singleton designated recipient group** \(G_0=\{u\}\), which also covers all \(A\)-secrets at the end of \(T\). The \(k+1\) groups \(G_0,G_1,\ldots,G_k\) are disjoint, and any other vertices are arbitrary unused helpers. The Stage 11/15 helper-robust chronological tree-cover bound implies

\[
|X|+1\ge2^{(k+1)-1}=2^k.
\]

If equality held, Stage 15's **helper-robust equality rigidity** forces every \(x\in G_j\) to have an original \(A\)-secret *private* to \(x\) within \(G_j\). Exact crossing with **every** reverse \(B_j\)-target forces \(x\) to be a complete reversed-tree-arm collector of \(B_j\). Each tree arm has at most two complete collectors, one of which is its outside-\(X\) root. Thus \(G_j\) contains at most one vertex for every \(j\), implying \(|X|\le k\). This contradicts equality \(|X|=2^k-1>k\) for \(k\ge3\).

Since all counts are integral, \(|X|+1\ge2^k+1\), so \(|X|\ge2^k\). QED.

This is an **all-\(n\) human proof**, not a claim about a finite computation or about strict all-arms-before-all-core order.

## Lemma B — A single size-two off-corner supplies the pre-terminal collector

Assume the hypothetical both-cyclic original \(3\times3\) split and \(m_{31}=2\). By Bumby's first original suffix-contact spine, the two complete reverse-time collectors of the suffix tree \(Q_1\) are in prefix tree rows \(P_1,P_2\); hence neither of the two people in \(P_3\cap Q_1\) is a complete reverse-time collector of \(Q_1\).

For the full original gossip to reach every \(Q_1\) target from every \(P_3\) source, the **two-vertex temporal crossing lemma** then forces **both people in \(P_3\cap Q_1\)** to be complete prefix collectors of \(P_3\).

The original final \(P_3\) contact has one endpoint in \(Q_1\) and one in \(Q_2\). Hence at least one of those **two distinct complete \(Q_1\)-cell collectors** is **not touched by the final call**. That participant was already complete at the end of \(P_3\)'s earlier chronological spanning tree. Since this person belongs to \(Q_1\), they are outside the center \(X=P_3\cap Q_3\).

Exactly the same reasoning works when \(m_{32}=2\). QED.

**Important timing discipline:** The lemma does **not** assume *both* off-corner collectors were complete before the final contact. It extracts precisely one untouched outsider collector, which is sufficient for Lemma A.

## Theorem — Three size-two off-corner cells force \(m_{33}\ge16\)

If the fixed original shortest successful schedule had both halves cyclic and

\[
m_{13}=m_{23}=2,\qquad (m_{31}=2\ \text{OR}\ m_{32}=2),
\]

then \(Q_3\) has **four** complete reverse-time collectors outside \(X=P_3\cap Q_3\), as proved via the two-point crossing and Bumby's spine in [Stage 14](../v3.1/CAUSAL_FOUR_ARM_BRIDGE.md). Hence \(Q_3\) is a **causally sealed four-arm** component in its *actual reversed local chronology*. Lemma B gives a complete outside-\(X\) collector at the end of the preceding tree of \(P_3\). Lemma A with \(A=P_3\), \(B=Q_3\), \(k=4\) implies

\[
\boxed{m_{33}\ge16.}
\]

Time reversal gives the separate symmetric implication

\[
\boxed{m_{31}=m_{32}=2,\quad (m_{13}=2\ \text{OR}\ m_{23}=2)
\ \Longrightarrow\ m_{33}\ge16.}
\]

**Scope contrasts:**
- One off-corner **pair** \(2,2\) but the other pair **both at least 3**: Stage 15 gives \(m_{33}\ge9\).
- One pair \(2,2\) and **exactly one** entry of the other pair 2: new Stage 16 gives \(m_{33}\ge16\).
- All **four** off-corner entries 2: Stage 14 gives the **stronger** \(m_{33}\ge64\).
- Neither pair \(2,2\): none of these center-size bounds is established, even if individual entries equal 2.

No assumptions are imposed on the four positive \(2\times2\) corner cell multiplicities.

### Immediate size consequences

The mixed three-size-two case needs \(4\) corner people, \(4\) in the first off-corner pair, at least \(2+3=5\) in the other pair, and at least \(16\) in the center. Therefore **\(n\ge29\)** in this subfamily.

If one pair is \(2,2\) and the opposite pair has **both sizes at least 3**, Stage 15 requires \(n\ge4+4+6+9=23\). If both pairs are \(2,2\), Stage 14 requires \(n\ge4+8+64=76\).

**Therefore, for every \(n\le22\), any hypothetical both-cyclic original schedule must have at least one size-\(\ge3\) cell in EACH off-corner pair.** This strengthens the Stage 15 finite frontier from \(n\le20\) to \(n\le22\). It does NOT exclude all such \(3\times3\) families at those sizes.

## Exact incidence prefilter, independent of chronology feasibility

For the baseline positive matrix \(M_0=((1,1,2),(1,1,2),(2,2,1))\), let \(k=n-13\) indistinguishable extra occupants be allocated among the nine **labelled** cells. The new exact necessary size-only test is:

- both off-corner pairs \(2,2\): center \(\ge64\);
- exactly one pair \(2,2\), with at least one 2 in the other pair: center \(\ge16\);
- exactly one pair \(2,2\), with the other two entries \(\ge3\): center \(\ge9\);
- neither pair \(2,2\): no added center threshold from Stages 14–16.

[Independent counter](count_mixed_arm_profiles.py) implements both exhaustive weak-composition enumeration and a **separate five-class generating-function count**: four corner extra occupancies contribute \((1-z)^{-4}\), while each off-corner *pair* has types \(0=(0,0)\), \(1=(0,a>0)\) or \((a>0,0)\), \(2=(a>0,b>0)\) with generating functions \(1\), \(2z/(1-z)\), \(z^2/(1-z)^2\). The center adds its type-dependent minimum excess occupancy. For \(n=13,\ldots,26\), the two independently implemented counting algorithms agree exactly; the latter extends to larger \(n\).

Some **labelled incidence** results (not counts of actual schedules):

| n | Raw positive \(3\times3\) sizes | Stage 15 survivors | Stage 16 survivors |
|---|---:|---:|---:|
| 18 | 1,287 | 489 | 489 |
| 19 | 3,003 | 1,365 | 1,365 |
| 20 | 6,435 | 3,333 | 3,333 |
| 21 | 12,870 | 7,359 | 7,359 |
| 22 | 24,310 | 15,019 | 15,015 |
| 23 | 43,758 | 28,769 | 28,745 |
| 24 | 75,582 | 52,293 | 52,209 |

The new bound is strictly stronger starting at \(n=22\) among raw incidence sizes. No count should be described as a genuine 2n−4-call chronology or a proved size-\(n\) conjecture certificate.

## Adversarial boundary and historical caution

The new \(m_{33}\ge16\) theorem depends critically on *both* (i) four collectors in one unicyclic side supplying a sealed four-arm opposing interface and (ii) one **other-side** off-corner size-two cell supplying a full **pre-terminal** collector. Without (ii), the Stage 15 one-sided bound \(9\) is the proved threshold; without (i), no four-arm lower bound is available. The equality \(t=15\) is ruled out by exact private-secret crossing, not by an arbitrary claim that two roots alone enforce a globally strict four-phase order.

The numerical endpoint \(16\) is necessary, not known sharp or constructible in a successful global schedule. The proof uses Bumby 1981 and earlier project-specific lemmas and has **not** been checked by a formal proof assistant, nor vetted for novelty against the entire classical gossip literature (notably Labahn 1995 and Krumme 1996).

**Universal chronological half-forest:** OPEN. **Independent global counterexample:** NONE. **PR #1:** DRAFT, UNMERGED. **Publication:** HOLD.
