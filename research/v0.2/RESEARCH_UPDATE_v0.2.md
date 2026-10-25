# Temporal Cliques: Exact-Size Spanner Research, v0.2

**Date:** 2026-10-24. **Objective:** a genuinely new proof/counterexample to the universal `2n-3` temporal-clique conjecture, not incremental engineering. **Status:** ORIGINAL CONJECTURE STILL OPEN. A new-to-this-investigation structural lemma is proved below; publication-level originality not established.

## 1. Model and literature constraints

`K_n` has a **single distinct timestamp** on each of its `n(n-1)/2` edges. A journey traverses edges in strictly increasing timestamp order. A temporal spanner is a subset of edges whose chronological journeys preserve all ordered-pair reachability. Every ordered pair is reachable in the original clique by its direct edge. For `n>=4`, classical gossiping gives `OPT>=2n-4`. It is an open problem whether `OPT<=2n-3` for **all** edge orders.

Verified public reference as of September 22, 2026: https://arnaudcasteigts.net/blog/open-problems.html . A 2026 paper provides the general bound `7n`: https://arxiv.org/abs/2606.05156 . The same open-problem update reports an analytic improvement to `6n` using that method. Published finite experiments already covered all `n<=8`. **Our earlier exhaustive K4/K5 checks do not establish a new result.**

### Research classification

| Claim | Status | Boundary |
|---|---|---|
| `OPT <= 2n-3` for all n | OPEN | Existing research problem |
| Non-edge-pivotable -> `OPT=2n-4` (POD) | OPEN, unverified priority | Stronger-than-original proposed dichotomy |
| Precedence relation below is strict partial order | PROVED (human-checkable below) | Priority not established |
| Indispensable edges have comparable endpoints | PROVED (human-checkable below) | Priority not established |
| Indispensable `u<v` has u minimal or v maximal | PROVED (human-checkable below) | Priority not established |
| Indispensable-edge orientation has no 3-edge directed path | PROVED consequence | Priority not established |
| Indispensable-edge graph is 2-degenerate | HYPOTHESIS ONLY | 2 million n9 trial schedules survived; no universal proof |
| No pivot implies at most n indispensable edges | HYPOTHESIS ONLY | Exhaustive n4/n5 and sampled n6..n9; no universal proof |
| Every optimum can be reduced to C4 by two-edge vertex peeling | REFUTED for an individual optimal spanner | Does not refute existence of an alternative peelable optimum |

## 2. A proved structural lemma (not a solution)

For vertices `u != v`, define `u ≺ v` when `lambda(u,w) < lambda(v,w)` for every vertex `w` other than `u,v`. Assume `n>=3`, injective timestamps.

**Lemma 1 (strict partial order).** `≺` is irreflexive and transitive.

**Proof.** Irreflexivity holds by definition. Suppose `a≺b` and `b≺c`. For any `w` outside `{a,b,c}`, `lambda(a,w)<lambda(b,w)<lambda(c,w)`. At `w=b`, the first relation evaluated at `c` says `lambda(a,c)<lambda(b,c)`, and the second relation evaluated at `a` says `lambda(a,b)<lambda(a,c)`. Thus `lambda(a,b)<lambda(b,c)`. Hence `a≺c`. Asymmetry follows because simultaneous `u≺v` and `v≺u` would impose contradictory strict inequalities for any third vertex. QED.

Call edge `uv` **indispensable** if `K_n - uv` is no longer temporally connected. Any reachability that fails after deleting `uv` must be `u->v` or `v->u`, since all other ordered pairs retain their direct edges.

**Lemma 2 (comparability).** Every indispensable edge `uv` has either `u≺v` or `v≺u`.

**Proof.** For each third vertex `w`, distinct timestamps imply exactly one of `lambda(u,w)<lambda(w,v)` and `lambda(v,w)<lambda(w,u)`. The first gives a two-edge path `u->w->v`, and the second gives `v->w->u`, avoiding `uv`. If the comparisons are not consistent for all `w`, there is a two-edge path in both directions avoiding `uv`, so the edge cannot be indispensable. Consistency in one direction is exactly `u≺v` or `v≺u`. QED.

**Lemma 3 (three-contact detour).** If `uv` is indispensable and `u≺v`, then `u` is minimal in the precedence order OR `v` is maximal.

