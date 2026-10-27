# Stage 7 — symmetric two-sided collector-surplus theorem (all component counts)

**27 October 2026. HUMAN PROOF, ALL n (conditional only on earlier published-in-repo tree collector and single-source entry lemmas). INDEPENDENT ENUMERATION: CI-GATED. General original-half forest property: OPEN. Novelty compared to Labahn/Krumme: UNRESOLVED.**

This strengthens the preliminary [one-sided all-n surplus gap](UNIVERSAL_SURPLUS_GAP.md) and includes it as a corollary. The earlier statement is mathematically correct but not sharp for r>=4.

## Statement

Let S=(e_1,...,e_{2n-4}) be a successful shortest bidirectional gossip schedule on n>=4 participants with pairwise-distinct unordered contacts. Keep the **original** first n-2 and last n-2 contacts without reordering. Suppose both their static edge sets contain a cycle, and let r,s be their respective numbers of connected components (necessarily r,s>=3). Then

\[
 \boxed{n \ge rs+2(r+s)-8.}
\]

Equivalently, if M is the strictly positive r×s prefix/suffix component-intersection matrix and E=sum(M_ij-1)=n-rs, then **E>=2(r-2)+2(s-2)**.

Unlike the preliminary bound n>=rs+2max(r,s)-2, this stronger bound grows with **both** r and s, and does not require r<=s or assume there are exactly two tree components.

Examples: 3×3 requires n>=13; 3×4 n>=18; 3×5 n>=23; 4×4 n>=24; 4×5 n>=30; 5×5 n>=37. These are purely necessary conditions for any both-cyclic original-half gossip chronology. An incidence pattern at equality is NOT a successful gossip witness.

## Assumptions imported from the earlier checked manuscripts

The proof uses only:

1. **Complete incidence and cycle rank:** every prefix component P_i meets every suffix component Q_j, and the static cycle ranks sum to r-2 and s-2 respectively. Therefore r,s>=3 and **at least two prefix components** and **at least two suffix components** are trees.
2. **Tree collector capacity:** a prefix-tree component can have at most two complete midpoint collectors; a singleton intersection necessarily consists of a collector. Time reversal supplies the same ≤2 reverse-collector bound for a suffix tree, so a suffix-tree column can have **at most two singleton entries**.
3. **Single-source tree entry (v2.0 Lemma 7):** if a suffix tree Q has a singleton intersection with any prefix component P, then **every other prefix component** has a full collector in its Q intersection. In particular, if we select *two prefix-tree rows* A,B and Q contains a singleton in a different row, A and B both require collectors in Q.

These are about the existing chronology and do not depend on graph reordering or speculative kernel classifications. The single-source entry lemma must remain independently reviewable; it is an explicit dependency, not an invisible axiom.

## Proof for arbitrary r,s

Choose **any two prefix-tree rows**, A and B, and **any two suffix-tree columns**, T_1 and T_2. The other r-2 prefix rows may be tree, cyclic or have higher cycle rank: the proof does NOT assume they are cyclic. Call these the **outside rows**.

A cell is *large* if it contains at least two vertices (M_ij>=2). Every large cell contributes at least one surplus vertex E=n-rs. Different large cells are disjoint contributions.

Every prefix-tree row has at most two singleton cells, since a singleton must be a complete collector, and a tree has at most two complete collectors. Thus each of A,B has at least s-2 large cells.

Every suffix-tree column has at most two singleton cells by the time-reversed bound. Thus each of T_1,T_2 has at least r-2 large cells.

Classify each chosen suffix-tree column as **rooted** if it has at least one singleton cell in an outside row (i.e. a row distinct from A and B). Otherwise call it **unrooted**; in an unrooted column, *all* r-2 outside-row cells are large.

**Case I: both T_1 and T_2 are rooted.** By the single-source tree-entry lemma both A and B require a complete collector in both chosen columns. Their capacity of two is exhausted, so neither A nor B may contain **any singleton cell outside T_1,T_2**. All 2(s-2) cells in rows {A,B} outside columns {T_1,T_2} are therefore large. The two suffix-tree columns each have at least r-2 large cells, contributing another 2(r-2) distinct large cells in columns {T_1,T_2}. These regions are disjoint.

