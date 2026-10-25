# Temporal Clique Research Campaign — v0.3

**Date:** 24 October 2026. **Core goal:** an original proof/disproof of universal `2n-3` temporal clique spanners, or a separately valuable new structural theorem that survives a literature priority audit. **The core goal is OPEN.**

## A. Definitions and correctness contract

In a simple temporal clique, all `n(n-1)/2` edges have distinct timestamps. Temporal journeys use strictly increasing labels. For an edge `e`, call it **indispensable** if deleting `e` breaks *some* ordered-pair reachability. The **compulsory graph** `F(G)` contains exactly these indispensable edges.

For distinct vertices `u,v`, define `u ≺ v` when `λ(uw)<λ(vw)` for *every* `w` distinct from `u,v`. This is a strict partial order (proof in v0.2). By the comparability lemma (proof in v0.2), every indispensable edge joins comparable vertices.

Two important caveats: (1) distinct paths replacing an edge `uv` **are** enough to prove that single edge redundant *in a clique*, since every other source-target pair retains its direct edge; (2) deleting all individually redundant edges simultaneously is **not** generally sound.

## B. Disproved candidate: quantitative compulsory-edge bound

The v0.3 candidate `|F(G)| <= max(0,2n-p-q-1)`, where `p,q` are counts of minimal and maximal vertices of `≺`, is **FALSE**, with a 4-vertex counterexample.

Chronological sequence: `01 13 02 03 12 23`, with endpoints numbered `0,1,2,3`. Its precedence consists of all relations from `{0,1}` to `{2,3}`, and no other relations. Thus `p=q=2`, `n=4`; predicted bound `3`. The four indispensable edges are `13,02,03,12`, hence `|F(G)|=4`. Independent information-propagation check confirms all four are indispensable, and the four form a valid temporal spanner.

**Audit correction:** Our earlier interpretation of the exhaustive K5 min/max histograms was wrong; those results already contained counterexamples to this bound. We explicitly withdraw the claimed supporting evidence and preserve this smallest finite witness.

## C. Proved special case: shared-extreme degree-two lemma

**Proposition (human-checked proof, no novelty priority claim).** Let `ab` be the globally earliest edge and `ac` be the globally latest edge of a temporal clique with `n>=3`, sharing vertex `a` (with `b!=c`). Then every indispensable edge incident with `a` is either `ab` or `ac`. In particular, `deg_{F(G)}(a) <= 2`.

**Proof.** Let `x` be distinct from `a,b,c`. If `x ≺ a`, the comparison at `w=b` would require `λ(xb) < λ(ab)`, contradicting global earliest `ab`. If `a ≺ x`, the comparison at `w=c` would require `λ(ac) < λ(xc)`, contradicting global latest `ac`. Thus `a,x` are incomparable. The comparability lemma says `ax` cannot be indispensable. Only the edges `ab,ac` remain possible. QED.

This special case does not assert that the two candidate edges are necessarily indispensable and does not solve the universal spanner conjecture.

## D. New research hypothesis: Four-Extreme Endpoint Conjecture (EEC)

Let the earliest edge be `ab` and the latest edge be `cd`, possibly sharing an endpoint. Among the vertices in `S={a,b,c,d}`, at least one has degree at most two in `F(G)`:

`min_{v in S} deg_{F(G)}(v) <= 2`.

For *overlapping* earliest/latest edges this follows from Proposition C. The unsolved case is **disjoint** earliest/latest edges.

### A proved implication

**Conditional theorem.** If EEC holds for every temporal clique with distinct edge timestamps, then `F(G)` is 2-degenerate for every such clique, and `|F(G)| <= 2n-3` for `n>=2`.

**Proof.** Fix any nonempty vertex subset `W` of `G`. Every edge indispensable in `G` with both endpoints in `W` is also indispensable in the induced temporal clique `G[W]`: otherwise deleting that edge would leave both directions between its endpoints reachable inside `G[W]` (thus also in `G`), and every *other* ordered pair in the complete `G` remains directly connected. Hence `F(G)[W]` is a subgraph of `F(G[W])`. Apply EEC to `G[W]` for `|W|>=3`: one of its earliest/latest endpoints has compulsory degree at most two in `G[W]`, and therefore degree at most two in `F(G)[W]`. For `|W|<=2` the conclusion is immediate. Thus every nonempty induced subgraph of `F(G)` has a degree-at-most-two vertex, exactly the definition of 2-degeneracy. Repeated removal of these vertices bounds the number of edges by `2n-3` when `n>=2`. QED (conditional).

