> **Stage 7 refinement:** The stronger [symmetric two-sided all-n theorem](TWO_SIDED_SURPLUS_THEOREM.md) proves the improved inequality `n >= rs + 2(r+s) - 8`. This file retains the independently checked weaker one-sided version for research provenance; use the two-sided theorem for subsequent deduction.

# Stage 7 — a uniform all-n collector-surplus lower bound

**27 October 2026. New all-n necessary-condition theorem (conditional only on the previously established tree-entry lemma); not the all-n half-forest conjecture.** PR #1 remains DRAFT/UNMERGED and historical originality remains UNRESOLVED.

## Scope and statement

Let S be any successful 2n-4-contact bidirectional telephone-gossip chronology on n>=4 vertices with pairwise-distinct unordered contacts. Fix its **original** chronological split after n-2 calls. Suppose **both** static halves have cycles. Write r and s for their respective component counts. Then r,s>=3.

**Proposition (uniform surplus gap).** Every such hypothetical chronology satisfies

\[
  \boxed{n\ \ge\ rs+2\max(r,s)-2.}
\]

Equivalently, when 3<=r<=s, the number E=n-rs of vertices *beyond the compulsory one per incidence cell* is at least 2(s-2)+2. The time-reversed statement handles s<=r.

This uniform formula generalizes the previously isolated 3×4 threshold n>=18 and strengthens the previous 3×s baseline n>=5s-4 by **two** vertices at every s>=3. Examples: 3×3 requires n>=13, 3×4 requires n>=18, 3×5 requires n>=23, 4×4 requires n>=22, and 4×5 requires n>=28. The bound eliminates entire infinite ranges of r,s,n; it does **not** exclude configurations above its threshold or prove the half-forest conjecture.

## Dependencies

The proof uses three lemmas already proved in [v2.0 manuscript](../v2.0/MANUSCRIPT.md), Section 2 and Section 3A.

1. **Incidence/edge count.** Every prefix component meets every suffix component. The aggregate cycle ranks in the two halves are r-2 and s-2, respectively.
2. **Tree collector capacity.** A prefix tree component has at most two vertices knowing every original secret in that prefix component at the cut. A singleton intersection with any suffix component forces its unique vertex to be such a collector. Reversing the complete schedule, a suffix-tree component has at most two reverse collectors, and each singleton intersection with a prefix component forces its vertex to be a reverse collector.
3. **Single-source tree entry.** If a suffix *tree* column has a singleton intersection with some prefix row, every other prefix row has at least one complete midpoint collector in its intersection with that column. Its time reversal is also true.

All three are about actual original chronological halves, not a beneficially reordered schedule.

## Human proof (arbitrary r,s)

By time reversal and symmetry of notation suppose 3<=r<=s. Let P_1,...,P_r be prefix components, Q_1,...,Q_s suffix components; define the positive integer incidence matrix M_{ij}=|P_i ∩ Q_j| and surplus E=sum(M_{ij}-1)=n-rs.

Since the prefix total cycle rank is r-2, **at least two prefix components are trees**. A tree prefix row has at most two midpoint collectors. Every singleton intersection is a collector, so at least s-2 of its s entries must be non-singletons, each costing at least one surplus vertex. Thus E >= 2(s-2).

For a contradiction assume E <= 2(s-2)+1. For s>=4, a third prefix tree would cost at least another s-2>=2 surplus vertices; impossible. For s=3, the assumption r<=s forces r=3, and total cycle rank one forces precisely two prefix trees. Thus in every case there are exactly two tree rows, label them A and B. All other r-2 prefix rows are cyclic and, since their cycle ranks sum to r-2, are necessarily unicyclic. **All** of the E surplus vertices are used by the two tree rows (s-2 each), except possibly **one** surplus vertex anywhere in the matrix.

A prefix tree row with exactly s-2 surplus vertices must have **exactly two singleton intersections** and s-2 size-two intersections: it needs at least s-2 distinct non-singleton cells, and has just s-2 extra vertices to supply them. Each of its two singleton participants is a mandatory collector, exhausting its two-collector capacity. In particular, it **cannot have any additional collector in a non-singleton cell**.

The suffix total cycle rank s-2 similarly forces at least **two suffix-tree columns**, denote a pair Q and Q'.

