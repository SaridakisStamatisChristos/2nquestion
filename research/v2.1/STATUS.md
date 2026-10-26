# v2.1 recovery: structural result verified; n15 theorem NOT certified

Recovery date: 26 October 2026. Status: PARTIAL.

The preceding chat interface stalled during export of an n=15 research package. The manuscript and review text survived, but the claimed exact chronological solver sources (prove_n15.py, profile_oracle.cpp, component_oracle.cpp, verify_n15_independent.py), N15_CERTIFICATE.json, and their claimed logs were not present in the recovered working files. Nothing was committed to this repository under v2.1 before recovery.

## Independently checked
A standalone independent Python reimplementation was executed locally with the following exact results, and the new repository checker reproduces them through the existing v2.0 implementation:

| n | total 3x3 allocations | eligible placements | original-filter survivors | stronger-filter survivors | orbit count |
| --- | ---: | ---: | ---: | ---: | ---: |
| 13 | 495 | 1278 | 9 | 0 | 0 |
| 14 | 1287 | 4698 | 738 | 81 | 3 |
| 15 | 3003 | 13680 | 4662 | 945 | 20 |

The standalone implementation is preserved in the current working-session export. The committed verification script explicitly tests n=13..15 as a reproducibility regression gate.

## NOT verified
The assertion that all 20 n15 orbits are UNSAT by seven local, ten exact global, and three optimistic relaxation proofs is PRESENTLY UNSUPPORTED by available executable artifacts. The interrupted manuscript made this claim, but the named source programs and complete machine-readable certificates were not preserved. Do not present n15 as proved on the strength of the text alone, and do not treat prior narration as execution evidence.

## Next evidence needed
Reconstruct exact component-order enumeration and the sound global temporal-information-profile oracle. For each of the 20 orbits, record complete state counts / UN SAT certificates; independently rerun at least one separate implementation; distinguish timeout from UNSAT; then gate the theorem via GitHub CI. The verified finite theorem through n=14 remains intact.

Universal original-half forest conjecture: OPEN. Scholarly priority: unresolved. Draft PR must remain unmerged.
