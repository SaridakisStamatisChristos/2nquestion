# Stage 6 n=17 closure — computer-assisted finite certificate

**27 October 2026 — bounded n=17: computational exclusion PASS, all n>=18: OPEN, historical originality: UNRESOLVED, publication readiness: HOLD.** This supersedes the older eight-class OPEN verdict in [N17_PROFILE_AUDIT.md](N17_PROFILE_AUDIT.md). PR #1 stays DRAFT/UNMERGED.

## Precise mathematical scope

Let n=17 and let S be a shortest successful bidirectional telephone-gossip chronology with 30 pairwise-distinct unordered contacts. The original first 15 and original last 15 contacts cannot **both** have a cycle in their static edge sets. No chronological reordering is allowed in this statement.

This is an **executable finite computer-assisted conclusion conditional on the stated structural lemmas and verifier soundness**, not a Lean/Coq formal proof, independently refereed proof, or all-n theorem.

## Complete disjoint frontier ledger

| Decision | Orbit classes | Marked configurations |
|---|---:|---:|
| Previous sound size-10 profile UNSAT | 246 | 15,300 |
| Earlier independent exact n17 residuals 30–31 | 2 | 45 |
| New exclusions 32–35 and 72–75 | 8 | 432 |
| **Total** | **256/256** | **15,777/15,777** |

Two independent [incidence generators](n17_structural.py) agree on the complete n17 3x3 canonical orbit map and multiplicities; structural analysis excludes all other both-cyclic component-count geometries at n17. The new [orbit index validator](verify_n17_closure_index.py) checks the eight exact canonical matrices, marked cyclic positions and multiplicities against the original generator. The [full capacity-10 profile scan](probe_n17_profiles.py) remains a *necessary-condition* checker: relaxed-SAT cases are not gossip witnesses.

## New mathematical mechanism

[exclude_n17_residual_eight.cpp](exclude_n17_residual_eight.cpp) uses three explicitly separated evidence components.

### 1. Exhaustive rooted-tree terminal histories

In a connected component with m-1 unique calls, the used edges are a tree. Just before the final call x-y, its two connected sides U and V cannot share secrets. If x is a final complete collector, it is an endpoint of that last call and must know all of U beforehand; likewise y must know all of V. The exact recurrence enumerates every side split U,V, every last-edge partner y, and all recursive rooted side-tree terminal knowledge states. Because calls between disjoint sides commute, their internal chronological shuffles do not create extra terminal information states.

A sound necessary pruning rule requires any grid cell containing neither final bridge endpoint to collectively know all secrets of *each* side using its local members on that side. Such members never receive information across the last bridge.

### 2. Unicyclic components requiring at least three complete collectors

Immediately before the final two calls of an m-call connected unicyclic component, the static contact graph is disconnected. If it has at least three components, no vertex can know all secrets after the penultimate call and at most the two final-call endpoints can be full. With at least three final collectors the graph must therefore have precisely two components, each a tree (as there are m-2 preceding edges). Their first crossing call must make both its endpoints fully informed, requiring each to know its complete side beforehand.

The verifier enumerates **every** two-side split, **every** exact rooted side-tree state, each first crossing call and **every** last call. It intentionally permits a last link that was already used internally, giving a conservative *superset* of legal unicyclic histories. Therefore UNSAT excludes true gossip chronologies, whereas SAT is **not** a real witness. Small unicyclic components are independently exhaustively enumerated with distinct contacts and connectedness verification.

### 3. Necessary inter-half B/D compatibility

For each prefix row-component, a B bitmask records those cell-member subsets collectively knowing all its secrets. For each time-reversed suffix column-component, a D bitmask records the recipient subset of each initial secret. Complete gossip requires bitwise B AND D = D in every grid cell. The CSP lets independent local components select profiles without enforcing all global consistency constraints. This is another sound relaxation: its UNSAT verdict eliminates the original chronology.

## Final eight classes

**Orbits 32 and 33.** Their suffix column 2 is an eight-vertex tree with cell sizes (2,2,4), mandatory collectors (0,2,0) and exact third-cell D=278. All four singleton receiving-subsets occur in D; the corresponding prefix tree would need **four full collectors in that cell**, impossible since a tree has at most two final collectors.

**Orbit 34.** The suffix column is the exact (2,2,4) four-collector unicyclic case, again with third-cell D=278. The prefix unicyclic row would require all four full collectors in that cell **plus three** mandated collectors in the other cells, exceeding the maximum four final collectors of an m-call unicyclic component.

**Orbit 35.** Its suffix column is a seven-vertex (2,2,3) tree with two mandated collectors in the middle pair and full collective coverage in all three cells. The exact local history domain is **empty**, confirmed by the independent brute-force history enumerator.

**Orbits 72–74.** Exact rooted-tree local B and D profiles and exact small-component profiles make the relaxed global compatibility CSP **UNSAT**.

**Orbit 75.** The exact small-component domains and the conservative two-last-call unicyclic envelope (three mandated collectors) make that same relaxed compatibility CSP **UNSAT**.

The verifier asserts all of these failures. An unexpected SAT or profile mismatch stops CI.

## Independence and reproducibility

- The previously audited n<=16 exact component reference is unchanged. The new recurrence independently reproduces the earlier eight-vertex tree profile B=(8,14,32768), D=(6,8,278), and the 48-terminal-state count; its four-collector unicyclic and swapped-collector profiles match the earlier n16 exact sources.
- [Independent Python oracle](verify_n17_local_independent.py) separately enumerates ordered distinct spanning-tree contact histories via union-find, not by reusing rooted-state recursion; it proves the local seven-vertex (2,2,3) domain empty and reproduces the eight-vertex B/D and 48 count.
- [Canonical index validator](verify_n17_closure_index.py) fails closed if the structural orbit map, cyclic placements or multiplicities change.
- The [Stage 6 CI workflow](../../.github/workflows/research-v23.yml) compiles the C++ checker with g++ -std=c++17 -O3 -Wall -Wextra -Werror, executes all eight exclusions and independent tests, and reruns the structural and balanced-ideal checks.
- [CI PASS — complete eight-exclusion verifier and independent brute-force test](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40518191357).
- [CI PASS — additional exact orbit-index validation](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40518593662).

## Limits and future proof obligations

1. **All-n remains open.** Already at n=18, new rectangular families survive the currently known necessary conditions; no induction or universal exclusion is supplied here.
2. The complete finite conclusion relies on the collector, single-source and profile-compatibility reductions documented in earlier stages. These are mathematical obligations to red-team independently; the code is not a formal proof assistant.
3. A current historical [Labahn (1995)](https://doi.org/10.1016/0012-365X(94)00031-D) and [Krumme (1996)](https://doi.org/10.1016/0012-365X(94)00302-Y) priority audit is not complete at the theorem-implication level. No global novelty claim is justified.
4. The separate fixed-order temporal-clique 2n-3-edge spanner conjecture is untouched.
5. Maintain PR #1 **DRAFT/UNMERGED** and publication **HOLD** pending adversarial mathematical audit, external review and historical implication closure.
