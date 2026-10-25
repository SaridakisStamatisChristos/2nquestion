# Research roadmap: pursue universal novelty, not incremental tuning

**Primary objective:** prove or refute that every distinct-time temporal clique has a `2n-3`-edge spanner. A known published construction attains only a larger linear bound; consult [REFERENCES](REFERENCES.md) for priority anchors.

## Highest-information tasks

1. **Adversarial structural generation.** Generate non-pivotable and non-dismountable chronologies; naive uniform shuffles frequently have a pivot at n=7,8 and waste search time. Preserve actual chronological edge order and random seeds.
2. **Certified n>=9 optimization.** Combine the v0.5 exact frontier-cut formulation with an independent time-expanded MILP formulation. For a suspected counterexample to `2n-3`, require a certified infeasibility result for every size-`2n-3` selection, not only a heuristic failure. Record solver logs, versions, time limits, and model files.
3. **Challenge treewidth 3.** Try constructing a temporal clique with **no spanning 3-tree**; require full independent 3-tree enumeration or an equivalent exact solver proof. If no counterexample emerges, attempt a universal 3-tree construction with a complete inductive invariant.
4. **Global exchange conditions.** Study whether the v0.4 unbounded simultaneous-deletion obstruction can be circumvented using constrained global information-flow invariants. Local pairwise tests alone are provably insufficient.
5. **Research-priority audit.** Compare proposed new structural statements against historical minimum-gossip, dismountability, 2-arch/2-degeneracy, temporal reachability sparsification and treewidth literature. Distinguish temporal stretch-3 from static treewidth 3.

## Gating criteria

A **breakthrough** requires either (a) a complete human-checkable universal proof with independent adversarial audit, (b) a minimal counterexample with a certified nonexistence result, or (c) another universal theorem plus verified scholarly-priority search showing genuinely new substance. A small instance or numerical pattern is a research artifact, not a paper-worthy novelty declaration by itself.
