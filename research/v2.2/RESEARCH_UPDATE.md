# v2.2 — sixteen-participant original-half forest extension

**Research date: 26 October 2026.** Target: a complete, independently reproducible finite exclusion of shortest both-cyclic original-half gossip schedules on 16 vertices. The main fixed-timestamp temporal-clique spanner conjecture and mathematical historical originality remain open.

## 1. The theorem being investigated

For n=16, every successful 28-call pairwise-distinct undirected full-information telephone-gossip schedule has a forest among its **first fourteen or last fourteen original chronological contacts**. This is not a rearrangement theorem or a static forest edge-partition statement.

**Computer-assisted n16 finite theorem: CI PASS.** The full script has now executed and independently compared every relevant exact local profile domain. The statement depends on the explicitly stated mathematical reduction lemmas and executable finite search; it has not been proof-assistant formalized or externally refereed.

## 2. New rectangular structural obstruction

Let r,s denote the respective numbers of contact components in the two halves. The static cycle ranks are r-2,s-2, and every prefix/suffix component pair intersects.

For both halves cyclic, r,s >=3 and rs<=16. If one side has three components and the other has five or more, the previously proved bound n>=5s-4 excludes n=16. Thus the only new candidate shapes beyond 3x3 are 3x4, 4x3 and 4x4.

**Proposition A (3x4 cannot occur at n=16).** Suppose the prefix has three components, exactly one unicyclic and two trees, and the suffix has four components with total cycle rank two. The positive intersection grid has twelve mandatory occupants and only four additional vertices. Each prefix tree row has at most two complete collectors and thus must have exactly two singleton cells and two size-two cells; the cyclic row is singleton in all four columns. The suffix has at least two tree components (its total cycle rank is two).

For every suffix tree column, the singleton entry from the cyclic prefix row triggers the single-source tree-entry lemma: **each** of the two prefix tree rows must have a complete collector in its intersection with that column. If there are three or more suffix trees, a prefix tree requires at least three complete collectors, impossible. If there are exactly two suffix trees, the two complete collectors of *each* prefix tree are already used in those two suffix columns. Its two singleton cells must therefore be in exactly those same columns: a singleton in any other column would demand a third collector. As the cyclic prefix row also has singleton entries everywhere, **both suffix tree columns have three singleton cells**. Reversing the tree-collector lemma, each requires three complete reverse collectors, impossible. Therefore the 3x4 case cannot occur. Time reversal excludes 4x3.

The independent exhaustive check [verify_n16_frontier.py](verify_n16_frontier.py) enumerates all 1,365 positive 3x4 grids, all three cyclic-prefix row choices and all ten rank-two suffix-cycle allocations: **40,950** marked instances. Eighteen pass only the initial prefix collector capacity test, and zero survive the two-sided necessary collector requirements.

**Proposition B (4x4 cannot occur at n=16).** Every intersection must be singleton. The prefix has total cycle rank two across four components, so at least two of those components are trees. Each tree row has four singleton intersections with distinct suffix components and would need four complete collectors, exceeding the maximum of two. Thus no 4x4 both-cyclic schedule exists.

**Corollary:** every hypothetical n16 both-cyclic schedule has exactly **three prefix and three suffix components**, one cyclic component in each half.

## 3. Exhaustive 3x3 structural frontier

Two independently implemented positive-composition and extra-vertex-multiset generators, with full orbit-map equality, establish:

| Stage | n16 count |
| --- | ---: |
| Positive 3x3 allocations | 6,435 |
| Eligible cycle placements | 34,092 |
| Original collector/bridge survivors | 16,704 |
| Strong singleton-entry survivors | 4,635 |
| Row/column/reversal symmetry classes | **81** |

The 81 orbit multiplicities are 1x9, 3x18, 27x36 and 50x72 (total 4,635).

## 4. Conservative temporal-information profile probe

