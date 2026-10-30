# 2n Question — recursive historical-priority and theorem-implication audit

**Audit date:** 25 October 2026  
**Repository:** [SaridakisStamatisChristos/2nquestion](https://github.com/SaridakisStamatisChristos/2nquestion)  
**Research head inspected:** `3d827a72a8b4d795170ec75759fd4a79a51c85d6`  
**PR:** [#1 (draft)](https://github.com/SaridakisStamatisChristos/2nquestion/pull/1)  
**Modes:** SOTA Research Auditor (novelty protocol); Knowledge Nexus (evidence dependence); Theorem Foundry (implication audit); Algorithm Foundry (reproducible witness).  
**Scope:** historical and current publicly discoverable research on ordered minimum-size telephone-gossip schemes, their kernels, label-connected graphs, original chronological halves, temporal-clique spanners, and related enumeration methods.

## Executive decision

**The novelty gate remains UNRESOLVED, not PASSED and not proven FAILED.**

We found **direct prior art** for the classical `2n-4` bound, static decompositions into two two-component forests, the original two-contact vertex extension, event-order/linear-extension analysis, and reordering by swapping independent calls. These elements should no longer be individually described as novel.

We found **no accessible source explicitly stating** the exact *original chronological midpoint* assertion for every shortest distinct-edge gossip scheme through 13 vertices, nor the v1.4 *first-bridge covering lemma* in precisely its `k=1,2,3` form. This is not a priority certificate: Labahn (1995) characterizes optimal kernel posets and their linear extensions, and Krumme (1996) proves a reordering theorem, while their full journal texts were **not obtainable** during this audit.

**Publication novelty claim:** BLOCKED pending full-text implication analysis and independent checking.  
**Mathematical finiteness evidence:** v1.4 CI reproducible, but this audit is mainly about priority, not a fresh independent full formal verification.  
**Universal `2n-3` temporal-clique spanner conjecture:** OPEN and not resolved by these findings.

## Claim-level priority matrix

| Repository statement / technique | Exact predecessor and scope | Audit state |
| --- | --- | --- |
| Every full telephone-gossip schedule needs at least `2n-4` calls, `n>=4` | Classical proofs 1971–72; reviewed by West (1982), §1, and Göbel et al. (1991), Theorem 1 | **KNOWN / NOT NOVEL** |
| A minimum-size label-connected graph admits a decomposition into two disjoint spanning **two-component forests** with 4-cycle crossing properties | Göbel–Cerdeira–Veldman (1991), **Theorems 3 and 9** (Cd-graph characterization). Their theorem is *existential over an edge partition*. | **DIRECT STATIC PRIOR ART** |
| One may add a fresh vertex with one call before and one call after a successful schedule while preserving temporal connectivity | Göbel–Cerdeira–Veldman (1991), **Theorem 13**, gives exactly this graph/label extension | **DIRECTLY PREVIOUSLY PUBLISHED** |
| A shortest optimum must contain a 4-cycle | Gossip four-cycle theorem; Göbel et al. (1991), Theorem 1, cites earlier proof | **KNOWN** |
| Represent minimal event order, initial/final kernel antichains and necessary cardinality equalities | Labahn 1993; 1995 Theorem 3.1 and Corollary 3.1 as reconstructed with explicit numbers in Renken (2023), printed pp. 97–102 | **KNOWN STRUCTURAL PREDECESSOR** |
| Classify optimal kernels using `κ` initial, `κ` final and `2κ-4` intermediate calls, plus permutation restrictions | Labahn (1995), Section 6 and Theorem 6.3, reconstructed by Renken (2023), printed pp. 99–102 | **DIRECT THEORY PREDECESSOR** |
| Count / sample linear extensions of gossip contact posets and analyze commuting disjoint calls | Labahn (1995) explicitly studies counts of linear extensions; Krumme (1996) reorders; 2026 Williams Lemma 2.5 uses adjacent swaps of disjoint calls | **METHOD ALREADY ESTABLISHED** |
| The exact *original* chronological half forests, rather than *some* static partition, obey a structural restriction | Static characterization does not fix original halves; verified constructive distinction in `verify_1991_cd_gap.py` | **LOGICALLY DISTINCT FROM GCV 1991 THM 9; original novelty still UNKNOWN** |
| First-bridge covering lemma: two singleton intersections force the first suffix-tree bridge, and a third prefix source requires carriers on both bridge sides | Structurally consistent with classical information-flow conservation and kernel/fringe theory; no accessible exact old statement found | **POSSIBLY DISTINCT FORMULATION; PRIORITY UNRESOLVED** |
| Every successful shortest simple 22-contact gossip scheme on `n=13` has at least one forest chronological half | v1.4 script and CI, plus published kernel structure as potential implication | **POSSIBLY DISTINCT FINITE COROLLARY; PRIORITY UNRESOLVED** |
| Minimal event-poset alone does not determine midpoint cycle rank | v1.5 witness verifies phenomenon; incomparable disjoint-call reordering and vertex extension both already known | **EXAMPLE DISTINCTION REPRODUCIBLE; NOVEL METHOD NOT ESTABLISHED** |
| Main clique universal `2n-3` sparse temporal spanner, preserving an **adversarial fixed time labeling** | Current Casteigts open-problems tracker (updated September 22, 2026), CPS 2019/2021, later 2026 `7n` bound | **OPEN, NOT PROVED HERE** |

## Key quantifier distinction established through a full 1991 primary source

**1991 Theorem 9:** A static graph with `2n−4` edges *admits some admissible edge labeling* if and only if it is a Cd-graph, meaning it has a *suitable partition* into two `n−2`-edge two-component forests satisfying special 4-cycle incidence constraints. Theorem 3 guarantees the sufficiency of the structural decomposition.

This **does not** assert that the two consecutive chronological halves in *every admissible labeling* are forest graphs. We proved that they can differ even when the very same graph has a Cd partition:

- The eight-vertex ordered witness has 12 distinct edges, is temporally all-to-all connected and its **first six and last six** contacts have cycle ranks **(0,1)**.
- It nevertheless possesses an edge partition (indexed from zero by chronology)
  - Cd-forest A = `{0,1,2,3,4,9}`
  - Cd-forest B = `{5,6,7,8,10,11}`
  - crossing 4-cycle `0–1–5–4–0` with opposite forest edges in distinct components.
- The independent script enumerated all `C(12,6)=924` oriented partitions, found **604** forest/forest partitions, and verified the explicit Cd certificate by exact graph-components and all-source temporal reachability checks.

**Logical conclusion:** Older *static forest decomposability* is not the same proposition as *forest half at the original chronological cut*. **Caveat:** This does not establish that Labahn's full kernel characterization cannot imply the latter via additional reasoning or analysis of compatible linear extensions.

### The extension is NOT novel

The new-vertex operation `new-u`, then the old sequence, then `new-v` was already published as **Theorem 13** in the same 1991 paper. Consequently, earlier research notes should describe v1.5's `n=8→13` lift as *application of a classical extension*, not as a novel construction technique. The paired schedules and their specific midpoint distinction remain concrete reproducible computational examples, but are not thereby publication-original.

## Theorem-level reading of historical sources

### Göbel, Cerdeira and Veldman (1991), COMPLETE primary text inspected

- Theorem 1: classical `2n−4` lower bound and optimal 4-cycle condition.
- Theorem 2: a spanning tree + disjoint spanning tree-pair suffices for label-connectivity.
- Theorem 3: two spanning tree-pairs linked through an alternating 4-cycle suffice.
- Theorem 9: exact Cd-graph structural characterization for static graphs with `2n−4` edges. It allows changing the forest partition relative to original chronology.
- Theorem 13: add a new vertex connected to two old vertices by earliest/latest contacts; preserves label-connectivity.

Primary full PDF: https://citeseerx.ist.psu.edu/document?doi=a74c209362173e4deda639e11a2b6dfcd7544b7f&repid=rep1&type=pdf  
Institutional source and published artifact: https://research.utwente.nl/en/publications/label-connected-graphs-and-the-gossip-problem/  
Publisher DOI: https://doi.org/10.1016/0012-365X(91)90068-D

### West (1982), Parts I–II, COMPLETE primary texts inspected

The NOHO ("No One Hears his Own information") restriction implies `n` is even. Part I establishes the canonical ordered graph representation by permutations and bit sequences; Part II characterizes realizable quadruples and special four-tree `M(G)` structure. Both are historically relevant to ordered gossip classifications. Neither, within its stated NOHO hypothesis, directly claims anything about all *unrestricted* optimal schedules on odd `n=13`.

- Part I: https://dwest.web.illinois.edu/pubs/gossip1.pdf
- Part II: https://dwest.web.illinois.edu/pubs/gossip2.pdf
- Part III is separately cited in Part II; it is an enumeration of NOHO-graphs, likewise restricted.

### Labahn (1993, 1995), original journals not completely accessible

- 1993 *Information flows on hypergraphs* introduces information-flow inequalities used in the modern derivation.
- 1995 *Kernels of minimum size gossip schemes* claims complete kernel classification, permutation descriptions, isomorphism and linear-extension enumeration. Closest prior art.
- 1992 reports **92774 (Part I)** and **92785 (Part II)** are verified as institutional catalog entries at University of Bonn, but not open full texts here.
- Renken (2023) thesis **full text inspected**, printed pp. 97–102 (PDF pp. 107–112). Reproduces Labahn Theorem 3.1 and Corollary 3.1, κ≥5 kernel Hasse structure, and cites Labahn Theorem 6.3 for admissible permutation counts.
- Major missing items: original Labahn Section 6 admissibility predicates; complete κ=2,3,4 exceptional patterns; compatibility and nonkernel-fringe construction rules. **A complete theorem-by-theorem implication proof cannot be synthesized honestly without them**.

References:
- https://doi.org/10.1016/0012-365X(93)90509-R
- https://doi.org/10.1016/0012-365X(94)00031-D
- https://www.dm.uni-bonn.de/publications.eng.html
- https://d-nb.info/1289610584/34

### Krumme (1996), primary abstract and bibliographic chain

*Reordered gossip schemes* proves that a successful scheme can be rearranged into a form in which each participant becomes fully informed through at most two calls, with an analogous property in reverse. This existential reordering statement **does not by itself** fix the midpoint of every original ordering. The full paper may contain additional consequences; no theorem numbering was invented here.

Reference: https://doi.org/10.1016/0012-365X(94)00302-Y

### Williams (2026), current methodological predecessor

*Greedy gossiping*, published **22 September 2026**. The published full-text excerpt for **Lemma 2.5** explicitly reasons about components after the first `n−2` calls, at least two being trees, and reordering disjoint contacts. Its result concerns *maximizing accumulated knowledge in fewer than `2n−4` calls*, rather than the original fixed-order half-forest property in a successful optimal `2n−4` schedule. The shared prefix decomposition/commutation **is not new methodology**.

Reference: https://doi.org/10.61091/cn238-05  
Full text: https://combinatorialpress.com/cn-articles/volume-238/greedy-gossiping/

### Modern temporal-clique literature, distinct problem

- Casteigts–Peters–Schoeters (ICALP 2019 / JCSS 2021), `O(n log n)` connectivity-preserving spanners.
- Angrick et al. (ESA 2024), reduction and pivot structures.
- Carnevale–Casteigts–Corsini (SAND 2025), dismountability and pivotability.
- Baligács (2026), universal `7n` upper bound, i.e., linear-size existence; the precise `2n−3` strong conjecture remains open as of the Sept. 22, 2026 maintained list.
- Baligács et al. (September 2026), almost-linear **stretch-3** temporal spanners: different approximation objective, not a `2n−3` reachability-preserving result.

References:
- https://doi.org/10.4230/LIPIcs.ESA.2024.11
- https://doi.org/10.4230/LIPIcs.SAND.2025.6
- https://arxiv.org/abs/2606.05156
- https://arxiv.org/abs/2609.02851
- https://arnaudcasteigts.net/blog/open-problems.html

## Independent gates and unresolved core proof obligation

| Gate | Status | Rationale |
| --- | --- | --- |
| Source discovery: original classic papers and descendants | PARTIAL | Full West I/II and Göbel 1991 plus Renken 2023, current scholarly sources accessed; full Labahn/Krumme not accessed |
| Theorem numbers and statement correspondence (Göbel 1991) | PASS | Source primary text contains Thms 1,2,3,9,13 |
| Logical nonimplication from static Cd property to given chronological halves | PASS | Concrete independent all-source witness verified |
| Claim that new-vertex lift is novel | REFUTED | Göbel 1991 Theorem 13 is direct predecessor |
| Precise v1.4 k=1/2/3 first-bridge lemma priority | UNRESOLVED | No exact predecessor *located*, but Labahn/Krumme source limitations material |
| `n=13` half-forest theorem mathematical priority | UNRESOLVED | No matching explicit theorem *located*, but kernel classification could imply it |
| Exhaustion of **all** Labahn-compatible n=13 kernels and linear extensions | NOT DONE | Missing published predicates and exceptional families |
| Original fixed-time clique `2n−3` bound | OPEN | Repo does not prove it |
| Standalone paper novelty gate | BLOCKED | No established new universal theorem and no priority certificate |

## Next executable priority test (non-circular, independently reviewable)

**A. Obtain full Labahn 1995 and Krumme 1996 primary papers** through authorized library/author access (or the Bonn 1992 reports). The institution catalogs / DOI landing pages are grounded but not substitutes for complete text. Do not present this missing source step as already done.

**B. Transcribe numbered admissibility predicates** (`ρ,σ`, exceptional κ≤4, all fringes) and verify that the implementation is equivalent to those published rules. On fully enumerated tiny instances, compare the generated class to an independent source-by-source gossip oracle, under both repeated-call and distinct-call models as needed.

**C. For each permitted n=13 kernel, reconstruct every valid fixed incidence realization and every compatible chronological linear extension** (or prove a valid quotient). Record at each `n−2` cut the cycle ranks and produce certificates for each exclusion; a timeout is UNKNOWN, not UNSAT. This will establish a decisive historical implication, if it exists.

**D. If already implied:** revise the n13 note to call it an executable finite corollary of classical kernel classification; cite theorem numbers.  
**If not directly implied:** identify the smallest new order-sensitive lemma beyond classical constraints and prove it independent of source gaps. Either way, continue to treat fixed-order temporal-clique spanner questions separately.

## Exact reproducibility

From directory containing the provided script:

```sh
python verify_1991_cd_gap.py
```

Verified in the current Python runtime:
```
PASS | ordered gossip: 8 vertices, 12 pairwise-distinct contacts
PASS | true chronological half cycle ranks: (0,1)
PASS | historical Cd partition: (0,0) with qualifying four-cycle
PASS | crossing four-cycle edge IDs: [0,5,1,6]
PASS | forest/forest (ordered orientation) partitions: 604
```

**Evidence independence:** only one primary example, newly recomputed. This confirms the *quantifier distinction* and not originality of n13. Other v1.4/v1.5 CI claims refer to previously recorded GitHub runs, not a freshly reproduced full solver certification in this audit.

## Access, provenance and integrity disclosures

I tried the publisher DOI routes, a CiteSeerX Labahn 1993-preprint link, ResearchGate bibliographic/full-text indexes, the University of Bonn institutional preprint catalog, full-text doctoral reconstruction, and other classic sources. The 1995/1996 publisher article text remained inaccessible. No copyrighted full journal articles are reproduced or uploaded; this dossier contains original analysis and bibliographic links. Full PDFs consulted for the 1991, 1982 and 2023 claims were read via accessible public links.

**Do not claim**: “complete global prior-art exclusion,” “n13 novelty established,” “all kernel classifications implemented,” or “universal half-forest proved.” Those statements outrun current evidence.