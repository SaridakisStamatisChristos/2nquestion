# Temporal Clique Research v0.7 — Pivot-Aware Structural Search

**Date:** 25 October 2026.  
**Research state:** reproducible finite certificates and a corrected empirical protocol; no new universal spanner theorem, no proof of the `2n−3` conjecture.  
**Originality state:** unverified for the specific finite seven-vertex certificates; known mechanisms are explicitly identified below.

## 1. Mathematical contract

Let `K_n` have one distinct label per undirected edge, and let temporal paths traverse edges in strictly increasing label order. A temporal spanner is a spanning edge-subgraph preserving temporal reachability of every ordered vertex pair. We study (i) the minimum number of retained edges and (ii) the minimum static treewidth of any temporally connected subgraph.

The **main open question** is whether all such cliques have a spanner using at most `2n−3` edges. Casteigts' open-problems page, last updated September 22, 2026, lists the problem as unsolved and reports exhaustive computational confirmation up to n=8.

## 2. Reproduction of v0.6 and its precise implication

Reran the standalone v0.6 Python checker on the six-vertex explicit chronology. Its 1,215 labelled spanning 2-trees contain zero temporally connected members. An eight-edge spanner exists with exact treewidth three. The eight-edge witness is also **2-degenerate**, verified by k-core analysis. Thus "2-degenerate" and "treewidth at most 2" **must not be conflated**: v0.6 is not a counterexample to the 2025 conjectural existence of 2-arch spanners.

## 3. New independently enumerated 3-tree catalogues

Constructed every labelled spanning 3-tree recursively from a 4-clique by attaching a new vertex to a prior triangle. Deduplicated by edge bit masks. Counts match the established labelled k-tree enumeration formula:

| n | 3-trees |
|--:|--:|
| 7 | 5,915 |
| 8 | 229,376 |

For each temporal ordering, temporal connectivity was checked using information propagation: each vertex initially knows its own source bit, and contact (u,v) replaces both endpoint bitsets by their union. All n vertices must end with all n source bits. This is equivalent to preservation of every ordered-pair strictly increasing journey.

100 seeded uniformly shuffled chronologies at each n=7 and n=8 admitted at least one 3-tree spanner. **This says nothing universal.**

Adversarial local search found, among other schedules, one 7-vertex chronology admitting 125 valid spanning 3-trees and an 8-vertex chronology admitting 1,296. But the 7-vertex schedule proved to be pivotable; minimizing raw 3-tree count is not an adequate hardness measure.

## 4. Crucial protocol correction: filter pivotable graphs

Definition from Carnevale–Casteigts–Corsini (SAND 2025): an edge e=(u,v) is a pivot if every source reaches e by its contact time and e can reach every destination thereafter. For edge-unique chronologies, this can be checked exactly: before e the union of information sets at u and v must contain all sources; starting at both endpoints immediately after e, the suffix contacts must reach all destinations.

Random seeded testing (`mt19937` seed 42, C++17):

| n | Samples | Pivotable | Non-pivotable |
|--:|--:|--:|--:|
| 7 | 10,000 | 9,822 | 178 |
| 8 | 600 | 598 | 2 |

These are **empirical frequencies at specific sizes**, not an asymptotic probability theorem. Pivotability itself and its `2n−3`-edge implication are **prior art**. Uniformly random inputs heavily oversample this already tractable structural case.

## 5. Two fully specified hard seven-vertex schedules

### A. Pivotable schedule with a unique minimum spanner

Chronological edges:

```
(3,6) (1,6) (0,6) (5,6) (0,3) (2,6) (4,6)
(0,1) (3,5) (0,5) (1,2) (1,5) (0,2) (0,4)
(1,3) (2,3) (1,4) (2,5) (4,5) (2,4) (3,4)
```

A pivot exists at contact time 7: edge (4,6). Independent Python enumeration found:

- 0 spanners of size 10;
- **exactly one** spanner of size 11, with chronological indices (1-based) `[1,2,3,4,6,7,14,17,19,20,21]`;
- exact static treewidth **2** for that unique spanner.

The classical `2n−4` lower bound excludes smaller sizes.

### B. Non-pivotable schedule with three minimum spanners and treewidth obstruction

Chronological edges:

```
(3,6) (5,6) (4,6) (3,4) (1,4) (0,6) (2,3)
(3,5) (0,3) (2,5) (2,4) (1,6) (4,5) (0,5)
(1,3) (1,5) (0,4) (2,6) (0,1) (1,2) (0,2)
```

- No pivot edge (independent source-reachability check).
- 0 spanners of size 9, **exactly three** spanners of size 10.
- Their 1-based chronological index sets are:
  - `[2,5,6,7,9,11,15,16,17,18]`
  - `[2,5,6,7,9,12,15,16,17,18]`
  - `[2,5,6,7,11,12,15,16,17,18]`
