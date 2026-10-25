# Temporal Clique Research v0.6 — A Minimal Treewidth-2 Obstruction

**Date:** 2026-10-25. **Status:** Exact finite mathematical/computational result; no resolution of the universal `2n-3` conjecture. **Novelty priority:** not established.

## Executive finding

For a complete simple properly timed graph with strictly increasing journeys, the following precise finite statement has been established by exhaustive computation:

> There exists an injectively edge-labelled temporal clique on six vertices such that no temporally connected spanning subgraph has static treewidth at most two. Nevertheless, it possesses an eight-edge temporally connected spanning subgraph of treewidth exactly three, and eight edges are optimal. No such counterexample exists on at most five vertices.

The first part refutes a possible stronger universal hypothesis, **that every temporal clique has a temporal spanner of treewidth ≤2**. It **does not refute** the `2n−3` spanner conjecture: eight edges is even better than nine for `n=6`.

## Concrete witness

Vertices: `0,1,2,3,4,5`. Strictly chronological contacts, times 1..15:

```
 t  endpoints
 1  (3,5)
 2  (0,5)
 3  (4,5)
 4  (0,2)
 5  (1,3)
 6  (2,3)
 7  (0,3)
 8  (1,2)
 9  (1,5)
10  (0,4)
11  (0,1)
12  (2,5)
13  (3,4)
14  (2,4)
15  (1,4)
```

One eight-contact spanner retains times `{3,4,5,7,9,11,12,13}`. An **independent source-by-source reachability checker** verified it reaches all six vertices from every source. Its exact static treewidth is three, verified by enumerating all 720 vertex elimination orders with fill-in.

No smaller feasible subset exists: direct enumeration of every edge subset with size below eight found none. The general `2n−4` lower bound gives the same conclusion, but the enumeration is an independent finite certificate.

## Why a 2-tree test certifies the treewidth assertion

A finite graph has treewidth at most 2 if and only if it is a subgraph of a 2-tree on the same vertex set (for n≥3). Every spanning 2-tree on 6 labelled vertices is formed from a triangle by repeatedly adding one vertex adjacent to both endpoints of an existing edge. A 2-tree on n≥3 vertices has exactly `2n−3` edges. Since temporal reachability is monotone under adding already-timed edges, if any spanner of treewidth ≤2 existed, at least one spanning 2-tree would also be a temporal spanner.

The independent constructive enumerator produced exactly **1,215** distinct labelled spanning 2-trees on the six vertices. The direct oracle found **zero** temporally connected ones. The original C++ adversarial probe used an unrelated recursive degree-two elimination test and independently obtained the same 1,215 and zero outcomes. Thus treewidth at most two is impossible for this specific chronology.

A compact exact certificate restricts the check to ten ordered reachability requests:

```
(0,5), (1,0), (1,3), (1,5), (2,1),
(2,3), (2,5), (4,0), (4,2), (4,3).
```

Every one of the 1,215 candidate 2-trees fails at least one of these ten requests. An integer set-cover solver certified that ten is the minimum number of requests needed *for this particular candidate-family-cover formulation*. This is **not** a claim of a minimum human-readable proof length.

## Minimality in number of vertices

All edge-permutation schedules of K4 and K5 were enumerated by C++. Because chronology changes only when two *incident* edges exchange order, we can quotient permutations by swaps of consecutive vertex-disjoint events. Two chronologies are in the same equivalence class precisely if their relative orders agree on every pair of incident edges. A temporal path consists of successive incident edges, hence every retained-edge subgraph has the same temporal reachability under such chronologies.

Enumeration results:

| n | All edge permutations | Relative-order classes | Labelled 2-trees | Classes with no temporally connected 2-tree |
|--:|--:|--:|--:|--:|
| 4 | 720 | 426 | 6 | 0 |
| 5 | 3,628,800 | 542,880 | 70 | 0 |

For n≤3 the claim is trivial: complete graphs have treewidth ≤2. Thus n=6 is the **smallest possible size** of a proper temporal clique forcing static spanner treewidth ≥3, within the stated model. The finite verification can be rerun from source; this is **not** an unbounded mathematical claim.

## Previous-research cross-check

