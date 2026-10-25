# 2n Question — Temporal Clique Research Laboratory

**Research snapshot:** 25 October 2026 · **Status:** open, reproducible research (not a proof)

> **Main open problem.** Given a complete graph on \(n\) vertices in which each undirected edge appears at a distinct time, does there always exist a subgraph with at most **\(2n-3\)** edges preserving every ordered-pair strictly increasing temporal journey?

This repository records a sequence of independent algorithmic and mathematical investigations (`v0.1`–`v0.7`). It contains actual scripts and experimental evidence from each checkpoint, including rejected hypotheses and counterexamples. **It is not a claim to have solved the conjecture.** Scientific originality of proposed subsidiary results has not been established by a comprehensive priority audit.

## Start here

- [Research status and evidence ledger](STATUS.md) — what is proved, experimentally verified, refuted, and open.
- [Reproduce the checks](REPRODUCE.md) — environment, selected deterministic commands, verification scope.
- [Research roadmap](ROADMAP.md) — highest-information next proof or falsification targets.
- [Primary references](REFERENCES.md) — source links and conceptual boundaries.
- [Complete checkpoint history](research/) — versioned source code, notes, logs, surveys and counterexamples.

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