- Each has exact static treewidth 3 (enumeration of all 7! elimination orders).
- An independent, constructive catalogue of **27,951** labelled spanning 2-trees contains **zero** temporally connected members. Therefore every temporally connected spanning subgraph has treewidth at least 3, while the listed size-10 spanners establish equality.
- The separate full 3-tree enumeration finds **130** temporally connected 3-trees for this schedule.

These exact finite computations validate the proposed POD `2n−4` value for **this one** non-pivotable K7 ordering; they do not establish POD for general n. Moreover, the v0.6 K6 already established a smaller treewidth-2 obstruction, so this K7 instance is not itself a new asymptotic separation.

## 6. Knowledge Nexus: novelty and contradiction ledger

| Claim | State | Evidence / dependency | Critical gap |
|---|---|---|---|
| Every temporal clique has at most `2n−3` edges in some spanner | OPEN | Casteigts 2026 open problem | Universal proof or certified n>=9 counterexample |
| Every temporal clique has a spanner of treewidth <=2 | REFUTED | v0.6 explicit K6 exhaustive certificate | None for refutation |
| Every temporal clique has a spanner of treewidth <=3 | HYPOTHETICAL | This turn's finite n=7,8 surveys | No universal proof; no certified counterexample |
| Pivotable temporal clique admits `2n−3` spanner | ESTABLISHED PRIOR ART | SAND 2025, Section 5 | None |
| Non-pivotable temporal cliques always attain `2n−4` edges (POD) | HYPOTHETICAL | Earlier bounded tests and new K7 exact case | n>=9 proof/counterexample |
| v0.6 8-edge graph is 2-degenerate despite treewidth 3 | VERIFIED FINITE FACT | Graph core calculation and v0.6 certificate | Not publication-level novelty |
| Seven-vertex nonpivot schedule above has min size 10 and min treewidth 3 | VERIFIED FINITE FACT | Independent enumerations | Scholarly priority not verified |

## 7. Next high-information research work

1. Build a deterministic generator of *non-pivotable and non-1/2/3-hop-dismountable* temporal cliques rather than accepting uniform random schedules.
2. For n=8 and 9, optimize not just the number of valid 3-trees, but the minimum cardinality of a spanner among the **non-pivotable** instances, with a reliable complete exact oracle or certified MILP bounds.
3. To challenge bounded treewidth, search for an instance admitting no spanning 3-tree (rather than merely one with few such trees). Any witness should be independently certified by complete 3-tree enumeration or an exact formulation.
4. If such a counterexample exists, examine whether it scales through a structure-preserving composition; otherwise concentrate on an inductive 3-tree existence proof.
5. Keep `2n−3` as the primary contribution target. Treewidth-3 even if true gives only `3n−6` and would need its own scholarly priority investigation before publication.

## 8. Reproduction

C++ commands from this package's `code/` directory:

```bash
g++ -std=c++17 -O3 probe_3trees.cpp -o probe_3trees
./probe_3trees 7 100 42
./probe_3trees 8 100 42
g++ -std=c++17 -O3 nonpivot_3trees.cpp -o nonpivot_3trees
./nonpivot_3trees 7 10000 42
./nonpivot_3trees 8 600 42
g++ -std=c++17 -O3 anneal_nonpivot.cpp -o anneal_nonpivot
./anneal_nonpivot 7 30000 42
g++ -std=c++17 -O3 exact_budget7.cpp -o exact_budget7
./exact_budget7 7
g++ -std=c++17 -O3 exact_nonpivot7.cpp -o exact_nonpivot7
./exact_nonpivot7 7
python independent_v07.py
python two_tree_probe_np7.py
```

C++ RNG and execution order are reproducible on compatible libstdc++/compiler builds with the pinned seed, not guaranteed cross-language/cross-library bit-identical. Independent Python scripts use complete enumeration and no random seeds. Tested in the current container with C++17 g++ and Python 3.

## 9. Prior art

- Arnaud Casteigts, *Open questions in temporal graphs*, updated 2026-09-22: https://arnaudcasteigts.net/blog/open-problems.html
- Daniele Carnevale, Arnaud Casteigts, Timothée Corsini (2025), *Dismountability in Temporal Cliques Revisited*, SAND 2025: https://doi.org/10.4230/LIPIcs.SAND.2025.6 (especially Section 5 and concluding discussion of 2-arch spanners).
- Júlia Baligács (2026), *Temporal Cliques Admit Linear Spanners*: https://arxiv.org/abs/2606.05156 . This supplies the published 7n upper bound.
- Júlia Baligács et al. (2026), *Almost Linear 3-Spanners of Temporal Cliques*: https://arxiv.org/abs/2609.02851 . This concerns **temporal stretch 3**, not **static treewidth 3**; these terms must never be conflated.

## Verdict

**Real research progress:** Verified a specific new non-pivotable K7 stress case, uncovered severe sampling bias in naive random testing, and refined the next falsification protocol. **No new universal theorem proved. No guaranteed scholarly novelty. No solution to the `2n−3` conjecture.**
