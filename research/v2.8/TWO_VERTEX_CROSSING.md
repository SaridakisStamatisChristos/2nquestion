# Stage 11 — Two-vertex crossing lemma and small-cell packing

**27 October 2026. ALL-n necessary condition for exactly specified rooted sealed-arm interfaces. Main chronological half-forest conjecture OPEN.**

## Binary information-crossing lemma (no tree assumption)

Let U={x,y} be two shared participants. Let A and B be two finite nonempty sets of secrets (for full temporal gossip, A denotes first-half *sources* and B reverse-time second-half *targets*). Suppose each participant has specified subsets of A and of B, and their two-person cell **collectively covers both A and B**.

For each a∈A, define its nonempty informed subset S_A(a)⊆U. For b∈B define S_B(b)⊆U. Assume the exact all-pairs temporal compatibility

\[
  \forall a\in A,\ b\in B:\quad S_A(a)\cap S_B(b)\ne\varnothing.
\]

**Lemma (iff).** This condition is equivalent to at least one of the following:

1. BOTH x and y individually know all A-secrets;
2. BOTH x and y individually know all B-secrets;
3. ONE of x,y individually knows ALL A-secrets and ALL B-secrets.

**Proof.** Sufficiency is immediate from cellwise coverage and from a common collector.

For necessity, if neither x nor y alone knows all A-secrets, select an A-secret absent from x (known only at y) and another A-secret absent from y (known only at x). Every B-secret must intersect BOTH singleton support sets {x} and {y}; hence every B-secret is present at both participants, proving (2).

Otherwise, x or y is complete for A. If x and y both are complete for A, (1) holds. Suppose only x is complete for A. Some A-secret is then known only at x, so every B-secret must be known at x; thus x is also B-complete and (3) holds. The case with y is symmetric. QED.

The iff was independently exhaustively checked over all **49 ordered pairs of nonempty support-set families** on {x,y}; 21 pairs are compatible and the exact trichotomy agrees with all 49.

## Corollary for sealed rooted tree arms

Take the Stage 10/11 k×k crossed-arm interface with k>=2, a single outside-X participant in each arm that is **already a full collector** of its local tree arm after the internal calls, and X_ij the nonempty intersection subcells. The exact B/D condition implies for every Ai-Bj arm pair the binary compatibility premise above whenever |X_ij|=2.

A connected chronological tree component has at most **two** final fully informed participants, the endpoints of its final contact. Since one is the designated outside-X root, **at most one X participant** can be fully informed within each A or B arm.

Therefore a size-two crossed cell cannot have both participants complete for either arm; by the binary lemma it must contain a participant who is complete for **BOTH** its row arm and column arm. A size-one crossed cell likewise consists of a participant complete for BOTH arms. As each tree arm has at most one complete participant in X, **each row and each column contains at most one cell of size 1 or 2**.

The other cells contain at least three participants. At most k cells can be small (one per row); consequently

\[
\boxed{t=\sum_{i,j}|X_{ij}|\ \ge\ k\cdot1+(k^2-k)\cdot3=3k^2-2k.}
\]

This all-n bound is logically independent of whether any tree arm is at its 2^k equality size. It combines with the tight-arm/private-secret bound in [STEINER_COVER_RIGIDITY.md](STEINER_COVER_RIGIDITY.md) to give

\[
\boxed{t\ge \max\{\,3k^2-2k,\ k(2^k-1)+k-1\,\}.}
\]

For k=2 the binary obstruction strengthens t≥7 to **t≥8**. For k=3 the combined bound is t≥23; for k=4 it is t≥63. No assertion of sharpness for the whole global gossip problem is made.

## Evidence

[two_vertex_crossing.py](two_vertex_crossing.py) generates every possible nonempty A/B support-family assignment on a two-person cell, checks necessity/sufficiency of the three-way alternative, and independently exhausts positive 2×2 subcell matrices of total t<=7 against exact row/column local-cover and small-cell capacity constraints. It reports zero structurally compatible candidates. It is a finite falsification/regression, not an all-n proof.

This improves *conditional* sealed-arm restrictions only; arbitrary optimal gossip chronologies may have components without this arm decomposition. Universal original-half forest: **OPEN**. Historical novelty: **UNRESOLVED**.
