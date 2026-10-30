# Chronological Half-Forest Restrictions in Minimum-Call Gossiping

## An Exact Thirteen-Participant Certificate and a Fifteen-Participant Reduction

**Working mathematical research manuscript — October 25, 2026. Not submitted, not externally peer reviewed. Author metadata to be confirmed.**

### Abstract

Let a successful telephone-gossip schedule on \(n\ge4\) vertices have exactly \(2n-4\) pairwise-distinct undirected calls; each call exchanges all information known by its endpoints. Split the **given chronological sequence** after \(n-2\) calls. We prove by a finite computer-assisted certificate that, when \(n=13\), at least one half is a forest. Component-intersection counting and a first-bridge information-flow lemma reduce the hypothetical both-cyclic case to a single exceptional \(3\times3\) configuration, whose chronological orders are excluded by independently implemented exact checks. We also prove a general rectangular-grid obstruction: if both halves are cyclic, the prefix has three components and the suffix has \(s\ge4\), then \(n\ge5s-4\). Thus every hypothetical counterexample with \(n\le15\) has exactly three components on each side. The same finite necessary-condition filter at \(n=14\) retains 738 placements in 11 matrix symmetry classes; no extrapolation of the \(n=13\) theorem follows. We distinguish a property of the **original** halves from existing static forest decompositions and reordering theorems. Originality of the finite result relative to all implicit corollaries of classical kernel classifications remains unresolved.

### 1. Introduction and model

The classical optimal telephone-gossip problem needs \(2n-4\) pairwise full-information exchanges for \(n\ge4\); its static supporting graphs, minimal event orders, kernel structures and reordering properties have long been studied [1–5]. Here the point of study is *not* whether a static graph admits a favorable order, nor whether one may rearrange a successful schedule, but what must be true of its *existing* chronological midpoint.

A schedule is an ordered list of undirected edges \(e_1,\ldots,e_{2n-4}\), all distinct, on \(n\) participants. Each vertex initially knows exactly its own secret; a call \(uv\) replaces each endpoint's knowledge set by their union. A schedule succeeds if every vertex knows all secrets at the end. Write \(L=(e_1,\ldots,e_{n-2})\) and \(R=(e_{n-1},\ldots,e_{2n-4})\).

Let \(P_1,\ldots,P_r\) be the static connected components of \(L\), and \(Q_1,\ldots,Q_s\) the components of \(R\), including all vertices. Let \(M_{ij}=|P_i\cap Q_j|\). A *prefix complete collector* of \(P_i\) is a vertex that knows every original secret of \(P_i\) at the cut. A *reverse collector* of \(Q_j\) is defined by reversing the full successful sequence. A component is cyclic if its static graph contains a cycle.

### 2. Fundamental structural lemmas

**Lemma 1 (Component intersection and cycle rank).** Every \(P_i\) intersects every \(Q_j\); consequently \(rs\le n\). The cyclomatic ranks of \(L\) and \(R\) are respectively \(r-2\) and \(s-2\).

*Proof.* Information from any \(P_i\) secret cannot enter a suffix component \(Q_j\) unless a vertex lies in both, because after the cut no call connects distinct \(Q\)'s. For a graph on \(n\) vertices with \(n-2\) edges and \(c\) connected components, cyclomatic rank is \((n-2)-n+c=c-2\). ∎

**Lemma 2 (Tree collectors and forced endpoints).** In a nontrivial prefix-tree component, only the endpoints of its *last* internal call can possibly possess all component secrets at the cut. If its intersections with two different suffix components are distinct singletons \(u,v\), the last internal call is necessarily \(uv\). In the time-reversed dual, a suffix tree with singleton intersections \(u,v\) in distinct prefix components must have \(uv\) as its *first* call.

*Proof.* The last edge \(xy\) of a tree separates it into two parts. Before that contact, no vertex in either part can have all secrets from the other; after that contact, no other tree contact occurs. Only \(x,y\) may become complete. A singleton entry into a suffix component must carry the entire prefix component's secrets, proving the forced-last-edge statement. Reverse time for the dual. ∎

**Lemma 3 (First-bridge covering).** Let a suffix-tree component \(Q\) have singleton intersections \(Q\cap P_a=\{c\}\), \(Q\cap P_b=\{d\}\) with different prefix components. Its first call is \(cd\). Removing that edge splits \(Q\) into sides \(A,B\). For any third prefix component \(P\ne P_a,P_b\), *every original secret of \(P\)* must already have a carrier in **each** of \(P\cap Q\cap A\) and \(P\cap Q\cap B\) at the cut. Hence \(k=|P\cap Q|=1\) is impossible; \(k=2\) forces both intersection vertices to be complete prefix collectors; and \(k=3\) forces at least one. The full time-reversed statement also holds.

