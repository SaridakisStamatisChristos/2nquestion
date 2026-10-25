# Theorem-by-theorem prior-art comparison — 2nquestion v1.3–v1.4

Date: 2026-10-25 · Auditor: SOTA Research Auditor · Scope: chronological gossip and optimal temporal-spanner structural results.

## Executive verdict

**PRIORITY NOT ESTABLISHED.** No located source **explicitly states** the ordered first-bridge covering rule, or the exact statement that **every** successful shortest *pairwise-distinct* 22-call gossip schedule on 13 vertices has at least one forest half. However, this is **not** evidence that those propositions are new: Labahn (1995) characterizes the entire minimum-gossip kernel order, and its consequences may imply both after an analysis of all compatible linear extensions. The classical structure/rounds results are definitively *not* novel. The original `2n-3` fixed-chronology temporal-clique conjecture and POD remain open.

**Critical source limitation:** complete authenticated text of Labahn (1995) and Krumme (1996) was **not obtained**. A 1993 author preprint of Labahn is indexed at CiteSeerX, but content access returned a cache miss; the publisher page provided only abstract. Krumme's full journal text was not acquired. Exact theorem-number associations below are established by the clearly marked sources: 2023 academic doctoral reconstruction, published 1996 abstract, and a *secondary* quote of Labahn 5.3. We therefore **cannot** honestly claim a completed page-by-page primary-source theorem comparison.

## Common model and important distinctions

- In this repository a gossip schedule is a fixed sequence of **pairwise-distinct undirected** calls, exactly `2n-4`, all-to-all information dissemination, cut after `n-2` calls. A claim about **every fixed ordering** cannot be inferred solely from a theorem that **some reordered equivalent schedule exists**.
- Classical optimal gossip results often allow repeated calls. All results valid for **all** minimum schemes still constrain the distinct-call subclass; the converse is not automatic.
- A *label-connected* graph can be given **some successful edge chronology**. The main temporal-clique spanner problem instead asks for a **subset preserving a chronology already fixed in advance**. Do not conflate these quantifiers.

## Statement-level comparison ledger