**Case 1: no extra surplus vertex, or its single extra vertex belongs to a non-tree prefix row.** Both A and B are minimum-size tree rows. Because there are at least two suffix-tree columns, choose a suffix-tree column T that does not contain the extra vertex, if any. Every non-tree row intersects T in a singleton (at least one such row exists since r>=3). By the single-source tree-entry lemma, both A and B have a collector in T. As their two singleton collectors already exhaust capacity, these intersection cells MUST be singleton. Hence T has at least three distinct singleton intersections (one from a non-tree row, one from A, one from B), contradicting the fact that a suffix tree has at most two reverse collectors.

**Case 2: the single extra surplus vertex belongs to tree row A** (exchange A,B if needed). Then B is minimum-size and every cyclic prefix row is singleton in every suffix-tree column. The single-source tree-entry lemma forces a collector in A and in B in **every** suffix-tree column. Since B has capacity two, exactly two suffix-tree columns exist, Q and Q', and they must be B's two singleton columns.

If r>=4, each Q already has r-2>=2 singleton intersections from cyclic prefix rows, plus the singleton from B. This is at least three, contradicting the suffix-tree reverse-collector bound.

If r=3, the single cyclic row C and row B provide **two** singleton intersections in each of Q and Q'. Therefore A must be non-singleton in **both** Q and Q' to avoid a forbidden third singleton. Yet A has only s-1 surplus vertices, fewer than the s required to make all its s cells non-singleton, so it has at least one singleton in a column outside {Q,Q'}. That singleton is necessarily a complete collector in A. In addition the single-source tree-entry lemma requires separate collectors in A∩Q and A∩Q'. Thus A would have at least **three** distinct complete collectors, impossible for a tree row.

Both cases are contradictory. Therefore E>=2(s-2)+2, i.e. n>=rs+2s-2. Reversal proves n>=rs+2r-2 in the complementary ordering; equivalently n>=rs+2max(r,s)-2. QED.

### Adversarial assumptions

- **At least one cyclic row exists** in Case 1 because r>=3 and there are exactly two prefix tree rows; the proof never silently relies on r=3.
- **Other row singleton at a tree column:** if the single extra vertex is in a non-tree row, one of the two tree columns avoids it.
- **Only one extra vertex:** this follows by subtracting the unavoidable two tree-row surpluses, not by claiming all other rows have baseline size in general.
- **Time reversal:** reversing all calls of any successful two-way schedule is again successful; the reversed full-information propagation condition is the transpose of the original temporal reachability relation, and is complete if and only if the original is.
- **No leap to conjecture:** n can be arbitrarily larger than the lower bound for fixed r,s. This is a proven necessary obstruction, not an induction step or a bounded-kernel theorem.

## Independent boundary falsification

[prove_universal_surplus_gap.py](prove_universal_surplus_gap.py) independently builds every low-surplus incidence grid with exactly two prefix-tree rows, an arbitrary position for its zero/one extra vertex, all choices of two singleton cells in each minimum tree row, and **every possible suffix-tree-column pattern** arising from nonnegative suffix cycle rank allocations summing to s-2. It checks both directions of forced collector constraints, with no invocation of the original v2.3 enumerators.

The test covers all marked necessary configurations with E=2(s-2) or E=2(s-2)+1 for (r,s)=(3,3),(3,4),(3,5),(4,4),(4,5),(5,5): **810, 14,040, 120,000, 36,720, 315,000 and 650,000** marked near-boundary instances respectively. The asserted number of survivors is zero in each case. In (3,s), s=3,4,5, the script also checks the next threshold E=2(s-2)+2, at which necessary-condition survivors **81, 396, 1440** reappear. These latter patterns are **not real gossip witnesses** and show only that the particular incidence relaxation cannot eliminate everything at equality.

The executable finite tests **falsify/check instances of the algebraic theorem but cannot by themselves establish its universal quantifier**. The proof above is the all-n argument.

## Next universal bottleneck

The new bound forces a hypothetical counterexample into grids with a strictly positive and growing surplus. It still permits such grids for arbitrarily large n. The next task is to seek a **bounded irreducible temporal kernel** or a **surplus-reduction transformation** preserving success, distinct-call optimality and cyclicity in *both original halves*. Any proposed reduction must be actively refuted with exact counterexample search before being used inductively.

Literature: Roger Labahn, *Kernels of minimum size gossip schemes* (1995), and David Krumme, *Reordered gossip schemes* (1996) precede this work; the new bound's novelty relative to their full results is NOT established from abstracts alone. Avoid publication novelty claims.
