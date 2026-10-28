# Stage 29 — sharp unbounded private-recipient phase transition in a chronological tree

**28 October 2026 — complete human proof + explicit infinite witness family + independent small chronology enumeration.** This is a local all-\(m\) mathematical result and an adversarial limitation on attempts to extrapolate the privacy minima. **It is NOT the universal original-half-forest theorem, a novel-priority certificate, or a globally realizable both-cyclic gossip chronology.** PR #1 stays DRAFT/UNMERGED; submission HOLD.

## Exact statement (helper robust)

Let \(T\) be a connected tree with \(m-1\) **distinct** bidirectional contacts, each tree edge contacted exactly once in a fixed chronological order. Initially each participant has their own independent secret. Let \(u,v\) be different participants, and \(C\subseteq V(T)\setminus\{u,v\}\) a nonempty recipient group; the remaining vertices, if any, are unassigned helpers. Assume that terminally **both singletons \(\{u\},\{v\}\) individually know all \(m\) secrets**, and **the group \(C\) collectively knows all \(m\) secrets**.

Call \(z\in C\) *private in C* if some original secret is known at terminal time by \(z\) and by **no other member** of C.

### Theorem 29.1 — exact zero-privacy threshold, ALL m

If **no** member of \(C\) is private, then
\[
\boxed{|C|\ge6.}
\]
Conversely, for **every integer \(c\ge6\)** there exists a valid edge-once chronological tree with two full singleton collectors \(u,v\) and a third group of exactly \(c\) recipients, each original secret known by at least two members of \(C\), hence **zero private members**.

Therefore the universal statement "*every such tree cover has at least one private C recipient*" holds for **all** \(c\le5\) (whenever a tree satisfying the hypotheses exists) and **fails for every** \(c\ge6\). This is sharp even without helpers.

### Proof: necessity

Since \(u\) and \(v\) are both full collectors in an edge-once chronological tree, they **must** be the two endpoints of the **last** contact \(uv\). Indeed deleting the last tree edge partitions the earlier calls into nonempty disconnected sides. Only its endpoints can learn secrets from both sides at the last contact, and no earlier participant could already know all secrets.

Delete that last edge and write \(U\ni u,\ V\ni v\) for the two preceding chronological tree histories. Neither \(u\) nor \(v\) belongs to \(C\), so **no C member participates in the final call**. Therefore a secret originating in \(U\) can have terminal recipients in \(C\) **only inside \(C_U=C\cap U\)**; a secret originating in \(V\) has terminal C recipients only inside \(C_V=C\cap V\).

Every original secret has **at least two** terminal C carriers, because C collectively covers all secrets and no C member is private. Hence **each** \(C_W\) doubly covers **every** original \(W\)-secret after the internal tree contacts, for \(W=U,V\).

Furthermore \(u\) is already a full collector of its own side \(U\) before the final call: since \(u\) is globally complete after \(uv\), it must have known every U-secret beforehand (the V endpoint could not know any U-secret before the cross-edge). Symmetrically \(v\) is full for \(V\).

Suppose \(|C_U|\le2\). As every U-secret has two **distinct** C_U recipients, \(|C_U|=2\) and BOTH its recipients individually know **all** U-secrets. Along with the third, disjoint complete collector \(u\), this gives **three** full collectors in the edge-once chronological tree U. But an edge-once chronological tree with at least two vertices has at most **two** full collectors, the endpoints of its last edge. A singleton U has no C_U recipients and cannot doubly cover its root's secret. Contradiction. Hence \(|C_U|\ge3\); similarly \(|C_V|\ge3\). Summing,
\[
|C|=|C_U|+|C_V|\ge3+3=\boxed6.
\]
No restriction on unused helpers, total \(m\), the ordering of unrelated internal calls, or the label distribution was used. QED.

### Proof: sufficiency and a sharp eight-vertex witness

