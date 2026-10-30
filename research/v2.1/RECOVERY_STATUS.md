# v2.1 interrupted-session recovery — closure record, 26 October 2026

**Recovery gate: CLOSED for the bounded n=15 computational certificate.** The originally missing verification source files were **not** recovered as byte-identical originals. Instead, a new independently constructed finite-search package has been committed, executed and checked in GitHub CI. See [STATUS.md](STATUS.md) and [RESEARCH_UPDATE_VERIFIED.md](RESEARCH_UPDATE_VERIFIED.md).

## What had been lost

The earlier chat stalled after creating MANUSCRIPT_DRAFT_UNVERIFIED.md and REVIEWER_DRAFT_UNVERIFIED.md. At the initial recovery commit, the named executable solvers, full 20-orbit certificate and GitHub CI were absent. Those historical documents were correctly marked UNVERIFIED. They remain archived and **must not** be used as independent evidence, even though the newly reconstructed verifier supports a bounded result.

## Newly checked recovery evidence

- Two structural enumerators agree at n=13,14,15 and identify 3,003 positive n15 grids, 13,680 eligible cycle placements, 4,662 basic survivors, 945 strong survivors and exactly twenty symmetry orbits.
- Exact connected component chronology enumeration for m<=7; sound optimistic two-side information overapproximation for larger tree components.
- All twenty orbits produce UNSAT under the necessary relaxed profile compatibility condition: **six local empty domains, ten global exact-profile incompatibilities and four global optimistic-tree incompatibilities**, covering all 945 placements. The historical unverified manuscript's 7/10/3 breakdown is superseded.
- Separate Python implementation of all twenty global profile compatibility checks; four independently enumerated smaller component domains; 3,200 direct semantics tests; 240 tree-overapproximation containment checks.
- Machine-readable [N15_CERTIFICATE.json](N15_CERTIFICATE.json), primary source [profile_oracle.cpp](profile_oracle.cpp), reproduction runner [prove_n15.py](prove_n15.py) and CI workflow.

## GitHub verification

The v2.1 workflow completed successfully after the additional independent structural enumerator was integrated, on commit 99bff1dfdd9ef30c29c68d4c2b9aafe69266bccd:

- Push run: https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40346862524
- Pull-request run: https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40346871327

A prior CI run failed due to a Python tuple-versus-JSON-list representation mismatch in the certificate comparison; it was corrected, and the completed passing runs checked all rows of the committed certificate.

## Remaining scientific boundaries

The result is a **computer-assisted finite classification for n<=15** conditional on the documented combinatorial lemmas and implementation soundness. The separate global checker consumes primary-oracle generated large-component domains; the seven-vertex local enumeration is not independently reimplemented in a second language. This is not Lean/Coq formal certification, external peer review, or a resolution of the all-n half-forest conjecture.

The fixed-order temporal-clique 2n-3 conjecture remains open, and historical originality versus the classical gossip-kernel literature is unresolved. **Keep PR #1 draft and unmerged.**


## 26 October 2026 Stage 3 independence closure (supersedes the above residual single-oracle caveat)

The residual statement above that the seven-vertex exact oracle lacked a second independent implementation has been **superseded**. [STAGE3_ADVERSARIAL_AUDIT.md](STAGE3_ADVERSARIAL_AUDIT.md) documents the second independently written C++ oracle, which uses union-find and an explicit final-two-call search rather than the primary memoized chronology DFS. The two programs produce exactly matching complete B/D profile sets for **all 33 exact component types**, including both seven-vertex unicyclic types; the all-20-orbit UNSAT result survives domain substitution. Exhaustive collector, tree dominance and temporal duality checks pass.

- [Stage 3 CI push PASS](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40356861884)
- [Stage 3 CI PR PASS](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40356872700)

The bounded n<=15 computational verification is now at **Stage 3 PASS**. Formal proof-assistant certification, external refereeing, priority analysis and unbounded generalization remain separate unfinished objectives. PR #1 remains draft/unmerged.
