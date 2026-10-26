# v2.1 interrupted-session recovery — 26 October 2026

**DO NOT LABEL THE n=15 THEOREM CI-VERIFIED.**

The session stalled during v2.1 publication. The existing PR's verified research state is **v2.0, through n=14**, commit `f2d421a91`. The two documents next to this file are **UNVERIFIED WORKING DRAFTS**, preserved for continuity. They describe a claimed n=15 exhaustive 20-orbit UNSAT result, but **the executable source and proof certificates were NOT preserved at the time of this recovery**, and no v2.1 GitHub Actions verification has run. Do not promote these draft claims to published or certified status.

## Recoverable evidence
- `MANUSCRIPT_DRAFT_UNVERIFIED.md`: v2.1 mathematical report and claimed 20/20 exclusion, not checked on GitHub.
- `REVIEWER_DRAFT_UNVERIFIED.md`: draft audit of the missing verifier and optimistic-profile relaxation, not externally peer reviewed.
- The original missing files expected by the manuscript: `prove_n15.py`, `profile_oracle.cpp`, `component_oracle.cpp`, `verify_profile_semantics.py`, `verify_n15_independent.py`, `N15_CERTIFICATE.json`, individual run logs, and `.github/workflows/research-v21.yml`. **None are in this commit.**

## Non-negotiable continuation gates
1. Reconstruct or retrieve every source verifier from the interrupted session and inspect it; do not derive fake certificates from this report.
2. Independently rerun the 945-placement / 20-orbit structural reduction from the verified v2.0 lemmas.
3. Independently establish soundness of any compressed temporal profiles, pruning and optimistic-tree overapproximation.
4. Complete a full exact 20/20 run with saved machine-readable certificate, a second independent implementation and green **GitHub CI**, not just a displayed success claim.
5. Only then update the manuscript as a computer-assisted n<=15 theorem and re-run research-auditor novelty gates.
6. Keep PR #1 draft and do not merge without explicit request.

**Working scientific status:** n<=14 CI-verified. n=15 claim **UNVERIFIED / OPEN** until the missing executable evidence is recovered and rerun. This handoff deliberately supersedes stronger v2.1 success language from the interrupted chat.
