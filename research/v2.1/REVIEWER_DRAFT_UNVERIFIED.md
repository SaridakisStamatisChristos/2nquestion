# Independent adversarial review — n=15 computer-assisted theorem

**25 October 2026; status: full in-scope certificate PASS; external peer review NOT performed.**

## Independent research claims

- **Formal model:** 15 distinct participants; 26 pairwise-distinct unordered full-information exchange calls; original fixed split after 13 calls.
- **Theorem claimed:** any successful schedule has at least one acyclic half.
- **Proof domain:** case exhaustion of both-cyclic halves after previously human-proved r=s=3 reduction and information-flow lemmas. The structural filter yields 945 placements in 20 paired cycle/incidence symmetry orbits.
- **Certified disjunction:** seven orbits excluded by component-order UNSAT; ten by exact compatible temporal-information-profile CSP UNSAT; three by the same CSP with artificially increased prefix tree information. Total 20/20.

## Mathematical audit of new machinery

1. **Profile soundness:** For a suffix temporal call order, reverse all contacts and use one token per suffix participant. The tokens that reach an entry x identify exactly the final suffix vertices reachable from x in the original direction (temporal path duality). For a row source, every destination gets all its original secrets iff the union of midpoint knowledge over its ancestor-entry subset is full. This gives the exact Boolean test `B & D == D`.
2. **Independent components:** Within each half, distinct connected components use disjoint vertices, so their local calls commute and any combination of local orders can be interleaved. This justifies modeling them independently.
3. **Cross-half edge reuse deliberately RELAXED:** The profile CSP allows a contact edge to occur in both halves. Any real distinct-edge schedule still induces a feasible relaxed assignment. UNSAT of the relaxed CSP is thus sufficient. SAT would NOT certify a genuine schedule.
4. **Optimistic last-edge tree relaxation:** Two demanded collectors in different cells force the tree's final edge to run between those cells; deleting the edge divides the tree into two sides. For every other participant, at the prefix cut no original secret from the opposite side can be present. Giving that participant all *same-side* secrets is an information-overestimate. Granting full knowledge to both endpoints only strengthens the overestimate. The CSP generated from these optimistic choices contains all real schedules, so its UNSAT is sound.
5. **Large component case coverage:** No eight-vertex tree is brute-force UNSAT-claimed. The three hardest cases use the optimistic argument. The requisite seven-vertex local UNSAT state enumeration uses a `(used-edge set, full knowledge vector)` memo key; future legal contact options and resulting information depend only on those two objects, so it is safe to merge histories with identical keys.
6. **Symmetry validity:** Original reversed chronology preserves all-to-all temporal gossip because it transposes the reachability relation. Row/column relabelings preserve the source-destination component relation, and a transpose accompanied by exchanging cyclic row/column preserves the both-cyclic possibility. Cycle positions were included when canonicalizing.

## Differential / adversarial checks actually executed

- 3,200 independently generated random prefix/suffix component-order pairs: exact compressed mask compatibility equals direct forward temporal information transfer.
- Four local sizes and collector-demand patterns exhaustively enumerated in an independent Python implementation: exact resulting domain profiles match the standalone C++ local oracle.
- 110 qualifying random eight-vertex tree chronologies and 130 qualifying random seven-vertex tree chronologies: each real prefix profile is contained in the independently reconstructed optimistic two-sided profile family.
- Second CSP implementation checks every suffix-profile triple first, instead of the primary prefix-first recursive search: thirteen global UNSAT classes independently confirmed, including all three optimistic-tree cases.
- The CI runner must fail if any of the 20 orbits is not UNSAT. Timeouts, crashes or UNKNOWN conditions are never converted into success.

## Reviewer objections and dispositions

| Potential objection | Severity | Response |
|---|---|---|
| A profile abstraction may discard information about which participant knows which source secrets. | Critical | It records the exact predicate 'the union of knowledge at every subset of entry vertices is full' for *every* subset; destination ancestry needs no other information. Full direct-vs-compressed randomized differential validation plus proof provided. |
| The optimistic tree relaxation might remove valid schedules. | Critical | It only **adds** knowledge to each vertex without restricting bipartitions; both mandatory collectors are final-edge endpoints. In any real chronology, all other vertices remain confined to their side before the final call. Proof and independent tests provided. |
| Combining local profiles might mishandle interleavings. | Major | Calls in distinct components within a half are disjoint and commute, so only each component's local contact order matters. |
| Actual contact edges must be distinct across halves, yet the CSP does not enforce this. | Major | Deliberate existential overapproximation: omission makes UNSAT strictly stronger, and no SAT is presented as a real schedule. |
| State-cache exploration may miss a chronology. | Major | Equality of used edges plus current knowledge vector implies identical future successor states; all possible next unused calls are visited, giving an exact quotient. |
| Information-flow filters may already be implicit in old kernel theory. | Major | No universal novelty claim; acknowledged overlap with Labahn 1995, Krumme 1996 and Göbel et al. 1991. |
| A green CI run is not a formal Lean/Coq proof. | Moderate | Explicitly classified as a reproducible computer-assisted finite proof; not machine-formally checked or externally refereed. |
| Could this settle fixed-timestamp temporal clique 2n-3? | Critical | No; different quantifiers and different object. Manuscript expressly disclaims it. |

## Contribution stress test and publication status

**Surviving contribution:** A bounded \(n\le15\) original-chronology half-forest invariant with a new exact information-profile method and conservative large-tree overapproximation; a stronger finite classification than v2.0. **Publication originality/impact:** not fully established; classic minimum-call bounds and static forest/reordering mechanisms belong to prior work.

**Readiness gates:** Mathematical finite certificate — PASS once GitHub CI confirms on the committed head; independent execution/differential tests — PASS locally; manuscript draft — complete; historical first-ever originality — UNRESOLVED; outside referee — NOT DONE; universal theorem — OPEN; formal prover certificate — NOT DONE. Keep PR draft/unmerged.