| ID, earlier result, provenance | Exact established earlier content | Corresponding local claim | Logical comparison, evidence state |
| --- | --- | --- | --- |
| B72 / Tijdeman–Baker–Shostak (1971–72), via 1991 journal and 2015 full conference paper | Optimal number of telephone gossip calls on n>=4 vertices is `2n-4` | v1.0–v1.4 assume the optimal `2n-4` regime and use the lower bound to rule out excessively small kernels | **DIRECTLY KNOWN**; no novelty |
| GCV91, *Label-connected graphs and the gossip problem*, original journal abstract | Minimum label-connected edge count `2n-4`; polynomial characterization of underlying graphs attaining this number; graph recognition of general label-connectivity NP-complete | v1.1 component patterns and v1.4 finite model; primary fixed-chronology conjecture | **KNOWN structural predecessor**, but not a proof of fixed-half/forced bridge property. In particular, 'there exists a labeling' differs from 'for the given labeling' |
| Labahn 1993, *Information flows on hypergraphs*, Lemma 5.1 and Theorem 5.1, reconstructed in Renken (2023) thesis, dissertation PDF pages 98–99 | Decomposition of optimal gossip order into initial/final edge sets and kernel. Lower bounds `|hatF|>=n-2|F|`, `|checkFminus|>=n-2|Fminus|`, `|K|>=2(|F|+|Fminus|)-4`; these must be equalities for an optimal `2n-4` schedule | v1.0 incidence-window condition; v1.1 component intersection counting; v1.3 collector budgets | **SUBSTANTIAL OVERLAP** in broad information-flow conservation, but *not* a demonstrated equivalence to our singleton last-contact lemma |
| Labahn 1995 Theorem 3.1, reconstructed in Renken (2023) thesis PDF page 99 | For minimum schemes, initial and final kernel antichains have equal cardinalities `|Fminus|=|F|`. The thesis notes a published typo: the theorem should say '(p,q)-kernel' rather than '(p,1)-kernel' | v1.1–v1.4 prefix/suffix balance and component-obstruction arguments | **OLDER AND STRONGER global kernel invariant**. It does not syntactically say that a fixed `n-2` edge half is a forest; that implication remains **NOT DERIVED** |
| Labahn 1995 Corollary 3.1, reconstructed in Renken (2023) thesis PDF page 101 | Union of vertices incident to the extremal kernel edges of the initial antichain is exactly the union of those incident to final extremal antichain edges | v1.3 complete-collector restriction and v1.4 first-bridge covering | **KNOWN boundary alignment**, but no identified direct same-statement implication concerning tree edge `cd` at the original midpoint |
| Labahn 1995 Section 6 structural classification, reconstructed in Renken (2023) thesis PDF pages 99–102 | Any kernel with order parameter κ≥5 has `4κ-4` elements arranged as κ initial edges, κ final edges, κ−2 elements on each of two intermediary chains; covering relations encoded by permutations ρ,σ with restrictions | v1.2–v1.4 classification of prefix/suffix component intersections | **HIGHEST PRIORITY THREAT.** Older work classifies the allowed kernel partial orders. It may logically constrain every chronological linear extension, but *a kernel-poset classification is not identical to a classification of the original prefix/suffix contact-components*. The reduction is **OPEN**, not proved and not disproved |
| Labahn 1995 Theorem 6.3, cited in Renken (2023) thesis page 102 | The proof gives a count for admissible pairs of kernel permutations ρ,σ at a fixed kernel parameter κ; invoked to bound numbers of kernel footprints | v1.4 enumerates 16 incidence orbits, 44 nominal placements, 43 structural exclusions and one exact residual UNSAT | **PRIOR ENUMERATION METHODOLOGY**; not the same enumerated objects or output theorem. Whether n13 result follows from finite enumeration of older kernel classes and their linear extensions remains **UNRESOLVED** |
| Labahn 1995 Theorem 5.3, quoted (secondarily, not independently primary-checked) in 2013 Math StackExchange | Minimum rounds of a `2n-4`-call scheme at least `2 ceil(log2 n)-3` | v1.0–v1.4 fixed chronological half-forest constraints | **DIFFERENT CLAIM / NO DIRECT DUPLICATION**; both involve time structure but rounds do not directly classify forests |
| Krumme 1996, *Reordered gossip schemes*, central **reordering theorem**, wording from publisher abstract | Any complete gossip can be rearranged so that at most two calls cause each participant to become completely informed, and the reversed sequence has the same property; classical four-cycle and structure theorem are corollaries | v1.3 fixed-order first/last edge requirement; v1.4 first-bridge covering | **DIFFERENT QUANTIFIER**: existence of a reordered scheme does **not alone imply** a claim about every unchanged chronology, since reordering can change midpoint halves. Strong conceptual overlap; **NO EXACT IMPLICATION PROVED**. The original theorem number is not accessible and MUST NOT be invented |
| Hovnanyan–Poghosyan–Poghosyan, 2015 full proceedings PDF, Lemmas 1–2 | Operations of local interchange preserve successful gossip, and compositions of such operations have order-independence under stated model | Current fixed-call chronology and possible canonicalization | **ESTABLISHED** equivalence-preserving transformations. Rewriting an ordering is not the same as preserving the original `n-2`-edge halves |
| Same 2015 paper, Theorem 1 / Lemma 4 / Theorem 2 | Recovers `2n-4` optimal calls and investigates minimal-round constructions as a function of a 'basis' and batch rounds | v1.0 finite butterfly boundary; v1.4 half-forest | **RELATED, NOT AN IDENTIFIED SAME THEOREM** |
| Renken, *Algorithmic and Structural Aspects of Temporal Graphs* (2023), Lemma 4.34 and proof, thesis pp. 98–102 | Applies Labahn kernel classification to bound optimal temporal spanners in random temporal graphs, including explicit kernel footprint structure and counts | v1.4 aspiration to fixed-edge temporal-clique spanners | **STRONG OVERLAP IN PROBLEM CONNECTOR**: using Labahn kernels for temporal spanners is itself already done. The specific `2n-3` universal bound is **not supplied** |

## Local v1.3 and v1.4 claims: direct overlap verdict

| Local proposition | Earlier proof that *directly implies it* found? | Outcome |
| --- | --- | --- |
| Singleton entry must be full prefix collector | No explicit matching numbered historical result accessed; follows trivially by cut information-flow argument | May be elementary and previously implicit; **priority unresolved / weak stand-alone novelty** |
| Tree with two singleton entries forces last prefix edge to connect the two entry vertices; suffix dual forces first edge | No historical verbatim statement or derivation located | **POSSIBLY DISTINCT FORMULATION**. Check against older kernel/NOHO proofs; no priority certificate |
| General first-bridge covering: every third-row original secret needs preexisting carrier on both sides of forced first suffix bridge; sizes 1/2/3 yield zero/two/at-least-one collector conditions | No exact predecessor found; proof self-contained and plausible as a basic tree-cut argument | **POSSIBLY DISTINCT EXPLICIT LEMMA**, but derived from elementary carrier conservation and previous singleton lemma; modest potential independent novelty |
| Every successful shortest 22-call distinct-edge n=13 gossip schedule has an acyclic first or second half | No explicit matching publication found | **POSSIBLY DISTINCT FINITE CONSEQUENCE**, but *could follow from Labahn's classification + linear extensions*. Computation is CI-reproducible; still requires independent complete algorithmic audit |
| All n at least one half forest | No proof in repo | **OPEN / NOT PROVED** |
| Every fixed-time temporal clique has a preserving `2n-3`-edge subgraph | Not proved in repo; remains open target | **OPEN / NOT PROVED** |

