# Research v1.4 — finite half-forest theorem through thirteen vertices

**25 October 2026.** **Verdict:** new *finite* n=13 classification, combining a human-proved general information-flow lemma, structural case reduction and a single exact exhaustive residual check. No universal temporal-clique spanner theorem is proved, and research priority against classical gossip theory remains unchecked.

## Contact model

A successful shortest simple-contact gossip schedule on n>=4 labelled vertices has exactly 2n-4 pairwise distinct undirected calls exchanging all known original secrets; at the end every vertex knows all secrets. Split after n-2 calls. Denote prefix contact components P_i and suffix contact components Q_j. For all i,j, P_i and Q_j must intersect. A *prefix complete collector* of P_i knows every original P_i secret at the split. A *reverse collector* of Q_j learns every Q_j secret under the suffix contacts reversed.

**Previously proved (v1.3):** a contact tree has at most two complete collectors, endpoints of its last contact. A tree prefix component with singleton intersections at u,v with distinct suffix components must contact uv *last*. The time-reversed dual forces the first suffix-tree contact between any two singleton intersections with different prefix components.

## General first-bridge covering lemma (human proof)

Let a suffix tree Q have singleton intersections c and d with two *different* prefix components. Then its first suffix contact is cd. Removing cd splits the suffix tree into A and B. For every *third* prefix component P, every original P secret must already have a carrier in **both** P∩Q∩A and P∩Q∩B at the midpoint.

**Proof.** Since c,d belong to prefix components different from P, they initially possess no original P secrets. The first suffix contact cd therefore transmits no P secrets. All later Q contacts are internal to A or B (cd is the unique cut edge). Both sides must eventually learn all P secrets, so every P secret must already have a carrier on both sides at the split. The carriers must be in P∩Q because prefix contact components are disjoint. QED.

Writing k=|P∩Q|, we obtain necessary conditions: **k=1 impossible; k=2 both intersection vertices must be prefix complete collectors of P; k=3 at least one intersection vertex must be a prefix complete collector of P.** For k=3, one of the two nonempty sides has just one carrier and that carrier must possess all P secrets. These statements also apply if P is unicyclic. Reverse time for the corresponding necessary conditions on reverse collectors of suffix components when a *prefix* tree has two singleton suffix intersections.

**Collector budget:** A contact tree has at most two (forward or reverse) complete collectors. An m-vertex unicyclic contact component with exactly m calls, for m>=5, cannot have all m vertices fully informed within the component, since classical telephone gossip needs at least 2m-4>m calls. This bound is classical, not original here.

## Complete n=13 reduction

**Finite claim:** Every successful 22-contact distinct-edge gossip schedule on 13 vertices has at least one acyclic chronological half (11 calls).

If both halves are cyclic, the prefix and suffix component counts r,s are each >=3 (cyclomatic number for 11 edges on 13 vertices is r-2). Since every P_i∩Q_j is nonempty, rs<=13, allowing only (r,s)=(3,3),(3,4),(4,3). For (3,4), 12 nonempty cells plus one extra vertex imply at least two prefix rows have four singleton cells. The prefix has exactly one cycle, so at least one such row is a tree and would need four complete collectors, impossible. Exclude (4,3) by reversing time. Thus r=s=3, with exactly one cyclic component per half.

Each 3x3 intersection matrix consists of nine 1s plus exactly four additional vertices. There are C(12,4)=495 extra-cell multisets, or **16 orbits** under independent row/column permutations and transposition. A tree row/column with all three intersections singleton would require three collectors, so we may restrict the possible locations of the unique cycles. The script `half_forest13_reduction.py` exhaustively produces **44 nominal cycle placements** across the sixteen representatives (placements are not all pairwise nonisomorphic). Applying the first-bridge 1/2/3 covering rules in both directions, tree collector budgets, and the classical m>=5 gossip bound excludes **43/44**. An entirely unquotiented pass over the 495 multisets yields **1,278** eligible placements, exactly **nine** unexcluded, all belonging to the same orbit.

**Only remaining layout:**

```
         Q0 Q1 Q2
P0        2  2  1     prefix 5-vertex tree (4 calls)
P1        2  2  1     prefix 5-vertex tree (4 calls)
P2        1  1  1     prefix triangle (3 calls)
suffix  tree tree triangle
```

This is precisely the square configuration studied in v1.3. The stand-alone `verify_square.py` independently lists every local connected tree-edge subset and chronological order, retaining only the necessary single-entry full-collector prefix condition. It enumerates **576** prefix local tree orders for each five-vertex prefix component and **3,000** suffix tree orders for each five-vertex suffix component. Bitset intersections impose complete transmission of every prefix-row's original secrets into both suffix tree components while excluding reuse of the same edge in the two halves. P2's three-call triangle gives all its vertices complete P2 knowledge; Q2's triangle then transmits the complete P0/P1/P2 groups because its three singleton-entry vertices already carry their entire prefix rows. Contacts in disjoint prefix or suffix components commute, so local-order enumeration is complete. No feasible combination exists: **EXACT_UNSAT**. Thus the n=13 finite theorem follows.

## Reproduce and evidence

```bash
python research/v1.4/half_forest13_reduction.py
python research/v1.4/verify_square.py
```

Executed locally with Python **3.13.5** on 2026-10-25. Results: 16 orbits, 44 cycle placements, 43 excluded, 1 residual; unquotiented 1278 eligible and 9 equivalent survivors; square prefix options [576,576,6], suffix [3000,3000,6], and EXACT_UNSAT. The two programs implement different levels of the proof. Neither is a general-n theorem prover. GitHub CI, a proof assistant, and outside peer review are **not** claimed.

**Scientific boundaries:** the prior v1.2 results cover <=12; the new finite n=13 exclusion relies on exact enumeration of one residual pattern and should undergo independent expert audit. The conjecture that *all* shortest gossip schedules have a forest half for n>=14 is OPEN. More importantly, gossip call-order constraints are **not equivalent** to finding a sparse subgraph under a *fixed* temporal clique edge ordering, so the main 2n-3 conjecture and POD remain OPEN.

**Priority barriers:** Göbel–Cerdeira–Veldman (1991), *Label-connected graphs and the gossip problem*; Labahn (1995), *Kernels of minimum size gossip schemes*, https://doi.org/10.1016/0012-365X(94)00031-D ; Krumme (1996), *Reordered gossip schemes*, https://doi.org/10.1016/0012-365X(94)00302-Y ; current temporal-clique open-problem tracker https://arnaudcasteigts.net/blog/open-problems.html .

**Review gate:** Keep the research PR in draft, do not merge before independent reproduction and priority review. No new universal theorem or publication novelty is claimed.

### CI verification addendum — 25 October 2026

**CI-VERIFIED EXECUTION on commit b3f889ff68c719b9754a0673068c133c5975599b:** GitHub Actions push run [40201117451](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40201117451) and pull-request run [40201117477](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40201117477) both completed **success**. Their `finite-certificate` jobs successfully ran both the structural classifier and the exact square checker from committed source. This establishes reproducible execution in a second runtime, **not** a machine-formal proof, independent implementation, originality finding, or universal theorem.
