# Original Chronological Half-Forest Restrictions in Shortest Telephone Gossip: A Computer-Assisted Finite Theorem Through Sixteen Participants

**Revised research working paper — 26 October 2026. NOT submitted, externally refereed, proof-assistant verified, or historically certified novel.** This supersedes the smaller numerical scope in [the v2.1 through-15 working draft](../v2.1/PAPER_DRAFT_STAGE4.md); all original source-attribution caveats continue to apply.

## Abstract

Consider a shortest successful, full-information, two-way telephone-gossip schedule among n participants, using exactly 2n-4 pairwise-distinct unordered contacts. We retain its original chronology and split the sequence after n-2 contacts. We establish by finite, independently reproduced computer-assisted verification that **at least one of these two original chronological halves induces a forest for every 4<=n<=16**. The sixteen-vertex boundary requires a new rectangular-component obstruction: any hypothetical both-cyclic schedule must have three prefix and three suffix contact components, rather than a three-by-four or four-by-four intersection pattern. Exhaustive structural reduction then leaves 4,635 cycle-position-aware placements in 81 symmetry classes. Necessary exact and safely optimistic temporal-information profiles exclude 79 classes; the two remaining classes share a single 3-by-3 incidence matrix and are excluded by rigorous eight-vertex local chronology reductions: an unicyclic four-collector rigidity case and a tree two-collector rigidity case. The resulting full verifier independently matches 77 exact local component-domain pairs between two C++ algorithms, checks the exceptional eight-vertex cases using independently implemented Python oracles, reruns all 81 global profile constraints and matches a checked-in complete certificate. The final exclusion ledger contains 13 locally impossible and 68 globally incompatible classes. The statement is finite, relies on explicitly documented mathematical reductions, and does not solve the unbounded half-forest problem or the separate fixed-timestamp temporal-clique 2n-3 sparse-spanner conjecture. Existing gossip-kernel, forest-decomposition and reordering results are recognized as prior art; global historical originality remains unresolved.

## 1. Formal model and result

Each v in V={1,...,n} initially knows exactly secret v. A bidirectional call uv simultaneously replaces the knowledge held at u and v by the union of their two information sets. A schedule is successful if after all calls every vertex knows V. We restrict to distinct unordered contact pairs and shortest sequences E=(e_1,...,e_{2n-4}), where 2n-4 is the classical optimum for n>=4.

Let L=(e_1,...,e_{n-2}) and R=(e_{n-1},...,e_{2n-4}) be the **unchanged consecutive chronological halves**. Each half also defines an undirected static edge graph.

**Theorem 1 (finite original-midpoint half-forest theorem; computer-assisted).** Every shortest successful pairwise-distinct telephone-gossip schedule on 4<=n<=16 has at least one forest among the static graphs of L and R.

Earlier v2.0 and v2.1 reductions establish all orders n<=15 with independent checks. We prove the sixteen-vertex step below. This is not a theorem about a favorable reordering or an arbitrary static edge partition, and not a claim for all n.

## 2. Component incidence and rectangular obstruction

Write P_1,...,P_r for the connected components of L, and Q_1,...,Q_s for those of R, with all isolated vertices counted. Define the incidence grid M_ij=|P_i intersect Q_j|.

**Lemma 2 (standard elementary incidence restrictions).** All M_ij are positive. The respective cycle ranks of L and R are r-2 and s-2.

**Proof.** A secret originating in P_i cannot leave that prefix component before the midpoint. In the suffix it cannot enter a Q_j component without an intersection vertex, so successful dissemination forces M_ij>0. A graph with n vertices, n-2 edges and c components has cycle rank (n-2)-n+c=c-2. QED.

A both-cyclic schedule has r,s>=3 and rs<=n. As previously established, if r=3 and s>=4 then n>=5s-4 because the two prefix tree components each meet all suffix components and can have at most two complete knowledge collectors, so at least s-2 intersections in each tree row have size at least two.

