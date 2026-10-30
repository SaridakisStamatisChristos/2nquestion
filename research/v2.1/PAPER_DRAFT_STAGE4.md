# Chronological Half-Forest Restrictions in Minimum Telephone Gossip: A Computer-Assisted Classification Through Fifteen Participants

**Revised Stage-4 research working paper, 26 October 2026. Not submitted, not peer reviewed, and not cleared for a historical novelty claim.**

## Abstract

We examine minimum-call telephone-gossip schedules on n participants, each participant initially holding a distinct secret and each call merging the information of its two endpoints. A successful shortest schedule has 2n-4 contacts for n at least four. We consider schedules with pairwise distinct unordered contacts and partition the **unchanged original chronological sequence** after n-2 calls. We give a computer-assisted finite classification establishing that for 4 <= n <= 15, at least one of these two chronological halves induces an acyclic graph. At n=15, a necessary-condition enumeration reduces 13,680 eligible cycle placements to 945 survivors in exactly twenty cycle-position-aware symmetry orbits. Six orbits have empty exact local chronology domains, ten have globally incompatible exact temporal-information profiles, and four remain incompatible after optimistic large-tree information relaxations. The complete exact information-profile domains of all 33 required component types, including two cyclic seven-vertex types, agree between two differently implemented C++ enumeration programs. Independently implemented Python programs check the structural reduction, the global compatibility decisions and targeted chronology assumptions. The work gives an explicitly reproducible **bounded classification** for original chronology. Classical minimum-gossip kernels, static forest decompositions, contact commutation and reordering theorems are fully acknowledged. Whether the finite result is an implicit consequence of the entire historical kernel classification remains unresolved; no universal theorem for arbitrary n or improvement of fixed-timestamp temporal-clique spanner bounds is claimed.

## 1. Model, scope, and theorem

Let V={1,...,n} and let E=(e_1,...,e_{2n-4}) be an ordered sequence of pairwise-distinct unordered pairs of participants. Initially participant v knows secret v. At time t, if e_t={u,v}, both participants replace their secret sets by their union. The schedule is successful when every vertex knows all n secrets after its final contact. We define L as its **first n-2 original contacts** and R as its **last n-2 original contacts**; no reordering, commuting or repartitioning of edges is permitted in the assertion.

**Theorem 1 (finite original-midpoint half-forest property).** For each 4 <= n <= 15, every successful shortest pairwise-distinct two-way telephone-gossip schedule has at least one half, L or R, whose underlying static contact graph is a forest.

This is a **finite computer-assisted result**. For n<=14 we rely on the prior independently tested mathematical reduction and finite certificates in research/v2.0; the n15 case is proved by the finite calculation described here. The classical two-contact vertex extension from Göbel, Cerdeira and Veldman (1991) also propagates a hypothetical smaller counterexample to a larger one while preserving the cycle rank of its corresponding halves. We do not claim the extension, gossip lower bound or basic information-flow model as inventions.

## 2. Midpoint intersection structure

Let P_1,...,P_r be connected components of the static first-half graph and Q_1,...,Q_s those of the second-half graph, including isolated vertices. Put M_ij=|P_i intersect Q_j|.

**Lemma 2.** In every successful schedule all M_ij are positive. The cycle ranks of the first and second halves are respectively r-2 and s-2.

**Proof.** Secrets originating in P_i cannot leave P_i during the first half. After the split, they cannot enter Q_j unless some vertex lies in both. Each vertex must eventually learn all secrets, so every intersection is nonempty and rs<=n. A graph on n vertices with n-2 edges and c components has cycle rank (n-2)-n+c=c-2. QED.

Both halves cyclic therefore implies r,s>=3. If r=3, the first half has one unicyclic component and two tree components. Each tree component meets every suffix component.

**Lemma 3 (rectangular collector bound).** If r=3 and s>=4 in a both-cyclic successful schedule, then n >= 5s-4. The time-reversed dual also holds.

**Proof.** In a tree component only the endpoints of the last call can possibly know every original secret of the component: that edge bridges two sides with no earlier crossing contact. A singleton intersection with a suffix component demands one complete collector at its unique vertex. A tree row meeting all s suffix components can therefore have singleton cells in at most two columns. Each of the two tree rows contributes at least s-2 additional vertices beyond its s mandatory cell occupants. Thus n >= 3s+2(s-2)=5s-4. Reverse all contacts for the dual. QED.

