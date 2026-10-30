# v2.2 research status — sixteen-vertex original half-forest theorem

**26 October 2026 | Computer-assisted finite verification: PASS | Novelty: UNRESOLVED | Submission readiness: HOLD**

## Canonical finite claim

For every n with **4<=n<=16**, every shortest successful 2n-4-call bidirectional telephone-gossip schedule with **pairwise-distinct** unordered contacts, when split into its **unchanged original** first n-2 and last n-2 calls, has at least one acyclic half.

This is a **bounded computer-assisted theorem**, not a universal n>=17 result, not Lean/Coq-formalized, and not a fixed-label temporal-clique sparse-spanner result.

## Executed n16 evidence

- **Rectangular elimination:** 3x4/4x3/4x4 cases impossible by tree collector bounds and single-source entry. [Independent structural CI PASS](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40375016489).
- **3x3 incidence:** 6,435 positive allocations, 34,092 eligible marked placements, 16,704 basic, **4,635** stronger survivors, **81** marked symmetry classes. Two different generators agree on every orbit and multiplicity.
- **Initial profile classification:** 13 locally impossible, 66 globally profile-incompatible, 2 relaxed-SAT (not legal witnesses).
- **Exact eight-vertex residuals:** [orbit 10](exclude_n16_orbit10.py) exact tree profiles and [orbit 11](exclude_n16_orbit11.py) exact cyclic profiles both violate a necessary B/D subset-compatibility bitmask check in their common four-vertex cell. Neither depends on large optimistic domain equality.
- **Independent exact local domains:** **77 of 77** distinct exact component profile B/D pairs were separately enumerated by two C++ algorithms, without shared memoization machinery.
- **Final full certificate:** **81/81 UNSAT**, multiplicity **4,635/4,635**, categories **13 local / 68 global**. [Successful full n16 CI run 40378654998](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40378654998).
- **Machine-readable:** [N16_CERTIFICATE.json](N16_CERTIFICATE.json) contains all 81 orbit records. The [full verifier](prove_n16.py) recomputes the entire classification from source and requires equality to this checked-in certificate, in addition to structural and independent-local checks.

## Manuscript and historical novelty

The [updated n<=16 research working manuscript](PAPER_DRAFT_N16.md) and detailed [mathematical research report](RESEARCH_UPDATE.md) state the finite proof, the new equality-case rectangular obstruction, local exact eight-vertex rigidity, complete certificate, algorithmic independence limits and bibliographic attribution.

The [Stage 4 source-by-source originality review](../v2.1/STAGE4_PRIORITY_AND_PUBLICATION_AUDIT.md) is **not** superseded in its risk decision: Labahn (1995), Krumme (1996), Göbel et al. (1991), West (1982) and Williams (2026) contain extensive related prior art. The full n<=16 result might be an implicit consequence of earlier classification. The independently verified [same-poset midpoint-rank witness](verify_kernel_scope.py) shows that individual fixed midpoint cycle ranks are **not determined by the minimal event poset alone**, but does **not** prove that the weaker at-least-one-forest theorem cannot be deduced by further classical theory.

**Next proof frontier:** n>=17 structural incidence (especially 3x4), general parameterized proof or true counterexample, and complete historical implication analysis. **PR #1 remains DRAFT and UNMERGED.**


### New historical finding

[Labahn–Pietsch, *Characterizing Minimum Gossip Graphs on 16 Vertices*](PRIOR_ART_N16_UPDATE.md) is a close-title predecessor about **minimum communication rounds and minimum supporting links**, **not** the same 28-call original-midpoint question. Its exact model difference and inconsistent public publication dates are documented. Historical novelty remains unresolved rather than claimed.