**Lemma 3 (new equality-case obstruction at sixteen).** A shortest successful both-cyclic gossip schedule on n=16 cannot have (r,s)=(3,4), (4,3), or (4,4).

**Proof.** If (r,s)=(3,4), then the bound n>=5s-4 is met **with equality**. Therefore the single cyclic prefix component meets each of the four suffix components in exactly one vertex, while each of the two prefix tree components has exactly two singleton and two double intersections. The suffix has total cycle rank two, hence at least two suffix contact components are trees.

By the single-source tree-entry lemma proved in [the earlier mathematical manuscript](../v2.0/MANUSCRIPT.md), a suffix tree receiving a *singleton* entry from the cyclic prefix component requires a complete prefix collector from each of the two remaining prefix components. If the suffix has at least three trees, either prefix tree would require at least three complete collectors, impossible.

If there are exactly two suffix tree components, then in each prefix tree its two complete collectors are already committed to those two suffix-tree columns. Every singleton intersection forces a complete collector at its sole vertex; consequently the two singleton intersections of each prefix tree must lie in exactly the two suffix-tree columns. The cyclic prefix row also consists entirely of singletons. Each of the two suffix-tree columns therefore meets all **three** prefix components in singleton cells and, under reversed chronology, requires three complete reverse collectors, impossible for a tree. This excludes 3x4. Reverse time to exclude 4x3.

In the 4x4 case positivity and n=16 force all sixteen intersections to be singletons. The prefix has total cycle rank two distributed among four components, hence at least two prefix components are trees. Each such tree meets four suffix components in singleton vertices and thus would require four full collectors instead of at most two. QED.

If both halves cyclic on sixteen vertices, Lemma 2 excludes r>=5 or s>=5 except possible 3x5/5x3, already ruled out by the earlier n>=5s-4 bound (which would require n>=21). Thus:

**Corollary 4.** Every hypothetical n16 both-cyclic chronology has r=s=3, one unicyclic contact component and two trees in *each* half.

The [independent rectangular enumeration](verify_n16_frontier.py) separately checks all 40,950 marked 3x4 placements at n16 using only necessary collector conditions: zero survive both directions of the tree-entry/collector restrictions. The 4x4 obstruction is also cross-checked.

## 3. Exact temporal-information profiles and sound relaxation

For prefix component P_i, suffix component Q_j, and cell X_ij=P_i intersect Q_j, the **prefix sufficiency predicate** B_ij(S) for S subset of X_ij is one precisely when the union of midpoint knowledge of S contains all original P_i secrets.

Run the suffix Q_j contact chronology **in reverse**, with one synthetic destination token initialized at each Q_j vertex. For each eventual destination v, its original-chronology ancestry cell set A_v contains precisely those x in X_ij from which the original suffix can transmit a secret to v. Let D_ji encode all these A_v subsets as required bits.

**Lemma 5 (exact necessary-and-sufficient cell compatibility).** The original suffix delivers *all* original P_i secrets to *all* Q_j destinations exactly when B_ij contains every bit in D_ji:
    
    (B_ij & D_ji) == D_ji .

**Proof.** A given original P_i secret can enter Q_j only through some midpoint cell participant carrying it. Original chronological reachability from such an entry x to destination v is equivalent to reversed-chronology synthetic-token reachability from v to x. Therefore v receives all P_i secrets if and only if its full ancestry subset A_v collectively possesses all of them at the cut. Repeat for all v. QED.

Calls from different prefix components commute, as do calls from different suffix components, because these components are vertex-disjoint. A successful global sequence therefore induces compatible independent component-local histories in every one of the nine grid cells.

The finite solver generates exact local chronology profiles when practical (component size at most seven), and deliberately **optimistic** profiles for large trees and large cyclic components. For a tree's last contact, removing its bridge splits all preceding information into two sides; grant every nonendpoint all its side's secrets and the endpoints all secrets. For an m-contact unicyclic component after its first m-2 calls, at least two connected static components remain; choose any coarsened binary partition of those components, grant each vertex full knowledge of its partition side, and then perform all choices of the final two ordered calls. These grants can only expand real knowledge and thus potential compatibility.

