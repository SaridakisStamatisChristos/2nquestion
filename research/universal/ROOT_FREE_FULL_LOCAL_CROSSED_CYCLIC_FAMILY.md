# All-width fully double-covered, mutually crossed ROOT-FREE unicyclic center pair

**30 October 2026. New exact original-order all-k parametric construction.** This is a much stronger local witness than U.20 or U.21 separately: BOTH cyclic histories cross across their common center, and EACH simultaneously double-covers its original sources in BOTH exterior cells AND the center, with NO full collectors. Calls are distinct even ACROSS the two histories. It remains a TWO-component local construction, NOT a globally successful shortest telephone-gossip chronology.

## Theorem U.22 — arbitrary-width mutually crossed three-cell root-free cyclic pairs

For EVERY integer k>=0, there exist two original-order edge-once chronological UNICYCLIC histories P and Q, with three disjoint cells for each, sharing exactly the designated center X, satisfying ALL of:

- The common center has |X|=4+k. Each cyclic component has exactly 64+k vertices and 64+k distinct chronological contacts. Their total vertex union has **124+k people**.
- In P, the two disjoint exterior cells A_P,B_P have 12 and 48 people, respectively; Q's disjoint exterior cells A_Q,B_Q likewise have sizes 12 and 48. The P and Q exterior cells are all pairwise disjoint, and V(P) intersect V(Q) = X.
- The first |V|-1 calls of EACH cyclic component form a connected spanning original-order TREE. Its final distinct call joins its own exterior A/B cells, closes exactly one cycle and touches NO X recipient.
- EVERY original P secret has >=2 terminal holders in EACH of A_P,B_P,X. EVERY original Q secret has >=2 terminal holders in EACH of A_Q,B_Q,X.
- **EVERY exact original-P-source X-support intersects EVERY exact original-Q-source X-support**. The intersection is witnessed by an explicit 2x2 center grid participant.
- Neither P nor Q has ANY terminal complete collector, before or after its last cycle-closing call.
- No unordered call is reused within either history OR between P and Q, including the calls involving added shared center people.

Thus no universal outside-collector forcing or local crossed-cyclic impossibility theorem can follow from the conjunction of the above precise local hypotheses, at ANY center width >=4.

### Explicit seed with four shared center hubs

Name the four center hubs x_00,x_01,x_10,x_11, indexed by row i and column j in {0,1}. Take the 32-person chronological equality tree H(6) in Theorem U.9b, with its SIX pairwise-disjoint collectively complete recipient groups

 G0, G1, G2, G3, G4, G5

of respective sizes 1,1,2,4,8,16. Its ONLY full terminal collectors are the singleton groups G0 and G1, the endpoints of its ACTUAL last tree call. The remaining groups are disjoint and contain no full collector.

Build P from TWO disjoint copies R0,R1 of H(6), where for row i the two full singleton roots (G0,G1) are **identified with center hubs** x_i0,x_i1. All remaining 30 people in each copy are unique P-outside people. Let

 A_P = (G2 union G3) from BOTH P rows,
 B_P = (G4 union G5) from BOTH P rows.

Thus |A_P|=2(2+4)=12 and |B_P|=2(8+16)=48. Execute all internal H(6) contacts as given, then join a nonfull G4 person in row0 to a nonfull G4 person in row1 with one NEW bridge contact. This produces a genuine P spanning tree on 64 people. Add one FINAL distinct A_P-to-B_P call between a nonfull G2 participant of row0 and a nonfull G5 participant of row1, neither a bridge endpoint. This closes the unique static cycle outside X.

Build Q by the SAME procedure on two DISJOINT new sets of exterior people, but use the TWO columns instead of rows: in its column j H(6), identify (G0,G1) with x_0j,x_1j. Define A_Q=(G2 union G3) across Q columns, B_Q=(G4 union G5) across Q columns. Join nonfull G4 participants across columns, and append a fresh last A_Q-B_Q closing contact between G2 in column0 and G5 in column1.

The only contacts with BOTH endpoints in the shared X are the LAST H(6) internal calls of each H(6) copy. In P they are the two HORIZONTAL hub edges x_00-x_01 and x_10-x_11; in Q they are the two VERTICAL edges x_00-x_10 and x_01-x_11. These four unordered edges are all distinct. Every other seed call has a participant in its history's unique exterior set, so **P and Q have no repeated unordered call**.