**Corollary 4.** For n<=15, a both-cyclic shortest successful schedule necessarily has exactly r=s=3, with one cyclic row and one cyclic column.

**Proof.** Since r,s>=3 and rs<=15, at least one equals 3. If the other were at least 4, Lemma 3 would require at least 16 vertices. QED.

The positive 3-by-3 matrix M records the sizes of all nine intersections. The location of each unicyclic component is recorded separately by an index (cyclic row, cyclic column).

We rely on additional previously proved necessary information-flow conditions: each cell collectively covers all original secrets of its prefix component; singleton cells in trees force complete information collectors; two singleton entries in a suffix tree force an earliest bridge and demand third-row secrets on both of its sides; a singleton entry into a suffix tree forces another prefix row's *complete* collector to enter that suffix tree, with a reversed-time dual. These rules are documented with mathematical proofs in research/v2.0/MANUSCRIPT.md. They are explicitly imported assumptions of the finite reduction, not discoveries generated by the verifier.

## 3. Exact component information profiles

Fix a prefix row P, suffix column Q and their intersection X. For any subset S of X, define the prefix-sufficiency predicate

    B(S)=1 if and only if the union of the midpoint knowledge at S contains every original secret of P.

For the suffix column Q, execute its contacts in **reverse order** beginning with a distinct synthetic token at every vertex of Q. Let T(x) be the set of reverse tokens reaching each x in X. For each final suffix destination v in Q define A_v={x in X: v in T(x)}.

**Lemma 5 (exact profile equivalence).** The original suffix sends every original P secret to every vertex of Q if and only if B(A_v)=1 for all v in Q.

**Proof.** Fix one original P secret and one suffix destination v. That secret enters Q after the midpoint only through a vertex x in X already carrying it. It can reach v using original suffix contacts precisely if those contacts admit a forward chronological path from x to v, equivalently a reversed chronological path from v to x. The artificial token from v therefore reaches x if and only if x could deliver its midpoint secrets to v in the original suffix. Taking the union over all eligible entry vertices gives the predicate B(A_v). Requiring it at every destination proves the claim. QED.

Represent B as bits indexed by subsets of X which are sufficient, and D as bits marking all required ancestry subsets A_v. The condition is the Boolean subset-mask inclusion **(B AND D) = D**.

Within either half, calls from different contact components are on disjoint vertex sets and commute. Any global schedule therefore induces one local chronology/profile for each prefix row and each suffix column. It induces a satisfying choice in the nine-cell compatibility system based on Lemma 5.

**Deliberate relaxation.** The global system permits reusing the same unordered edge across the two halves. Real distinct-edge schedules form a subset of this relaxation, so UNSAT for the relaxed system proves UNSAT for the original. A relaxed SAT assignment is not a legal full schedule without additional verification.

## 4. Exact local chronology domains and optimistic trees

A tree on h vertices contains h-1 distinct internal calls and a unicyclic component contains h calls. For all relevant exact local components of up to seven vertices, the primary C++ source enumerates chronological contact sequences, checks connectedness, mandatory full collectors in designated cells, and collective secret coverage of each cell. Each accepted terminal state contributes an exact forward sufficiency profile and a reversed ancestry profile.

A second C++17 implementation, developed for the Stage-3 audit, uses **incremental union-find and cycle-rank accounting** and explicitly enumerates the final two contacts without the original source's used-edge/knowledge-state memoization. The implementations produce *identical sets of B and D profiles for each of 33 exact component types*, including both seven-vertex cyclic types. Source files and complete CI evidence appear in Section 6.

To avoid unsupported exact enumeration for larger trees, we use a sound **overapproximation**. Suppose a tree's two mandated full collectors lie in distinct intersection cells. The endpoints x and y of the tree's final contact must be those collectors. Removing their connecting edge splits the preceding contacts into two disjoint information sides A containing x and C containing y. At the midpoint, only x and y could have collected all component secrets; every other vertex can hold only original secrets from its own side. Therefore it is optimistic but safe to grant both endpoints *all* original component secrets and every other vertex all secrets of its own side. Enumerating every feasible x,y and every possible side bipartition pointwise dominates the real knowledge vectors.

