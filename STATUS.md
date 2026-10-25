# Scientific status and evidence ledger

**Snapshot:** 25 October 2026. All claims below use the model of undirected temporal cliques with pairwise distinct contact times and strictly increasing journeys. The original clique is temporally strongly connected through its direct contacts.

| ID | Statement | State | Evidence / qualification |
| --- | --- | --- | --- |
| Q0 | Every time-labelled `K_n` has a temporal spanner with `<=2n-3` edges | **OPEN** | External open-problem tracker; no proof/counterexample here |
| C1 | Non-pivotable `K_n` always has a `2n-4`-edge spanner (POD) | **CONJECTURE** | Exact finite cases and biased random testing; not established universally |
| C2 | Every temporal clique has a treewidth-2 spanner | **REFUTED** | Explicit K6 chronology and exhaustive 1,215 spanning 2-tree test (v0.6) |
| C3 | Every temporal clique has a treewidth-3 spanner | **OPEN HYPOTHESIS** | Only finite sampled n=7,8 evidence; universal `3n-6` implication would be conditional |
| C4 | Ordinary random edge permutations frequently have a pivot in small sampled sizes | **EMPIRICAL** | v0.7: K7 9,822/10,000 and K8 598/600, RNG-controlled |
| C5 | Frontier cuts are valid for *arbitrary* selected subgraphs | **PROVED (human proof)** | v0.5 containment argument; finite differential tests |
| C6 | The basic all-frontier-cut LP is integral | **REFUTED** | K4 instance with fractional optimum 3 and integral optimum 4 (v0.5) |
| C7 | A proposed formula `|F|<=max(0,2n-p-q-1)` for compulsory edges | **REFUTED** | K4 counterexample recorded in v0.3 |
| C8 | Small/individual edge-deletion tests certify arbitrary simultaneous removals | **REFUTED** | v0.4 higher-order obstruction family |
| C9 | Certain indispensable-edge precedence restrictions | **PROVED (human proofs)** | v0.2/v0.3, scope in original notes; novelty not assessed |
| C10 | An explicitly listed nonpivotable K7 has exactly three size-10 spanners and min spanner treewidth 3 | **VERIFIED FINITE** | Independent C++/Python enumeration (v0.7) |

### Not established

- No universal upper bound better than the cited published literature was proved in these checkpoints.
- No solution of `2n-3`; no certified n>=9 counterexample.
- No new complexity separation or publication-priority conclusion.
- No full Lean/Coq/Isabelle formal verification.
- No assertion that an exact finite obstruction is necessarily absent from prior literature.

### Evidence provenance and caveats

The versioned `research/v0.x/` directories preserve original evidence, including hypotheses later rejected. A green local script provides only the claimed *finite* scope. Source code is research/prototype quality; benchmark timing is not a state-of-the-art performance claim. README summaries never supersede mathematical definitions in the checkpoint notes.

## Immediate audit requirements

1. Independently check every claimed exhaustive enumeration's domain and symmetry reductions.
2. Audit the v0.4 infinite-family proof for temporal chronology assumptions and priority.
3. Investigate historical gossip and temporal spanner literature before claiming that any treewidth separation is novel.
4. For proposed universal results, demand a complete proof or a small independently checkable falsifying instance.

## v0.8 update — 25 October 2026

| ID | Statement | State | Evidence / qualification |
| --- | --- | --- | --- |
| C11 | The 14 v0.2 hard, non-pivotable `K9` schedules all admit 14-edge spanners | **VERIFIED FINITE** | `research/v0.8/certificates_pod9.json`; independently checked with 14 source-by-source oracles and time-reversal / relabeling tests |
| C12 | Fixed-restart greedy hardness indicates absence of a 14-edge spanner | **REFUTED AS AN INFERENCE** | `research/v0.8/adversarial_best9.txt` scored 15 under 24 deletion orders; independent greedy seed 3 found a verified 14-edge witness |
| C13 | The v0.8 scripts provide an unbounded proof of POD or `2n-3` | **NOT ESTABLISHED** | All evidence is restricted to individual orders; see `research/v0.8/RESEARCH_UPDATE_v0.8.md` |

Selected independent verifier: `python research/v0.8/independent_verify_v08.py` — 14 `K9` certificates plus 46,080 `K4` differential checks passed in the recorded local run. No formal proof assistant or GitHub CI run is claimed. Scholarly novelty remains unresolved.