Additionally, the global CSP **does not forbid an unordered pair used in the prefix from appearing again in the suffix**. That is a further relaxation. UNSAT of the enlarged system remains a valid impossibility certificate, but SAT never proves that a real legal gossip schedule exists.

## 4. Complete sixteen-vertex computation

Every positive 3x3 incidence matrix at n=16 is obtained by distributing seven extra participants over nine already occupied cells, producing C(15,8)=6,435 allocations. The verified tree/collector/first-bridge/single-source constraints yield:

| Computational stage | Count |
| --- | ---: |
| Positive 3x3 allocations | 6,435 |
| Eligible placements with marked cycle row/column | 34,092 |
| First-bridge/collector survivors | 16,704 |
| Strengthened tree-entry survivors | 4,635 |
| Marked symmetry classes | **81** |

The two independently written structural enumerators agree on every orbit and multiplicity, not merely these totals. The 81 orbit multiplicities are one class of size 9, three of size 18, twenty-seven of size 36 and fifty of size 72.

Before exact analysis of larger components, the conservative profile solver eliminates 79 classes: thirteen with empty local domains and sixty-six with global incompatible profiles. Exactly two relaxed SAT classes remain, representatives orbits 10 and 11, both having incidence matrix

    [1 1 2]
    [1 1 2]
    [2 2 4]

Their marked cycle positions are respectively (0,0) and (2,2), with multiplicities 36 and 9.

### 4.1 Exact eight-vertex unicyclic rigidity: orbit 11

The cyclic prefix and suffix components each have eight vertices, grouped (2,2,4), and require **both** vertices of each of their first two cells to be fully informed collectors; their remaining four vertices must collectively cover all eight component secrets.

With only six of the eight contacts used, the static contact graph is disconnected, so nobody can yet know all eight secrets. To finish with four full collectors, the final two contacts must involve four distinct endpoints. The first of those contacts already makes two complete, forcing the first six edges to have exactly two connected components and zero cycles: a forest of two trees. Both final contacts cross between the same two pre-existing trees.

In each preforest tree, both future crossing-edge endpoints are complete about that tree's own secrets. Its last internal edge necessarily joins these two collectors. Removing those last internal edges yields **four disjoint collector-rooted branches**. The remaining four vertices collectively cover all eight original secrets, which forces at least one of them into each branch: a branch collector's original secret cannot reach any other remaining vertex across an internal collector bridge after its last use. There are exactly four remaining vertices, hence each branch has just one of them. Thus all four full collectors are globally informed, and each of the other four vertices knows exactly its own original secret and one designated collector secret.

An independently written [complete finite chronology enumeration](exclude_n16_orbit11.py) reconstructs all such cases. The **exact** groupwise forward-sufficiency and reverse-ancestry sets are respectively

    B = {(14,14,32768)}
    D = {(8,8,278)}.

For their shared size-four cell, the prefix B permits only the **full set of four** entry vertices (bit 32768), while the suffix D requires four distinct singleton ancestry subsets (bits 1,2,4,8; encoded as 278). Since 32768 & 278 is not 278, the necessary information-transfer compatibility condition fails. **Orbit 11 is impossible**, without relying on optimistic cyclic profiles or a global chronological solver.

### 4.2 Exact eight-vertex two-collector tree rigidity: orbit 10

In orbit 10, the critical large prefix and suffix components are instead trees on eight vertices. Both have group sizes (2,2,4) and two mandatory complete collectors in the *middle* size-two group. Their last internal edge joins those collectors; removing it yields two information-isolated sides.

Their *first* size-two group contains two other vertices. To collectively cover all eight original secrets, one must lie on each side and must know **all its side's secrets** before the final bridge. Each prebridge side tree consequently has two complete collectors (one from the first group, one from the middle group); the last internal edge of that side joins these collectors. This creates four branches, each requiring a distinct participant from the remaining size-four group to collectively cover the original component secrets. Consequently every such branch consists of one collector and one remaining vertex.