The sufficiency predicate is monotone under knowledge enlargement; in the reversed suffix analogue, artificially enlarged reverse-token knowledge enlarges the set of potential ancestors and cannot make the necessary propagation condition harder to satisfy. Consequently **UNSAT using the optimistic domains remains a valid impossibility certificate**. This does not imply that optimistic profile assignments correspond to actual chronological trees.

## 5. Fifteen-vertex classification and proof

Positive matrices M contain nine mandatory entries and six additional vertices. There are **C(14,6)=3,003** positive allocations. Exhausting cycle-row and cycle-column locations and applying the necessary collector and bridge constraints gives:

| Reduction step | Placements remaining |
| --- | ---: |
| Eligible positive incidence/cycle placements | 13,680 |
| Earlier first-bridge/collector necessary conditions | 4,662 |
| Single-source-entry strengthened necessary conditions | 945 |
| Orbits under marked row/column relabeling and time reversal | **20** |

Two independently implemented Python enumeration strategies agree not only on these counts but also on the complete orbit-multiplicity map. All twenty orbit representatives are independently checked for the existence of a relaxed globally compatible collection of temporal-information profiles.

| Case resolution | Symmetry classes |
| --- | ---: |
| Exact local component chronology domain empty | **6** |
| Global CSP infeasible with exact component domains | **10** |
| Global CSP infeasible even with optimistic large-tree domains | **4** |
| **Total** | **20** |

The individual canonical matrices, marked cyclic row and column, orbit multiplicities, exact-domain sizes, optimistic flags and outcomes are part of the committed **N15_CERTIFICATE.json**. The multiplicities sum to exactly **945**. The interrupted, unverified historical manuscript's proposed 7/10/3 breakdown is superseded by the executed **6/10/4** record.

A decisive seven-vertex cyclic component with cell sizes (2,2,3) and required full collectors (2,2,0) has **zero** admissible profiles in both implementations. The alternative cyclic seven-vertex type (2,3,2), collector requirements (2,1,0), has **9** forward sufficiency profiles and **27** reversed ancestry profiles in both. The second enumerator visited 5,287,680 and 61,229,520 corresponding terminal chronological configurations respectively, rather than relying on the primary history-state quotient. These counts describe the independently implemented search, not a novel complexity bound.

**Proof of Theorem 1 for n=15.** Assume a successful sequence of 26 distinct contacts on fifteen participants has cycles in both original chronological halves. Lemmas 2 and 3 force a marked positive 3-by-3 incidence system. Every such system occurs in the exhaustive structural allocation enumeration. Necessary first-bridge and singleton-collector rules reduce the possible configurations to the 945 placements represented by the twenty marked symmetry classes. Every real chronology induces admissible exact local profiles or profiles dominated by the sound optimistic-tree construction, and induces a compatible global assignment according to Lemma 5. The finite searches explicitly exclude compatible assignments in every class, including in the relaxed edge-reuse model. This contradicts the hypothetical both-cyclic schedule. Together with the previously independently verified n<=14 cases and the classical two-contact extension, the bounded theorem follows. QED.

This proof depends on exhaustive finite code and mathematical reduction lemmas. It is a **computer-assisted finite verification**, not proof-assistant formal certification.

## 6. Reproducibility

The complete proof package is in the draft research branch of the same repository. From its root execute:

    python3 research/v2.1/prove_n15.py
    python3 research/v2.1/stage3_adversarial_check.py
    python3 research/v2.1/stage3_exhaustive_stress.py

The first command recompiles the primary C++17 component oracle, checks the independent structural reduction, evaluates all twenty compatibility cases and validates the machine-readable certificate. The second rebuilds both C++17 implementations from checked-in source, asserts exact equality of all **33** relevant B and D domain sets, substitutes the independently enumerated exact domains into the global search and confirms all **20** UNSAT orbits. The third independently examines 360,360 five-edge candidate tree orders on six vertices, complete shorter tree/unicyclic cases and 8,272 time-reversal reachability comparisons on four vertices.

On the Stage-3 source-check head cf683be1eac7d0d51c843a509fcb18b3436d3b10, the independent audit passed in [GitHub CI run 40357841017](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40357841017), and the primary n15 certificate passed in [run 40357840881](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40357840881). The full [Stage 3 mathematical audit](STAGE3_ADVERSARIAL_AUDIT.md) records implementation differences and residual assumptions. Timeout, disagreement or SAT of the relaxed CSP must cause a failed verifier, never an UNSAT assertion.

