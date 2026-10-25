# Research v1.0 — Chronological four-cycle cores: exact finite classification and falsification search

**Date:** 2026-10-25. **Main status:** universal `2n-3` temporal-clique spanner conjecture remains OPEN; Pivot–Optimal Dichotomy remains OPEN. **Novelty:** UNVERIFIED and close to existing minimum-gossip kernel literature. This is a research checkpoint, **not a breakthrough claim**.

## Formal question

A shortest *simple-contact* gossip protocol on `n >= 4` labelled vertices is a list of exactly `2n-4` **distinct** undirected edges, processed in the listed order, such that simultaneous information exchange over every selected contact makes all vertices know all initial sources. Every such list occurs as a subset of some injectively labelled temporal clique chronology (complete the omitted edges arbitrarily). By the classical minimum-gossip lower bound, such a list is cardinality-optimal.

A **chronological butterfly** is a selected four-cycle `ab, bc, cd, da`, ordered chronologically such that its *two earlier* edges are vertex-disjoint and its *two later* edges are vertex-disjoint. Equivalently, the opposite-edge pairs of the cycle are separated in time, with either opposite pair occurring before the other. The claim under test is:

> **BF(n):** Every shortest simple-contact gossip protocol on `n` vertices contains a chronological butterfly.

This is **not** the assertion that every input temporal clique has a `2n-4` spanner; in fact some need `2n-3`. BF is a *necessary pattern* in optimal-size witnesses, not an existence theorem.

## Exact finite proposition (exhaustive, not universal)

**BF(n) holds for every `4 <= n <= 6`.** The finite cases are certified by full enumeration of all contact lists of length `2n-4` having first edge `(0,1)`. Fixing that first edge is complete up to vertex relabeling, because any initial edge may be renamed `(0,1)` without affecting either reachability or butterfly existence. Remaining contacts range injectively over all `m-1` other edges, where `m=n(n-1)/2`. No other ordering equivalences, heuristic pruning, or undocumented symmetry reductions are used.

| n | examined sequences with first edge `(0,1)` | temporally connected shortest sequences | connected without butterfly |
|---:|---:|---:|---:|
| 4 | 60 | 4 | **0** |
| 5 | 15,120 | 324 | **0** |
| 6 | 17,297,280 | 83,808 | **0** |

To reproduce, compile `exhaustive_kernel.cpp` under a C++17 compiler and run for each n. The enumerator uses a chronological bitset information union; it inspects all length-`2n-4` distinct-edge protocols. A separately written Python oracle enumerated all 15,120 `n=5` sequences, verifying its 324 successful protocols, with no butterfly-free case. Two independently implemented source-wise and bitset reachability predicates also agreed across **8,000** random `n=4,...,11` subgraph tests.

**Evidence interpretation:** This is a finite computer-assisted theorem restricted to `n<=6` and simple contacts, with human-auditable exhaustive C++ code. It has **not** been formalized in a proof assistant. It does NOT prove BF for `n>=7`.

## Adversarial stochastic search

`kernel_walk.cpp` starts from a standard shortest four-chief gossip schedule and proposes swaps or replacements of its contacts; only still-connected distinct-edge schedules of length `2n-4` enter the search. A seeded Metropolis-style walk of **350,000 mutation proposals at each n=6,7,8,9,10** found no butterfly-free valid schedule. Across all five sizes, the smallest number of butterflies in a visited valid schedule was **one**. This constitutes a biased exploration of a connected component of schedule space, *not* random sampling of every possible minimum protocol, let alone proof of BF.

No novel universal theorem, impossibility lower bound, or improvement over the published `7n` (and reported `6n`) bound is established. The original `2n-3` problem and the POD assertion remain unresolved.

## Proof obligations and competing explanations

1. **Universal BF:** Prove or disprove BF for `n>=7` using a structural characterization of the temporal order of calls in minimum gossip schemes. One must not simply import the (static) four-cycle theorem; it guarantees an undirected 4-cycle, *not explicitly the opposite-pairs time pattern*.
2. **Priority:** Roger Labahn's 1995 *Kernels of minimum size gossip schemes* characterizes minimum gossip kernels and is close enough that BF may be an existing consequence. A literature audit must inspect that characterization before publication or novelty claims. The classical 1980/81 four-cycle theorems are also direct antecedents.
3. **Main theorem bridge:** Even universal BF would be only a necessary condition for a `2n-4` spanner. It could serve as a structurally justified branch-and-bound filter for POD searches, not prove `2n-3` on its own.
4. **Counterexample search:** To refute BF find a fully gossiping, distinct-contact `2n-4` sequence containing no chronological butterfly. To refute POD find a *nonpivotable full temporal clique* whose `2n-4` feasibility is **certifiably impossible**; a greedy or MILP timeout is UNKNOWN.

## Execution details

- Python: 3.13.5 standard-library-only for `independent_kernel_verify.py`.
- C++: GCC 14.2.0 with `-O3 -std=c++17`.
- Seeded walk: seed `20261025+n` for each `n`; 350,000 iterations.
- Results from chronological exhaustive enumeration are deterministic, independent of random seeds.

```sh
g++ -O3 -std=c++17 research/v1.0/exhaustive_kernel.cpp -o /tmp/verify_butterfly
for n in 4 5 6; do /tmp/verify_butterfly "$n"; done
python research/v1.0/independent_kernel_verify.py
g++ -O3 -std=c++17 research/v1.0/kernel_walk.cpp -o /tmp/attack_butterfly
for n in 6 7 8 9 10; do /tmp/attack_butterfly "$n" 350000; done
```

## Sources and originality boundary

- R. T. Bumby (1981), *A Problem with Telephones*, DOI: https://doi.org/10.1137/0602002 (four-cycle necessary in minimum schemes).
- D. J. Kleitman and J. B. Shearer (1980), *Further gossip problems*, DOI: https://doi.org/10.1016/0012-365X(80)90116-8 (four-cycle theorem, including partially one-way calls).
- R. Labahn (1995), *Kernels of minimum size gossip schemes*, DOI: https://doi.org/10.1016/0012-365X(94)00031-D (structural kernel characterization; chronological BF priority unknown).
- A. Casteigts, https://arnaudcasteigts.net/blog/open-problems.html (updated September 22, 2026): `2n-3` question remains open, `7n` universal bound, AI-assisted refinement to `6n` reported.
- J. Baligács (2026), https://arxiv.org/abs/2606.05156 (published `7n` constructive bound).

**Scientific verdict:** A rigorous finite classification and a new-to-this-project universal *candidate*, but **not a verified publication-level novelty or an open-problem solution**. Competing explanation—BF follows from established gossip-kernel theory—has not been eliminated.
