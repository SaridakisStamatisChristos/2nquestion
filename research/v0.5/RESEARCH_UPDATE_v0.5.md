# Temporal Clique Research v0.5 — Chronological Frontier Cuts and the Integrality Barrier

**Date:** 25 October 2026. **Target:** prove or disprove that every injectively timed complete graph on n vertices admits an all-pairs temporal spanner with at most `2n−3` edges. **Target status: still OPEN.** This note establishes a source-reachability cut characterization and an explicit fractional LP obstruction. Neither is asserted to be an independently established novel contribution or a solution of the conjecture.

## 1. Model

Let `e_1,...,e_m` be all `m=n(n−1)/2` undirected edges of `K_n`, appearing exactly once in this order. A temporal journey traverses edges in strictly increasing order. For a subset H of these edges, `R_H(s,i)` is the set of vertices reached by the source `s` after processing the first `i` edge events; `R_H(s,0)={s}`. H is temporally connected exactly when `R_H(s,m)=V` for every s.

## 2. Proved global chronological-frontier theorem

Fix **any** H and source s for which `R_H(s,m) != V`. Define its omitted temporal frontier:

`C(H,s) = { e_i={u,v} not in H : exactly one of u,v lies in R_H(s,i−1) }`.

**Theorem.** For **every** all-pairs temporally connected X (not necessarily containing H),

`X ∩ C(H,s) ≠ ∅`.

**Proof (reachability containment).** Suppose `X∩C(H,s)=∅`. We prove inductively that `R_X(s,i) ⊆ R_H(s,i)` for all i. At i=0 both sets equal `{s}`. Consider event `e_i={u,v}`. If X does not retain `e_i`, `R_X` does not expand, and the inclusion remains true because `R_H` is monotone in time. If X retains `e_i` but neither endpoint is X-reachable at i−1, again nothing changes. Otherwise, some endpoint is in `R_X(s,i−1) ⊆ R_H(s,i−1)`. If the other endpoint is *outside* `R_H(s,i−1)`, there are two possibilities. If `e_i ∈ H`, then H also traverses the edge and adds that endpoint at event i, preserving containment. If `e_i ∉ H`, then `e_i ∈ C(H,s)`, contrary to `X∩C(H,s)=∅`. Thus in all cases every vertex newly reached by X at event i belongs to `R_H(s,i)`, proving inclusion. At the final time, `R_X(s,m) ⊆ R_H(s,m) ≠ V`; hence X cannot be temporally connected. Contraposition proves the claim. QED.

The theorem is **globally valid**; the proof does not assume H⊆X. The time-reversed event ordering produces further globally valid inequalities (temporal reachability directions reverse simultaneously).

### Exact global characterization

The following 0–1 linear system describes *exactly* the temporal spanners:

`x_e∈{0,1}` for all e, and for **every** temporally disconnected H and every deficient source s,

`sum_{e∈C(H,s)} x_e ≥ 1`.

Necessity is the global frontier theorem. Sufficiency follows by taking H=X: if X itself were disconnected, for some s its frontier consists entirely of omitted edges, so its own cut constraint would be violated. Thus the system is exact, although it may have exponentially many distinct inequalities.

### Cutting-plane algorithm

Start from necessary degree constraints, solve the binary optimization (minimize sum x_e), inspect the proposed subgraph by chronological reachability, and, whenever it is disconnected, add its violated source frontiers (both forward and time-reversed). Repeat until a verified all-pairs connected optimum is found. **All these cuts are globally valid**, and any globally certified MILP optimum for the master problem is also the global optimum of the temporal-spanner problem if its solution is actually connected. If a per-iteration solver hits its time limit, the result must be marked unknown unless the final candidate is feasible (then only an upper bound is established).

This is a generic exact approach, not independently validated novelty or a practical improvement over time-expanded MILP.

## 3. Fractional integrality barrier already on K4

Consider the six-event clique chronology (0-based vertices):

`t1=01, t2=23, t3=02, t4=13, t5=03, t6=12`.

