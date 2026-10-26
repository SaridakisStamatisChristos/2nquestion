# Stage 6 — Unbounded chronological half-forest question: reduction and n=17 frontier

**Research status, 26 October 2026:** finite structural verification **PASS**, novel/general all-n theorem **OPEN**, n=17 complete theorem **OPEN**, historical originality **UNRESOLVED**, submission decision **HOLD**.

## 1. Canonical unrestricted problem

Let \(S=(e_1,\ldots,e_{2n-4})\) be a successful shortest bidirectional telephone-gossip schedule with pairwise-distinct unordered contacts, \(n\ge4\). Let \(L\) and \(R\) be its unchanged first and last \(n-2\) edges. Investigate

\[
\mathcal H:\qquad \text{at least one of }L,R\text{ has an acyclic underlying static graph}.
\]

Computationally supported for all \(4\le n\le16\) by the [complete earlier certificate](../v2.2/STATUS.md). **No proof or counterexample for arbitrary \(n\)** has been established. In particular, \(\mathcal H\) is distinct from static-graph edge decompositions, reordering existence and the fixed-timestamp temporal-clique 2n-3 conjecture.

## 2. New structural result: rectangular 3-by-4 requires at least 18 vertices

For any hypothetical both-cyclic schedule, let \(r\) and \(s\) be the numbers of prefix and suffix connected components; all \(rs\) intersections are nonempty, the total cycle rank in each half is \(r-2\), respectively \(s-2\).

**Proposition (human proof).** If \(r=3,s=4\) in such a schedule, \(n\ge18\). By reversing chronology, the same bound holds for \(r=4,s=3\).

**Proof.** The three prefix components comprise exactly one unicyclic component \(C\) and two tree components \(A,B\). Each tree row meets all four suffix components, and a singleton intersection with any suffix component requires a complete midpoint collector at that vertex. Only endpoints of the last internal tree call can be complete, so each tree row contains at most two singleton cells; hence it uses at least two vertices in excess of its baseline four intersections.

The suffix graph with four components has total cycle rank two; therefore **at least two suffix components are trees**. Write \(T\) for these suffix-tree columns. When a suffix-tree column \(Q\) has a singleton intersection with \(C\), the established single-source tree-entry lemma forces one complete prefix collector in each of its intersections with \(A\) and \(B\). Conversely, a suffix tree has at most two complete reverse collectors, so it cannot meet **three** prefix components in singleton cells.

Assume for contradiction \(n\le17\). There are twelve mandatory positive grid cells, leaving at most five extra vertices. Rows \(A,B\) already consume four extras, so row \(C\) has at most one.

**Case I: \(C\) has one extra vertex.** Then each \(A,B\) has **exactly two extras**. Since \(|T|\ge2\), there is some suffix-tree column \(Q\in T\) with a singleton intersection with \(C\). The single-source lemma requires a collector of \(A\) in \(A\cap Q\). If this cell were non-singleton, then \(A\), which has exactly two extras in four cells, would also have at least two singleton cells *elsewhere*. These require two further distinct collectors, giving three, impossible. Thus \(A\cap Q\) must be singleton; likewise \(B\cap Q\) is singleton. But \(Q\) now has three singleton intersections, requiring three reverse collectors. Contradiction.

**Case II: \(C\) has no extras.** It is singleton in every suffix column. If there are three or more suffix-tree columns, the single-source entry lemma demands at least three distinct prefix collectors in \(A\), impossible. Therefore exactly two suffix components are trees, with the other two cyclic. Each \(A,B\) must have a collector in **each** tree column, exhausting its two-collector capacity. Hence every cell of \(A,B\) in the **two cyclic suffix columns** must be non-singleton, costing at least four extras overall. For either suffix-tree column, its \(C\) singleton forbids both \(A,B\) also being singleton (else three reverse collectors); therefore each of the two tree columns needs another extra vertex in \(A\) or \(B\). This costs at least six extras in total, but only five are available. Contradiction. Hence \(n\ge18\). QED.

The proof relies only on the explicitly documented collector and single-source lemmas of [v2.0](../v2.0/MANUSCRIPT.md), not on the machine search. A *separate exhaustive check* independently enumerates all marked positive 3x4 matrices at n=16 and 17 with both extra-vertex multisets and positive divider-compositions. It tests both forward and time-reversed necessary collector constraints:

| n | marked grid/rank configurations | pass forward collectors | pass full necessary collectors |
|---|---:|---:|---:|
| 16 | 40,950 | 18 | 0 |
| 17 | 131,040 | 396 | 0 |

