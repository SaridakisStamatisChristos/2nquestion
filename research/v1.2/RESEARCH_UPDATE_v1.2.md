# Research v1.2 — The at-least-one-forest theorem through twelve vertices

**Date:** 2026-10-25. **State:** Universal mathematical proof for `4 <= n <= 11`; exhaustive symmetry-reduced finite certificate for `n = 12`. **Novelty:** unverified, potentially overlaps minimum-gossip structure theory. **Primary temporal-clique spanner conjecture (`2n−3`) and POD:** both remain open. No breakthrough claim.

## Definitions

A *successful shortest simple-contact gossip schedule* on `n >= 4` participants is an ordered list of `2n-4` **pairwise distinct**, undirected contacts, each exchanging all presently known original secrets, such that every participant knows every secret at the end. The first and last chronological halves contain `n-2` contacts each. Contact graphs are static undirected graphs formed from edges in the relevant half.

Let `P_1,...,P_r` be connected components of the first-half graph and `Q_1,...,Q_s` the components of the second-half graph. Every `P_i ∩ Q_j` is nonempty, otherwise some original secret from `P_i` can never reach `Q_j`. Thus `r*s <= n`. If both halves have a cycle, `r,s >= 3` because each half has `n-2` edges on `n` vertices and a cyclic half has at least three components.

## Theorem A (complete proof): for every n <= 11 at least one half is acyclic

**Statement.** For each integer `4 <= n <= 11`, every shortest successful simple-contact gossip schedule on `n` vertices has at least one acyclic half.

### Reduction to n=11

The result for `n<=10` was proved in `research/v1.1/BOTH_HALVES_BOUND.md`. For `n=11`, suppose both halves are cyclic. The component intersection bound `r*s<=11` and `r,s>=3` force `r=s=3`. Each half has `n-2=9` edges and precisely three components, so its cyclomatic number is `9-11+3=1`: exactly **one** component contains a cycle. Every component has size at least three, since it meets all three opposite-half components. The only possible size partitions are `(3,3,5)` or `(3,4,4)`.

**Singleton collector lemma.** If `P_i ∩ Q_j={v}`, then `v` must know **all** secrets originally within `P_i` at the half cut. Indeed, all first-half contacts are contained in `P_i`, and all second-half contacts are contained in `Q_j`, so `v` is the sole carrier through which any `P_i` secret can enter `Q_j`.

**Tree collector lemma.** In an `m`-vertex component whose `m-1` contacts form a tree, at most **two** vertices can know all `m` secrets by the end of those contacts. Let `e` be the final tree contact. Deleting `e` separates the graph into two nonempty components with no earlier cross-contact. Immediately before `e`, no vertex has secrets from both sides. Afterwards only the two endpoints of `e` change information. Thus any complete collector must be an endpoint of `e`.

A three-vertex `P_i` intersects each of three `Q_j` in exactly one vertex. All three must be complete collectors by the singleton lemma; the two-contact tree is impossible by the tree collector lemma. Hence every three-vertex `P_i` must be a triangle with three contacts and consume one cycle. Since the entire first half has exactly one cycle, the partition `(3,3,5)` is impossible. Therefore prefix component sizes are `(3,4,4)`. By reversing the successful schedule and exchanging the two halves, suffix component sizes are also `(3,4,4)`.

### The forced 3x3 geometry

Label components to put the three-vertex prefix component at `P_2` and three-vertex suffix component at `Q_2`. Each of the nine cells `P_i∩Q_j` contains at least one vertex. There are only two excess vertices beyond this 3x3 grid. Because component sizes are `(4,4,3)` on **both** sides, the excess vertices occupy distinct rows and distinct columns. Permuting the component names, they occupy cells `(P_0,Q_0)` and `(P_1,Q_1)`. Thus `P_0∩Q_0` contains **two** vertices, call them `a,b`; and both `P_0∩Q_1` and `P_0∩Q_2` are singletons, `x,y`. The unique prefix cycle occurs in `P_2`, so `P_0` uses exactly three tree contacts. By singleton collectors, `x` and `y` are complete collectors for all four `P_0` original secrets, and by the tree collector lemma they must be the endpoints of `P_0`'s final contact. Therefore **neither `a` nor `b` knows all four `P_0` secrets at the half cut**.

Consider the suffix component `Q_0`, consisting of `a,b` and singleton vertices `c∈P_1∩Q_0`, `d∈P_2∩Q_0`. It has four vertices and three tree contacts, since the suffix's unique cycle is in its three-vertex component `Q_2`. Reverse the entire successful schedule. In that reversed schedule, `Q_0` becomes a prefix component and `c,d` are its singleton intersections with two opposite-half components. Hence `c,d` are complete collectors for the four original `Q_0` secrets in the **reversed** suffix; therefore its **last** reversed contact is `(c,d)`. Equivalently, the **first** forward contact inside `Q_0` is `(c,d)`.

