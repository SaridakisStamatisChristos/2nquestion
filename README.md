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

The **auxiliary fixed-ORIGINAL-midpoint half-forest theorem** now has a newly constructed **human proof for n=22**, CONDITIONAL on the earlier source-grounded Bumby 1981 fixed-order spine and original chronological tree/privacy/collector lemmas. This is a genuine fixed-instance mathematical deduction if the dependencies hold, NOT an exhaustive 40-call history enumeration or a formal proof-checker result. [Stage34 manuscript](research/v5.1/N22_ORIGINAL_FOREST_THEOREM.md) and [independent finite census](research/v5.1/n22_final_center_support.py) reduce **all 24,310** 3×3 necessary-incidence matrices to ZERO, closing the last 24 candidates by 20 five-or-fewer center privacy contradictions and 4 six-center double-path incompatibilities. [Stage34 original-current-head GitHub Actions success, run 40764166711](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40764166711) confirms its finite reason partition and earlier chronological regression tests. **External referee/formal theorem checker and original scholarly-priority audit are still missing.** The unrestricted fixed-half property for n≥23 is **OPEN**.

**All-n auxiliary mathematical ingredients:**
- [Stage29](research/v4.6/PRIVATE_THRESHOLD_THEOREM.md): exact private-recipient minimum for (1,1,c) chronological tree groups: p(c)=2 (c=2,3), 1 (c=4,5), 0 (c≥6), with a genuine infinite construction. Do NOT extrapolate positive privacy beyond c=5.
- [Stage30](research/v4.7/DOUBLE_PATH_RIGIDITY.md): at sharp c=6, privacy-free two-singleton tree cover forces two disjoint three-vertex exact-support paths; two such original-order tree supports cannot be globally cross-compatible. The last unicyclic calls are outside center, permitting this tree theorem's use on their PRECEDING original-ordered spanning trees when its hypotheses hold.
- [Stage31](research/v4.8/LAST_CONTACT_COLLECTOR_TRANSFER.md): a full two-person exterior cell passes completeness to the opposite exterior via the actual last cycle edge. A size-three counterexample prevents an invalid generalization.
- [Stage32](research/v4.9/CENTER_ROOT_BOOTSTRAP.md): if one exterior has two full collectors and center has a full collector, the opposite exterior also has one. Combined with Stage28 yields universal center-root exclusion when exterior occupancy ≤8. All 4/5-person local histories exhaustively audited.
- [Stage33](research/v5.0/EXACT_TWO_RECIPIENT_PRIVACY.md): for (a,b,2) designated group chronological tree covers, a zero-private two-person group exists **iff a≥2,b≥2,a+b≥6**; exact all-size constructions and helper-robust converse.
- [Stage34](research/v5.1/N22_ORIGINAL_FOREST_THEOREM.md): all-n **conditional** root-to-tree double coverage and center-six incompatibility lemmas plus the complete n22 24,310-to-zero reason-partition. Remaining n23 necessary profiles: **396 labelled matrices / 104 tree-row/column orbits**, not realizable schedules.

**No claim of a universal temporal spanner breakthrough.** Existence of a 2n−4-call shortest gossip schedule on a time-labelled clique cannot be assumed; these structural results about an existing schedule do not establish the primary 2n−3 reachability-spanner conjecture.

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