## v0.9 checkpoint — 25 October 2026

| ID | Statement | Evidence state | Proof/data |
| --- | --- | --- | --- |
| C14 | Incident-local MILP exactly encodes strict chronological temporal reachability with only `m` binary edge variables and `n^3` continuous state variables | **PROVED (human argument); implementation tested** | `research/v0.9/RESEARCH_UPDATE_v0.9.md` and `incident_milp.py`. Novelty **not established** |
| C15 | Exact solver matches independent brute-force optimum on all `K3`, all `K4`, and 120 seeded `K5` schedules | **VERIFIED FINITE** | `research/v0.9/verify_incident_milp.py`, `validation_results.json` |
| C16 | Six selected non-pivotable `K10` extensions admit optimal `2n-4=16`-edge spanners | **VERIFIED FINITE** | `research/v0.9/targeted_n10_results.json`, independent `independent_check_v09.py`; one initial timeout resolved by longer run |

**No change to main verdict:** the universal `2n-3` conjecture, POD, and treewidth-3 hypothesis remain open. No priority-verified new universal theorem has been established.

## v1.0 checkpoint — 25 October 2026

| ID | Statement | Evidence state | Proof/data |
| --- | --- | --- | --- |
| C17 | Every shortest *distinct-edge* gossip protocol on `4 <= n <= 6` contains a chronological 4-cycle butterfly | **VERIFIED FINITE EXHAUSTIVE** | `research/v1.0/exhaustive_kernel.cpp`; 17,297,280 first-contact-normalized K6 sequences, 83,808 optimal connected cases, zero butterfly-free; see v1.0 note. No universal theorem or novelty priority claimed. |
| C18 | The chronological butterfly hypothesis holds for all `n` | **OPEN** | Heuristic 350,000-proposal walks each on n=6..10 found no counterexample; minimum-gossip kernel priority unresolved, including Labahn (1995). |

**No change to the main question:** `2n-3` and POD remain OPEN. Finite BF(n<=6) does not prove their universal bounds.

### v1.0 universal necessary condition

| C19 | In every `2n-4`-call all-to-all gossip schedule, each vertex participates in a call among the first `n-2` and another among the last `n-2` | **PROVED (human argument); novelty unchecked** | `research/v1.0/INCIDENCE_WINDOW_LEMMA.md`. Source-information carrier count increases at most once per call; reverse time for the last-call bound. |
This is a necessary condition for an optimal-length protocol, not a proof of the `2n-3` upper bound; likely existing elementary gossip theory.

## v1.1 — sharp chronological half-forest threshold (25 October 2026)

| ID | Statement | State | Evidence / qualification |
| --- | --- | --- | --- |
| C20 | At every temporal cut of a successful gossip protocol, every prefix contact-graph component intersects every suffix component | **PROVED (human proof)** | The component incidence graph is complete; hence c_prefix*c_suffix <= n. See `research/v1.1/RESEARCH_UPDATE_v1.1.md`. Originality unchecked. |
| C21 | Every shortest 2n-4 call protocol for n=4..7 has each chronological half a two-component forest | **PROVED (human proof)** | Sharp seven-vertex contradiction from three prefix components and a suffix three-vertex tree. |
| C22 | Every shortest gossip protocol (any n) has forest contact graphs in both halves | **REFUTED** | Explicit 8-vertex 12-contact witness, independently verified using time-respecting path DFS; see `research/v1.1/sharp_half_forest.py` and `audit_threshold.py`. |
| C23 | Shortest gossip schedules with a cyclic chronological half exist for every n>=8 | **PROVED (constructive induction)** | Prefix one contact from new vertex to old u, run original protocol, suffix contact from new vertex to a distinct old v. |

**No change to the primary targets:** POD and the universal 2n-3 temporal-clique bound remain OPEN. The v1.1 result is a sharp negative boundary for a structural proof strategy, not a solution to either conjecture. Labahn (1995) and Krumme (1996) are important priority risks; publication novelty remains unverified.

| C24 | Every shortest gossip schedule on n<=10 vertices has at least one forest half | **PROVED (human proof); novelty unverified** | `research/v1.1/BOTH_HALVES_BOUND.md`: 3x3 intersection and three-agent gossip lower bound exclude two cyclic halves for n=9,10; n<=8 handled by component product and sharp threshold. |