### Exact X-support crossing

For EVERY original P source in row i, the two complete roots x_i0 and x_i1 of its original H(6) copy already know that source before the inter-row bridge. No call subsequently touching a center hub joins the rows; its terminal center support therefore contains **both** x_i0,x_i1 and no opposite-row hub. Symmetrically every Q source in column j is possessed by BOTH x_0j,x_1j and by no other-column hub. For every P source a in row i and every Q source b in column j, the SAME shared center person x_ij knows a at the P midpoint and b at the Q reversed endpoint.

This proves EXACT all-pairs source-support crossing in the common center. No source from an extra outside person is excluded.

### Complete triple double cover and zero complete collectors

Inside each P H(6) row, each of G2 and G3 individually collectively covers its entire local set of original sources, hence their DISJOINT union A_P has at least two distinct recipients of every such source. Likewise G4 and G5 yield B_P q2 coverage. The two individually complete local center hubs yield X q2 coverage. These witnesses are already present BEFORE the global P inter-row bridge, and union-of-knowledge calls never remove them. Therefore P is doubly covering in its THREE cells. The Q proof is identical, using columns.

The bridges connect locally NONFULL G4 people, so their recipients remain missing some of their own row/column original secrets; all participants not on a bridge have no opposite-arm secrets. The LAST contacts connect NONFULL G2 from one arm to NONFULL G5 in the other, neither of whom was a bridge endpoint. Each last endpoint therefore remains missing an original secret of its own arm after the call (the opposite endpoint never learned that secret through the bridge); all other participants were already not globally full and are unchanged. Thus each cyclic component remains entirely root-free.

### Adding k arbitrary shared center recipients

For arbitrary k>=0 add new common center people w1,...,wk. In P, insert early one-time leaf contacts (x_00,w_t) BEFORE ALL its row0 H(6) calls; in Q insert DIFFERENT early one-time leaf contacts (x_10,w_t) BEFORE ALL its column0 H(6) calls. The two sets of new unordered edges are disjoint because x_00 != x_10. Each new source secret tracks the corresponding original complete-root source throughout its local H(6) history, so both row0 center roots in P, both column0 center roots in Q, and both disjoint exterior cover groups in EACH cyclic component still collect it. Old-source coverage is preserved and no nonroot terminal complete collectors appear; bridge and cycle endpoints are unchanged. The exact crossing at x_ij therefore remains valid for all original and new sources.

The construction has |X|=4+k, |V(P)|=|V(Q)|=64+k and |V(P) union V(Q)|=124+k. It remains chronologically exact, distinct-call, no-full and triple-doubly-covering for ALL k. QED.

## Exact falsification / important global limitations

The executable [root_free_full_local_crossed_unicyclic_family.py](root_free_full_local_crossed_unicyclic_family.py) builds every call and every designated group, replays each actual chronological history, validates tree-then-one-cycle topology, checks no full collectors and no shared call edge, verifies EVERY original source's q2 coverage across all THREE cells, and checks every P/Q source pair meets at its precise hub x_ij. It locally executed eight sample widths k=0,1,2,4,8,16,32,64 (center sizes 4..68) and 54,485 ordered source-pair crossings. This is **finite corroboration**, not the all-k proof above.

**Critical boundary:** the four positive corner cells and FOUR additional original/reversed closed TREE components P1,P2,Q1,Q2 of the full Bumby 3x3 midpoint are NOT constructed here. Their own original-order last-contact spine and exact crossing across ALL NINE cells remain mandatory. This U.22 witness is NOT a successful 2n-4-call global gossip chronology, NOT a refutation of the universal original-half-forest conjecture, and NOT a proof or disproof of the separate temporal-clique 2n-3 spanner problem.

**Scientific impact:** The conjunction of (1) fully crossed center source supports, (2) all four offcorner q2 cover requirements, (3) both last cycle calls exterior-only and (4) globally distinct contacts is **realizable at every common center width**, without any full collectors. Thus a global original-half forest proof must leverage the missing four corner TREE components and their four offcorner crossing compatibility constraints; purely central cyclic-core arguments cannot settle it.

Human proof, exact executable falsifier; no external mathematical referee, historical originality assessment or Lean/Coq formal certification. PR #1 DRAFT, publication HOLD.