**Reproduce:** \`python3 research/v2.3/n17_structural.py\`.

## 3. Consequence: all n=17 both-cyclic candidates have 3x3 incidence

For \(r,s\ge3\), an \(r\times s\) incidence matrix needs at least \(rs\) vertices. If either dimension is three and the other is five or greater, the previous two-prefix-tree bound \(n\ge3s+2(s-2)=5s-4\) implies \(n\ge21\). For \(r=s=4\), n=17 gives at most one extra vertex beyond 16 singleton cells; at least two prefix components are trees, each has at least three singleton intersections and thus requires at least three collectors, impossible. The new proposition rules out (3,4)/(4,3). Hence \(r=s=3\).

Two independent n17 square-grid generators, including equality of *all* canonical orbit multiplicities, establish:

| Checkpoint | n=17 |
|---|---:|
| eligible marked placements | 75,933 |
| basic collector/first-bridge survivors | 45,783 |
| strong singleton-entry survivors | 15,777 |
| surviving marked 3x3 symmetry classes | **256** |

**Important:** 256 means structural candidates awaiting temporal-profile exclusion. They are *not* 256 realizable both-cyclic schedules or counterexamples.

## 4. General all-n search equivalence: balanced event-order ideals

For each successful schedule, create a poset \(P_S\) on its uniquely identifiable contact events, where \(e_i\prec e_j\) when \(i<j\) and the calls share an endpoint; take transitive closure. A **balanced ideal** is a down-closed subset \(I\) of exactly \(n-2\) events.

**Lemma (all n, elementary).** Every linear extension of \(P_S\) is a successful chronology with exactly the same contacts. Every balanced ideal is the original prefix of some linear extension. Consequently:

\[
\exists \text{ a both-cyclic original split among extensions of }P_S
\iff
\exists I\triangleleft P_S,\ |I|=n-2:\quad
E(I)\text{ and }E(P_S\setminus I)\text{ both cyclic}.
\]

**Proof.** Incomparable events can be commuted across one another using adjacent swaps. Since calls sharing a vertex are comparable, any adjacent incomparable events have disjoint endpoints. Their knowledge-set updates commute, so every linear extension preserves information propagation and the final success. Conversely, any ideal can be ordered first using a linear extension of its restricted order and then a linear extension of the remaining events. Cycle ranks depend only on the sets of edges in the two halves. QED.

This is an *exact equivalence*, not a claim to have invented order-ideal theory. It is useful because it converts factorial chronological enumeration into checking the balanced ideals of realizable contact-event posets. For the historical eight-participant \(W_8\) witness:
- **51,200** valid linear extensions of the fixed contact-event order;
- only **6 balanced ideals**, with two yielding (0,0), two (0,1), two (1,0) prefix/suffix cycle ranks;
- no (1,1), hence no counterexample for that poset;
- two linear extensions with the SAME full poset and the SAME Labahn kernel can have distinct individual midpoint cycle ranks. Their common-poset property and those separate ranks persist under the classical two-call extension through n=17.

**Reproduce:** \`python3 research/v2.3/balanced_ideal_audit.py\`.

### Essential historical scope

The poset equivalence covers a *fixed realizable full event-poset* and all its linear extensions. It does **not** enumerate every admissible classical Labahn kernel, exceptional case or attachment/fringe configuration. Hence it does not demonstrate novelty independence from Labahn 1995; the fact that a kernel does not *uniquely determine the exact midpoint ranks* does not imply that the weaker at-least-one-forest condition fails to be a classical corollary.

## 5. Remaining proof obligations, in evidence order

1. **n=17:** Refute the 256 square-grid structural orbits using complete exact/sound optimistic profile domains, or extract and independently check a valid 30-call counterexample. Never call a relaxed CSP SAT assignment a gossip schedule.
2. **General n:** Analyze the residual \((r,s)\) families as n grows. A bounded \(r=s=3\) proof is not an all-n theorem; new rectangular cases become feasible under the present necessary-condition filters starting at n=18.
3. **Classical priority closure:** Lift Labahn's complete kernel families, exceptional kernels, fringe trees and admissible event-poset extensions into the balanced-ideal decision test. Verify the lift matches all small exhaustive chronology cases before making completeness or originality claims.
4. **Adversarial independent review:** Attack the single-source lemma, optimistic-domain soundness and orbit completeness; retain the distinction between machine checks and formal proof assistant verification.
5. **Publication:** Keep the finite n<=16 paper as a versioned working manuscript, maintain attribution for all old foundational components, and leave historical novelty and submission gate HOLD.

**Evidence decision:** The new rectangular exclusion and balanced-ideal reformulation are mathematically reasoned and backed by runnable CI. The unrestricted conjecture, all-classical-kernel implication closure, and genuine priority remain OPEN.
