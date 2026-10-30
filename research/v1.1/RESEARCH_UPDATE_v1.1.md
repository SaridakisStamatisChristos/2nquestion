# Research v1.1 — A sharp chronological half-forest threshold

**Date:** 2026-10-25. **Mathematical state:** a proved universal necessary-condition lemma, a proved sharp threshold, and a proved infinite counterexample family to an attractive but false structural strengthening. **Publication novelty:** unchecked/likely overlapping classical minimum-gossip theory (especially Labahn 1995). **Main `2n−3` temporal-clique spanner question:** OPEN. **POD:** OPEN.

## Model and definitions

A *simple-contact gossip schedule* on `n >= 4` vertices is a chronological sequence of pairwise distinct undirected edges, each used once for instantaneous bidirectional exchange of every secret currently known to the endpoints. A schedule is *successful* if every vertex knows every original secret at the end. It is *shortest* when it has exactly `k=2n−4` contacts (the classical telephone-gossip lower bound).

The *first half* consists of contacts 1 through `n−2`; the *last half* consists of contacts `n−1` through `2n−4`. For each half, its *contact graph* is the static graph on all `n` vertices made from its contacts. A half is a *forest* if this graph contains no cycle.

## Theorem 1: all-prefix/suffix component intersection (proved)

**Statement.** Given any successful gossip schedule and any cut between contacts, let `P_1,...,P_r` be the connected components of the graph of contacts *before* the cut, and `Q_1,...,Q_s` the connected components of contacts *after* the cut, all including isolated vertices. Then `P_i ∩ Q_j != ∅` for all `i,j`; hence `r*s <= n`.

**Proof.** Pick an original secret originating from vertex `a ∈ P_i`. The prefix cannot transmit that secret outside `P_i`, since it contains no edges between distinct `P` components. If a suffix component `Q_j` were disjoint from `P_i`, none of its vertices would know `a`'s secret at the cut. No contact after the cut leaves `Q_j`, so none could ever learn it. This contradicts successful all-to-all gossip. Consequently every ordered pair of a prefix component and a suffix component intersects, and the `r*s` pairwise disjoint nonempty intersections imply `r*s <= n`. QED.

**Limit:** Intersection is necessary, not claimed sufficient; the lemma is elementary and scholarly novelty is NOT established. It holds for any number of calls and does not require simple contacts.

## Theorem 2: sharp half-forest threshold (proved)

**Statement.** Every shortest successful gossip schedule with `4 <= n <= 7` has **both** chronological halves as forests; necessarily each half has exactly **two** connected components. Conversely, for every `n >= 8` there exists a shortest successful simple-contact schedule with a cycle in the last-half contact graph. By reversing chronology, for every `n >= 8` there also exists one with a cycle in the first half.

### Proof: `n <= 7`

The v1.0 first/last-contact incidence-window lemma implies that every vertex participates in the first `n−2` calls, and (by reversal) in the last `n−2` calls. Thus each half's `n−2`-edge contact graph has **no isolated vertices**.

For `n=4`, the half has two edges, so no cycle. For `5 <= n <= 6`, a cycle uses at least three edges and covers at most all of its edges' endpoints, and each remaining edge adds at most two new endpoints. In particular a cycle with `l>=3` edges plus `n−2−l` arbitrary edges can cover at most `l+2(n−2−l)=2n−4−l <=2n−7 < n` vertices for `n<=6`. Hence neither half can be cyclic.

For `n=7`, suppose the first half (five edges, covering all seven vertices) contains a cycle. The same bound forces that cycle to be a triangle and the other two edges to be disjoint from it and from each other. The first-half components `P` therefore have sizes `(3,2,2)`, i.e. `r=3`. The second half has five edges on seven vertices, so it has `s>=2` connected components. By Theorem 1, `3s<=7`, so `s=2`, and each of the two suffix components intersects all three prefix components. In particular they each contain at least three vertices; since their sizes sum to seven, one suffix component `Q` contains **exactly three** vertices, one from each prefix component. The suffix contains only five edges and exactly two components, so it is a forest. Thus `Q` has exactly two contacts (a 3-vertex tree).

Before these two contacts, the three members of `Q` are in different prefix components and consequently none knows either of the other members' original secrets. Two bidirectional calls cannot convey all three distinct original secrets to all three members: the two edges form a path, and whichever of them occurs first, its leaf endpoint cannot learn the other leaf's secret through the later edge. Contradiction. So the first half must be acyclic. Apply the same argument to the **reversed** schedule to conclude the last half is also acyclic. Having `n−2` edges and no cycle on `n` vertices implies exactly two components in each half. QED for `n<=7`.

