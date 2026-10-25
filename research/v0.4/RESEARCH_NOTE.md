# Temporal-Clique 2n-3 Research Campaign — Evidence Ledger v0.1

**Research date:** 2026-10-24. **Status:** OPEN mathematical conjecture; independently implemented finite verification. **Do not claim a general proof or original priority.**

## 1. Canonical problem

Let \(K_n\) have \(m=\binom n2\) undirected edges, each with one distinct time label (equivalently, every ordering of its edges). A temporal path traverses contacts in **strictly increasing** time order. Find a subset \(S\subseteq E(K_n)\) preserving reachability for every ordered vertex pair. Let \(\operatorname{OPT}(K_n,\lambda)\) be the minimum size of such a subset. The open **strong conjecture** is \(\operatorname{OPT}(K_n,\lambda)\le 2n-3\), for any labeling, with \(n\ge 2\).

**Known results:** the general lower bound for \(n\ge4\) is \(2n-4\) (telephone/gossip theorem, Bumby 1981). Baligács (2026) proved \(7n\) as an unconditional upper bound; Casteigts' open problem page dated 2026-09-22 reports further improvement to \(6n\) using the same method, and says \(2n-3\) remains open.

## 2. New research *hypothesis*: Pivot–Optimal Dichotomy (POD)

> **Conjecture POD (unproved, global novelty not confirmed).** For every properly labeled temporal clique on \(n\ge4\) vertices, at least one of these holds: **(P)** the clique has an *edge pivot*; or **(O)** there is a temporally connected subgraph containing exactly \(2n-4\) edges.

An edge \(e=uv\) at time \(t\) is a pivot if every vertex reaches \(\{u,v\}\) at times earlier than \(t\), and starting from \(\{u,v\}\) every vertex is reachable at times later than \(t\). A pivot yields a temporal spanner with at most \(2n-3\) edges by combining incoming and outgoing time-respecting forests with the pivot edge; this is **established prior art**, not our finding. If POD is true, it **implies** the open \(2n-3\) conjecture, and the non-pivot branch gives the sharper optimum \(2n-4\).

The novelty of POD as an explicitly stated dichotomy is **not fully established**. Similar pivotability discussions in the 2019/2024/2025 literature, as well as older optimal-gossip graph characterizations, must be checked before any public originality claim.

### Finite computational certification

All global edge permutations were exhaustively enumerated for the following cases:

| n | All edge orderings | No-pivot orderings | Those with a \(2n-4\) spanner | Result |
|--:|--:|--:|--:|---|
| 4 | 720 | 48 | 48 | exhaustive verification of POD |
| 5 | 3,628,800 | 225,360 | 225,360 | exhaustive verification of POD |

`exhaustive_small.cpp` is the full finite-case verifier. On each non-pivot schedule, it enumerates every \((2n-4)\)-edge subset until a temporal spanner is found. A false POD schedule would be printed with its chronological edge order and would terminate with `REFUTED`. Compiling with `g++ -O3 -std=c++17` returned `pass` on both finite domains. Finite enumeration **does not prove POD for larger n**.

### Reproducible deterministic random survey

Independent Python `random.Random` generators, seeds `20261024+n` for each n, and multi-start randomized greedy deletion yielded these outcomes:

| n | Edge-order permutations sampled | No-pivot samples | No-pivot samples with verified \(2n-4\) witness |
|--:|--:|--:|--:|
| 6 | 200,000 | 7,876 | 7,876 |
| 7 | 100,000 | 1,895 | 1,895 |
| 8 | 100,000 | 779 | 779 |
| 9 | 100,000 | 222 | 222 |
| **Total** | **500,000** | **10,772** | **10,772** |

- n=6: 7,865 found by 12 greedy deletion orders; the remaining **11** were proved to have an eight-edge witness by combinatorial subset enumeration.
- n=7: 1,886 found by 12 greedy orders; all remaining **9** had a ten-edge witness **certified** by MILP (`HiGHS status 0`).
- n=8: 759 found by greedy; the remaining **20** had a twelve-edge witness **certified** by MILP (`HiGHS status 0`).
- n=9: 208 found by 12 greedy orders; all remaining **14** yielded a fourteen-edge witness with up to 2,000 more deterministic greedy deletion orders.

The survey is **not** unbiased evidence about the hardest non-pivotable cliques, since non-pivotable schedules become rare in uniformly random permutations and greedy may find easy optima. Samples do not prove the general statement. The archived JSON contains all initially difficult schedules and evidence metadata.

## 3. Reliability of the temporal reachability oracle

For injectively labelled contacts \(e_i=\{u,v\}\), store the set \(R_x^{(i)}\) of original source labels learned by vertex \(x\) after the first \(i\) selected events. Initialize \(R_x^{(0)}=\{x\}\). For a selected edge, update **simultaneously**

\[ R_u^{(i+1)} =R_v^{(i+1)}=R_u^{(i)}\cup R_v^{(i)}. \]

For unselected edges, do nothing. A subset is a temporal spanner exactly when all final sets equal the entire vertex set. Proof: induction over chronologically processed events; any temporal path delivering a source's information at event \(i\) must arrive at one endpoint strictly earlier, and the contact sends the union of the endpoints' previous knowledge to both. Conversely all newly obtained information corresponds to such a path. Because times are distinct there is no same-time chaining.

The bitset oracle was independently compared to a DFS which explicitly explores all time-increasing paths:
- **46,130** exhaustive `(edge permutation, retained-edge subset)` cases for n=2,3,4;
- **1,400** seeded random n=2..8 cases.
- Efficient forward/backward pivot detection was also compared to a separately written pair-of-roots temporal reachability implementation on **7,000** random schedules, n=3..9.