**Case II: exactly one is rooted, say T_1; T_2 is unrooted.** Each of A,B must have a collector in T_1, so it can contain at most one singleton across its other s-1 columns. Hence at least s-2 large cells occur **in each of A,B outside column T_1**, for 2(s-2) distinct large cells. Since T_1 is a suffix tree it has at least r-2 large cells in column T_1. Since T_2 is unrooted, all its r-2 outside-row cells are large. These three groups of cells are pairwise disjoint (A/B outside T_1, all rows of T_1, and outside rows of T_2). Total at least 2(s-2)+2(r-2).

**Case III: neither chosen suffix-tree column is rooted.** Both are unrooted, so each of the r-2 outside rows contributes a large cell in both columns, totaling 2(r-2) large cells **outside A,B**. Independently A and B each require at least s-2 large cells somewhere in their rows, totaling 2(s-2) cells **inside A,B**. These regions are disjoint.

All cases force at least 2(s-2)+2(r-2) distinct large cells. As each large cell contributes at least one surplus vertex, E>=2(s-2)+2(r-2), proving n>=rs+2(r+s)-8. QED.

### Adversarial audit: what the argument does NOT assume

- The r-2 outside rows are NOT required to be cyclic, and the s-2 outside columns need not be trees.
- A large cell may contain 3, 4, or more vertices; counting it as **only one** extra vertex gives a safe necessary lower bound.
- Collector obligations apply to **the same fixed original midpoint**; no reordering or feasible global tree chronology is inferred from cell structure.
- An unrooted suffix tree need not lack all singleton cells: it lacks singleton cells **in the outside rows** only. This is exactly the set needed for the disjoint counting.
- In Case II the cost of T_2 in A or B is already included in the A/B outside-T_1 count, so it is not double-counted.
- No assumption is made that the chosen A,B or T_1,T_2 are the only tree components.
- A necessary incidence matrix can satisfy these inequalities without being realizable as an actual successful schedule.

## Independent exhaustive binary-incidence checker

[test_symmetric_surplus.cpp](test_symmetric_surplus.cpp) takes a wholly different verification route from earlier positive-integer matrix generators: represent each cell only by whether it is singleton or large (one bit per cell). By permuting row and column labels, fix two prefix-tree rows at indices 0,1 and two suffix-tree columns at 0,1. Enumerate **all** binary large/singleton cell masks with at most 2(r+s)-8 large cells. Check complete necessary forward and time-reversed collector requirements using the earlier single-source lemma, and assert:

1. **No mask below the all-n theorem's bound survives.**
2. **At least one mask at the bound survives.** These equality masks are *necessary-condition patterns*, NEVER claimed realizable successful gossip schedules.
3. Exact checked mask counts, surviving equality counts and representative bitmasks match expected fixtures, so an unexpectedly truncated search fails.

| r×s | Required minimum E | Masks tested (E<=bound) | Surviving equality masks |
|---|---:|---:|---:|
| 3×3 | 4 | 256 | 5 |
| 3×4 | 6 | 2,510 | 12 |
| 3×5 | 8 | 22,819 | 30 |
| 4×4 | 8 | 39,203 | 19 |
| 4×5 | 10 | 616,666 | 37 |
| 5×5 | 12 | 16,777,216 | 55 |

These computations are **independent falsification evidence**, not a substitute for the unbounded proof above, and their success does not justify claiming a solution to the full original-half-forest conjecture.

## Logical status and next bottleneck

- **Two-sided collector-surplus theorem:** PROVED by the written argument, conditional on the previously stated tree-entry lemma's correctness; finite mask verifier tests representative cases, no proof-assistant formalization or external refereeing yet.
- **Original-half forest property for every n:** OPEN; the inequality still permits large incidences at large n.
- **Minimal counterexample induction via automatic degree-two deletion:** FAILS as a general premise: [adversarial_induction_obstruction.py](adversarial_induction_obstruction.py) verifies the valid 8-person 12-call W8 optimal scheme has **every vertex degree 3**. This does NOT rule out a deletion theorem with additional restrictions on hypothetical both-cyclic schedules.
- **Historical contribution:** no source-level equivalence theorem has been established against [Labahn 1995](https://doi.org/10.1016/0012-365X(94)00031-D) or [Krumme 1996](https://doi.org/10.1016/0012-365X(94)00302-Y). Novelty remains UNRESOLVED.

**Research priority:** derive a reduction preserving the **original midpoint** or lift the complete classical kernel/poset characterizations into a fixed-chronology impossibility argument. The new symmetric inequality is a structural tool for that effort, not a stopping criterion.