### Counterexample at `n=8` (explicit and independently checked)

Chronological contacts at times 1..12 are:

```
(0,1), (4,5), (3,7), (2,6), (2,3), (1,5),
(0,4), (1,2), (6,7), (4,6), (3,5), (0,7)
```

All contacts are distinct. The information-propagation oracle and an **independent source-to-destination strictly increasing simple-path DFS** agree that all 56 ordered pairs are temporally reachable. Thus this is successful with exactly `2*8−4=12` calls, hence shortest by the classical gossip lower bound. The first half has two tree components `{0,1,4,5}` and `{2,3,6,7}`. The **last half has three components** `{0,4,6,7}`, `{1,2}`, `{3,5}`. Contacts `(0,4)` at time 7, `(6,7)` at 9, `(4,6)` at 10, and `(0,7)` at 12 form a **static 4-cycle** inside the last half. This refutes “every shortest gossip schedule has forest halves.”

### Infinite extension (proved)

Suppose `S` is a successful shortest schedule on vertices `0,...,n−1`, with pairwise distinct contacts and a cycle in its last half. Add new vertex `x=n`, choose two *distinct* old vertices `u ≠ v`, and define

`S' = [(x,u)] + S + [(x,v)]`.

The first new call gives `u` the new secret. Since `S` was successful, the new secret (now with `u` at the start of `S`) propagates to **every original vertex** by the end of `S`; all original secrets also become common knowledge. The last new call gives `x` all original secrets. Thus `S'` is successful. It contains `2n−2=2(n+1)−4` distinct contacts, so remains shortest. The new first half is the new initial call followed by the old first half, and the new last half is the old last half followed by the final new call. Its last-half cycle survives unchanged. Induction from the eight-vertex instance proves an infinite family for all `n>=8`. Reverse the contact order to obtain a first-half-cycle family. QED.

**Prior-art boundary:** The two-call induction extension is already documented in classical gossiping references, and minimum gossip kernels were characterized by Roger Labahn in 1995. The exact threshold theorem has not been shown absent from those works, so NO publication novelty is asserted.

## Executed adversarial tests

- Fresh C++ stochastic search targeting a *false half-forest conjecture* located a shortest 16-contact `K10` schedule with a cyclic second half. The exact contact list is archived in `half_cycle_witness.json`.
- Backward degree-two vertex eliminations preserving all-to-all gossip reduced the witness first to `K9`, then to the displayed `K8`, whose participants all have degree three. These reductions are **witness search**, not proofs of smallest order.
- The proved lower threshold certifies minimality without relying on exhaustive `K7` schedule enumeration.
- Python `sharp_half_forest.py` independently checks the witness, its reverse, and extensions for `n=8,...,24` using chronological bitset propagation and checks the complete prefix/suffix component intersection property.
- The independently implemented `audit_threshold.py` exhaustively enumerates and checks all 56 ordered pairs for time-respecting simple paths in the `K8` witness and all `C(21,5)=20,349` five-edge graphs on seven vertices, confirming that the **105** vertex-covering cyclic edge sets have precisely triangle-plus-two-independent-edges structure.

## Corollary: both halves cannot be cyclic for `n<=10`

A separate proof in `BOTH_HALVES_BOUND.md` establishes that **every shortest gossip schedule on at most ten vertices has at least one forest half**. It combines the complete component-intersection lemma with the three-agent gossip lower bound. For `n>=11`, the stronger assertion remains OPEN, with only heuristic negative-search evidence. No scholarly novelty is claimed.

## Implications for the `2n−3` program

- This **eliminates** any universal optimal-spanner proof that presupposes two chronological forest halves for all `n`.
- The prefix/suffix complete-intersection condition is a sound necessary structural filter and may guide exact MILP/SAT branching; it is **not** sufficient for temporal reachability.
- This does **not** refute Pivot–Optimal Dichotomy or the `2n−3` bound. These remain OPEN.
- Further originality screening must compare the sharp half-forest threshold with Labahn (1995) and other minimum-gossip classifications before describing it as a publishable theorem.

## Sources

- R. T. Bumby, *A Problem with Telephones* (1981), https://doi.org/10.1137/0602002.
- D. J. Kleitman and J. B. Shearer, *Further gossip problems* (1980), https://doi.org/10.1016/0012-365X(80)90116-8.
- R. Labahn, *Kernels of minimum size gossip schemes* (1995), https://doi.org/10.1016/0012-365X(94)00031-D.
- A. Casteigts, *Open questions in temporal graphs* (last updated September 22, 2026), https://arnaudcasteigts.net/blog/open-problems.html.
