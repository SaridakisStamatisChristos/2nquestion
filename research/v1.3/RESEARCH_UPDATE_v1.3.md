# Research v1.3 — an ordered two-singleton rule

**25 October 2026.** Model: one undirected contact exchanges all currently known original information. Split any successful schedule at any cut. Let `P_i` be prefix contact components and `Q_j` suffix contact components.

## Theorem (human-proved, necessary)

If a prefix component `P_i` is a tree and intersects two different suffix components `Q_a,Q_b` each at exactly one vertex, respectively `u,v`, then its **last prefix contact must be uv**.

Dually, if a suffix component `Q_j` is a tree and intersects two different prefix components `P_a,P_b` each at exactly one vertex, respectively `u,v`, then its **first suffix contact must be uv**.

In particular, a tree component on either side cannot meet **three different opposite-side components in singleton intersections**.

### Proof

Tree collector fact: in a connected tree whose edges each contact once, if `xy` is the final contact, removing `xy` divides the graph into two nonempty vertex sets. Before the final contact no original secret crosses this cut. Thus no vertex other than `x,y` can know every original secret from its tree component at the end: all other vertices retain information only from one side.

For the prefix statement, suppose `P_i∩Q_a={u}`. Every original secret held in `P_i` has to reach every vertex of `Q_a`, and no prefix contact leaves `P_i`, while no suffix contact leaves `Q_a`. Consequently **all secrets originally in `P_i` must already be at `u` at the cut**. The same argument forces `v` to hold all of them. The collector fact requires `u,v` to be the endpoints of the last prefix contact.

For the suffix statement, reverse the entire successful undirected contact sequence. Every increasing journey in the original reverses into an increasing journey of the reversed sequence; so all-to-all gossip success is preserved. Components `Q_j` become prefix components in the reverse and the original `P_i` become suffix components. Apply the prefix result in reverse: the last reversed `Q_j` contact, i.e. its first original forward contact, is `uv`. Three singleton intersections would force three distinct unordered vertex pairs to be the same first/last edge, impossible. QED.

This lemma is valid for **all successful contact schedules and all cuts** satisfying its assumptions, not only optimal-length schedules. It is a necessary condition, not a replacement for full temporal reachability verification.

### Practical use

Sound branch-and-bound / exact solver pruning: once a component-intersection grid and a tree side are fixed, enforce the forced first/last contact before considering other permutations. It is not valid for arbitrary cyclic components without a separate proof.

## Exact finite regression

`two_singleton_rule.py` enumerates all distinct-edge shortest contact schedules and runs a separate chronological information-propagation check before checking the forced-contact statement.

| n | Enumerated schedules | Successful | Forced-contact obligations | Violations |
|---|---:|---:|---:|---:|
| 4 | 360 | 24 | 96 | 0 |
| 5 | 151,200 | 3,240 | 6,480 | 0 |

Also tested: 30,000 seeded `n=6` schedules; 121 successful, 155 obligations, zero violations. These finite tests corroborate the human proof; they do not replace it.

## Specific K13 negative certificate (not the full n=13 question)

Consider 13 vertices grouped into three prefix rows and three suffix columns with intersection-cardinality matrix

```
     Q0 Q1 Q2
P0    2  2  1
P1    2  2  1
P2    1  1  1
```

Require the first 11 contacts to form prefix components `P0,P1` as 5-vertex trees (4 calls each) and `P2` as a triangle (3 calls). Require the last 11 contacts to form suffix components `Q0,Q1` as 5-vertex trees and `Q2` as a triangle. No temporally successful 22-contact schedule realizes these exact requirements.

`v13_bitset.py` enumerates the 576 possible prefix tree orders for each size-five row that deliver full row information to its singleton in column 2; 6 triangle orders; 3,000 possible suffix tree orders for each size-five column; and 6 suffix triangle orders. Because information propagation is bitwise union, the requirement that each separate prefix group reach a suffix group is evaluated independently for the same chosen suffix ordering. Integer-bitset intersections represent exactly the suffix orders satisfying all three source-group requirements; empty intersections certify infeasibility for this grid and these cycle positions. A separate `search_row3.py` in the bundled working research package implemented the search differently and returned the same negative result.

**Do not interpret this as exclusion of all n=13 schedules.** Other component grids and cyclic-half placements remain open.

## Status and originality

- PROVED: ordered two-singleton tree-contact necessity.
- EXECUTED FINITE: exhaustive K4/K5 regressions and this *one* K13 layout exclusion.
- OPEN: whether every shortest gossip schedule has an acyclic half; whether arbitrary temporal cliques admit `2n−3`-edge spanners; POD.
- NOVELTY UNVERIFIED: Labahn (1995), *Kernels of minimum size gossip schemes*, https://doi.org/10.1016/0012-365X(94)00031-D ; Krumme (1996), *Reordered gossip schemes*, https://doi.org/10.1016/0012-365X(94)00302-Y.
- Contemporary open problem: https://arnaudcasteigts.net/blog/open-problems.html

No formal proof-assistant verification, complete n13 classification, better universal upper bound, or solution to the main conjecture is claimed.