**Limitation:** A small indispensable-edge set is *necessary* for a very small spanner but is not itself necessarily a spanner. EEC—even proved—would NOT resolve `OPT(K_n,λ) <= 2n-3`.

## E. Executed adversarial evidence, reproducible

- EEC true for all `720` permutations of edges of `K4` and all `3,628,800` permutations of `K5`, confirmed using an independently coded chronological propagation oracle. Shared-extreme special case also checked on every overlapping order. Sources: `extreme_exhaustive.cpp`; C++17 `-O3`.
- EEC true in `2,000,000` deterministic K9 trials spanning random, lex-perturbed, and reverse-lex-perturbed schedules; max observed *minimum forced degree among extreme endpoints* was exactly `2`. Source: `extreme_degree_probe.cpp`, RNG MT19937 seed `476734+n`.
- EEC true in `300,000` deterministic K12 trials with same families, max observed extreme minimum forced degree `2`.
- Quantitative bound tested and falsified at n9 on trial `18,715` by `critical_bound_v03.cpp`, then *minimized* to the simpler K4 counterexample using independently coded `check_counter_v03.py`. This confirms that passing random tests is not proof; early broad histograms contained overlooked violations.
- Separate shortcut `every forced edge belongs to the union of the unique minimum and maximum spanning trees` is false already on K4. No new claim is based on it.

**Do not inflate counts:** trials may contain duplicates and are not exhaustive at n>=6. The K4/K5 enumeration is exhaustive over labelled edge orders, not a universal proof.

## F. Current evidence/novelty ledger

| Statement | Validity state | Novelty state |
|---|---|---|
| `OPT <=2n-3` universal | OPEN | Existing published open problem |
| Non-pivot => `OPT=2n-4` (POD) | OPEN | Priority unresolved; resembles known heuristic patterns |
| Compulsory-edge precedence/comparability | PROVED v0.2 | Priority unresolved |
| `|F|<=2n-p-q-1` | **REFUTED** | Not applicable |
| Shared-extreme degree-2 lemma | PROVED (human-checkable) | Priority unresolved; consequence of comparability |
| EEC, disjoint extremes | SURVIVING computational tests, NOT PROVED | Priority unchecked |
| EEC => compulsory graph 2-degenerate | PROVED CONDITIONAL statement | Originality unchecked |
| Compulsory graph 2-degenerate unconditionally | OPEN | Related-but-distinct: SAND 2025 discusses 2-degenerate spanners |

### Priority warning

Carnevale, Casteigts and Corsini, *Dismountability in Temporal Cliques Revisited* (SAND 2025), already explicitly discuss **2-degenerate (2-arch) temporal spanners**; do NOT claim the 2-degeneracy concept or temporal-spanner approach to be original. The compulsory-edge graph is a distinct object, but the novelty of EEC and its implications has not been independently established.

## G. Next proof bottleneck

The high-information question is to **prove or refute EEC for disjoint global earliest and latest edges**. If proved, it would establish a necessary-edges sparsity theorem—still not the main conjecture. More ambitiously, identify *exchange/replacement* mechanisms that allow removing redundant edges **together** while preserving chronological paths, so a size bound on compulsory edges can be upgraded to a spanner construction. If no such bridge is found, EEC is not sufficient for the user's breakthrough criterion and should be deprioritized.

## H. Sources

1. Arnaud Casteigts, Open questions in temporal graphs, update Sep 22 2026: https://arnaudcasteigts.net/blog/open-problems.html
2. Baligács, Temporal Cliques Admit Linear Spanners (2026): https://arxiv.org/abs/2606.05156
3. Carnevale, Casteigts & Corsini, Dismountability in Temporal Cliques Revisited (2025): https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SAND.2025.6
4. Akrida et al., The Complexity of Optimal Design of Temporally Connected Graphs (2017), Theorem 4: https://pmc.ncbi.nlm.nih.gov/articles/PMC6979514/

**Bottom line:** No universal breakthrough has been proved. This checkpoint contains one falsification with a minimal witness, one proved structural special case, one proved conditional implication, and a sharply defined new conjecture. Publication-level originality cannot currently be claimed.