Label vertices \(0,\ldots,7\), set \(u=0,\ v=1,\ C=\{2,3,4,5,6,7\}\). Make exactly these seven **distinct** chronological contacts:
\[
(0,3),\ (2,4),\ (0,2),\ (1,6),\ (5,7),\ (1,5),\ (0,1).
\]
The first six edges form two disjoint 4-person trees, the final edge joins their full-information roots. Thus 0 and 1 become global full collectors, and the entire static graph is a tree.

The actual six C knowledge masks, in vertex order \(2,3,4,5,6,7\), are:
\[
(29,\ 9,\ 20,\ 226,\ 66,\ 160)
\]
(where bit \(i\) denotes the original secret of vertex \(i\)). Each original secret is present **exactly twice** among these C masks, so no C member is private. The masks for 0 and 1 are both \(255\).

For arbitrary \(c>6\), append vertices \(8,9,\ldots,c+1\) to the same group C. Before ALL seven displayed calls, contact each extra vertex \(z\) once with vertex 3, i.e. prepend \((z,3)\) for every new \(z\). Every new original secret then appears at least twice in C (at \(z\) and vertex 3), and vertex 3 transfers all these secrets through \((0,3)\) and \((0,2)\) to collector 0, and through final \((0,1)\) to collector 1. The old C secret multiplicities do not decrease. Each added contact is a distinct new tree edge, so the construction holds at every \(c\ge6\). QED.

## Consequences for the original 2nquestion research

1. **Exactly closes the unknown \((1,1,c)\) privacy *zero/nonzero* boundary:** the earlier [Stage 21](../v3.8/N20_PRIVACY_FRONTIER.md) and [Stage 25](../v4.2/N21_CONSERVATIVE_77_PROFILE_FRONTIER.md) exact n≤7 privacy tables correctly force positive off-corner privacy at c=4,5. They must **not** be extrapolated to c=6,7,...: this theorem constructs an unbounded family with zero private recipients starting at c=6. The finite table's conservative default ZERO for unknown triples is justified for this entire infinite subfamily.
2. **Implication for exterior full-collector forcing:** if a full original/reversed chronological tree has singleton corner cells \((1,1)\) and off-corner size \(|C|\le5\), a private member of C must exist, forcing a full collector in the opposite cyclic component by the original fixed-midpoint source-target intersection. When \(|C|\ge6\), no such inference follows solely from collective group coverage and chronological tree order.
3. **Clear falsifier of an attractive all-n shortcut:** it is false that every closed chronological tree with singleton outer collectors must contain an off-corner private recipient, without a bound on the off-corner size. Our exact witness contradicts that overstrong extension. **It is not a counterexample to the fixed-original-half forest conjecture**, because no compatible opposite-half globally successful minimum schedule is constructed.
4. **All-n progress vs project objective:** the primary fixed-label temporal-clique \(2n-3\) exact reachability-spanner conjecture remains open. An auxiliary structural lemma for minimum gossip chronologies cannot, by itself, establish the temporal clique result.

## Reproducible independent check

Run from repository root:

~~~bash
python3 -B research/v4.6/private_threshold.py
~~~

This independent Python source performs Prüfer-sequence plus chronological-contact enumeration for eligible 3–5-vertex trees with two prescribed full singleton collectors, verifying that no privacy-free C occurs; it replays the EXACT c=6 example and extensions through c=40, checks that every contact graph is a tree with unique edges, two complete collectors, ≥2 carriers of every secret inside C, and invariance of C knowledge across the last call. It tests executions only at finitely many c; the above root-edge proof and explicit parameterized construction establish the full universal quantifiers.

**Evidence states:** theorem = HUMAN PROOF; construction c≥6 = EXACT SYMBOLIC FAMILY + executable finite regressions; latest-head GitHub CI = must be separately observed; novelty = UNVERIFIED, with explicit Bumby/Labahn/Krumme dependencies; original both-cyclic full forest = OPEN for n≥22; temporal clique \(2n-3\) spanner = OPEN. Publication HOLD and PR DRAFT/UNMERGED.
