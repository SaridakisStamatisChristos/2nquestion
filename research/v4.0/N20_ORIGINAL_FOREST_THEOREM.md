# Stage 23 — Original chronological half-forest at n=20

**28 October 2026. Complete human proof from the explicitly cited Bumby 1981 theorem, all-n local lemmas and independently exhaustive finite n<=7 tree-privacy facts. Universal all-n half-forest conjecture OPEN. No formal-assistant or independent referee certificate. PR #1 DRAFT/UNMERGED.**

## 1. Fixed-original-chronology reduction

For a successful shortest DISTINCT-contact telephone-gossip chronology on n=20 people, the first and last 18 calls are the **actual original halves**, not reorders. Suppose both are cyclic. Bumby's 1981 Theorem 3 and case-II proof constrain them to original prefix closed trees P1,P2, unicyclic P3, reversed original suffix closed trees Q1,Q2, unicyclic Q3, with a positive 3x3 intersection matrix M. The last local call in every original prefix component joins Q1 to Q2, and the last local call in every fully reversed suffix component joins P1 to P2; the unicyclic last calls close their unique cycles.

Stage 22's independently exhaustive local-tree privacy and nine-cell enumeration (see ../v3.9/N20_THREE_STAR_FRONTIER.md and count_n20_three_star.py) leaves exactly these five symmetry orbits:

1. ((1,1,2),(1,1,4),(2,4,4))
2. ((1,1,2),(1,1,5),(2,5,2))
3. ((1,1,2),(1,1,5),(3,4,2))
4. ((1,1,3),(1,1,4),(2,5,2))
5. ((1,1,3),(1,1,4),(3,4,2))

Each represents four matrices under independent exchanges of the two tree rows and two tree columns, for a total of 20 labelled necessary profiles. **They are not successful schedules.**

For EACH of the two unicyclic components U=P3 and reverse-Q3, its two outside-center cell groups may be named A and B, with |A|=2 or 3 and |B|=4 or 5. The common center X=P3 intersect Q3 has size 2 or 4. The adjacent chronological opposite tree contacting A has recipient-group sizes (1,1,|A|), and the one contacting B has (1,1,|B|), with their last edges outside the shared cells.

Exact independently enumerated chronological-tree privacy minima used in Stage 21 are:
- (1,1,2): TWO private third-group recipients;
- (1,1,3): TWO private third-group recipients;
- (1,1,4): at least ONE;
- (1,1,5): at least ONE.

A private recipient in the adjacent chronological tree cell forces that same person to be complete for U in its own orientation, by exact ORIGINAL midpoint source-target crossing. Therefore **both** U=P3 and reverse-Q3 have at least two FULL collectors in A and at least one FULL collector in B, all outside X.

## 2. All-n conditional four-root exclusion with small B and center

**Lemma 23.1.** Consider either unicyclic local component U of a hypothetical globally successful original both-cyclic schedule. Suppose its three disjoint vertex groups are A,B,X, where |A|<=3, |B|<=5 and |X|<=5, with AT LEAST TWO full U collectors in A and AT LEAST ONE in B. Suppose every original U-secret has at least TWO terminal carriers in B, U's final cycle edge joins A and B outside X, and the adjacent opposite chronological TREE T_B sharing B has its actual last edge outside B. Suppose the other cyclic component has its actual last on-cycle contact outside X. Then U cannot have FOUR full collectors.

**Proof.** If U has four complete collectors, Stage 14 proves they are the four roots of four CAUSALLY SEALED original chronological tree arms: all root-to-root calls have root endpoints, every arm's internal calls precede any core call incident to its own root, and no nonroot learns secrets from another arm.

The four complete roots distribute as follows, given |A|<=3, A-full>=2 and B-full>=1:

(a) At least TWO complete collectors in B or THREE in A. Then all four collectors are outside X. By the proven helper-tolerant one-sided causal four-arm crossing theorem (Stage 20 Lemma 20.0), the other unicyclic component with final cycle edge outside X requires |X|>=9. Contradiction.

(b) Exactly TWO A-full, ONE B-full y, and ONE X-full. Since y carries every U-secret and B's other |B|-1 members are nonroots, each one of the four distinct arm-root original secrets must have a SECOND B carrier. A B nonroot knows only original secrets of its own arm, so each of four arms must contain a different B nonroot. Hence |B|>=5. Since |B|<=5, precisely FOUR B nonroots exist, call them z1,z2,z3,z4, one in each arm. Let rho_i be the original secret of the root of arm i. The terminal U-support of rho_i inside B is EXACTLY {y,zi}; no other B nonroot can know rho_i.

These FOUR two-person star supports are incompatible with the adjacent opposite chronological TREE T_B, whose last actual contact joins two people outside B. Remove that last tree edge to form independent earlier sides V,W and assume y in V. Take any secret from W. Since no B person participates in T_B's final contact, y cannot know that W-secret in the relevant orientation. Exact fixed-midpoint crossing of every U-source/target rho_i with every T_B opposite source/target forces zi to know that same W-secret for ALL i=1,2,3,4. Repeating for every W-secret, the four distinct zi must lie in W and each be a complete collector of the earlier chronological W-tree. A chronological edge-once tree can have at most TWO complete terminal collectors. Contradiction.

