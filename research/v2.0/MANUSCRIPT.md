# Chronological Half-Forest Restrictions in Optimal Telephone Gossip

## A Single-Source Entry Lemma and a Finite Certificate Through Fourteen Participants

**Working mathematical research manuscript — October 25, 2026. Not submitted, not externally peer reviewed. Author metadata to be confirmed.**

### Abstract

For successful, minimum-size two-way telephone-gossip schedules with exactly \(2n-4\) **pairwise-distinct** undirected calls, we consider the **original chronology**, split after \(n-2\) calls. We prove a single-source tree-entry lemma: if a suffix-tree component meets one prefix component in a singleton, every other prefix component must supply a complete collector in its intersection with that tree. This eliminates the formerly exceptional \(n=13\) grid using only finite incidence counting, without exhaustive chronological order enumeration. At \(n=14\), the lemma reduces 738 surviving cycle placements to 81 and then, under row/column permutation and time reversal, to exactly three symmetry orbits. A finite complete local-order certificate excludes all three orbits; one requires a separately checked incompatibility of 48 prefix and 288 suffix local orders. Thus **every successful schedule on \(4\le n\le14\)** has at least one **original chronological half** inducing a forest. The classical two-contact extension yields the result for smaller sizes. We distinguish the statement from static forest decompositions and existential reordering results, without claiming a universal \(n\)-theorem or an improvement to fixed-label temporal-clique spanners. No verbatim match was located in the audited classic originals, but global historical priority remains unestablished.

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


### 3A. Cellwise coverage and the single-source entry lemma

**Lemma 6 (Cellwise coverage).** For each pair of prefix and suffix components \((P_i,Q_j)\), the union of the midpoint knowledge sets of vertices in \(P_i\cap Q_j\) contains *all* original \(P_i\)-secrets.

*Proof.* Once the prefix ends, a secret originating in \(P_i\) can reach \(Q_j\) only from vertices already in the intersection: subsequent calls never leave \(Q_j\), and no other prefix component possesses the original secret at the cut. Since everyone must ultimately know the secret, some intersection vertex must possess it. ∎

**Lemma 7 (Single-source tree entry).** Suppose a suffix contact component \(Q\) is a tree and \(Q\cap P_a=\{x\}\) for a prefix component \(P_a\). For every *different* prefix component \(P_b\), at least one participant in \(P_b\cap Q\) must already know all original \(P_b\)-secrets at the midpoint. The fully time-reversed statement holds for prefix trees.

*Proof.* Choose one original \(P_a\)-secret \(\alpha\). At the midpoint, \(x\) is the unique vertex of \(Q\) holding \(\alpha\). Each edge of the suffix tree must be used at the moment it conveys \(\alpha\) from a previously informed endpoint to a previously uninformed one: using an edge before either endpoint has \(\alpha\) would permanently block \(\alpha\) from crossing that tree cut, and both endpoints cannot have acquired \(\alpha\) earlier without already crossing the same unique edge. Consequently the suffix contacts grow a connected \(\alpha\)-informed subtree rooted at \(x\); no vertex can have participated in an earlier suffix contact before first receiving \(\alpha\).

Let \(y\) be the first vertex of \(P_b\cap Q\) to receive \(\alpha\), through contact \(zy\) with the informed subtree. The informed side initially contains no vertex from \(P_b\), hence no \(P_b\)-secret, and \(y\) has not participated in earlier suffix calls. The used edge \(zy\) is the unique bridge between its two tree sides. For every original \(P_b\)-secret to reach **both** sides, \(y\) must transmit that secret at contact \(zy\), meaning \(y\) already knows it at the midpoint. Thus \(y\) is a complete prefix collector. Reversing the entire successful gossip schedule proves the dual. ∎

**Consequence for the \(n=13\) proof.** Each surviving configuration under the earlier first-bridge/collector filter belongs to the square incidence grid
\[
\begin{pmatrix}2&2&1\\2&2&1\\1&1&1\end{pmatrix}
\]
with the last row and column cyclic. Both of the first two prefix rows are five-vertex trees and must each have a complete collector in the last-column singleton. Each of the first two suffix columns is a tree with a singleton entry from the last prefix row. By Lemma 7, each of those same prefix trees must provide an **additional** complete collector in each of those two columns. This requires **three distinct collectors in a tree**, impossible by Lemma 2. Thus the previously necessary 576-by-3000 residual chronology enumeration is no longer needed for this finite case. The 495 incidence allocations and 16 symmetry classes remain part of the complete finite grid reduction; the scripts enumerate these exactly.

### 4. Exact fourteen-participant theorem

**Theorem 8 (Computer-assisted).** Every successful 24-contact minimum telephone-gossip schedule on \(n=14\) participants, with pairwise-distinct undirected contacts, contains a forest among its first twelve or last twelve **original** calls.

*Proof.* If both chronological halves are cyclic, Corollary 5 yields \(r=s=3\); each half contains exactly one unicyclic component. Distributing five extra participants among nine positive intersection cells produces \(\binom{13}{5}=1287\) multiset incidence matrices. For each possible cyclic-row/cyclic-column placement, apply the original tree-collector and two-singleton first-bridge restrictions. There are **4698** eligible placements and **738** survivors. Applying Lemma 7 and its time-reversed dual further reduces the 738 to **81** placements. Under independent row and column relabeling and transposition (time reversal), the 81 placements form precisely **three** cycle-position-aware orbits:

| Orbit | Representative incidence matrix | Cyclic row/column | Placements |
|---|---|---|---:|
| A | \(\left(\begin{smallmatrix}1&1&2\\1&1&2\\2&2&2\end{smallmatrix}\right)\) | \((0,0)\) | 36 |
| B | Same matrix | \((2,2)\) | 9 |
| C | \(\left(\begin{smallmatrix}1&1&2\\1&2&2\\2&2&1\end{smallmatrix}\right)\) | \((2,2)\) | 36 |

The symmetry group also transforms the position of each cycle; quotienting only the matrix would be insufficient.

For A, the third prefix component is a tree on six vertices, partitioned across suffix components into cells of sizes \((2,2,2)\). Both vertices in its middle cell are necessarily complete collectors, and **each** cell must collectively possess every original prefix-component secret by Lemma 6. Enumerating *all* \(15P5=360360\) ordered distinct five-edge sequences gives 155520 connected choices, 4992 with cellwise coverage, 2880 with the required collector locations, and **zero satisfying both**.

For B, the third prefix component is unicyclic with six vertices and six calls; it must have complete collectors at all four vertices of its first and middle size-two cells while each of the three size-two cells collectively covers every original component secret. Enumerating all \(15P6=3603600\) ordered distinct six-edge sequences gives 2635200 connected choices, 369312 satisfying cell coverage, 1728 satisfying collector locations, and **zero satisfying both**.

For C, consider *only* the five-vertex prefix-tree component in the middle row and the five-vertex suffix-unicyclic component in the last column. Necessary complete collector and cell-coverage conditions leave exactly **48** connected local prefix orders and **288** connected local suffix orders (the latter checked under **reversed suffix chronology** for reverse collectors). Across all **13824** pairs, no pair transmits every original middle-row secret to each participant of the last suffix column: there are **zero** duplicate-edge conflicts and **13824** information-flow failures. The C++ verifier independently reproduces the Python result. These conditions are all necessary in every successful global schedule, so every orbit is impossible. ∎

**Corollary 9 (Through fourteen participants).** For every \(4\le n\le14\), every successful shortest pairwise-distinct two-way gossip schedule has a forest in at least one original chronological half.

*Proof.* The \(n=14\) result is Theorem 8. The classical two-contact vertex extension of Göbel–Cerdeira–Veldman (1991, Theorem 13) prepends a contact from a new participant to an old participant and appends a contact to a *different* old participant. All-to-all gossip remains successful, and the new first/last contact in each corresponding half is a leaf attachment, preserving both cyclomatic ranks. A hypothetical smaller both-cyclic schedule would therefore extend to a both-cyclic fourteen-participant schedule, contradicting Theorem 8. ∎

### 5. Reproducibility and boundary

Deterministic certificate files are in \`research/v2.0/\`: \`half_forest14_grid.py\` checks all incidences and orbit multiplicities; \`local_component_exact.cpp\` checks all six-vertex contact orders for A and B; \`n14_final_cross.py\` exhaustively checks the remaining pair for C; and \`independent_cross_check.cpp\` independently implements the last check in C++. \`verify_n14.py\` runs the complete finite certificate. Its GitHub Actions job compiles the C++17 code and runs each exact check from committed sources.

The general \(n\ge15\) half-forest conjecture remains **OPEN**. The temporal-clique fixed-order \(2n-3\) spanner conjecture is a different problem and is not solved. Although the two full historical papers were inspected in v1.8 and no matching fixed-half theorem was explicitly found, the possibility of a previously implicit corollary remains; priority should therefore be described as **unresolved**, not certified first-ever.

### 6. Related work and novelty boundaries

West [3,4] classifies the special NOHO optimal schemes under extra assumptions; Göbel, Cerdeira, and Veldman [1] characterize statically label-connected graphs attaining \(2n-4\) edges and give the two-contact vertex extension. Labahn [2], notably his Theorem 6.1, completely characterizes p-grid kernel admissibility and studies linear extensions. Krumme [5] proves reordering theorems and static structural decompositions. A recent study by Williams [6] uses the first n−2 contacts and swaps of disjoint consecutive calls. Those classical and recent ingredients are **prior art**, not advertised as new here.

An existence theorem for *some* static partition into two forests does not assert that the original first and last n−2 contacts are each forests. Likewise a theorem constructing *some reordered successful schedule* does not by itself decide a fixed-original-midpoint statement. The n=8 witness in \`research/v1.6/\` concretely separates these properties. It does **not** show that stronger historical structural results could not imply Theorem 6 as a corollary.

The original Labahn and Krumme articles were provided and examined directly in v1.8. No exact explicit statement of the first-bridge k=1/2/3 rule or the n=13 fixed-original-half theorem was identified there, but the absence of a verbatim statement is **not** a proof of priority across all historical work or of non-derivability from older classifications.

The fixed-time-label temporal-clique spanner problem is distinct. Casteigts, Peters, and Schoeters [7] established sparse temporal-clique spanners, and Baligács [8] established a universal linear 7n bound in 2026; the proposed universal 2n−3 bound remains listed as open [9]. Our gossip result does **not** prove it or imply an improvement.

### 7. Conclusion and limitations

The finite original-chronology half-forest theorem is now certified through fourteen participants rather than thirteen, including an independently proved single-source entry lemma and two separately implemented chronology checks. The thirteen-participant case no longer requires exhaustive component contact-order enumeration. The n=14 certificate is finite and computational; external mathematician review and global originality investigation remain warranted. No universal claim for n≥15 and no temporal-clique spanner solution is made.

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
