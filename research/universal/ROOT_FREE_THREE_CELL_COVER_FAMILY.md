# Root-free unicyclic three-cell q=2 cover at every center width >=48

**30 October 2026. Exact original-order construction, all finite k>=0.** This demonstrates that even the **FULL offcorner twice-covered** local necessity for a hypothetical both-cyclic 3x3 gossip midpoint DOES NOT, by itself, force a complete collector in the cyclic component. It does **NOT** supply an opposite chronologically crossed component, and is NOT a global successful 2n-4 gossip schedule.

## Theorem U.21 — all-width three-cell double coverage without any full collector

For each integer k>=0 there is an edge-once chronological unicyclic component H_k with 64+k vertices partitioned into THREE nonempty disjoint recipient cells A,B,X such that

1. |A|=6, |B|=10, |X|=48+k.
2. H_k has EXACTLY 64+k pairwise-distinct unordered chronological calls; its first 63+k calls form a connected spanning edge-once tree, and its final distinct call closes the unique static cycle between A and B, outside X.
3. **Every original participant secret is terminally held by at least TWO DISTINCT recipients in EACH of A, B, X.**
4. No participant is a terminal complete collector, either after the preceding spanning tree or after the final cycle-closing call. The final cycle call leaves all X knowledge unchanged.

All four conclusions hold for arbitrary k, with no n bound or helper assumptions.

### Construction

Use the exact universal group-cover sharp tree H(6) from [U.9b](GENERAL_COVER_PACKING.md), with **32 vertices and 31 original-order tree contacts**. Its SIX disjoint collectively complete recipient groups are G0,G1,G2,G3,G4,G5, of sizes 1,1,2,4,8,16; both singleton groups G0,G1 are its only terminal complete collectors, at the endpoints of its actual last tree call.

Take two disjoint copies L,R of H(6), perform all their H(6) calls internally, then join them with one EXTRA bridge call e_L-e_R, where e_L is a participant of G4 in L, e_R the corresponding G4 participant in R. These are NOT local complete collectors. Their resulting 64-vertex prefix is a genuine connected spanning original-order tree: 31+31+1=63 distinct calls.

Define cells by **pairing complete recipient groups**, per copy, and then taking unions across the two copies:

- A=(G0 union G2)_L union (G0 union G2)_R, of size 2(1+2)=6;
- B=(G1 union G3)_L union (G1 union G3)_R, of size 2(1+4)=10;
- X=(G4 union G5)_L union (G4 union G5)_R, of size 2(8+16)=48.

Because EACH G_i individually collectively covers every secret originating in its own H(6) copy, each original secret has ≥2 DISTINCT recipients in each group A, B, X: one in each of the pair's constituent disjoint G groups, both within the secret's original copy. The bridge cannot remove any information.

Now add the last call d_A-d_B, where d_A is a participant of G2 inside L, and d_B is a participant of G3 inside R. Both are nonfull inside their own local H(6) copies, and **neither participates in the bridge**. Since the prefix L and R components were joined by exactly ONE bridge edge, the additional distinct L-R edge creates exactly one static cycle. Its endpoints lie in A and B, so no X recipient's knowledge changes.

### No-complete-collector proof

Before the bridge, both local H(6) trees have exactly two full collectors within their own side; e_L,e_R,d_A,d_B are NOT among them. At the bridge, only e_L,e_R can obtain secrets from the opposite side. They remain nonfull globally because each was already missing at least one original source secret from its OWN side, and the other side had no information about that missing local secret before the bridge. Every other participant lacks all opposite-side original secrets at this point, so none is globally complete.

At the final d_A-d_B call, neither d_A nor d_B was a bridge endpoint, so d_A has no R-original secrets and d_B has no L-original secrets beforehand. Their last call makes their knowledge equal, but each still lacks some original secret from its OWN side: d_A's missing L-secret is not known to d_B (which never received L information), and symmetrically for d_B's missing R-secret. Thus neither becomes complete. All other participants are unaffected by this last call and were nonfull already. Hence zero terminal full collectors.

### Padding to arbitrary k>=0

Choose the L copy's full root r∈G0. BEFORE any original H(6) internal calls, append k fresh center vertices w_1,...,w_k by consecutive new leaf calls (r,w_i). Put all w_i in X. Each new w_i's original secret is present at r before the remainder of the local H(6) chronology. Therefore, throughout every later original H(6) call, its transmission tracks the original secret of r; that original secret has ≥1 designated recipient in EACH of G0,...,G5. Thus each new secret is still received at least twice in each A,B,X (once in EACH paired group). Old-source group coverage cannot decrease. None of the nonroot original collectors is made complete for the now larger local copy: at its original last local call, only the original two full endpoints can be complete, and each added leaf knows no other side's secrets. The bridge and closing contacts use the unchanged nonfull endpoints, so the no-complete argument remains valid. Exactly k new participants and k new distinct tree edges were introduced, while the final extra L-R edge still closes a unique cycle.

This proves U.21 for every finite k and thus for EVERY integer |X|>=48, with fixed |A|=6 and |B|=10. QED.

## What this theorem DOES and DOES NOT establish

- It refutes any proposed **unconditional offcorner collector-forcing principle derived solely from the three disjoint groups A,B,X doubly covering each original secret**, even with the last cycle call between A,B and exact original chronology.
- It complements [U.20](ROOT_FREE_UNICYCLIC_CROSSING_FAMILY.md): U.20 supplies TWO fully crossed root-free cyclic histories with double coverage in X, but does not meet the strong offcorner double-coverage condition; U.21 supplies ONE cyclic history with full three-way double coverage, but does not build a SECOND mutually crossed history.
- **The crucial remaining global obligation is to COMBINE these two features** with the original 3x3 offcorner tree cross-support constraints and all globally distinct calls, or prove that such a combination is impossible. Neither separate construction is a successful original 2n-4 gossip chronology. The full original-half forest and separate primary 2n-3 spanner questions are still OPEN.
- The executable [root_free_three_cell_unicyclic_family.py](root_free_three_cell_unicyclic_family.py) replays k=0,1,2,4,8,16,32,64, up to |X|=112 and 128 people, and checks actual tree/cycle topology, full-knowledge masks, final-X invariance and all three q2 recipient-group guarantees. The **human parametric construction** (not eight finite trials) establishes the all-width quantifier.
- Proof label: HUMAN PROOF, external mathematical review and historical novelty check pending, NOT Lean/Coq-certified. PR DRAFT, publication HOLD.