*Proof.* The first contact is \(cd\) by Lemma 2. Its endpoints contain no \(P\)-secrets before the suffix begins. The edge transmits no \(P\)-secret, and every later contact of \(Q\) lies entirely within \(A\) or \(B\). For both sides ultimately to know every \(P\)-secret, that secret must have had a carrier on *both* sides at the cut, necessarily within \(P\cap Q\). The cardinality consequences follow by pigeonhole counting of the two sides. ∎

**Known bound.** A unicyclic component on \(h\ge5\) vertices has \(h\) contacts and cannot fully inform every one of its own vertices of its \(h\) original secrets using only \(h\) contacts: the classical lower bound is \(2h-4>h\). We use this as prior art, not as a new theorem.

### 3. New structural extension: a rectangular-grid bound

**Proposition 4.** Suppose both halves contain cycles and \(L\) has precisely \(r=3\) components whereas \(R\) has \(s\ge4\). Then

\[
\boxed{n\ge 3s+2(s-2)=5s-4.}
\]

The same assertion holds with the two halves interchanged.

*Proof.* Since the rank of \(L\) is \(r-2=1\), at least two of its three components are trees. Each tree row has nonempty intersections with all \(s\) suffix components. A singleton intersection demands one complete collector and the row has at most two collectors. Consequently each of those two tree rows has at least \(s-2\) cells with size at least two. Relative to the mandatory \(3s\) vertices in the grid, this contributes at least \(2(s-2)\) additional vertices. ∎

**Corollary 5 (Grid confinement to \(n\le15\)).** If \(n\le15\) and both halves are cyclic, then **\(r=s=3\)**.

*Proof.* Lemma 1 gives \(r,s\ge3\) and \(rs\le n\le15\). Thus both cannot be at least 4. If one equals 3 and the other is at least 4, Proposition 4 gives \(n\ge16\). The only remaining possibility is \((r,s)=(3,3)\). ∎

### 4. Finite theorem at thirteen participants

**Theorem 6 (Computer-assisted).** For \(n=13\), every successful sequence of 22 pairwise-distinct calls has at least one acyclic original chronological half of 11 calls.

*Proof.* Suppose both halves are cyclic. Corollary 5 gives \(r=s=3\) and Lemma 1 gives total cycle rank 1 in each half. Thus there is one unicyclic prefix component and one unicyclic suffix component, and the other components are trees. Every entry of \(M\) is positive, and the entries sum to 13: there are nine mandatory vertices and four excess vertices. There are exactly \(\binom{12}{4}=495\) multisets distributing those excess vertices among nine cells; 16 orbits result under row and column permutation and transposition.

For every matrix and possible cyclic row/column placement, impose necessary conditions from Lemmas 2 and 3, tree collector capacities, and the classical unicyclic \(2h-4\) lower bound. An **unquotiented** exact enumeration gives 1,278 eligible cyclic placements; all but nine are excluded. These nine configurations belong to the same symmetry orbit represented by

\[
M_*=\begin{pmatrix}2&2&1\\2&2&1\\1&1&1\end{pmatrix},
\]

where the third row and third column are three-vertex triangles and the other four components are five-vertex trees. Both a case-classifier and an independently written classifier check this finite reduction.

To exclude the residual configuration, each of the first two prefix five-vertex trees must fully inform the vertex in its unique third-column intersection by the cut (it is the unique entry for its row into that suffix component). Enumeration of connected 4-edge subsets and all orders satisfying this collector condition gives **576 prefix orders** per tree. Each of the first two suffix trees has a unique vertex in the third prefix row; it alone initially carries that prefix triangle's information into the suffix tree. To disseminate the triangle's information, the suffix tree must propagate this one-vertex origin to all five vertices, and an independent enumeration gives **576 suffix orders** per tree satisfying this necessary condition.

Now propagate, for each row separately, its five source secrets through one prefix tree order and one suffix column order; reject any pair reusing the same undirected contact. The necessary condition is that all five members of the suffix column learn all five row secrets. For each row, **288** prefix orders can work with the first suffix column individually and **288** with the second individually; **no prefix order can work with both**. This contradiction excludes the residual matrix. Since calls in different prefix components commute with one another (and likewise for suffix components), enumerating local component orders covers every global chronology relevant to this proof. Therefore the two-half-cyclic case is impossible. ∎