The established primary n15 profile algorithm, extended only for n8 cyclic local components by a *sound optimistic last-two-call bound*, examined the 81 cases.

First run (where four oversized cyclic components were intentionally deferred):
- 10 classes locally impossible,
- 66 classes globally PROFILE_UNSAT,
- one class RELAXED_SAT,
- four with n8 cycles untested.

The follow-up n8-cycle overapproximation checked those last five:
- 3 more classes locally impossible due to empty **exact smaller component** domains,
- 2 relaxed profile assignments remained possible (orbits **10 and 11**).

All UNSAT findings are conservative: exact domains are complete for m<=7; larger trees are **optimistically** granted additional side information after their last edge; an eight-vertex cyclic component is granted the full information of an arbitrary coarsened binary partition before its final two contacts. None of these relaxations removes real chronologies. The global CSP also permits reuse of unordered edges across the halves, further enlarging its set of assignments.

Thus **79/81** classes were excluded before targeting the final two.

## 5. The only two residual incidences

Both surviving relaxed cases use
\[
M=\begin{pmatrix}1&1&2\\1&1&2\\2&2&4\end{pmatrix},
\]
with marked cycle positions (cyclic row, cyclic column) equal to **(0,0)** (orbit 10, multiplicity 36) and **(2,2)** (orbit 11, multiplicity 9). The former requires exact eight-vertex tree local analysis and the latter exact eight-vertex unicyclic local analysis.

### 5.1 Orbit 11: four-collector eight-vertex unicyclic rigidity

Both critical unicyclic components have groups (2,2,4) and require both vertices in each of the first two groups to be **full collectors**; the size-four third group collectively covers all eight secrets.

Because a graph with six edges on eight vertices is disconnected, nobody can know all secrets after the first six contacts. Four distinct full collectors at termination must thus be exactly the four distinct endpoints of the final two contacts. The first of those contacts must already make two of them fully informed, forcing the first six contacts to form **two disjoint trees**. Both of the last two contacts must connect these two trees.

Within each of the two pre-last-call trees, its two designated future collectors must already know every secret in that tree. Those two collectors must be the endpoints of the tree's final internal contact. Removing each internal final contact gives **four disjoint branches**, each with exactly one designated collector. Since the remaining four participants must collectively hold all eight original secrets, every one of the four branches must contain at least one of these remaining participants (in particular, that branch's collector secret cannot cross its internal final contact and reach a different noncollector). Exactly four participants remain, so every branch comprises a collector and a unique additional participant. The only admissible local knowledge vectors therefore have **all four collectors fully informed**, and each of the four noncollectors knowing its own original secret and its branch collector's original secret.

This implies the **exact** local domain masks:
- B = {(14,14,32768)}
- D = {(8,8,278)}

The independently written [exhaustive unicyclic eight-vertex oracle](exclude_n16_orbit11.py) enumerates all eligible preforest side assignments and every chronological tree order; 144 terminal decompositions pass coverage and give exactly those sets. For the size-four shared intersection, B third coordinate only accepts subset 15 (bit 32768), whereas D requires singleton subsets 1,2,4,8 (bitmask 278). Thus (32768 AND 278) differs from 278: the two cyclic components are **incompatible**, excluding orbit 11 even under the relaxed edge-reuse convention.

### 5.2 Orbit 10: two-collector eight-vertex tree rigidity

Both critical trees have groups (2,2,4) and mandate two complete collectors in the **middle** size-two cell; every group must collectively cover all original secrets.

The tree's final bridge joins its two designated complete collectors. Before that bridge, the two vertices in the **first** size-two cell cannot cross the bridge. For them to cover all eight secrets together, they must lie on opposite sides and **each must know all secrets of its own side**. Hence in each side tree, the middle-group collector and the first-group collector are both complete before the final global bridge. The internal last edge joins them. Removing the internal last edges creates four collector-bearing branches. The four remaining vertices must collectively cover all original secrets, so each branch contains exactly one of them. The final information profiles are thereby rigid.

