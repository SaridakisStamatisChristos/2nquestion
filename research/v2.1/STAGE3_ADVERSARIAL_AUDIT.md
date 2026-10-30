# Stage 3 adversarial verification — 26 October 2026

**Verdict: PASS for the bounded n=15 computational certificate, not formal proof or publication readiness.**

## Claim and attack surface

Every successful shortest 26-call distinct-contact telephone-gossip schedule on 15 vertices has an acyclic original chronological half. A structural reduction yields 945 remaining placements in 20 symmetry orbits. The weakest Stage 2 dependency was one C++ local component oracle, especially the seven-vertex unicyclic component.

## New independently implemented oracle

The new source [stage3_independent_oracle.cpp](stage3_independent_oracle.cpp) enumerates component contact histories with an incremental disjoint-set graph and an explicit cycle-rank budget. For unicyclic components it enumerates the first m-2 contacts, then iterates *both* last contacts and calculates the final gossip state. For trees it enumerates cycle-free contact prefixes and the final bridge.

Unlike the original program, **the new oracle never memoizes by the used-edge and knowledge-vector pair**. Its raw history counts therefore differ from the primary's, but its complete sets of B (prefix sufficiency) and D (reverse ancestry requirements) profiles **match exactly on all 33 exact component types** needed for n=15.

The exact seven-vertex cases are:

| Group sizes | Collector requirements | New DFS prefix states | Final schedules checked | B/D profile counts |
| --- | --- | ---: | ---: | --- |
| (2,2,3) | (2,2,0), unicyclic | 2,568,742 | 5,287,680 | **0 / 0** |
| (2,3,2) | (2,1,0), unicyclic | 2,568,742 | 61,229,520 | **9 / 27** |

The independent driver [stage3_adversarial_check.py](stage3_adversarial_check.py) builds both executables, checks the 33 profile-domain pairs for exact set equality and **substitutes all independently generated exact domains back into the global CSP**. It then confirms 20/20 UNSAT orbits covering 945/945 placements.

## Proof-assumption and pruning audit

**Tree final-edge collectors.** Removing the last edge of a tree separates the earlier calls into two disjoint components. Only the two endpoints of the final edge can acquire missing secrets across that edge. Therefore every final complete collector is an endpoint.

**Unicyclic last-two collectors.** After m-2 contacts on m vertices, the static contact graph is disconnected; nobody can yet know all m original secrets. Hence every final complete collector must be among the endpoints of the last two calls. The independent implementation counts distinct endpoints and the original implementation overcounts duplicates, a safe weakening.

**Cycle rank.** Adding contacts never decreases cycle rank. Partial graphs with more than one independent cycle cannot become connected unicyclic graphs. The new oracle prunes such prefixes; the old oracle does not rely on this condition.

**Original memoization.** In the first oracle, the remaining legal contacts depend only on which pairs were used, and all future gossip states depend only on the current full knowledge vector. Merging histories with identical used pairs and knowledge therefore preserves their possible terminal profiles. The second enumerator does not assume this fact; its complete profile-set equality is the practical stress test.

**Temporal information profiles.** Reverse-order synthetic tokens exactly identify original forward-reachable destinations. A prefix cell's midpoint secret-sufficiency bitmask and a suffix cell's ancestry requirements are compatible precisely when every destination can receive the whole prefix component's secret set. Independent components within a half use disjoint participants, so their contact orders commute.

**Optimistic large-tree bound.** Deleting a final tree edge separates earlier contacts into two sides. Giving the endpoints all secrets and every other vertex all secrets of its own side enlarges possible midpoint knowledge. This is a sound overapproximation. Similarly, permitting duplicate unordered pairs between the prefix and suffix only enlarges the global constraint domain. Therefore UNSAT under both relaxations remains a valid impossibility result.

## Additional exhaustive attacks

The separate Python checker [stage3_exhaustive_stress.py](stage3_exhaustive_stress.py) ran complete candidate contact-order spaces without importing either C++ oracle:

| n | Contact shape | Distinct-edge orders | Connected |
| --- | --- | ---: | ---: |
| 3 | Tree | 6 | 6 |
| 3 | Unicyclic | 6 | 6 |
| 4 | Tree | 120 | 96 |
| 4 | Unicyclic | 360 | 360 |
| 5 | Tree | 5,040 | 3,000 |
| 5 | Unicyclic | 30,240 | 26,640 |
| 6 | Tree | 360,360 | 155,520 |

**No contradiction** to last-contact collector bounds or optimistic tree domination was found. Independently, all 517 distinct-edge chronological K4 sequences of lengths 0–4 were tested against reversed-token reachability for 16 source/destination pairs each: **8,272/8,272** comparisons agreed.

Previous v2.1 tests additionally passed 3,200 direct gossip/profile comparisons and 240 randomized tree-containment tests.

## CI and reproducibility

From repository root:

    python3 research/v2.1/stage3_adversarial_check.py
    python3 research/v2.1/stage3_exhaustive_stress.py

Stage 3 [workflow](../../.github/workflows/research-v21-stage3.yml) is pinned to a checkout commit and builds two independent C++17 executables. Successful executions:

- [First independent-oracle push run 40356398259](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40356398259)
- [First independent-oracle PR run 40356407255](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40356407255)
- [Full expanded audit push run 40356861884](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40356861884)
- [Full expanded audit PR run 40356872700](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40356872700)

## Evidence limits

The two local enumerators share the mathematical definitions of gossip and sufficient information, but not their search-state mechanisms. Large-tree optimistic-domain generation still uses the original source, with a mathematical overapproximation proof and separate exhaustive/sampled containment checks. The finite classification also depends on earlier human mathematical reductions: component intersections, 3-by-3 confinement, collector/first-bridge lemmas, and the single-source entry lemma. These dependencies have not been imported into a Lean, Coq or Isabelle proof assistant.

**No universal n>=16 theorem; no solution of the distinct temporal-clique 2n-3 conjecture; no global priority or external peer-review claim.** Keep PR #1 draft and unmerged. Stage 3 can be closed for the requested independent seven-vertex verification, pending the final green check on the updated branch.