## 7. Priority and relation to existing results

The optimal 2n-4 gossip bound and four-cycle restrictions are classical. Göbel, Cerdeira and Veldman (1991) prove structural properties of minimum supporting static graphs and the two-contact extension. Labahn (1995) characterizes minimum kernel partial orders, permutation conditions, isomorphism and linear extensions. Krumme (1996) proves that *some favorable rearrangement* is available and develops related static forest decompositions. West (1982) studies ordered gossip under the more restrictive NOHO hypothesis. Williams (2026, circulated as a 2025 preprint) studies the first n-2 contacts and commuting disjoint calls for the **different problem** of optimizing total information with fewer than 2n-4 calls.

The original fixed-half universal quantifier is not the same as existence of a good reordered schedule or static forest partition. Existing verified same-contact-order examples show that midpoint cycle ranks may change under commutation; such examples **do not establish independence** of our weaker at-least-one-forest assertion from Labahn's or Krumme's complete classification. The prior theorem-by-theorem comparison in research/v1.8 inspected complete copies of their originals, and [Stage 4 priority audit](STAGE4_PRIORITY_AND_PUBLICATION_AUDIT.md) identifies the remaining implication gap. We did not find the exact explicit finite original-midpoint n15 statement in the investigated sources, but **it might follow implicitly from older kernel theory**. Scholarly originality is consequently *unresolved*, not certified.

The **fixed-timestamp temporal clique 2n-3 spanner problem** is fundamentally different: a label-order of all clique edges is adversarially given and the task is to find a small selected set preserving temporal reachability. The available 2026 linear bound 7n (Baligács) and the still-open 2n-3 target (Casteigts's September 2026 problem list) are not improved by the gossip half-forest classification.

## 8. Limitations and submission disposition

The proof is bounded to n<=15. The rectangular-grid argument no longer reduces all possible both-cyclic configurations to 3-by-3 at n>=16. Our exact local C++ oracles are genuinely independent as algorithms but share the explicitly defined information-exchange semantics; the optimistic large-tree domain generator is justified by its proof and adversarial tests rather than a second exact large-tree enumerator. Neither the mathematical reduction nor the programs has been checked by Lean/Coq/Isabelle or independently peer-reviewed.

The bounded claim and computational artifact can support a research working paper or discussion with specialists, but the broader mathematical significance and priority against the complete Labahn/Krumme kernel consequences have not been closed. This version **is not a submission-ready claim of original general mathematics**, and a journal-acceptance prediction would not be evidence.

## References

1. F. Göbel, J. O. Cerdeira and H. J. Veldman, "Label-connected graphs and the gossip problem", Discrete Mathematics 87 (1991), 29-40. DOI: https://doi.org/10.1016/0012-365X(91)90068-D
2. R. Labahn, "Kernels of minimum size gossip schemes", Discrete Mathematics 143 (1995), 99-139. DOI: https://doi.org/10.1016/0012-365X(94)00031-D
3. D. W. Krumme, "Reordered gossip schemes", Discrete Mathematics 156 (1996), 113-140. DOI: https://doi.org/10.1016/0012-365X(94)00302-Y
4. D. B. West, "A class of solutions to the gossip problem", Parts I and II, Discrete Mathematics 39 (1982), 307-326 and 40 (1982), 87-113.
5. R. Labahn, "Some minimum gossip graphs", Networks 23 (1993), 333-341. DOI: https://doi.org/10.1002/net.3230230416
6. K. Williams, "Greedy gossiping", Congressus Numerantium 238 (2026), 113-121. DOI: https://doi.org/10.61091/cn238-05 ; arXiv:2506.17804.
7. A. Casteigts, J. Peters and J. Schoeters, "Temporal cliques admit sparse spanners", Journal of Computer and System Sciences 121 (2021), 1-17. DOI: https://doi.org/10.1016/j.jcss.2021.04.004
8. J. Baligács, "Temporal Cliques Admit Linear Spanners", arXiv:2606.05156 (2026). https://arxiv.org/abs/2606.05156
9. A. Casteigts, "Open questions in temporal graphs", updated September 22, 2026. https://arnaudcasteigts.net/blog/open-problems.html
