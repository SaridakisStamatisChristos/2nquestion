# v2.1 status — n=15 finite half-forest certificate independently checked and CI PASS

Date: 26 October 2026. **Status: BOUNDED COMPUTER-ASSISTED RESULT THROUGH n=15.**

## Exact scope

Every successful shortest schedule of pairwise-distinct undirected full-information telephone calls on 4 <= n <= 15 has at least one *original, unchanged chronological half* whose static contact graph is a forest. For n=15 this follows from a finite exhaustive reduction and sound profile relaxation, as verified by the committed C++17 and Python execution. It is not a universal all-n result or a fixed-order temporal-clique 2n-3 spanner proof.

## Completed v2.1 recovery

The earlier chat lost the executables and certificates. New sources were independently **reconstructed**, not merely copied from the optimistic lost manuscript. The verified source package contains:

- profile_oracle.cpp: exact m<=7 component-order search and optimistic large-tree domains, followed by global suffix-first profile CSP.
- verify_n15_independent.py: second Python CSP for all twenty orbits plus four independently enumerated small component domain checks.
- verify_n15_structural_independent.py: positive-composition structural enumeration, distinct from the earlier extra-vertex multiset algorithm.
- verify_profile_semantics.py: 3,200 direct temporal semantics differentials and 240 optimistic-tree checks.
- prove_n15.py: complete deterministic compilation/verification gate.
- N15_CERTIFICATE.json: twenty representative matrices, cycle placements, multiplicities, reasons and profile domain sizes.
- .github/workflows/research-v21.yml: fresh GitHub Linux CI verification.

| n | Positive grid allocations | Eligible | Basic survivors | Strong survivors | Orbits |
| --- | ---: | ---: | ---: | ---: | ---: |
| 13 | 495 | 1,278 | 9 | 0 | 0 |
| 14 | 1,287 | 4,698 | 738 | 81 | 3 |
| 15 | 3,003 | 13,680 | 4,662 | 945 | 20 |

**All 20 n=15 orbits excluded:** 6 exact empty local domains; 10 exact-profile global CSP UNSAT; 4 optimistic-tree-profile global CSP UNSAT. Total multiplicity **945/945**. The lost draft's proposed 7/10/3 split is superseded by these executed 6/10/4 counts.

## Independent execution and CI

The second Python CSP independently reruns all 20 compatibility cases using exported component profiles. Structural cases and orbit multiplicities are regenerated with two algorithms; four small local component-domain types are independently enumerated in Python. The expensive seven-vertex local enumeration is still implemented in the primary C++ oracle only — it is **not** a second fully independent large-component proof.

GitHub Actions success on commit 99bff1dfdd9ef30c29c68d4c2b9aafe69266bccd:

- Push: https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40346862524
- PR: https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40346871327

Run from root: python3 research/v2.1/prove_n15.py

See RESEARCH_UPDATE_VERIFIED.md for the profile equivalence proof, pruning and optimistic-relaxation soundness, independence limitations, and exact evidence chain. The MANUSCRIPT_DRAFT_UNVERIFIED.md and REVIEWER_DRAFT_UNVERIFIED.md remain archival drafts, not accepted certificate sources.

## Unresolved

Unbounded n>=16 half-forest assertion: **OPEN**. Separate temporal-clique 2n-3 conjecture: **OPEN**. Scholarly historical novelty: **UNRESOLVED**. No Lean/Coq proof or external peer review. PR #1 remains **DRAFT and UNMERGED**.


## Stage 3 — second exact local oracle and adversarial falsification: PASS (26 October 2026)

The originally unverified seven-vertex local oracle has now been **fully and independently reimplemented**, not merely rerun. The independent disjoint-set/two-phase C++ enumerator performs no history-state memoization, enumerates all 33 exact component types used by the finite proof, and obtains **identical complete B/D profile sets** to the original oracle. Both n=7 unicyclic types are checked: (2,2,3) with collector needs (2,2,0) has no admissible profile; (2,3,2) with needs (2,1,0) has 9 B and 27 D profiles.

After replacing every exact original profile domain with its independently generated counterpart, all **20 global UNSAT orbits** remain excluded, covering **945 of 945** placements.

A separate exhaustive Python adversarial check covers every selected connected or disconnected tree/unicyclic contact order on n=3..5 and every 5-edge candidate tree order on n=6 (360,360 sequences), with no violation of necessary final-contact collector restrictions or optimistic tree information bounds. An independent forward/reverse temporal test checks all 517 distinct-edge K4 sequences through four contacts, **8,272 source/destination comparisons**, without mismatch.

- [Complete Stage 3 mathematical and implementation audit](STAGE3_ADVERSARIAL_AUDIT.md)
- [Independent C++ oracle](stage3_independent_oracle.cpp)
- [Full-domain comparison and 20-orbit audit](stage3_adversarial_check.py)
- [Exhaustive falsification checks](stage3_exhaustive_stress.py)
- [Successful extended push run](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40356861884)
- [Successful extended PR run](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40356872700)

**Stage 3 disposition: PASS for bounded computer-assisted n<=15 verification.** Formal proof-assistant verification, external peer review and classical-priority determination are still absent. Stage 4 (novelty/publication review) has **not** been completed. PR #1 remains DRAFT and UNMERGED.
