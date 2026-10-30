# v1.7 — end-to-end independent mathematical verification and priority gate

**25 October 2026.** Source branch: PR #1, v1.4–v1.6. **Verdict:** independent finite n=13 mathematical classification **PASS**, complete historical-priority clearance **UNRESOLVED** because specific original full texts remain inaccessible.

## Precise result

Every all-to-all successful schedule on 13 vertices with exactly 22 pairwise-distinct, undirected, full-information-exchange contacts has at least one *acyclic* half when divided chronologically after 11 contacts.

### Human proof reduction

If both halves have cycles, both have at least three connected components (11 edges on 13 vertices), and every prefix contact component intersects every suffix component, giving r*s<=13. For (r,s)=(3,4) or (4,3), at least two components on the side with 3 components have four singleton opposite-side intersections, but at most one component contains the unique cycle. A tree cannot have four full prefix collectors when its edges contact only once: only endpoints of the last edge can possibly be full. Hence r=s=3 and both halves have exactly one unicyclic component. The 3x3 intersection matrix consists of nine ones and four extra vertices.

A tree with two singleton opposite-side intersections must have their entries as endpoints of its last prefix contact (or first suffix contact by reversing time). Removing that forced first suffix bridge separates two sides. All information from a **third** prefix source must already appear on *both* sides because no subsequent contact crosses the bridge. Thus a third-source intersection of size one is impossible; of size two, both must be full collectors; of size three, at least one must be full. A tree has <=2 full collectors. A unicyclic m-vertex component with m>=5 cannot inform all m internally in m calls since the classical minimum is 2m-4>m.

## New independent computational check

The two files are independently authored and do not import the repository's v1.4 checkers.

- **independent_grid.py** enumerates all 495 distributions of four extras into nine cells (not using symmetry to prune), yielding 16 symmetry classes and 1,278 eligible placements of the unique prefix and suffix cycles. Exactly **nine placements** survive the necessary information-flow constraints; all lie in one orbit: the square extra-cell pattern (0,0), (0,1), (1,0), (1,1), with triangles in row 2 and column 2.
- **independent_square.py** enumerates prefix 5-vertex tree contact orders in the square, retaining the necessary complete collector at the column-2 singleton, and suffix tree orders broadcasting full P2 knowledge from the row-2 singleton. There are 576 prefix and 576 suffix orders per 5-vertex component after filters. Independently propagating source information and rejecting reused edges yields **288** possible prefix orders independently for each suffix column, but **zero** prefix orders can work for **both columns**. This stronger necessary obstruction proves the residual square case cannot succeed. P2 and Q2 each have all three triangle contacts, so their cross-column/row dissemination is already accounted for. Local component orders commute, making enumeration complete.

GitHub CI runs the two files from a clean checkout; an earlier implementation of the finite result is also independently present in v1.4. The result is a finite computer-assisted proof, not a Lean/Coq machine-checked theorem.

## Historical priority: what is and is not verified

Direct prior art covers the classical 2n-4 minimum calls, forest-decomposition for graphs admitting some good edge labeling (Göbel–Cerdeira–Veldman 1991 Theorems 3 and 9), two-contact vertex extension (their Theorem 13), ordered NOHO families (West 1982), optimal gossip kernel posets/linear extension machinery (Labahn 1995), and reordering principles (Krumme 1996). Renken (2023) reconstructs Labahn Theorem 3.1 / Corollary 3.1 and κ>=5 kernel structure and applies it to temporal spanners.

The 1991 **static Cd-graph forest partition** is not synonymous with the **original fixed chronological halves**. A v1.6 verified witness has a cyclic suffix half but an alternative static two-forest Cd partition. The original kernel-poset classification may nevertheless imply the finite n13 statement after analyzing all admissible chronological linear extensions, and the v1.5 identical-poset witness does not refute that possibility.

Publisher pages for **Labahn 1995** (https://doi.org/10.1016/0012-365X(94)00031-D) and **Krumme 1996** (https://doi.org/10.1016/0012-365X(94)00302-Y) were located but complete original journal bodies could not be read (HTTP 403); Labahn 1992 Bonn Parts I/II are bibliographic records, not downloaded texts. Consequently the specific first-bridge 1/2/3 lemma and n13 result have **no located exact predecessor** but also **no justified negative implication proof** from those original works. They remain **possibly distinctive, novelty unresolved**. The universal fixed-temporal-clique 2n-3 conjecture remains open and independent of this finite result.

## Final gates

| Gate | Disposition |
|---|---|
| Information-flow lemmas and assumptions | PROVED in scoped human argument |
| Unquotiented finite n13 classification | INDEPENDENT EXACT CHECK PASS |
| Unique residual n13 pattern | INDEPENDENT EXACT UNSAT PASS |
| Independent GitHub CI | See workflow verification status |
| Earlier classical techniques and reductions | PRIOR ART FOUND |
| Full Labahn/Krumme implication exclusion | UNVERIFIED — missing complete primary sources |
| Scholarly novelty or first-ever claim | BLOCKED |
| Fixed-time temporal clique 2n-3 conjecture | OPEN |

**No further mathematical finite enumeration is needed for the n=13 claim** unless independent reviewers find an error in the stated reduction/assumptions. The remaining historical-priority gap is a concrete inaccessible-source limitation, not a deferred execution phase.
