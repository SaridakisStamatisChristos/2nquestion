# Universal first/last-contact incidence-window lemma

**Status:** PROVED (human-checkable); **novelty:** NOT ESTABLISHED, likely elementary/folklore relative to minimum-gossip literature. Does not settle universal `2n-3` or POD. The elementary statement is included as a verifiable preprocessing condition for the exact solver.

**Model:** `n>=4`; `k=2n-4` bidirectional pairwise telephone calls, no assumptions on repeated edges for this lemma. At the beginning every participant knows its own distinct initial secret, and after the last call everyone knows every initial secret.

**Theorem.** For each vertex `v`, the *first* call incident to `v` occurs no later than position `n-2`; its *last* incident call occurs no earlier than position `n-1`. Thus every participant is incident to at least one contact in **both** chronological halves (first `n-2` calls and last `n-2` calls).

**Proof.** Fix a secret originally known only to `v`. At any call, the number of people who know this particular secret increases by at most one: if exactly one endpoint knows the secret, it passes to the other; otherwise the count does not change. Moving from one knowledgeable participant to all `n` therefore requires at least `n-1` calls that increase the carrier count. If the first call involving `v` is at position `f`, then all first `f-1` calls leave the carrier count equal to one. At most `k-f+1` later calls remain, so `k-f+1>=n-1`, implying `f<=k-n+2=n-2`.

For the other inequality, reverse the order of all calls. A time-respecting path from `u` to `v` in the original protocol reverses to a time-respecting path from `v` to `u` in the reversed protocol, so all-to-all temporal reachability is preserved under reversal (with the ordered source and destination interchanged). The reversed protocol still has `k` calls, so applying the first-contact result to its first occurrence of `v` implies that the last occurrence of `v` in the original schedule is at or after position `k-(n-2)+1=n-1`. QED.

**Corollary (n=4 butterfly).** At `n=4`, the first two contacts cover all four vertices and are therefore disjoint. The last two contacts also cover all four and are disjoint. Any shortest *distinct-edge* four-call gossip protocol therefore consists of two distinct perfect matchings. Their union is a four-cycle, and the first matching is temporally earlier than the second: a chronological butterfly.

**Algorithmic application:** A candidate `2n-4` schedule that omits some vertex from its first `n-2` or last `n-2` selected calls is invalid without running the full temporal-connectivity oracle. This rejection is sound under the theorem, not merely a heuristic. For arbitrary longer-than-optimal schedules the same cutoff is **not** asserted.

**Why it matters:** This pins down a global, temporal constraint on any hypothetical shortest-spanner witness. It may help prune exactly solvable fixed-chronology instances or future searches for a butterfly-free optimal schedule; it is not a proof of the butterfly hypothesis for `n>=7`.

**Prior art:** Classical minimum-gossip proofs by Baker–Shostak (1972), Kleitman–Shearer (1980), Bumby (1981), and kernel characterization by Labahn (1995) may already imply this lemma. Treat originality as unchecked.