The independent [exact tree chronology enumerator](exclude_n16_orbit10.py) exhausts admissible side partitions and all chronological tree orders; 48 valid decompositions reduce to the exact domain sets

    B = {(8,14,32768)}
    D = {(6,8,278)}.

Once again the shared four-vertex cell has incompatible B and D masks (32768 & 278 != 278), ruling out the orbit under even the relaxed global model. **Orbit 10 is impossible**.

### 4.3 Full certificate

After replacing the two optimistic eight-vertex local domains with these separately obtained exact domains, the independent global CSP excludes **all 81** marked classes, covering **4,635/4,635** placements.

| Final exclusion type | Classes |
| --- | ---: |
| Empty necessary local domain | 13 |
| Globally incompatible information profiles | 68 |
| **All structurally surviving classes** | **81** |

The full [machine-readable N16_CERTIFICATE.json](N16_CERTIFICATE.json) lists all 81 marked matrices, their multiplicities, original relaxed outcomes, final categories and component-domain cardinalities.

For every exact local component type used at n16, the primary C++ chronology enumerator is independently compared to a separate C++ union-find/two-final-contact enumerator without history-state memoization. **All 77 distinct exact B/D component-domain pairs match.** The exceptional larger component types use independently implemented Python exhaustive side-chronology enumerators, not a fabricated "exact" assignment by the original optimistic C++ source.

**Proof of Theorem 1 at n=16.** Assume a successful 28-call distinct-contact chronology has cycles in both original halves. Lemmas 2–3 confine its component intersection system to a marked positive 3x3 grid. Every such grid is represented in the exhaustive structural enumeration, and the necessary collector and bridge constraints leave only the 81 marked symmetry classes with total multiplicity 4,635. Any legal local component chronology appears in an enumerated exact domain or is dominated by an allowed optimistic profile; any legal global chronology satisfies the nine-cell compatibility constraints of Lemma 5. The independent exhaustive finite checks exclude every one of the 81 cases, using the exact eight-vertex rigidity lemmas for the two cases that had survived optimism. Therefore no such both-cyclic schedule exists. The previously certified result through n=15 gives the stated n<=16 conclusion. QED.

The proof has mathematical lemmas and **finite computations** as dependencies; it has not been checked in Lean, Coq or Isabelle.

## 5. Reproducibility

All code and generated evidence is committed with the working paper in PR #1.

Run from repository root:

    python3 research/v2.2/verify_n16_frontier.py
    python3 research/v2.2/exclude_n16_orbit11.py
    python3 research/v2.2/exclude_n16_orbit10.py
    python3 research/v2.2/verify_kernel_scope.py
    python3 research/v2.2/prove_n16.py

The full verification script checks all 81 marked orbits, independently reconstructs all 77 exact local profile domain sets in C++, independently recomputes the two special exact eight-vertex sets in Python, reruns every global CSP with a separate Python implementation and requires its entire freshly computed certificate to equal the committed JSON.

Original full certificate execution: [GitHub Actions run 40378654998](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40378654998), **SUCCESS**, independent 77/77 domain comparison, 81/81 UNSAT and 4,635/4,635 placements excluded. The artifact-integrity-enhanced rerun is tracked separately by the updated workflow.

The primary source SHA-256 for this executed run was 3bf98d2fdd4e877c2442bbd751755af906d37a96b6b16698416e149e5939fc18. The exported primary/secondary local domain logs have respective SHA-256 fingerprints 0accd52bb8a6fc36e21bf9ca7acb26ee55dd3a8701b2971416046fc4d62fedaa and 2dbe8f93e38177339d6aa90d264d17c2f1a567d56a5da87304c68fc941d06bb1.

## 6. Historical position, limitations, and conclusion

