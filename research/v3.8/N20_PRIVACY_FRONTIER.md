# Stage 21 — \(n=20\) privacy frontier: 221 necessary matrices → 52, in 13 orbits

**28 October 2026.** New exact finite local enumeration and a complete, conservative incidence necessary-condition filter. The **unrestricted original chronological half-forest conjecture at \(n=20\)** remains OPEN; **none** of the 52 surviving labelled matrices is asserted to be a valid full 36-call original chronology. PR #1 remains DRAFT/OPEN/UNMERGED. Publication HOLD. No formal proof assistant/referee certification.

## Source and implication contract

The exact target is the original, non-reordered chronological half-forest conjecture for shortest successful distinct-call bidirectional gossip schedules. Assume both original \(n-2\) halves cyclic; by Bumby's Theorem 3 their original prefix components are \(P_1,P_2\) closed trees and \(P_3\) unicyclic, and reversed suffix components \(Q_1,Q_2\) closed trees and \(Q_3\) unicyclic. Define \(m_{ij}=|P_i\cap Q_j|\), all nine cells positive, four off-corners \(\ge2\), last contacts of each original prefix tree across \(Q_1,Q_2\) and last contacts of each reversed suffix tree across \(P_1,P_2\).

The following previously established source-constrained claims are invoked without conflating rearranged schedules: [Stage 18 all-n \(|P_3|,|Q_3|\ge9\)](../v3.5/FOUR_LEAF_STAR_GLOBAL_EIGHT_EXCLUSION.md); [Stage 19 exact privacy exclusion and finite \(n=19\) frontier](../v3.6/SMALL_TREE_PRIVACY_N19_FRONTIER.md); and [Stage 20 clarified helper-tolerant one-sided causal four-arm theorem](../v3.7/N19_ORIGINAL_CHRONOLOGY_THEOREM.md). If either unicyclic component has FOUR terminal complete collectors **outside the central cell \(X=P_3\cap Q_3\)**, the other cyclic component's spanning tree and the four causal arm groups force \(|X|\ge9\), **even if extra arm non-root participants lie outside X**. The precise helper-tolerant proof is Stage 20 Lemma 20.0.

## Lemma 21.1 — complete privacy histograms for the additional small tree classes

For a labelled chronological tree with \(v=a+b+c\) people and \(v-1\) distinct calls, partition vertices into groups \(G_0,G_1,G_2\) of sizes \((a,b,c)\). Require (i) the LAST actual call joins \(G_0\) to \(G_1\), and (ii) EVERY one of the three groups collectively knows ALL \(v\) original secrets at termination. A member \(z\in G_2\) is *private* if there exists a T-secret known by z and no other G2 member.

The following histograms are exact for the **additional six- and seven-person classes** needed for \(n=20\). [C++17 exhaustive enumerator](exact_seven_tree_privacy.cpp) produces every labelled tree with Prüfer words and every chronological edge order whose final contact joins the first two groups, replays union of singleton secret bitmasks, validates all three group covers, and counts private third-group recipients.

| Group sizes (a,b,c) | Vertices | Complete three-group chronological histories | Histograms: private receivers → histories | Minimum |
|---|---:|---:|---|---:|
| (1,1,5) | 7 | 57,600 | 1→24,000; 2→33,600 | **1** |
| (1,2,4) | 7 | 78,720 | 1→9,600; 2→59,520; 3→9,600 | **1** |
| (2,1,4) | 7 | 78,720 | 1→9,600; 2→59,520; 3→9,600 | **1** |
| (1,3,3) | 7 | 59,040 | 2→51,840; 3→7,200 | **2** |
| (3,1,3) | 7 | 59,040 | 2→51,840; 3→7,200 | **2** |
| (2,2,3) | 7 | 115,200 | 2→88,320; 3→26,880 | **2** |
| (1,3,2) | 6 | 864 | 2→864 | **2** |
| (3,1,2) | 6 | 864 | 2→864 | **2** |
| (2,2,2) | 6 | 1,664 | 2→1,664 | **2** |

Stage 19 already independently exhaustively checked the remaining necessary groups, including (1,1,2) min2, (1,1,3) min2, (1,1,4) min1, (1,2,2) min2, (1,2,3) min2 and their row/column reversals. The corpus of 16 exact group classes is all that is needed for the present \(n=20\) SIZE-ONLY filter. It is NOT a universal tree privacy theorem for arbitrary group sizes; in particular the one-private examples above actively refute a naive blanket two-private assertion.

## Lemma 21.2 — exact four-private necessity and resulting \(n=20\) reduction

For each original prefix tree row \(P_i\) (\(i=1,2\)), every person private in the third recipient cell \(P_i\cap Q_3\) becomes a **complete reversed-suffix collector of \(Q_3\)** by exact fixed-midpoint source/target crossing. Thus the sum of the two row-minimum privacy counts is a lower bound on the number of distinct complete Q3 collectors outside the center. Similarly the sum of the two reversed suffix-tree column minima lower-bounds the number of complete prefix P3 collectors outside X. If EITHER minimum sum is at least FOUR, Stage 20 Lemma 20.0 forces \(|X|\ge9\).

At \(n=20\), after Stage 18's all-n structural size constraints, ALL possible centers satisfy \(|X|\le6\). Therefore a necessary matrix must have BOTH privacy-minimum sums at most three.

Independent [nine-dimensional positive-cell occupancy enumeration](count_n20_privacy_orbits.py) generates all \(\binom{15}{8}=6435\) labelled baseline 3×3 matrices with all four off-corners \(\ge2\), applies the Stage 18 universal inequalities and Stage 15 size-two-pair restrictions to leave 221, and then applies the above exhaustive *finite local minimum* table to exclude 169 more:

\[
\boxed{221-169=52\text{ labelled necessary incidence matrices}.}
\]

Row/column swaps of the two tree prefix/suffix components are the only equivalence used. Exactly **13** \(S_2\times S_2\) orbits survive, each containing four labelled matrices. The centers of the surviving labelled matrices have the following distribution:

| Center size \(m_{33}\) | Labelled survivors |
|---|---:|
| 2 | 16 |
| 3 | 32 |
| 4 | 4 |
| **Total** | **52** |

For full independent falsification and deterministic regeneration of these 13 candidates, the script prints each canonical 3×3 representative. No tree call order or global original gossip chronology is asserted for any of them.

## Research and assurance decision

**Established:** The precise small chronological trees have the pinned private-recipient histograms (complete labelled exhaustion), and the \(n=20\) incidence list has at most 52 labelled necessary profiles / 13 component-index orbits, assuming the historically grounded all-n Stage18/20 causal covering theorems.

**Unestablished:** Which, if any, of the 13 surviving incidence orbits admits pairwise-distinct original 36-call chronology realizing full gossip and making both actual first/last 18-call halves cyclic. No original schedule, counterexample, or complete \(n=20\) proof has been produced. The **unrestricted** conjecture remains OPEN for \(n\ge20\), despite the \(n=18,19\) human proofs and finite regressions.

**Next falsification strategy:** eliminate each 13-orbit candidate by *both-sided* chronological support compatibility, using explicit last-contact closed-tree spine and independent original-order replay; beware that a locally feasible unicyclic 2/4/3 example may still be globally impossible. Do not infer existence from incidence counts, or universal private minima from six-/seven-person data.

**Gate:** PR #1 DRAFT and UNMERGED, submission HOLD; formal assistant and historical novelty checks remain outstanding.