The earlier K6 counterexample in v0.1, which ruled out star-plus-tree temporal spanners, was also subjected to the new independent verifier. It likewise admits **no** spanning temporal 2-tree. Hence the phenomenon is not unique to the v0.6 witness. This does not mean the broader treewidth obstruction was recognized or claimed in the v0.1 report.

## Novelty and scope

- **Established prior mechanisms:** temporal spanners, 1/2/3-hop dismountability, pivotability, and 2-arch (maximal 2-degenerate) spanners. In particular, **2-degenerate** is *not* the same as **treewidth at most two**; some 2-degenerate graphs have arbitrarily large treewidth. Do not present this result as a counterexample to the SAND 2025 discussion of 2-arch spanners.
- **Established analogous encoding:** relative order of incident temporal edges (2026 model-checking work) and the classical adjacent-commutation/linear-extension principle. The quotient construction is useful here but **not independently new**.
- **Finite result checked here:** an explicit smallest-order obstruction to temporal spanners of treewidth ≤2. Initial targeted literature searches found no statement of this exact separation. This does **not** establish scholarly priority or publication-grade originality.
- **Open:** universal `2n−3` bound, Pivot–Optimal Dichotomy, whether some fixed k≥3 suffices to bound the *treewidth* of a temporal spanner for every temporal clique, and whether a fixed-k bounded-treewidth spanner can be found with ≤`2n−3` edges.

If a universal bounded-treewidth-three spanner theorem could be proved, completing such a spanner to a spanning 3-tree would give a general upper bound `3n−6` (for n≥4), stronger than the published `7n` and the discussed `6n` refinement. **No evidence provided here establishes that conjecture**, and the existing n=6 witness only rules out treewidth two.

## Code and execution

- `trace_classes.cpp` — exhaustive counts of orderings modulo incident-edge ordering, and exact optimum histograms for K4/K5.
- `trace_twotree.cpp` — exhaustive evidence that every K4 and K5 ordering has a temporal 2-tree spanner.
- `twotree_probe.cpp` — deterministic adversarial generation of the K6 witness; independently enumerates 2-trees by degree-2 elimination.
- `independent_verify.py` — constructs 2-trees by *forward augmentation*, checks all directed temporal paths using distinct source-by-source reachability, confirms the eight-edge optimum, calculates exact treewidth.
- `certificate_pairs.py` — checks reachability obstructions for all 1,215 candidates and selects the smallest set of ordered pairs covering all failures (SciPy/HiGHS MILP).
- `verification.log` and `reachability_certificate.txt` — recorded commands/results. Linux g++ 14.2.0, Python 3.13.5.

Re-run:

```bash
g++ -std=c++17 -O3 trace_classes.cpp -o trace_classes
./trace_classes 4 && ./trace_classes 5
g++ -std=c++17 -O3 trace_twotree.cpp -o trace_twotree
./trace_twotree 4 && ./trace_twotree 5
g++ -std=c++17 -O3 twotree_probe.cpp -o twotree_probe
./twotree_probe 20000
python independent_verify.py
python certificate_pairs.py  # additionally requires scipy/numpy
```

## Sources and priority boundaries

1. A. Casteigts, *Open questions in temporal graphs* (updated Sep 22 2026): https://arnaudcasteigts.net/blog/open-problems.html
2. D. Carnevale, A. Casteigts, T. Corsini, *Dismountability in Temporal Cliques Revisited* (SAND 2025): https://doi.org/10.4230/LIPIcs.SAND.2025.6
3. S. Angrick et al., *How to Reduce Temporal Cliques to Find Sparse Spanners* (ESA 2024): https://doi.org/10.4230/LIPIcs.ESA.2024.11
4. J. Baligács, *Temporal Cliques Admit Linear Spanners* (2026): https://arxiv.org/abs/2606.05156
5. *FO and MSO Model Checking on Temporal Graphs* (SAND 2026; incident-edge order encoding): https://drops.dagstuhl.de/storage/00lipics/lipics-vol373-sand2026/html/LIPIcs.SAND.2026.9/LIPIcs.SAND.2026.9.html

## Verdict

**Mathematically certified finite structural obstruction: yes** (exhaustive verification with source). **New universal theorem: no.** **Established scholarly priority: no.** **Main strong conjecture resolved: no.**
