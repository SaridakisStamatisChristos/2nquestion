# Research v2.0 — original chronological half-forest theorem through n=14

**Status:** Exact finite computer-assisted theorem for n=14 and, using the classical two-contact vertex extension, every 4 <= n <= 14. The universal n>=15 statement and fixed-time temporal-clique 2n-3 question remain OPEN; historical global priority unresolved.

[Full manuscript](MANUSCRIPT.md) · [Adversarial review](REVIEWER_AUDIT.md)

## Reproduce

Run from the repository root with Python >=3.9 and g++ supporting C++17:

```sh
python3 research/v2.0/verify_n14.py
g++ -O3 -std=c++17 research/v2.0/independent_cross_check.cpp -o /tmp/independent_cross
/tmp/independent_cross
```

The first command covers both the old and new incidence filters, checks 81 remaining labelled placements in 3 cycle-position-aware orbits, enumerates the two decisive 6-vertex local obstructions, and verifies all 13,824 P1/Q2 pairings in the remaining orbit. The second command is an independent C++ implementation of the final local-order contradiction.

### Expected evidence
- n=13: 1278 eligible -> 9 older survivors -> **0** with the single-source lemma.
- n=14: 4698 eligible -> 738 older survivors -> **81** strengthened survivors -> **3** complete symmetry orbits.
- Orbits A/B: no local component orders meeting collector + cellwise secret coverage.
- Orbit C: 48 prefix orders, 288 suffix orders; **0** feasible pairs, **13824** information failures.
- GitHub workflow: `.github/workflows/research-v20.yml` compiles and executes code from committed sources with read-only permission and pinned checkout action.

### Sources
Original Labahn (1995) and Krumme (1996) full primary papers were user supplied and audited in [v1.8](../v1.8/ORIGINAL_PRIMARY_SOURCE_PRIORITY_AUDIT.md). Their copyrighted PDFs are not redistributed.

**Do not conflate** a valid finite certificate with global priority certification, a formal proof-assistant check, an n>=15 proof, or an improved fixed-time temporal-clique spanner bound.
