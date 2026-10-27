# Stage 9 — all-n midpoint straddling and universal two-call fringe invariance

**27 October 2026. All-n theorem with independent n4/n5 full schedule and generalized insertion enumeration. Main original-half forest conjecture remains OPEN.**

## Theorem 1: Every vertex participates in both original chronological halves

Let S be any successful minimum-size bidirectional telephone gossip chronology on n>=4 participants with 2n-4 distinct contacts, split at its ORIGINAL midpoint into two blocks of n-2 calls.

**Claim.** Every participant appears in at least one contact of the prefix AND at least one contact of the suffix.

**Proof.** After n-2 prefix contacts, **nobody can know all n original secrets**. Indeed, knowing all secrets at a particular vertex requires the STATIC contact graph used so far to connect all n original vertices, since information cannot cross a static connected-component boundary. Any connected graph on n vertices needs at least n-1 edges, while the prefix has only n-2. If a participant v makes no suffix contact, its knowledge cannot change after the cut and it never becomes fully informed. Contradiction.

Dually, suppose v makes no prefix contact. Then v's original secret has remained exclusively at v at the cut. For that secret to reach all n participants through the suffix contacts, the STATIC contact graph of the suffix must connect all n vertices. It cannot: it has only n-2 edges. Contradiction. QED.

**Corollary.** Every degree-two participant appears EXACTLY ONCE in each half. This is a statement about the original time split; no reordering is assumed or permitted.

## Theorem 2: ALL valid two-call insertions preserve both half-cycle ranks

Let S be any successful minimum-size distinct-contact chronology on n original participants. Create any new chronology S' on n+1 participants by inserting exactly two contacts (v,a) and (v,b) involving a new participant v, leaving all previous contacts in their original relative order. Allow the insertion slots to be **arbitrary**, not necessarily the first and last contacts. Require that S' genuinely succeeds at the new size and its unordered contacts remain distinct.

Then the two original chronological half-cycle ranks of S' are EXACTLY the same ordered pair as those of S.

**Proof.** S' has 2n-2=2(n+1)-4 calls, so Theorem 1 at size n+1 says v must appear at least once in its first n-1 calls and once in its last n-1 calls. Since v has precisely two calls, it appears **exactly once in each half**. Removing the new-vertex call in each half leaves precisely n-2 original S contacts in each block, in the same original sequence; the underlying original-vertex edge sets are exactly S's two original halves. The one new edge in each S' half meets the previous graph only at one old endpoint v is new, so it is a leaf edge and creates no static cycle. Therefore the cycle ranks of each half are unchanged. QED.

This is stronger than the specific first/last two-call extension of [Stage 8](../v2.5/UPWARD_CLOSURE_LEMMA.md), because **every** possible successful slot arrangement has the same cycle-rank invariance. It also tells us that every counterexample of minimal participant count must be irreducible with respect to a success-preserving deletion of a degree-two participant.

**Crucial logical limitation.** It does **not** say that every existing degree-two participant can be deleted while preserving successful gossip. [Stage 8's exact boundary deletion counterexample](../v2.5/BOUNDARY_DELETION_CRITERION.md) proves the converse false already at n=5. It does not imply that a minimal counterexample has minimum degree >=3.

## Executed independent exhaustive tests

[check_midpoint_straddling.py](check_midpoint_straddling.py) is independent of the tree-cover verifier. It exhaustively enumerates EVERY successful ordered distinct-contact minimum gossip chronology on n=4 and n=5, independently simulates secrets and half-cycle ranks, checks first-half/last-half participation of every participant, and considers THREE choices of distinct insertion endpoints (a,b) over ALL possible two-contact insertion positions. It checks whether each insertion actually succeeds; only successful schedules are asserted to preserve the two ranks and have one new call in each half.

| Starting size | Complete optimal schedules | Marked degree-two vertices | Insertion attempts | Successful insertions |
|---|---:|---:|---:|---:|
| 4 | 24 | 96 | 1,080 | 216 |
| 5 | 3,240 | 9,720 | 272,160 | 49,248 |

Every one of the 49,464 successful tested insertions preserves BOTH original chronological cycle ranks. Unsuccessful insertions are correctly discarded rather than counted as counterexamples.

**Scientific decision:** This all-n theorem and the tight exponential tree-cover theorem are new proof mechanisms within this research program, but universal original-half forest **OPEN** and historical novelty against old minimum gossip literature **UNRESOLVED**. Maintain manuscript HOLD and PR #1 DRAFT/UNMERGED.
