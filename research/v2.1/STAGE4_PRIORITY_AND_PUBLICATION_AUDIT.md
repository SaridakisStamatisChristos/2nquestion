# Stage 4 — historical priority, contribution defense and publication readiness

Audit: 26 October 2026 | Repository: SaridakisStamatisChristos/2nquestion | PR #1 **draft** | Governing evidence: v2.0 and v2.1 Stage-3 CI certificates.

**DECISION: AUDIT EXECUTED; REFRAME THE PAPER AS A BOUNDED COMPUTATIONAL CLASSIFICATION. NOVELTY/CONTRIBUTION GATE CONDITIONAL, SUBMISSION GATE HOLD.**

This is a source-calibrated research audit, not a statement that all possible mathematical publications have been inspected. A second independent seven-vertex oracle and all 20 orbit checks passed before this audit. A green program does not establish original scholarly priority.

## 1. Model and exact research claim

Fix n >= 4 and an ordered list e_1,...,e_{2n-4} of **distinct unordered pairs** of n participants. Initially v knows secret v. Each call between its endpoints replaces both their secret sets with their union. We consider only successful schedules: everyone eventually knows all n secrets.

Let L be the **first n-2 original calls** and R the **last n-2 original calls**; the permutation of calls is not changed. Claim H_15:

> For 4 <= n <= 15, every such successful minimum-call schedule has at least one acyclic underlying static contact graph among L and R.

H_15 is **computer-assisted for n=15** and inherits earlier v2.0 proof dependencies for n<=14. It is neither (i) that some reordering has forest halves nor (ii) that the underlying static graph has an arbitrary partition into forests. It does not determine a minimal spanner of an adversarially pre-labelled temporal clique.

## 2. Literature acquisition and provenance

Primary originals supplied and inspected in the prior repo audit: [v1.8 exact primary-source theorem comparison](../v1.8/ORIGINAL_PRIMARY_SOURCE_PRIORITY_AUDIT.md), with PDF page labels and SHA-256 fingerprints. Those copyrighted PDFs are **not** committed. Their full bodies were not separately reacquired in this Stage 4 run; publisher/author records and the prior source-anchored audit were cross-checked. This limitation matters: do not write "new exhaustive line-by-line implication proof of the 1995/1996 papers."

External checks as of 2026-10-26, distinguished by source level:

1. F. Göbel, J. O. Cerdeira, H. J. Veldman (1991), *Label-connected graphs and the gossip problem*, Discrete Mathematics 87, 29-40, DOI [10.1016/0012-365X(91)90068-D](https://doi.org/10.1016/0012-365X(91)90068-D); [University of Twente record](https://research.utwente.nl/en/publications/label-connected-graphs-and-the-gossip-problem/). Complete paper was examined in v1.6.
2. R. Labahn (1995), *Kernels of minimum size gossip schemes*, Discrete Mathematics 143, 99-139, DOI [10.1016/0012-365X(94)00031-D](https://doi.org/10.1016/0012-365X(94)00031-D). Prior v1.8 source-inspected theorem statements.
3. D. W. Krumme (1996), *Reordered gossip schemes*, Discrete Mathematics 156, 113-140, DOI [10.1016/0012-365X(94)00302-Y](https://doi.org/10.1016/0012-365X(94)00302-Y). Prior v1.8 source-inspected theorem statements.
4. D. B. West (1982), *A class of solutions to the gossip problem*, Parts I/II, Discrete Mathematics 39/40; [Part I](https://dwest.web.illinois.edu/pubs/gossip1.pdf), [Part II](https://dwest.web.illinois.edu/pubs/gossip2.pdf). Restricted NOHO subclass.
5. R. Labahn (1993), *Some minimum gossip graphs*, Networks 23, 333-341, DOI [10.1002/net.3230230416](https://doi.org/10.1002/net.3230230416). Optimizing rounds as well as edge count; not a blanket n14 fixed-original-half theorem.
6. K. Williams (2026 publication, original arXiv preprint June 2025), *Greedy gossiping*, Congressus Numerantium 238, 113-121, DOI [10.61091/cn238-05](https://doi.org/10.61091/cn238-05); [full publisher HTML](https://combinatorialpress.com/cn-articles/volume-238/greedy-gossiping/). Its Theorem 1.1 maximizes total known information for m <= 2n-5, not H_15. **Lemma 2.5 explicitly uses the first n-2 calls and commuting disjoint calls**; attribute those techniques. The online publisher gives 2026-09-22 as publication date.
7. A. Casteigts, J. Peters, J. Schoeters (2021), *Temporal cliques admit sparse spanners*, JCSS 121, 1-17, DOI [10.1016/j.jcss.2021.04.004](https://doi.org/10.1016/j.jcss.2021.04.004); and J. Baligács (2026), *Temporal Cliques Admit Linear Spanners*, [arXiv:2606.05156](https://arxiv.org/abs/2606.05156). Different fixed-label sparse-spanner problem; 7n general bound.
8. A. Casteigts, [Open questions in temporal graphs](https://arnaudcasteigts.net/blog/open-problems.html), last updated **2026-09-22**: 2n-3 temporal-clique target explicitly still open. The page also notes the 7n result and a refinement of its analysis to 6n; **neither** is our result.
9. M. Renken (2023), *Algorithmic and Structural Aspects of Temporal Graphs*, thesis, [institutional copy](https://d-nb.info/1289610584/34), reproduces historical gossip kernel context. Repo v1.6/v1.8 cover theorem context.

Query coverage: exact title/author pairs; "chronological halves", "original half", "first n-2 calls", "both cyclic", "minimum gossip graph forest", kernel linear extension, gossip contact ordering, temporal clique spanner. Publisher bibliographic records confirm the works; online searchable publisher HTML supplies Williams's full theorem and lemma. Broad negative search is **not** a proof of mathematical independence, novelty or completeness.

## 3. Theorem-by-theorem closest-work comparison

| Source/result | Already established | Distinction from H_15 | Conclusion |
| --- | --- | --- | --- |
| Classical minimum 2n-4 call bound | Optimal gossip length | Used as foundational model; no independent contribution | **DIRECT PRIOR ART** |
| GCV 1991 Thms 3, 9 | Existence of static Cd-graph edge decompositions, special crossing four-cycle | Edge-partition existence does not force the **given** first/last n-2 chronological edge sets to equal those forests. v1.6 independently checked an n8 example with one cyclic original half and a qualifying static partition | **SUBSTANTIAL OVERLAP** in forests; original-order quantifier distinct |
| GCV 1991 Thm 13 | Two-contact extension attaching an additional participant at beginning/end | Exactly the technique used to lift small cases | **DIRECT PRIOR ART** |
| Labahn 1995 Thm 5.2 | Static four-cycle and nonkernel two-forest attachment structure | Could constrain chronological halves after additional analysis, not shown to state H_15 | **STRONG PRIORITY BARRIER** |
| Labahn 1995 Thm 6.1 + 6.2-6.3 | Exact admissible p-grid permutations and isomorphism; later linear extensions | Full kernel-poset classification may permit deriving fixed-half finite facts. Complete **all-kernel + fringe + linear-extension implication closure** has not been established | **UNRESOLVED POSSIBLE IMPLICIT COROLLARY** |
| Krumme 1996 Thm 1 | Exists a favorable **rearranged** complete gossip scheme | Existential reordering is not a theorem about **every original** ordering | **DIFFERENT QUANTIFIER**, but other source lemmas could still imply H_15 |
| Krumme 1996 Cor. 3 / Cor. 7 | Static forest decomposition; existence of reorderings with favorable prefixes | Neither by itself forces current fixed equal halves | **OVERLAP AND QUANTIFIER DISTINCTION** |
| West 1982 NOHO | Structured ordered optimal schemes with additional NOHO constraint | H_15 concerns unrestricted optimal schedules and odd n15; special class is not complete coverage | **RELATED RESTRICTED SUBCLASS** |
| Williams 2026 Thm 1.1, Lemma 2.5 | Greedy score optimum when m<2n-4; first n-2 prefix argument and disjoint-call swaps | Does not claim forest-half property of every fully successful 2n-4-call original schedule; the local techniques themselves are not new | **NEARBY CHRONOLOGICAL PRIOR ART** |
| CPS 2021 / Baligács 2026 | Fixed-label temporal clique connectivity with sparse selected edges | H_15 studies minimum gossip schedules with order freely chosen; does not prove a tighter spanner bound | **DISTINCT TASK, NOT SPANNER PROGRESS** |

**Hard logical caveat.** The statement "static/reordered theorem does not *by itself* imply fixed original half structure" is not the statement "fixed half structure cannot be deduced from the full original classification." The latter would require a complete derived implication analysis; we **did not** settle it. No claim of priority independence is licensed.

## 4. Contribution preflight and destructive stress test

Counterfactual: grant that optimal gossip, four-cycle, forest decompositions, contact commutation, complete kernel characterization, linear extensions and two-contact extension are all classical. Subtract all of those from the paper.

| Claimed contribution | Residue after subtraction | Status |
| --- | --- | --- |
| General gossip minimum and structural two-forest mechanisms | None; remove from novelty claims | **COLLAPSED — classical** |
| First-bridge k=1/2/3 and singleton-entry collectors | Explicit, relatively elementary information-conservation lemmas adapted to the original midpoint; possible implicit consequences of older theory | **WEAK / UNRESOLVED priority** |
| n<=15 invariant for the original unchanged midpoint | Explicit bounded theorem with new, inspectable 20-orbit computational proof, not located verbatim in surveyed originals | **BOUNDED, CONDITIONAL** |
| Information-profile B/D compatibility and conservative optimistic two-side tree relaxation | Transparent finite-proof method for the bounded case, independently checked on exact components; not an established general faster algorithm or provably novel representation | **BOUNDED, METHODS ARTIFACT** |
| Proof of all-n forest midpoint, POD, fixed-time temporal-clique 2n-3 | None | **NOT CLAIMED / OPEN** |

**Safest priority text:** "In the investigated source set, no explicit statement of this particular n<=15 fixed-original-midpoint classification was identified. Whether it follows implicitly from earlier complete gossip-kernel characterizations remains unresolved."

**Impact:** mathematically nontrivial finite exclusion and reproducible artifact; **unknown broader importance** without a general theorem, counterexample, clean characterization, independent consequence or literature-recognized open question about original halves. This is not an argument that the finite statement is false.

**Novelty per claim:** minimum-call/K4/four-cycle/static forest/extension = PRIOR ART; first-bridge and single-source lemmas = UNRESOLVED; finite H_15 = LIKELY DISTINCT EXPLICIT RESULT WITHIN SEARCH SCOPE, GLOBAL NOVELTY UNRESOLVED; B/D method = bounded technique, originality unestablished.

## 5. Claim-to-evidence ledger

| Claim | Evidence | Status |
| --- | --- | --- |
| For n<=15 both-cyclic implies 3x3 midpoint incidence | Previous v2.0 rectangular-grid proof | HUMAN MATHEMATICAL DEPENDENCY, scope-specific |
| Structural enumeration n15 is 3,003 -> 13,680 -> 4,662 -> 945 -> 20 | Two different Python enumerators, Github CI | VERIFIED FINITE |
| 33 exact component profile domains agree | Two independent C++17 component oracles; Stage-3 CI, including both n7 cyclic types | VERIFIED FINITE |
| All 20 orbits ruled out, 945 placements covered | Exact domain substitution, independent compatibility checker, published certificate, Stage-3 CI | VERIFIED FINITE RELAXED UNSAT |
| Optimistic large-tree information dominates real tree knowledge | Mathematical last-edge-side lemma + exhaustive/sampled tests | MATHEMATICAL ARGUMENT + SUPPORTING TESTS |
| H_15 is new to all scholarship | No complete global implication closure; negative search only | UNRESOLVED |
| H_15 solves fixed-label temporal clique 2n-3 | Different problem/model; no mapping shown | UNSUPPORTED / MUST NOT CLAIM |
| The paper meets peer-reviewed submission standards | No independent external mathematical referee, unresolved significant originality | MAJOR BLOCKERS |

## 6. Reviewer #2 adversarial objections

**Critical A — "Classical kernel theory already implies it."** The absence of matching sentence is not sufficient defense. Provide a complete implication closure for the full Labahn classes and their linear extensions/fringe attachments or explicitly state unresolved; this audit chooses honest unresolved.

**Major B — "Finite n<=15 result has limited mathematical impact."** Current contribution should be sold as a bounded computational classification and reusable certificate, not universal SOTA. Stronger impact would follow from a general parameterized characterization, n16 progression or a consequence for existing open problems.

**Major C — "Computations aren't a self-contained paper proof."** The mathematical reduction and exact profile/relaxation completeness must appear in manuscript, with traceable machine-readable orbit details, exact commands and two-oracle comparison. Retain all assumptions and CI links.

**Major D — "Manuscript reports 7/10/3 from unavailable code."** The lost interrupted draft is *not* the canonical source; correct to **6 local / 10 exact global / 4 optimistic global** from reconstructed executable evidence, with total multiplicities 945.

**Major E — "Reordered forest means original forest."** Explicitly distinguish existential static decomposition, existential reordering and fixed-original-half universal quantification; do not assert a complete nonimplication from all classical theory.

**Major F — "A result on gossip advances the open 2n-3 spanner question."** Withdraw implication; different quantifier over input time labels and edge subsets.

## 7. Independent publication gates

| Gate | Status | Reason |
| --- | --- | --- |
| Exact model and bounded proof | PASS, COMPUTATION-ASSISTED | Stage-3 dual oracle + structural lemmas |
| Reproducibility and artifact integrity | PASS, BOUNDED | Check-in, certificates, two oracles, CI |
| Citation precision | PASS WITH CONDITIONS | Verified core bibliographic records and source-level separation; retain original-paper access caveat |
| Contribution after prior-art subtraction | **PASS-CONDITIONAL / REFRAME** | A limited explicit finite result survives but implicit-classification subsumption unclosed |
| Historical priority | **UNRESOLVED** | Labahn kernel/extension implication not fully settled |
| Significance for major graph-theory venue | **MAJOR RISK** | Finite n15 classification without general consequence |
| External refereeing/formal theorem prover | NOT DONE | Neither required for truth, but relevant to independent publication assurance |
| Submission readiness | **MAJOR BLOCKERS REMAIN — HOLD** | Scholarly distinctness and mathematical impact require stronger case; no venue-specific submission package |

**Decision:** Produce a carefully qualified new canonical research **working draft** now; **do not submit, upload as a claimed novel breakthrough, merge PR #1 or mark it ready for review**. Stage 4 as an audit can close with **RESEARCH/PUBLICATION DECISION: HOLD**, rather than pretend the publication conditions were met.

## 8. Manuscript repair contract

The corresponding [canonical n<=15 manuscript draft](PAPER_DRAFT_STAGE4.md) should: (i) limit title/abstract to fixed-original-half finite result; (ii) present the mathematical reduction and explicit profile lemma/optimistic relaxation; (iii) use exactly 6/10/4 breakdown and the 33-exact-type Stage-3 certification; (iv) contrast historical theorems by their actual quantifiers, credit existing techniques; (v) explicitly state unresolved priority and general conjectures; (vi) include exact code/CI references and machine-readable provenance; and (vii) abstain from unverifiable "first ever"/"SOTA" or journal acceptance claims.

A separate Stage 5 expansion or further complete classical-kernel implication formalization may improve publication value, but is **not** retroactively counted as finished here.