Minimum 2n-4 telephone-gossip bounds, classical four-cycle structure, static Cd-graph/two-forest decompositions, event-kernel classifications, permissible kernel permutations, linear extensions and contact reordering are already covered by Göbel–Cerdeira–Veldman (1991), West (1982), Labahn (1995), Krumme (1996) and related work. Williams (2026) also explicitly analyzes the first n-2 calls in a *different* total-knowledge optimization setting. None of those methods should be claimed as newly invented here.

An [independent same-poset verification](verify_kernel_scope.py) checks 51,200 linear extensions of one n8 optimal contact-event order and constructs n8–n16 pairs with the same full contact poset but different individual chronological half cycle ranks. This confirms that the **given original midpoint statistic** is not determined by the underlying poset alone. Both witness members nevertheless have an acyclic half; the observation **does not prove that Theorem 1 is mathematically independent of all consequences of Labahn's complete kernel classification**. No such global priority certificate has been obtained.

A separately fixed-time-labelled temporal clique spanner seeks a sparse subset preserving all temporal reachabilities under adversarial labels; it is not the same problem as an optimal telephone-gossip schedule. Neither the 2n-3 spanner conjecture nor the half-forest statement for n>=17 follows from this work.

The defensible result is an **explicit, reproducible and bounded n<=16 computational classification** with original-order quantification. Historical novelty, broad mathematical significance, formal proof-assistant verification and external review remain distinct open gates. This document is an unsubmitted research working manuscript, not a claim of journal readiness.

## Selected primary references

1. F. Göbel, J. O. Cerdeira, H. J. Veldman, “Label-connected graphs and the gossip problem,” Discrete Mathematics 87 (1991), 29–40. DOI https://doi.org/10.1016/0012-365X(91)90068-D
2. R. Labahn, “Kernels of minimum size gossip schemes,” Discrete Mathematics 143 (1995), 99–139. DOI https://doi.org/10.1016/0012-365X(94)00031-D
3. D. W. Krumme, “Reordered gossip schemes,” Discrete Mathematics 156 (1996), 113–140. DOI https://doi.org/10.1016/0012-365X(94)00302-Y
4. D. B. West, “A class of solutions to the gossip problem,” Parts I and II, Discrete Mathematics 39–40 (1982).
5. K. Williams, “Greedy gossiping,” Congressus Numerantium 238 (2026), 113–121. DOI https://doi.org/10.61091/cn238-05
6. A. Casteigts, J. Peters, J. Schoeters, “Temporal cliques admit sparse spanners,” Journal of Computer and System Sciences 121 (2021), 1–17. DOI https://doi.org/10.1016/j.jcss.2021.04.004
7. J. Baligács, “Temporal Cliques Admit Linear Spanners,” arXiv:2606.05156 (2026). https://arxiv.org/abs/2606.05156
8. A. Casteigts, “Open questions in temporal graphs,” project page updated September 22, 2026. https://arnaudcasteigts.net/blog/open-problems.html


### Additional sixteen-vertex historical title disambiguation

A separate prior-art check found Labahn and Pietsch, *Characterizing Minimum Gossip Graphs on 16 Vertices* (University of Bonn Report 91707; archival manuscript dated 12 October 1993, independently indexed as a 1991 report). Despite the close title and equal vertex count, that work studies **minimum-link graphs achieving the minimum number of synchronous communication rounds**, namely four rounds on sixteen vertices (eight simultaneous calls per round, 32 call occurrences). This differs from our **28-call minimum-total-contacts** problem and its original fourteen/fourteen chronological cut. Accordingly we acknowledge this result but **do not assert direct theorem equivalence or complete historical nonimplication**. See [focused source and model audit](PRIOR_ART_N16_UPDATE.md), [Bonn catalogue](https://www.or.uni-bonn.de/publications.de.html) and [manuscript facsimile](https://www.researchgate.net/publication/2297002_Characterizing_Minimum_Gossip_Graphs_on_16_Vertices).