### One rigorous non-implication to preserve

Let R state: '*for each successful schedule S, there exists a reordered successful schedule S\' with good property G*'. Let H state: '*for each successful original schedule S, its first or second specific n-2-call contact graph is a forest*'. R does not imply H by elementary predicate logic alone. A bridge proof must show that transformations preserve H or show an independent invariant of every original S. No such implication appears in the accessible formulation of Krumme's theorem. This observation *does not* refute any stronger corollary Krumme may derive in the inaccessible full paper.

### Additional caution from the complete classification

The condition that a kernel is a permitted p-grid partial order is stronger than a local collector check, but v1.4's 3x3 incidence matrix counts **vertices classified simultaneously by connected components at one chronological cut**, while Labahn's grid tracks the **partial order among essential contacts**. Their grid terminology is not a direct bijection. Any priority proof based on this resemblance needs an explicit map preserving labels, contact endpoints and the midpoint split.

## Primary source and checkability ledger

**Direct primary abstract/publisher metadata**:
- Labahn (1995), *Kernels of minimum size gossip schemes*, Discrete Mathematics 143, 99–139, https://www.sciencedirect.com/science/article/pii/0012365X9400031D
- Krumme (1996), *Reordered gossip schemes*, Discrete Mathematics 156, 113–140, https://www.sciencedirect.com/science/article/pii/0012365X9400302Y
- Göbel–Cerdeira–Veldman (1991), *Label-connected graphs and the gossip problem*, https://www.sciencedirect.com/science/article/pii/0012365X9190068D

**Full inspectable scholarly derivative containing explicit references to Labahn theorem identifiers and proofs**:
- Malte Renken (2023), *Algorithmic and Structural Aspects of Temporal Graphs*, doctoral dissertation, https://d-nb.info/1289610584/34 , PDF *physical* pp. 107–113 (thesis printed pp. 97–102). See section 'Lower bound for optimal spanners'; note Labahn 3.1 typo.

**Direct full 2015 article**:
- V. Hovnanyan, V. Poghosyan, S. Poghosyan (2015), *Open Problems in Gossip/Broadcast Schemes and the Possible Application of the Method of Local Interchange*, https://csit.am/2015/proceedings/DMCA/DMCA7.pdf (6 PDF pages).

**Secondary-only claim**:
- Labahn (1995) Theorem 5.3 quoted at https://math.stackexchange.com/questions/576326/minimal-time-gossip-problem . Use cautiously.

**Historical accessible candidate, content unavailable in this audit**:
- Labahn preprint, 3 Nov 1993: https://citeseerx.ist.psu.edu/document?doi=5967c6074c472122f6ff58cf4d0c82d0549bf135&repid=rep1&type=pdf (indexed text exists; direct PDF retrieval failed). Bonn historical working papers 92774 and 92785 listed at https://www.dm.uni-bonn.de/publications.eng.html .

## Final research/paper gate

- **Directly duplicated material:** minimum `2n-4` call bound, established kernel/antichain existence, basic reordering principles, historical four-cycle theory.
- **Not proved duplicated:** precise fixed-original-midpoint first-bridge lemma and full n13 half-forest claim.
- **Not proved original:** those same two local claims; need line-by-line access to full Labahn/Krumme and a constructive/not-derivable comparison against permitted kernel-poset linear extensions.
- **Publication readiness for novelty claims: BLOCKED.** Preserve the finite theorem as a reproducible mathematical observation, emphasize its domain, do not claim a new universal theorem.
- **Next decisive experiment:** generate all Labahn-compatible kernel structures with `n=13` and original call-order linear extensions, reconstruct the original midpoint components, and explicitly verify whether the half-forest theorem is an already-immediate corollary of Labahn's structure. If equivalent, cite Labahn as theorem source and present our code only as an executable consequence. If not equivalent, isolate the additional order-sensitive invariant.