An **independent exact** side-tree chronology enumerator [exclude_n16_orbit10.py](exclude_n16_orbit10.py) checks every admissible partition and ordered tree history (48 final decompositions survive all cellwise coverage obligations). The unique exact local profile sets are
- B = {(8,14,32768)}
- D = {(6,8,278)}.

Again B of the shared size-four intersection accepts only subset 15 (32768), whereas D demands singleton ancestry subsets 1,2,4,8 (278). The compatibility test fails and **orbit 10 is excluded**.

## 6. Full certificate and independence gate

The complete driver [prove_n16.py](prove_n16.py):
1. Re-enumerates all 3x4, 4x4 and 3x3 structural possibilities.
2. Compiles the primary C++ component oracle with safe optimistic large-component domains.
3. Compiles the **separately implemented Stage-3 union-find/two-phase C++ oracle** and compares **every exact local component B/D domain** occurring in the 81 n16 cases.
4. Replaces the two exceptional optimistic eight-vertex domains with the independently enumerated, exact Python chronology-domain sets above.
5. Re-runs **all 81 global compatibility tests** with the independent Python CSP and verifies the 81 original statuses and exact case/orbit multiplicities.
6. Fails on SAT, omitted case, local-domain mismatch, unexpected classification, timeout or structural discrepancy. Prints machine-readable full 81-orbit certificate records and SHA256 digests.

**Executed full classification:** **13 empty local domains plus 68 incompatible global profile CSP cases; total 81/81 orbits and 4,635/4,635 placements excluded**. The independent C++ second oracle matches all **77 exact local B/D domain types** needed at n16. Stored [N16_CERTIFICATE.json](N16_CERTIFICATE.json) contains every marked incidence matrix, orbit multiplicity, exact/optimistic exclusions, domain sizes and final status.

**Full CI evidence:** [n16 complete certificate GitHub Actions run 40378654998](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40378654998) — SUCCESS. Main source `profile_oracle16_relaxed.cpp` SHA-256 `3bf98d2fdd4e877c2442bbd751755af906d37a96b6b16698416e149e5939fc18`, primary component-domain output SHA-256 `0accd52bb8a6fc36e21bf9ca7acb26ee55dd3a8701b2971416046fc4d62fedaa`, independent domain output SHA-256 `2dbe8f93e38177339d6aa90d264d17c2f1a567d56a5da87304c68fc941d06bb1`. The post-run version also compares its freshly recomputed complete case ledger with the checked-in JSON certificate; that stronger storage-integrity gate is separately checked in CI.

## 7. Historical and mathematical scope

The [same-event-poset checker](verify_kernel_scope.py) extends the previously exhaustive 51,200-linear-extension eight-vertex witness to n16. It confirms that *separate* original midpoint cycle ranks can differ for two valid schedules having the same entire incident-event order and kernel, even up to sixteen vertices; this demonstrates the need to check chronology for a fixed-order proposition. It does **not** show that the bounded half-forest theorem is independent of Labahn's complete kernel characterization.

Original mathematical priority against an implicit classical corollary remains unresolved. Neither a fixed-time-label temporal-clique 2n-3 spanner theorem nor a universal n>=17 half-forest statement is implied by this finite campaign. PR #1 should remain **draft and unmerged**, pending source-level novelty/impact work and external scholarly review.


## 8. Bounded theorem decision

**Theorem (computer-assisted, n<=16):** Every shortest successful pairwise-distinct two-way telephone-gossip chronology on (4\le n\le16), split after its original (n-2)th call, has at least one acyclic chronological half. The n=16 instance follows from the rectangular propositions, the complete marked 3x3 enumeration and the independent necessary-profile UNSAT certificate covering all 81 orbits. The older independently checked n<=15 result supplies the smaller orders. **No conclusion for n>=17** and no historical novelty certificate follows. Publication status remains a cautious research draft.
