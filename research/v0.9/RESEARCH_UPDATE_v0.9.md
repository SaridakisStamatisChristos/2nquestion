# Research v0.9 — Incident-local exact formulation and hard K10 witnesses

**Date:** 25 October 2026. **Mathematical target:** universal `2n-3` temporal-clique spanner conjecture. **Verdict:** open; no counterexample or universal theorem found. POD (`non-pivotable => 2n-4`) likewise open.

## 1. Exact model (fixed edge chronology)

For a complete undirected graph on `n >= 2` vertices, let `e_1,...,e_m` be a permutation of its `m = n(n-1)/2` edges. A selected contact shares all knowledge between its endpoints; an omitted contact does nothing. Every node starts knowing one unique source. All-to-all temporal reachability is equivalent to all nodes knowing all sources by the last event.

For every vertex `v`, let its `n-1` incident events have their inherited chronological order. Set `y[s,v,r]` to the amount of information from source `s` known by `v` after its first `r` incident events (`r=0,...,n-1`), constrained in `[0,1]`; `x_t in {0,1}` chooses edge `e_t`.

For an event `e_t=(u,v)`, with incident indices `r_u,r_v` immediately *before* that event, let

`p = y[s,u,r_u]`, `q = y[s,v,r_v]`, `a = y[s,u,r_u+1]`, `b = y[s,v,r_v+1]`.

For every source impose:

```text
a >= p
a >= q + x_t - 1
a <= p + x_t
a <= p + q

b >= q
b >= p + x_t - 1
b <= q + x_t
b <= q + p
```

Initial states: `y[s,v,0] = 1` iff `s=v`, else `0`. Terminal requirements: `y[s,v,n-1] = 1` for every `(s,v)`. Minimize `sum_t x_t` or impose `sum_t x_t <= B` for a threshold test.

### Correctness theorem (proved for this formulation)

For a fixed integer selection `x`, all continuous states are uniquely forced to be binary and exactly equal the chronological gossip-propagation states. Proof by induction on `t`: prior to any event, states are binary by initialization; local states unchanged until their next incident event. If `x_t=0`, `a>=p`, `a<=p+x_t` force `a=p`; similarly `b=q`. If `x_t=1`, the inequalities imply `max(p,q)<=a<=p+q` and `max(p,q)<=b<=p+q`. For binary `p,q` and bounds `[0,1]`, these force `a=b=p OR q`. Thus after every incident event the state is its true Boolean information set. Terminal equalities hold exactly when every source reaches every vertex. Therefore MILP feasibility for budget `B` is logically equivalent to a temporal spanner of size at most `B`, and every integer solution includes a directly checkable edge witness.

**Size:** `m + n^3` variables, only `m` integer; exactly `8nm` recurrence inequalities plus one optional budget row, with variable bounds forcing `2n^2` initial/final equalities. The construction is `O(n^3)` in constraints and variables (not polynomial-time solution: MILP remains combinatorial). The model works even though state variables are only continuous. This formulation is an independently derived technical instrument; **no scholarly originality is asserted**, because local-time-expanded flow encodings and binary-selector linearizations are established optimization practices.

## 2. Independent finite validation

`verify_incident_milp.py` enumerates all candidate subgraphs as an independent brute-force oracle, searching by increasing cardinality, and compares the optimum with the MILP:

| n | tested chronological permutations | independently checked optimums | exact infeasibility checks at opt-1 | exact feasibility checks at opt |
|---|---:|---:|---:|---:|
| 3 | all 6 | 6 | 6 | 6 |
| 4 | all 720 | 720 | 30 | 30 |
| 5 | 120 seeded random | 120 | 30 | 30 |

All checks passed under Python 3.13, NumPy 2.3.5 and SciPy 1.17.0, with HiGHS as the scipy `milp` solver. This is validation of the implementation, **not** a proof of a universal spanner bound.

## 3. Nonpivotable hard instances

Three v0.8 hard `K9` chronologies (two historical and the adversarial example) were solved independently by this new MILP with budget 14. Each returned a validated 14-edge witness and solver status optimal, with elapsed times approximately 0.28, 3.24, and 2.60 seconds.

A targeted `K10` generator preserves the relative chronology among the nine original vertices and uniformly interleaves the new vertex's nine incident contacts (seed `2026102509`). From the first 45 generated extensions, six were nonpivotable according to a separate source-by-source pivot test. Each six has a validated 16-edge witness; the first five were discovered within a 3-second time budget (solver feasible-but-unproven at exit), and the sixth required a retry (9.39 seconds; returned optimal). **Since the established gossip lower bound is `2n-4`, all these finite 14-/16-edge witnesses are instance-optimal regardless of whether the MILP completed its search.**

`independent_check_v09.py` uses no MILP or historical checker code to validate the six K10 schedules, their nonpivotability, all chronological witnesses, reversal invariance, and independent vertex relabellings. All checks passed.

## 4. Falsification outcomes

- No certified `K9` or `K10` counterexample to POD was found.
- An initial 3-second budget failed to find a witness on one `K10`; it was **UNKNOWN**, never INFEASIBLE. A subsequent 18-second-budget call found a 16-edge witness, refuting the *heuristic* inference that the schedule required more than `2n-4` edges.
- The remaining constraints are universal: a valid single-instance witness does not prove `POD`, and failure of any finite-budget heuristic or solver is not a counterexample.

## 5. Priority and future proof obligations

The general bound of `7n` was proved by Baligács in 2026; Casteigts' open-problem page dated September 22, 2026 still lists `2n-3` as unresolved. The `2n-4` lower bound and four-cycle necessity for minimum-length gossip protocols are due to Bumby (1981). Dismountability, pivotability, and structure of non-dismountable cliques are described by Carnevale–Casteigts–Corsini (SAND 2025). The incident-local MILP is a verification tool, not a claimed independent novel result.

Primary open path: use this exact solver, independent reachability oracle, and adversarial generators to target *nonpivotable, non-{1,2,3}-hop-dismountable* cliques; seek either a mathematically proved universal reduction or an independently certified infeasible `2n-4` instance (POD refutation) or `2n-3` instance (main refutation). For solver `status=UNKNOWN` or a mere heuristic failure, no theorem can be inferred.

### References

- A. Casteigts, [Open questions in temporal graphs](https://arnaudcasteigts.net/blog/open-problems.html), updated 22 Sep 2026.
- J. Baligács, [Temporal Cliques Admit Linear Spanners](https://arxiv.org/abs/2606.05156), 2026.
- D. Carnevale, A. Casteigts, T. Corsini, [Dismountability in Temporal Cliques Revisited](https://doi.org/10.4230/LIPIcs.SAND.2025.6), 2025.
- R. T. Bumby, [A Problem with Telephones](https://doi.org/10.1137/0602002), 1981.
- F. Göbel, J. O. Cerdeira, H. J. Veldman, [Label-connected graphs and the gossip problem](https://doi.org/10.1016/0012-365X(91)90068-D), 1991. Distinguish *existence of a favorable chronology* from the fixed-chronology task here.

## 6. Reproduce

From the root, with `numpy` and `scipy` installed:

```bash
python research/v0.9/verify_incident_milp.py
python research/v0.9/independent_check_v09.py
python research/v0.9/incident_milp.py --n 9 --seed 17 --upper 14 --seconds 15
# The targeted K10 generation may take considerably longer:
python research/v0.9/targeted_n10.py
```

`targeted_n10_results.json` stores original solver statuses, including a timeout that was later resolved. Do not replace the historical record with the retry status.
