# Universal unicyclic-to-rooted-crossing transfer (30 October 2026)

**Scope:** a new ALL-n exclusion for a precisely identified class of original-order both-cyclic gossip midpoint structures. The full original-half forest conjecture and the primary 2n-3 temporal-clique spanner conjecture are NOT settled.

## Theorem U.19 — one two-outside-root tree plus one outside-root tree is impossible

Let P and Q be connected edge-once chronological UNICYCLIC contact components with exact original (for P) and fully reversed original (for Q) contact orders. Let X=V(P) intersect V(Q). Suppose each actual last local contact in its unicyclic history closes its single static cycle and BOTH endpoints of that final contact lie OUTSIDE X. Let T_P and T_Q be their respective original-order preceding SPANNING chronological trees (remove only the actual final cycle-closing contact, without reordering).

Assume:
1. The actual terminal knowledge of X for P secrets and for reversed-Q original secrets satisfies exact **ALL-source-pairs crossing**: for every P-original secret a and every reversed-Q-original secret b, some X participant knows both in the respective separate histories.
2. ONE of T_P,T_Q has two terminal full collectors, its ACTUAL last-tree-call endpoints, BOTH outside X.
3. The OTHER of T_P,T_Q has at least ONE terminal full collector outside X (its other terminal complete endpoint may lie in X or outside).

Then these premises are inconsistent for ANY finite n, any |X|, and any number of unassigned exterior helpers.

**Proof.** The actual last cycle-closing call of each unicyclic component has both endpoints OUTSIDE X, so that call changes no participant's knowledge inside X. Hence the exact original-source X-support families in P and reversed Q are IDENTICAL to the corresponding families in their pre-final chronological trees T_P,T_Q. Their all-pairs support crossing transports unchanged to T_P,T_Q.

Both preceding trees are original-order edge-once and have at least one complete root outside X, and at least one of them has both last-tree-call complete endpoints outside X. This is precisely the rooted crossed pair type R excluded by [Theorem U.17](ROOTED_CROSSING_NO_GO.md). Contradiction. QED.

No double-cover or no-center-full-collector premise is required. In particular the second tree MAY have a full center collector: type R permits its second complete tree endpoint inside X.

## Useful sufficient hypotheses in the original gossip reduction

An exterior collector full at the end of a unicyclic history and NOT involved in its last cycle-closing call remains full in the preceding tree. By the final-edge property, its preceding tree has two full last-call endpoints. If the first cyclic component has no center full collector, both tree endpoints are exterior; if the second cyclic component has an untouched exterior full collector, at least one of its preceding tree endpoints is exterior, even if the other is central. Under the original exact midpoint crossing, U.19 forbids this arrangement for ALL n.

This generalizes the previous conditional |X|>=14, and later |X|>=28, center lower bounds to **impossibility** whenever their root/chronology hypotheses apply. It does not force exterior full collectors to exist in arbitrary both-cyclic cases; separate root-free exterior configurations remain open.

## Verification / publication boundary

Human proof conditional on exact U.17, the valid original fixed-half / reversed-half gossip midpoint crossing translation, and the last-cycle-call-outside-X structure. The theorem is all-n via exact support invariance; finite replay audits in ROOTED_CROSSING_NO_GO.md challenge but do not establish its universal quantification. Historical originality unverified; no independent referee or formal checker. Main n-unbounded original-half forest and 2n-3 spanner still OPEN. Maintain PR DRAFT and manuscript HOLD.
