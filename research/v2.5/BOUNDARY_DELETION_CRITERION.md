# Stage 8 — exact criterion for deleting a two-call boundary participant

**27 October 2026. A rigorous necessary-and-sufficient deletion rule; the unconditional deletion induction is REFUTED, including at n=5.** This is not a solution to the all-n half-forest conjecture.

## Setup

Let S be any successful *distinct-contact* n-person gossip schedule using 2n-4 calls. Suppose a participant v appears only in the **very first** call (v,a) and the **very last** call (v,b), where a≠b are original participants. Let T be the middle 2n-6 calls, restricted to the other n-1 participants (and simply relabel the participants if desired). Then T has the optimal *call count* 2(n-1)-4 for n>=5, and contains distinct pairs.

## Exact iff lemma

**T is a successful gossip schedule on the n-1 original participants if and only if b knows a's original secret after the T contacts (but before the final call to v).**

**Proof.** Consider only the original n-1 secrets. The first (v,a) contact changes none of the original participants' knowledge of original secrets: a already knows their own original a-secret; v holds only the new v-secret. The knowledge of original secrets among the original n-1 participants during the middle contacts T is therefore precisely what it would have been in T alone.

Since v makes no intervening calls, immediately before the last call its knowledge consists only of the v-secret and a-secret. Every original participant other than b must already know all original secrets before that last call, because that final call does not involve them and S succeeds. Only b can acquire an original secret from v at the last call, and the only such secret is a. Therefore after T the original participants all know every original secret **except possibly b's knowledge of a**. Thus T succeeds precisely when b already knew a. QED.

**Cycle-rank invariance:** Removing the first and last boundary calls also preserves both *original-half* static cycle ranks, because they were leaf contacts attached to the two original halves, and the half lengths shrink correctly by one contact each. Hence a successful boundary-fringe excision can descend a hypothetical both-cyclic counterexample, but only if the additional a→b delivery criterion holds.

## Smallest demonstrated obstruction to unconditional deletion

One valid optimal 5-participant distinct-contact schedule is:

    (0,1), (2,3), (2,4), (0,2), (0,3), (1,4)

It uses six distinct contacts and successfully disseminates all five secrets. Vertex v=1 appears only in the first and last contacts, with a=0 and b=4. Removing both v contacts leaves:

    (2,3), (2,4), (0,2), (0,3)

which has four contacts on four vertices **but fails gossip**: b=4 does not know a=0's secret. The final v-b contact in the five-person schedule was essential to supply precisely that missing secret. This refutes the naive claim that any degree-two boundary participant can be deleted from a shortest successful scheme to yield another shortest successful scheme.

## Independent exhaustive n=5 falsification

[test_boundary_deletion.py](test_boundary_deletion.py) enumerates every 5-person successful 6-contact distinct-contact schedule, checks every participant with exactly the first and last contacts, simulates T independently on its 4 remaining vertices, checks exact agreement with the criterion, and checks both midpoint cycle ranks before and after deletion (regardless of success). Among **1,800 marked boundary-fringe cases**, **360 fail** deletion and **1,440 succeed**. The above explicit minimal witness is separately pinned as a regression test.

This is a useful precise restriction on proposed minimal-counterexample inductions. It is not a proof that any hypothetical both-cyclic counterexample necessarily contains a boundary participant, nor that the a→b condition always holds in a minimal counterexample. The all-n half-forest conjecture remains OPEN.