**Proof.** Otherwise take `x≺u` and `v≺y`. The vertices `v,x,y,u` are distinct because `x≺u≺v≺y` and `≺` is a strict order. At vertex `x`, the relation `v≺y` yields `lambda(v,x)<lambda(y,x)`. At vertex `y`, the relation `x≺u` yields `lambda(x,y)<lambda(u,y)`. Thus `v->x->y->u` is a time-increasing path avoiding `uv`. The reverse ordered pair `u->v` is reachable via any third vertex because `u≺v`. No other ordered-pair reachability can be lost by deleting `uv`, contradicting indispensability. QED.

**Corollary.** Orient indispensable edge `uv` from `u` to `v` when `u≺v`. The resulting directed graph has no directed path of length three, because the middle edge in such a path would have both a predecessor and a successor under `≺`, violating Lemma 3. **No formal proof assistant has checked these arguments.**

**Pivot corollary.** If the precedence order has a universal least vertex `a` and a universal greatest vertex `z`, the contact `az` is a pivot: for every other vertex `v`, `v≺z` implies `lambda(av)<lambda(az)`, and `a≺v` implies `lambda(az)<lambda(vz)`. Thus every vertex reaches `a` before `az`, and `z` can reach every vertex after it. This supplies the familiar `2n-3` pivot spanner. It is a conditional structural corollary, not a new resolution.

## 3. Exact tight extremal family

Put edge `(i,j)` for `0<=i<j<n` at its lexicographic position, so all edges with smaller first endpoint occur earlier, and within a first-endpoint block the second endpoint increases.

**Proposition.** For every `n>=4`, the unique minimum temporal spanner consists of the union of the stars at `0` and `n-1`, exactly `2n-3` distinct edges.

**Proof of necessity.** For every `j>0`, deleting `(0,j)` destroys the journey `j->0`. Any path to `0` must finish with an edge `(0,k)` from the first chronological block. Before that first-block edge, a path starting at `j` cannot use a nonzero-first-endpoint edge, and cannot change vertices without entering `0`. Hence it must use `(0,j)` to reach `0`. Similarly, deleting `(i,n-1)` for each `i<n-1` destroys `n-1->i`: the first step from `n-1` to any `k<n-1` is edge `(k,n-1)`, the **latest** edge incident to `k`; hence `k` cannot forward the information along any later edge. Thus the stars at the two extremes are forced.

**Proof of sufficiency.** `0` directly reaches each other vertex. `n-1` directly reaches each other vertex. Every interior vertex `j` directly reaches `0` at time `(0,j)`, then `n-1` at the later time `(0,n-1)`, then every interior target `k` along `(k,n-1)`, which is later still. The source can also reach `0` directly. Hence this double-star spans all ordered pairs and, being exactly the forced-edge set, is the unique minimum spanner. QED.

**Novelty caveat:** This is an independently written proof of a tight extremal family, **not** a claimed original result; tightness/examples are already part of the temporal-spanner literature. Its purpose is to construct adversarial instances.

## 4. Falsified proof shortcut: compulsory degree-two peeling

A six-vertex example chronological edge list is:

```
(0,3) (3,4) (0,5) (0,4) (1,3) (0,2) (1,5) (2,5)
(4,5) (1,2) (2,3) (2,4) (0,1) (1,4) (3,5)
```

The **eight-edge** spanner at zero-index positions `(1,2,3,9,10,11,12,14)` is temporally connected. It has two vertices of degree two; deleting either together with its two edges does **not** leave a connected five-vertex temporal graph with six edges. Exhaustive enumeration finds **38** minimum eight-edge spanners for the parent temporal clique: **2** are irreducible in this vertex-peeling sense, while **36** do admit a two-edge vertex peel. Therefore the **universal-over-spanners peeling claim is false**, but the **existential-over-spanners version is not refuted**. Gossip literature already contains sophisticated nontrivial optimal-call classifications, so novelty is not claimed.

## 5. New adversarial computation (all experiments are evidence, not proofs)