Immediately before suffix processing, neither `c` nor `d` knows **any** original `P_0` secret, as both belong to distinct prefix components. Their initial contact `(c,d)` does not change that. There are only **two** further contacts inside `Q_0`. In order that both `c` and `d` eventually receive all `P_0` secrets, each must participate in at least one of the two later contacts. As the three contacts form a spanning tree of `Q_0`, the two later contacts must be `(c,a)` and `(d,b)` (or with `a,b` exchanged). Neither `a` nor `b` knows all four original `P_0` secrets, and no subsequent contact can transfer missing `P_0` information between the `c` and `d` branches. Therefore at least one original `P_0` secret fails to reach `c` or `d`, contradicting successful gossip. QED.

*The proof uses the established gossip lower bound only to identify the `2n-4` regime, not to infer the conclusion.*

## Theorem B (finite exact certificate): n=12 has the same property

**Statement.** Among all distinct-contact schedules on `n=12` vertices containing exactly `2n-4=20` contacts, none is successful and cyclic in both chronological halves.

### Complete finite search reduction

If both halves are cyclic, `r,s >= 3` and `rs<=12`. If `{r,s}={3,4}`, all twelve grid cells contain exactly one vertex. Then each of three four-vertex prefix components must have four complete collectors (each singleton is the only entrance into a distinct suffix component). Yet the first half's cyclomatic number is one, so at least two of these four-vertex components are trees, with at most two collectors. Impossible. Reverse time for `(4,3)`. Consequently `r=s=3`.

Then each half contains precisely one cyclic component. Its component-size partition has at most one size-three component, because any three-vertex component meets the three opposite components through singletons and hence needs a cycle. The 12 vertices fill a 3x3 intersection matrix with precisely three additional vertex occurrences (possibly in repeated cells). Up to independent prefix/suffix component permutations and simultaneous transposition/time reversal, the valid extra-cell multisets form **four** classes:

1. `[(0,0),(0,0),(1,1)]`
2. `[(0,0),(0,1),(1,0)]`
3. `[(0,0),(0,1),(1,2)]`
4. `[(0,0),(1,1),(2,2)]`

When a side contains a size-three component, that side's sole cycle must occur there; otherwise any component may carry the cycle. The four classes produce **14 cycle placements** in total.

For each cycle placement, `double_cycles.py` enumerates every connected undirected edge choice *and every chronological order* on each prefix/suffix component, with component size `m` and exactly `m-1` edges for trees or `m` edges for the unique unicyclic component. It prunes only after checking the necessary singleton-collector condition (in forward time on prefix components, and reverse time on suffix components). The full schedule must use each edge at most once. For every surviving independent prefix-component contact ordering, the verifier checks every allowed suffix-component ordering for complete final information dissemination.

This enumeration is complete: contacts in distinct prefix components commute (no shared vertices), and contacts in distinct suffix components likewise commute. Therefore every global chronological schedule is equivalent, for reachability, to the set of local component orders explored. The code also checks cross-half edge disjointness. Every candidate class failed.

**Execution:** `python research/v1.2/exhaust12.py`; Python 3.13, no external dependencies; four symmetry classes, 14 placements, zero successful both-cyclic schedules, about eight seconds in the research runtime. `exhaust12.log` records every placement. `verify_v12.py` independently checks all 56 ordered reachabilities of the v1.1 eight-vertex one-cyclic-half witness and 864 necessary nine-cell configurations at n=11.

**Certificate caveat:** The n=12 statement is a finite computational theorem contingent on the transparent enumeration code and the proved symmetry reduction; it has not been formally certified by Lean/Coq/Isabelle or a second independent full n12 implementation.

## Implications and prior art

- The n=11 human proof strengthens the existing half-forest exclusion by one vertex; n=12 adds an exhaustive finite exclusion, not a universal theorem.
- Prior classical minimum gossip kernel characterization is a substantial novelty threat: R. Labahn, *Kernels of minimum size gossip schemes*, Discrete Mathematics 143 (1995), DOI: 10.1016/0012-365X(94)00031-D. The results should **not** be represented as novel without a scholarly priority assessment.
- This is **not** a proof of `2n−3` temporal clique spanners; fixed-edge chronology extraction remains a different problem from arbitrary minimum gossip protocols. POD remains unproved.
- The genuinely useful conceptual lemma is **two-collector obstruction across singleton-vs-duplicated component intersections**, which may become a valid pruning mechanism for future exact or constructive research.

## Open next steps

(1) Construct or refute a successful shortest gossip schedule with *both* halves cyclic at `n>=13`; (2) check Labahn's full 1995 characterization for priority; (3) derive any general restrictions on minimum-spanner edge order that genuinely help the primary `2n−3` conjecture. Avoid algorithmic incrementalism without mathematical implications.
