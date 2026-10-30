# Stage 8 — All-n collector-budget obstruction for large incidence grids

**27 October 2026. Mathematical statement: human proof below; independently falsified by exhaustive small-component chronologies.** The universal chronological half-forest conjecture remains OPEN. PR #1 remains DRAFT/UNMERGED. Historical novelty not established.

## New theorem

Let S be a successful bidirectional telephone gossip chronology on n>=4 participants with **exactly 2n-4 distinct calls**, and use its **original, unchanged** first and last n-2 calls. Suppose both static halves contain cycles. Let r,s (both at least 3) be the component counts of the prefix/suffix halves. Then

\[
\boxed{n\ge 2rs-4\min(r,s)+4.}
\]

Combining with the [Stage 7 symmetric surplus bound](../v2.4/TWO_SIDED_SURPLUS_THEOREM.md), this yields the stronger necessary condition

\[
\boxed{ n\ge\max\big(rs+2(r+s)-8,\quad 2rs-4\min(r,s)+4\big). }
\]

This is **not** the statement that one original half is necessarily a forest: the combined inequality is consistent with hypothetical counterexamples for arbitrarily large n.

### Lemma: collector budget of a connected chronological component

Consider a connected component of m>=2 vertices whose chronological contacts comprise exactly m-1+k edges, with nonnegative static cycle rank k. There are at most **2(k+1)** vertices that know *all m original component secrets* after these contacts.

**Proof.** Initially each of the m secrets lies at its originating vertex. Before the contact graph on these vertices becomes connected, nobody can know all the secrets: a vertex can only know secrets from the connected component of the **already used** contact graph containing it. A connected graph on m vertices requires at least m-1 distinct contacts; therefore no vertex can become a complete collector before the (m-1)-st contact. Only endpoints of a contact can gain new knowledge. Starting with contact number m-1, there are precisely (m-1+k)-(m-2)=k+1 contacts during which anyone can first become complete. At most two new complete collectors can be created by each such contact. Thus at most 2(k+1) final complete collectors. QED.

This upper bound is deliberately conservative: not every component can saturate it.

### Proof of the global incidence theorem

Let P_1,...,P_r be the prefix components and Q_1,...,Q_s the suffix components. Set M_ij=|P_i∩Q_j|. By the established component-intersection lemma, **every M_ij>=1** and the total cycle rank of all prefix components is r-2 (since the prefix has n-2 edges). Write k_i for each prefix component's cycle rank. Every singleton cell (M_ij=1) must contain a **complete prefix collector** of P_i, since its single vertex is the only entry path for that component's original secrets into Q_j after the midpoint. Because each P_i meets s>=3 suffix components, it contains at least three vertices, so the connected-component collector lemma applies. Hence, with Z the total number of singleton cells,

\[
Z\le \sum_{i=1}^{r}2(k_i+1)
  =2\big((r-2)+r\big)=4r-4.
\]

Run the same argument in reverse chronology, using the fact that a successful two-way gossip schedule remains successful under chronological reversal (temporal reachability transposes). The suffix components have total cycle rank s-2, so

\[
Z\le 4s-4.
\]

Therefore Z<=4min(r,s)-4. At least rs-Z cells are non-singletons. Each non-singleton cell contributes **at least one extra vertex** beyond the mandatory one per positive cell:

\[
n=\sum_{i,j}M_{ij}
\ge rs+(rs-Z)
\ge 2rs-4\min(r,s)+4.
\]

This proves the asserted all-n inequality. QED.

The proof uses elementary graph connectivity and the earlier **component-intersection** fact; it does **NOT** need Stage 7's deeper single-source tree-entry lemma, B/D profiles, finite orbit enumeration, Labahn's kernel classification or the outcome of a SAT solver.

## Concrete boundaries

| Component grid r×s | Stage 7 lower n | New collector-budget lower n | Combined necessary n |
|---|---:|---:|---:|
| 3×3 | 13 | 10 | 13 |
| 3×5 | 23 | 22 | 23 |
| 3×6 | 28 | 28 | 28 |
| 3×7 | 33 | 34 | 34 |
| 3×8 | 38 | 40 | 40 |
| 4×4 | 24 | 20 | 24 |
| 4×6 | 36 | 36 | 36 |
| 5×5 | 37 | 34 | 37 |
| 6×6 | 52 | 52 | 52 |
| 8×8 | 88 | 100 | 100 |
| 10×10 | 132 | 164 | 164 |

For the 3×s family this improves the previously applicable bound from n>=5s-2 (Stage 7) to n>=6s-8 as soon as s>=7. At s=6 they agree; for s<=5 retain Stage 7. For balanced grids the quadratic collector-budget obstruction becomes strictly stronger at r=s>=7.

## Adversarial numerical tests and limitations

[check_collector_budget.py](check_collector_budget.py) independently simulates **every chronological sequence of distinct unordered calls** for m=3,4,5 and cyclic excess k=0,1,2 (and k=3 where available), retains connected static contact graphs, tracks knowledge bitmasks, and checks the 2(k+1) upper bound for the number of full collectors. It also checks exact empirical maxima and counts, so weakening/truncating the verifier triggers failure.

These exhaustive small component tests are empirical checks, not the logical proof of the universal upper bound. The written proof above supplies that universal argument.

The proof is a necessary bound only and cannot imply that a counterexample exists at the displayed thresholds. The all-n half-forest conjecture, minimal-counterexample reduction, and chronological kernel classification remain **OPEN**. The novelty and implicit implication against Labahn (1995) and Krumme (1996) need historical source-level review before publication.