All possible four-root distributions are excluded. QED.

This is an ALL-n conditional lemma with original-order chronology. It does not claim four-root impossibility for larger B or X, or without the specified collector bounds. Stage 20 already proves the analogous THREE-star crossing impossibility; an independent SEVEN-person four-star tree enumeration is added in this stage.

## 3. Dual center two-fold cover, and six-recipient lower bound

**Lemma 23.2.** In any hypothetical successful both-cyclic fixed-original chronology, if BOTH unicyclic components P3 and reverse-Q3 have EXACTLY THREE terminal full collectors, all outside their shared center X, then |X|>=6.

**Proof.** Fix any original secret a in P3, with terminal prefix center support A_a. It is nonempty by global success. If A_a were a singleton {x}, then full original source-to-all-Q3-target crossing would make x a complete REVERSED Q3 collector, contrary to the absence of any complete Q3 center collector. Thus every P3 secret has at least TWO original-prefix carriers in X. The symmetric argument shows every original reversed-Q3 secret has at least TWO reverse-time Q3 carriers in X, because P3 has no center collector.

Consider the actual reverse-time Q3 unicyclic chronology. Its last on-cycle edge touches no center participant. The preceding v-1 actual calls therefore form a chronological spanning TREE T. At least three people are complete in Q3's terminal state. Since the last call can create at most two new complete people, T must have a complete person already. In an edge-once spanning tree a complete person first appears only at the LAST tree call, and that call makes BOTH endpoints complete. Both complete T collectors are outside X, as X has no terminal complete person. Further every original Q3 secret was already carried by at least TWO X people at the end of T, because X is untouched by the final cycle edge.

Apply the Stage 13 two-outside-root chronological tree lemma: if every T-secret is known by at least two designated X recipients and two complete T collectors u,w lie outside X, then |X|>=6. For clarity, remove T's final edge uw to form U,V. No X person participates in this edge, so each side's original secrets are doubly covered inside that side's X recipients. Each side has its own complete outside-X root, u or w. In any chronological tree with a complete outside root and a two-fold recipient cover, at least THREE designated recipients are required (two opposite-side recipients for their own secret, and one on the root's side for the other side's secret). Therefore each U,V has at least three X recipients and |X|>=6. QED.

This is a conditional ALL-n theorem, not a claim of a schedule or a formally checked Lean proof.

## 4. THEOREM 23.3 — n20 original chronological half-forest

**Theorem.** In EVERY successful shortest pairwise-distinct bidirectional telephone-gossip schedule on exactly n=20 people, at least one of its ORIGINAL chronological halves (the first 18 calls or last 18 calls of the actual order) is a forest.

**Proof.** Suppose both halves cyclic. By Bumby and the Stage 22 finite exhaustive privacy enumeration, the incidence matrix belongs to one of the five orbits in Section 1. On EACH of P3 and reversed Q3, privacy forcing gives at least two outside complete collectors in A and one in B; also |A|<=3, |B|<=5 and |X|<=4. The Stage 17 original four-off-corner double-carrier theorem gives the B twice-covered secret requirement. Lemma 23.1 eliminates a possible fourth complete collector on either unicyclic side. Hence each component has EXACTLY three complete collectors, all outside X. Lemma 23.2 then forces |X|>=6. But every one of the five matrices has |X|=2 or 4. Contradiction. Therefore a forest exists in at least one ORIGINAL half. QED.

## 5. Executable verifier, scope and next research boundary

[exact_seven_tree_four_star.cpp](exact_seven_tree_four_star.cpp) independently enumerates EVERY labelled seven-person tree containing edge (0,1), then all orders of the other five tree calls followed by last contact (0,1), with B={2,3,4,5,6}, full-star root y=2 and leaves zi=3,4,5,6. It directly replays knowledge and checks whether all four support pairs {2,zi} cross every opposite-tree target/source secret. The exact tree count is 4802, the chronological history count 576240, and the compatible history count ZERO. A six-person three-star regression independently reports 432 fixed-edge trees, 10368 histories, and ZERO compatible. This finite checker corroborates the *unbounded* tree-versus-star proof, not vice versa.

[Stage 23 finite closure counter](count_n20_final.py) independently regenerates the Stage 22 necessary 20 matrices and confirms every one has the 2/3 A, 4/5 B and <=4 X collector-forcing properties. It never calls a locally valid relaxed profile a global schedule.

Truth ledger:
- n=18, n=19, n=20: HUMAN proofs plus finite exhaustive local regression (not formal proof-assistant verification).
- unrestricted original chronological half-forest conjecture for ALL n: **OPEN**.
- genuine both-cyclic successful original chronology: **NONE validated**.
- historical priority vs Bumby/Labahn/Krumme: **UNRESOLVED**.
- PR #1: **DRAFT, OPEN, UNMERGED**; publication HOLD.