1. **n9 extensions of hard n8 instances**: 1,000,000 deterministic sampled schedules; 123,341 were non-pivotable; 24,715 failed to yield a 14-edge spanner in the first 12 randomized deletion orders, but every such case yielded a verified 14-edge spanner within the next 512 deletion attempts. Source `hard_search.cpp`, seed `20261024`.
2. **n9 perturbations of hard n9 instances**: 1,000,000 deterministic sampled schedules; 106,042 non-pivotable; 16,055 failed the first 12 deletion orders; all yielded size 14 within the next 512 orders. Source `hard_search9.cpp`, seed `20261024`.
3. **Compulsory-edge 2-degeneracy probe**: 2,000,000 mixed random and near-lex n9 schedules; maximum observed compulsory-subgraph degeneracy 2, maximum count 15. Source `mandatory_core.cpp`, seed `1927`. This is a tentative NEW RESEARCH HYPOTHESIS, **not established**.
4. **Near-lex adversarial search**: 2,000,000 perturbations of lex n9; 188,975 non-pivotable; largest compulsory-edge count among non-pivotable cases was 9. Source `forced_search.cpp`, seed `232347`.
5. **Exhaustive compulsory-edge count**: n4 all 720 orderings (48 non-pivotable, max 4 compulsory); n5 all 3,628,800 orderings (225,360 non-pivotable, max 5 compulsory). Source `forced_survey.cpp`. These finite facts do **not** verify POD, but are additional structural evidence.
6. **Formal-lemma executable checks**: 720 exhaustive n4 orderings + 7,500 seeded random orders n5..9, plus the tight lex family n4..15, all passed. Source `essential_poset.py`, seed `20261024`.

Sampling duplicates/order-isomorphic schedules is possible and no independent exact-optimization certificate was produced for **every** new n9 sample. A found 14-edge witness proves only the claimed instance has an optimal-size spanner (by the classical lower bound), not that all similar instances do.

## 6. Priority audit and highest-value remaining research tasks

- The open `2n-3` question and `7n` universal construction are firmly established: Casteigts et al. (2019/2021) and Baligács (2026).
- Bumby's 1981 four-cycle theorem and Göbel–Cerdeira–Veldman (1991) preclude calling four-cycle gossip cores themselves original.
- Michail and Spirakis et al., *The Complexity of Optimal Design of Temporally Connected Graphs* (2017), Theorem 4, already gives generic edge-deletion facts in a temporal clique. A mandatory-edge graph lemma MUST be compared carefully against this earlier work.
- There is **no basis yet** to claim novelty for the precedence lemmas; a structured literature priority check and external expert review remain necessary.

**Next mathematical attack:** either (a) prove/refute that compulsory-edge graphs are 2-degenerate; (b) prove/refute the sharper non-pivot compulsory-count bound `<=n`; (c) derive from these or a stronger temporal causal decomposition a universal `2n-3` construction. These are exploratory routes, not claims of a solved major problem. Pursue exact n>=9 *hard instances*, not more uniform random surveys. STOP and report counterexamples to proposed lemmas rather than patching them silently.

## 7. Primary sources

- Casteigts, *Open Questions in Temporal Graphs*, updated 2026-09-22: https://arnaudcasteigts.net/blog/open-problems.html
- Baligács (2026), *Temporal Cliques Admit Linear Spanners*: https://arxiv.org/abs/2606.05156
- Casteigts, Peters, Schoeters (2019/2021), *Temporal Cliques Admit Sparse Spanners*: https://arxiv.org/abs/1810.00104
- Angrick et al. (2024), *How to Reduce Temporal Cliques to Find Sparse Spanners*: https://arxiv.org/abs/2402.13624
- Casteigts, Carnevale, Corsini (2025), *Dismountability in Temporal Cliques Revisited*: https://arxiv.org/abs/2502.01321
- Bumby (1981), *A Problem with Telephones*: https://doi.org/10.1137/0602002
- Göbel, Cerdeira, Veldman (1991), *Label-connected graphs and the gossip problem*: https://doi.org/10.1016/0012-365X(91)90068-D
- *The Complexity of Optimal Design of Temporally Connected Graphs* (2017): https://link.springer.com/article/10.1007/s00224-017-9757-x

**Integrity statement:** No unconditional resolution of the `2n-3` problem has been found or is asserted here. Algorithmic constructions and original priority must remain separate from verified correctness and experimental behavior.