**Reproducibility.** Exact scripts: \`research/v1.7/independent_grid.py\` and \`research/v1.7/independent_square.py\`, with alternative independent machinery in \`research/v1.4/\`. Both v1.7 checks have passed GitHub Actions. These are finite executable certificates supported by the proof of their reduction and completeness; they are *not* Lean/Coq machine-formal proofs.

### 5. Where generalization currently stops

Corollary 5 also reduces n=14 and 15 to the \(3\times3\) grid. Increasing the excess-cell count to five or six and applying **the same necessary-condition filter only** gives:

| \(n\) | Excess allocation multisets | Eligible cycle placements | Placements not excluded | Surviving matrix symmetry classes |
| --- | ---: | ---: | ---: | ---: |
| 13 | 495 | 1,278 | 9 | 1 |
| 14 | 1,287 | 4,698 | 738 | 11 |
| 15 | 3,003 | 13,680 | 4,662 | 42 |

\`research/v1.9/n14_reduction.py\` reproduces these exact counts. A deterministic bounded annealing search at n=14 did **not** find a genuine both-cyclic successful schedule after five million mutations; this is an exploratory null result and does **not** establish UNSAT. The universal half-forest statement for n≥14 remains **OPEN**.

### 6. Related work and novelty boundaries

West [3,4] classifies the special NOHO optimal schemes under extra assumptions; Göbel, Cerdeira, and Veldman [1] characterize statically label-connected graphs attaining \(2n-4\) edges and give the two-contact vertex extension. Labahn [2], notably his Theorem 6.1, completely characterizes p-grid kernel admissibility and studies linear extensions. Krumme [5] proves reordering theorems and static structural decompositions. A recent study by Williams [6] uses the first n−2 contacts and swaps of disjoint consecutive calls. Those classical and recent ingredients are **prior art**, not advertised as new here.

An existence theorem for *some* static partition into two forests does not assert that the original first and last n−2 contacts are each forests. Likewise a theorem constructing *some reordered successful schedule* does not by itself decide a fixed-original-midpoint statement. The n=8 witness in \`research/v1.6/\` concretely separates these properties. It does **not** show that stronger historical structural results could not imply Theorem 6 as a corollary.

The original Labahn and Krumme articles were provided and examined directly in v1.8. No exact explicit statement of the first-bridge k=1/2/3 rule or the n=13 fixed-original-half theorem was identified there, but the absence of a verbatim statement is **not** a proof of priority across all historical work or of non-derivability from older classifications.

The fixed-time-label temporal-clique spanner problem is distinct. Casteigts, Peters, and Schoeters [7] established sparse temporal-clique spanners, and Baligács [8] established a universal linear 7n bound in 2026; the proposed universal 2n−3 bound remains listed as open [9]. Our gossip result does **not** prove it or imply an improvement.

### 7. Conclusion and limitations

The finite thirteen-vertex theorem is supported by complete reduction and independent exhaustive computational exclusion; a general component-grid restriction is proved through fifteen participants. The proof remains a computer-assisted finite result awaiting external mathematical peer review, and the historical novelty/significance of the specific finite boundary remains conditional. The n=14 and n=15 cases and the 2n−3 temporal-clique conjecture are **not settled**.

### References

1. F. Göbel, J. Orestes Cerdeira, H. J. Veldman, “Label-connected graphs and the gossip problem,” *Discrete Mathematics* 87 (1991), 29–40, [DOI](https://doi.org/10.1016/0012-365X(91)90068-D).
2. R. Labahn, “Kernels of minimum size gossip schemes,” *Discrete Mathematics* 143 (1995), 99–139, [DOI](https://doi.org/10.1016/0012-365X(94)00031-D).
3. D. B. West, “A class of solutions to the gossip problem, part I,” *Discrete Mathematics* 39 (1982), 307–326, [DOI](https://doi.org/10.1016/0012-365X(82)90153-4).
4. D. B. West, “A class of solutions to the gossip problem, part II,” *Discrete Mathematics* 40 (1982), 87–113, [DOI](https://doi.org/10.1016/0012-365X(82)90191-1).
5. D. W. Krumme, “Reordered gossip schemes,” *Discrete Mathematics* 156 (1996), 113–140, [DOI](https://doi.org/10.1016/0012-365X(94)00302-Y).
6. K. K. Williams, “Greedy gossiping,” *Congressus Numerantium* 238 (2026), 113–121, [DOI](https://doi.org/10.61091/cn238-05).
7. A. Casteigts, J. G. Peters, J. Schoeters, “Temporal cliques admit sparse spanners,” *Journal of Computer and System Sciences* 121 (2021), 1–17, [DOI](https://doi.org/10.1016/j.jcss.2021.04.004).
8. J. Baligács, “Temporal Cliques Admit Linear Spanners,” arXiv:2606.05156 (2026), [arXiv](https://arxiv.org/abs/2606.05156).
9. A. Casteigts, “Open questions in temporal graphs,” updated September 22, 2026, [problem list](https://arnaudcasteigts.net/blog/open-problems.html).
