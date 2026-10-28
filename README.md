# 2n Question — Temporal Clique Research Laboratory

**Research snapshot:** 28 October 2026 · **Status:** open, reproducible research; main temporal-clique conjecture unproved

> **Main open problem.** Given a complete graph on \(n\) vertices in which each undirected edge appears at a distinct time, does there always exist a subgraph with at most **\(2n-3\)** edges preserving every ordered-pair strictly increasing temporal journey?

This repository records a sequence of independent algorithmic and mathematical investigations (`v0.1`–`v0.7`). It contains actual scripts and experimental evidence from each checkpoint, including rejected hypotheses and counterexamples. **It is not a claim to have solved the conjecture.** Scientific originality of proposed subsidiary results has not been established by a comprehensive priority audit.

## Start here

- [Research status and evidence ledger](STATUS.md) — what is proved, experimentally verified, refuted, and open.
- [Reproduce the checks](REPRODUCE.md) — environment, selected deterministic commands, verification scope.
- [Research roadmap](ROADMAP.md) — highest-information next proof or falsification targets.
- [Primary references](REFERENCES.md) — source links and conceptual boundaries.
- [Complete checkpoint history](research/) — versioned source code, notes, logs, surveys and counterexamples.

## Latest research and proof boundary (28 October 2026)

**Two separate objectives must not be confused.** The principal **fixed-label temporal clique spanner** statement asks whether every edge-ordering of \(K_n\) has a reachability-preserving subset of at most \(2n-3\) contacts. This is **OPEN**. The *auxiliary* original chronological half-forest property concerns the structure of a minimum \(2n-4\)-contact gossip chronology **if that chronology already exists**. Proving a structural property of an existing optimum does **NOT** prove existence of an optimum or the \(2n-3\) bound for every clique.

The auxiliary fixed-original-half forest statement has a human proof plus finite regression coverage for n<=21, conditional on the exact classical/source-level and local lemmas; n>=22 is **OPEN**. For n22, the previously verified necessary-incidence census has **104 labelled survivor matrices / 28 tree-row/column symmetry orbits** after the all-n Stage28 collector obstruction. A survivor is NOT a successful 40-contact gossip chronology or a counterexample.

**New all-n auxiliary mathematics (not a global proof):**
- [Stage29 exact private-recipient theorem](research/v4.6/PRIVATE_THRESHOLD_THEOREM.md) — for chronological tree recipient groups (1,1,c), the minimum private recipient count is exactly 2 for c=2,3; 1 for c=4,5; 0 for c>=6, even allowing unassigned helpers. All bounds have explicit parameterized witnesses. [Source/independent executable regression](research/v4.6/private_threshold.py).
- [Stage30 double-path source-support rigidity](research/v4.7/DOUBLE_PATH_RIGIDITY.md) — a sharp six-recipient privacy-free tree forces four exact 2-person source supports forming two disjoint 3-vertex paths. An opposing two-person target support is forced to their centers; only 25 of 63 nonempty target masks satisfy the four forced crossings. **Both opposing sharp six-recipient trees cannot be fully cross-compatible**, but an arbitrary opposing unicyclic component is NOT excluded. [Exact chronological and 90x90 labelled Boolean falsifier](research/v4.7/double_path_rigidity.py) and [n22/n23 CSP target registry](research/v4.7/n22_double_path_targets.py).
- [Stage30 CI](.github/workflows/research-v47.yml) verifies independent chronological, combinatorial and earlier regression gates. **Always inspect the current commit's actual run conclusion before quoting PASS.**

**Contemporary reference boundary:** [Baligács 2026](https://arxiv.org/abs/2606.05156) proves a 7n reachability spanner upper bound, with an author's [September 2026 open-problem summary](https://arnaudcasteigts.net/blog/open-problems.html) describing a refinement to 6n using the same algorithm. The [September 2026 almost-linear *3-spanner*](https://arxiv.org/abs/2609.02851) concerns multiplicative temporal **hop stretch**, a different objective, and does not solve exact reachability preservation with 2n−3 edges. No claim of global novelty, formalized proof, or publishable readiness is made here.

**Research governance:** [PR #1](https://github.com/SaridakisStamatisChristos/2nquestion/pull/1) remains DRAFT, OPEN, UNMERGED, manuscript submission HOLD. [Updated next steps](ROADMAP.md) prioritize the true exact-chronology information CSP and direct spanner conjecture, not indefinite finite-size enumeration.

## Research trajectory

| Checkpoint | Investigation | Outcome |
| --- | --- | --- |
| [v0.1](research/v0.1/RESEARCH_NOTE.md) | Pivot–Optimal Dichotomy (POD); finite exact optimization | Hypothesis and finite evidence; **not** universally proved |
| [v0.2](research/v0.2/RESEARCH_UPDATE_v0.2.md) | Temporal precedence, indispensable contacts | Restricted proved lemmas; speculative structural bounds |
| [v0.3](research/v0.3/RESEARCH_UPDATE_v0.3.md) | Precedence conjectures and adversarial repair | Overstrong counting bound **refuted**; limited extremal lemma |
| [v0.4](research/v0.4/RESEARCH_UPDATE_v0.4.md) | Simultaneous deletions and exchange obstructions | Explicit higher-order obstruction family; novelty unverified |
| [v0.5](research/v0.5/RESEARCH_UPDATE_v0.5.md) | Global chronological-frontier cuts and exact solver | Sound cut validity; **nonintegral** LP witness |
| [v0.6](research/v0.6/RESEARCH_UPDATE_v0.6.md) | Treewidth-2 spanner hypothesis | Six-vertex counterexample, checked exhaustively |
| [v0.7](research/v0.7/RESEARCH_UPDATE_v0.7.md) | Treewidth-3 searches; pivot-aware sampling | Reproducible finite K7 certificates; universal questions still open |

## Reproduced checks from this import

Executed with Python in the local research environment:

- `research/v0.4/v04_independent_verify.py` — tested hypercube-style obstruction families at `n=16,32,64`.
- `research/v0.5/verify_v05.py` — complete K3/K4 cut checks, selected K5 cases, and fractional LP example: **PASS**.
- `research/v0.6/independent_verify.py` — zero successful spanning 2-trees among 1,215 and an eight-edge treewidth-3 witness: **PASS**.
- `research/v0.7/code/independent_v07.py` — pivot and nonpivot seven-vertex witness counts and treewidth: **PASS**.

These are selected local reruns, not a CI-verified or machine-formalized universal theorem. Computational certificates about small graphs must not be generalized without proof.

## Contributing / priority

Please open issues or pull requests for minimized counterexamples, corrected proofs, independent verifiers, or precise prior-art matches. Distinguish a **proof**, **exhaustive finite computation**, **sampled experiment**, and **novelty hypothesis** explicitly. Do not present v0.6's treewidth-2 counterexample as refuting the 2025 **2-degenerate / 2-arch** conjecture: the concepts differ.

Research snapshots are preserved to keep negative results and historical conjectures auditable. Some v0.1–v0.4 tools are exploratory and may require execution from their own checkpoint directories.