Exhaustive enumeration of all 64 edge subsets shows the optimum temporal spanner uses exactly 4 edges. In contrast, the **complete** LP relaxation obtained by making all variables continuous in `[0,1]` in the exact global frontier formulation has optimum **3**. Hence its integrality gap on this instance is `4/3`.

A proof of LP optimum 3 that does not rely on numerical optimization:

1. Every one of the six edges is individually deletable while preserving temporal connectivity, checked by direct chronological information propagation. Since the global frontier theorem holds, no frontier cut can be a singleton (such a cut would rule out the all-except-one-edge connected spanner). Thus setting `x_e=1/2` for all six edges satisfies every frontier inequality and has objective `3`.
2. Exhaustive enumeration yields 12 distinct cardinality-two frontier cuts. Each of the six edges appears in exactly four of these 12 cuts. Summing their 12 inequalities gives `4∑_e x_e ≥ 12`, i.e. `∑_e x_e ≥3`.
3. The integer optimum is 4 (exhaustive 64-subset enumeration, independently consistent with the classical 2n−4 gossip lower bound). So the LP optimum is exactly 3 but the integer optimum is 4.

This refutes the proposed shortcut that *the exact chronological-cut system is integral*. It does not refute the main 2n−3 conjecture, which is an existence statement rather than an LP integrality statement.

## 4. Executed evidence and honest limitations

- Exhaustive frontier soundness for all 6 edge orders of K3 and all 720 orders of K4, over every candidate H and every supergraph avoiding its frontier: **PASS** (42,378 disconnected candidate-subgraph cases across the enumerated schedules).
- Separately, every connected candidate was checked to satisfy all extracted frontier cuts for K3, K4, and 50 seeded random K5 schedules (not in the packaged default suite; optional test added separately).
- Exhaustive K4 LP witness: 26 distinct frontier cuts, of which 12 have two edges; every variable occurs in four two-edge cuts. `linprog` independently returned 3.
- Two independently formulated MILPs agreed on the optimum for three prior adversarial schedules: K4 optimum 5; K5 optimum 7; K6 optimum 8. Status 0 and witness verification for both solvers. These are selected instances, not a universal theorem.
- The frontier MILP is *slower* than the standard time-expanded MILP in several tests and reached its time limit on some random K7/K8 instances. No SOTA speed claim.

## 5. Novelty and research direction

Chronological frontier cuts are directly analogous to cuts in time-expanded reachability networks, and temporal reachability/minimum-cut concepts have extensive previous literature. This is a useful exact formalization, not a validated new paradigm. Our 4-vertex integrality-gap witness is a tested negative observation, not an established publication-worthy discovery.

**Remaining essential challenge:** discover a genuinely new *integral structural* argument that constructs a ≤2n−3 spanner universally, or provide an exactly certified K9-or-larger counterexample. The global cut characterization is suitable as a correctness oracle for that effort, but its integrality gap shows that a generic LP-duality argument is insufficient without a new structural inequality, rounding invariant, or restricted class theorem.

## Sources (priority boundary)

1. Arnaud Casteigts, *Open questions in temporal graphs*, updated Sep 22 2026: https://arnaudcasteigts.net/blog/open-problems.html
2. Júlia Baligács, *Temporal Cliques Admit Linear Spanners* (2026): https://arxiv.org/abs/2606.05156
3. Casteigts, Peters & Schoeters, *Temporal Cliques Admit Sparse Spanners* (JCSS 2021): https://doi.org/10.1016/j.jcss.2021.04.004
4. Angrick et al., *How to Reduce Temporal Cliques to Find Sparse Spanners* (ESA 2024): https://doi.org/10.4230/LIPIcs.ESA.2024.11
5. Temporal minimum cut overview in *Robust Temporal Cut* (SAND 2026): https://drops.dagstuhl.de/storage/00lipics/lipics-vol373-sand2026/html/LIPIcs.SAND.2026.14/LIPIcs.SAND.2026.14.html
