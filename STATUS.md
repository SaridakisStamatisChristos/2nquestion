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