All checks passed. These tests support implementation fidelity, not novelty.

## 4. Exact MILP certificate architecture

Let binary \(x_i\) indicate whether contact \(i\) is retained, and binary \(r_{s,v,i}\) whether initial source \(s\)'s information is at vertex \(v\) after step \(i\). For contact \(\{u,v\}\), impose the exact Boolean recurrences:

\[r_{s,u,i+1}=r_{s,u,i}\lor (x_i\land r_{s,v,i}),\quad
r_{s,v,i+1}=r_{s,v,i}\lor(x_i\land r_{s,u,i}).\]

All other vertex-state bits remain unchanged. Impose \(r_{s,v,0}=[s=v]\) and \(r_{s,v,m}=1\), minimize \(\sum_i x_i\). The conjunction/disjunction is linearized by four inequalities per updated value:

- \(r'\ge r\)
- \(r'\ge x+q-1\)
- \(r'\le r+x\)
- \(r'\le r+q\).

Binary case analysis proves these inequalities equivalent to \(r'=r\lor (x\land q)\). Thus feasible integer solutions correspond **exactly** to temporal spanners, and solver status 0 certifies optimum under the solver's assumptions. In our survey, the MILP search often used an upper constraint \(\sum x_i\le 2n-4\); a certified feasible witness attains the independent lower bound and is therefore optimal.

## 5. Refuted structural shortcuts

### Hub-plus-tree restriction — FALSE

For \(n=6\), a deterministic search (`star_tree.cpp`, seed 2177, trial 2966) found the chronological edge order:

```text
(2,3) (0,2) (0,1) (2,5) (1,2) (3,4) (0,3) (1,5)
(0,4) (3,5) (2,4) (0,5) (4,5) (1,3) (1,4)
```

An independent enumeration examined all **735 distinct** retained edge sets consisting of a spanning star and a spanning tree on the other five vertices; none was temporally connected. Nevertheless, the **eight** time positions **3, 4, 5, 6, 7, 11, 12, 14** (one-indexed) are temporally connected and attain the lower bound \(2n-4\). This failure mode was already anticipated in the literature: **not a new counterexample to the main problem or a novelty claim**.

### Edge pivot alone — INSUFFICIENT

The same n=6 witness has **no** edge pivot, yet admits an optimal spanner. Therefore any proof requiring a global edge pivot for every instance fails. This is consistent with established pivotability literature.

## 6. Open obligations

1. **Prove or refute POD for n≥6:** find a properly labeled non-pivotable clique with no \((2n-4)\)-edge spanner, or derive a general construction. A counterexample to POD does **not** automatically refute the main \((2n-3)\) conjecture.
2. **Investigate four-cycle optimality kernels.** Bumby (1981) proved that any \((2n-4)\)-call scheme contains a static four-cycle. Göbel–Cerdeira–Veldman (1991) characterized label-connected graphs with that many edges. Determine whether non-pivotability forces a chronologically compatible four-cycle kernel and its attachments. **This is a suggested route, not an established lemma.**
3. **Avoid standard ingredients posing as novelty:** pivotability, dismountability, 2-arch graphs, bipartite reductions, the 7n construction, and chronological gossip bitsets are all known or straightforward.
4. **Falsification-first n≥9:** use biased generation toward non-pivotable, hard-to-delete schedules; exact MILP with checkable reachability witnesses and solver logs. Run independent literature and claim-priority audit before describing POD as a new research conjecture.
5. **A publishable target** is a proof of POD or a genuine counterexample that yields a new structural theorem or tight obstruction family. Enumeration and heuristic surveys alone fall below the user's requested novelty standard.

## 7. References and priority boundaries

- Casteigts, A. (2026-09-22). *Open questions in temporal graphs*. https://arnaudcasteigts.net/blog/open-problems.html
- Baligács, J. (2026). *Temporal Cliques Admit Linear Spanners*. arXiv:2606.05156 https://arxiv.org/abs/2606.05156
- Casteigts, A., Peters, J., Schoeters, J. (2019/2021). *Temporal Cliques Admit Sparse Spanners*. https://doi.org/10.1016/j.jcss.2021.04.004
- Angrick, S. et al. (2024). *How to Reduce Temporal Cliques to Find Sparse Spanners*. https://arxiv.org/abs/2402.13624
- Casteigts, A., Carnevale, D., Corsini, T. (2025). *Dismountability in Temporal Cliques Revisited*. https://arxiv.org/abs/2502.01321
- Bumby, R. T. (1981). *A Problem with Telephones*. https://doi.org/10.1137/0602002
- Göbel, F., Cerdeira, J. O., Veldman, H. J. (1991). *Label-connected graphs and the gossip problem*. https://doi.org/10.1016/0012-365X(91)90068-D
- Kleitman, D. J., Shearer, J. B. (1980). *Further gossip problems*. https://doi.org/10.1016/0012-365X(80)90116-8
- Casteigts, A., Molter, H., Zehavi, M. (2026). *Minimum Temporal Spanners in Happy Graphs*. arXiv:2604.24227 (general happy graphs; do not infer clique-specific NP-hardness).

## Verdict

**Independently verified:** correctness of finite computational search and witnesses, complete POD verification on n=4 and n=5, 10,772 non-pivotable random instances n=6..9 each with an optimal-size \(2n-4\) witness.

**Still unresolved:** the universal POD dichotomy, the original \(2n-3\) conjecture, original priority of POD as a statement, and any general-case theorem stronger than the published bounds.
