# Root-free unicyclic crossed cores at EVERY center width >=4

**30 October 2026 — exact original-order CONSTRUCTIVE counterfamily.** This is an explicit, replayable, unbounded-width falsifier to any attempt to remove the outside-complete-root hypothesis from Theorem U.17. **It is NOT a completed successful global 2n-4-call gossip chronology, not a counterexample to the original-half-forest conjecture, and not a solution to the separate 2n-3 temporal-clique spanner problem.**

## Exact six-person-per-component seed, common center four

Let the common designated center be X0={0,1,2,3}. The original-order P-side chronological UNICYCLIC component has vertices {0,1,2,3,4,6} and EXACT contacts in this order:

  1. (0,6)
  2. (1,0)
  3. (3,1)
  4. (0,4)
  5. (2,0)
  6. (4,6) — FINAL cycle-closing call OUTSIDE X0

The independent Q-side chronological UNICYCLIC component has vertices {0,1,2,3,5,7} and EXACT calls:

  1. (0,7)
  2. (2,1)
  3. (0,5)
  4. (1,5)
  5. (3,0)
  6. (5,7) — FINAL cycle-closing call OUTSIDE X0

For a gossip midpoint application, the Q-side chronology may be interpreted as the fully REVERSED original suffix; these are separate original-order chronological components in their respective relevant directions. The unordered call edge sets of the two components are DISJOINT, even across components. The first five calls of each are edge-once spanning trees and their final respective calls add one new cycle without changing ANY center participant's information.

## Exact terminal center supports (seed, independently replayed)

| Original secret | P source support in X0 | Original secret | Q source support in X0 |
| --- | --- | --- | --- |
| 0 | {0,1,2,3} | 0 | {0,1,3} |
| 1 | {0,1,2,3} | 1 | {1,2} |
| 2 | {0,2} | 2 | {1,2} |
| 3 | {1,3} | 3 | {0,3} |
| 4 | {0,2} | 5 | {0,1,3} |
| 6 | {0,1,2,3} | 7 | {0,1,3} |

Every original secret is known by at least TWO distinct X0 people in its respective history. Every P source support intersects EVERY Q source support, including the four critical 2-support intersections:

- {0,2}∩{1,2}={2};
- {0,2}∩{0,3}={0};
- {1,3}∩{1,2}={1};
- {1,3}∩{0,3}={3}.

P's secrets 2 and 3 have DISJOINT global recipient sets after its history (the 2 secret occurs only at {0,2}; the 3 secret only at {1,3}). Thus no P participant can be a complete collector, even after its final cycle call. Q's secrets 2 and 3 similarly have disjoint global recipient sets: secret 3 is confined to {0,3}, whereas secret 2 is held only outside that set. Thus Q has NO complete collector either. The pre-final trees also have zero full collectors.

## Theorem U.20 — parametric arbitrary-width extension, with globally distinct unordered calls

For each integer k>=0 introduce k further distinct center vertices W_k={w1,...,wk}, disjoint from 0,...,7; put X_k=X0 union W_k, so |X_k|=4+k.

In P, start with call (0,6), then call (0,w1),...,(0,wk) in that exact order, then run the P seed's four calls (1,0),(3,1),(0,4),(2,0), then the same last cycle-closing call (4,6).

In Q, start with (0,7), then call (1,w1),...,(1,wk) in that exact order, then run the Q seed's four calls (2,1),(0,5),(1,5),(3,0), then the last cycle-closing call (5,7).

**For EVERY k>=0, both original-order contact graphs are connected edge-once unicyclic, their full call edge sets are pairwise-disjoint ACROSS the two component histories, their final calls touch only outside vertices, their exact X_k source supports doubly cover every original secret, ALL P/Q original source support pairs intersect, and NEITHER component's pre-final tree nor its complete cyclic history possesses ANY terminal full collector.**

**Proof.** Each new w_i is attached by one fresh leaf edge to P's vertex 0 and, separately, Q's vertex 1 BEFORE any of the four respective seed tree calls. The pre-final static graph remains a tree and the same final exterior call closes its existing cycle. Distinctness across histories holds because P uses {0,w_i} and Q uses {1,w_i}, and the seed edge sets are disjoint.

The original seed secret X0 supports cannot change when prepending these new calls: the new participants contain no old seed secrets before their initial call, and no old seed participant's knowledge of other old seeds is changed. Each NEW w_i original secret, after its early contact, accompanies all future P transmissions of original secret 0, so its X0 recipient support includes all four original center people. In Q it accompanies all future Q transmissions of original secret 1, and its X0 support includes at least {1,2}. Thus every new-secret support crosses every opposite old or new support, because P's old supports {0,2} and {1,3} both meet {1,2}, and P's new supports contain ALL X0. Every old source pair still intersects already in X0. All sources retain at least two X0 recipients and therefore doubly cover X_k. The exterior last closing calls do not touch X_k and preserve all center supports.

Finally, in P the original secrets 2 and 3 remain on disjoint global recipient sets, since their originating contacts occur AFTER all newly inserted leaf contacts; neither can propagate to a new leaf, nor do the old two recipient sets overlap. In Q the original source 3 is received only at {0,3}, while the original source 2 is absent at both 0 and 3. Hence both components remain root-free. This holds for every k, with no finite upper bound. QED.

## Scientific implications and strict scope

1. Theorem U.17's outside-full-collector assumption is genuinely ESSENTIAL, even if we also demand double center coverage, original order, unicyclic contact graphs, exterior-only final calls, all source-pair support crossing, and NO REPEATED UNORDERED CALLS across the two local component histories.
2. The remaining original both-cyclic minimum-gossip problem cannot be resolved from ONLY those local properties, by any size bound on X. The family gives valid local information-flow cores for every center width >=4.
3. **Not a global shortest-gossip counterexample:** the full original fixed-half 3x3 configuration requires FOUR ADDITIONAL tree components, nine positive crossing cells, offcorner support obligations, and a SINGLE globally successful pair of fixed original halves on the same full n participants. None of those missing constraints are certified here. Likewise the distinct temporal-clique 2n-3 spanner conjecture is not addressed.
4. The finite replay checker [root_free_crossed_unicyclic_family.py](root_free_crossed_unicyclic_family.py) executes k=0,1,2,3,4,8,16,32,64 (up to center size68), checks all call-graph and support conditions, 7,354 total original-source cross pairs and no full collectors. The **explicit induction-free parameterized construction and support-transport proof** establish the unbounded claim, not the finite checks.

**Evidence:** human proof of parametric construction; finite original-contact replay actually executed; external referee and novelty review pending; no formal proof assistant. Publication HOLD, PR DRAFT.
