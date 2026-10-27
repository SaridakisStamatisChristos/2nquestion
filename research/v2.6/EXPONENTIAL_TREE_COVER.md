# Stage 9 — An exact exponential information-cover theorem for chronological trees

**27 October 2026. Result: human-checkable ALL-n theorem plus exact equality constructions and exhaustive adversarial small-tree tests. NOT an all-n proof of the original chronological half-forest conjecture.**

## 1. Universal exact local theorem

Fix an integer \(s\ge1\). Let \(T=(V,E)\) be a connected tree on \(m\) labelled vertices. Make exactly \(m-1\) bidirectional gossip calls, once along every edge of \(T\), in an arbitrary chronological order. Initially vertex \(v\) alone knows its secret \(v\). Partition the vertices into \(s\) nonempty, disjoint **recipient groups** \(G_1,\dots,G_s\). Assume that **after all calls** each group collectively knows all \(m\) original secrets:

\[
\forall j,\quad\bigcup_{v\in G_j} K_v=V.
\]

**Theorem (exponential tree-cover lower bound, exact).**

\[
\boxed{m\ge 2^{s-1}.}
\]

For every \(s\ge1\), equality is attained by an explicit recursively generated legal tree-call chronology, so the bound is **sharp for this local tree-cover problem**.

### Proof of the lower bound, without solver assumptions

Write \(f(s)\) for the smallest \(m\) in such an instance; existence follows from the recursive construction below. Clearly \(f(1)=1\).

For any instance with \(s\ge2\), take its *chronologically last* edge \(xy\). Because the contact graph is a tree, deleting \(xy\) separates it into two nonempty components \(U,V\), with \(x\in U\) and \(y\in V\). Before the last call **no U-secret has reached V and no V-secret has reached U**. After that call, \(x\) and \(y\) are the *only* vertices that might have learned secrets from the opposite side.

Let \(b\) denote the recipient group that contains \(y\). For **every** group \(G_j\) with \(j\ne b\), every U-secret must already be represented among vertices in \(G_j\cap U\) *before the final call*: its holders inside \(V\) cannot have received it (the sole possible new recipient in \(V\) is \(y\), which is not in group \(j\)); the new U-secret knowledge of \(x\), if any, cannot originate at \(y\), whose knowledge before the call contains no U-secret. Consequently the \(s-1\) nonempty disjoint subsets \(G_j\cap U\), \(j\ne b\), each collectively cover **all U-secrets** after the internal calls on U.

These subsets may leave some U-vertices unassigned (those in \(G_b\cap U\)); arbitrarily *absorb* such vertices into any of the \(s-1\) recipient subsets. Enlarging a collectively covering group cannot invalidate its coverage. We obtain a genuine partition of \(U\) into \(s-1\) nonempty groups whose union-of-knowledge condition holds after exactly \(|U|-1\) internal tree contacts. Therefore \(|U|\ge f(s-1)\).

The identical argument on \(V\), excluding the group containing \(x\), gives \(|V|\ge f(s-1)\). Thus \(f(s)\ge2f(s-1)\). With \(f(1)=1\), induction yields \(f(s)\ge2^{s-1}\). Importantly, the proof works **even when x and y lie in the same recipient group**; their groups simply get excluded in their respective subproblems. QED.

### Explicit equality construction

For \(s=1\), take one vertex, no calls, one recipient group, and mark that vertex as a *complete root collector*.

To build an \(s\)-group instance from a rooted \((s-1)\)-group instance \(H\) on \(h=2^{s-2}\) vertices, take **two disjoint copies** U,V of H, perform all calls inside U and V in their original order, then call their two designated full root collectors \(x\in U\), \(y\in V\) exactly once.

Relabel U's root group as group 0 and V's root group as group 1. For each other original group \(j=1,\dots,s-2\), combine its U and V copies into group \(j+1\). After the final call, x and y know all \(2h\) secrets, so groups 0 and 1 are collectively complete. For each \(j\ge2\), its two copies collectively cover the original secrets of U and V, respectively. The final graph is a tree with \(2h-1\) **distinct calls**, and x is again a full root collector in group 0.

Inductively the construction has \(m=2^{s-1}\) vertices and satisfies every group-cover condition. QED.

## 2. General global consequence for the original chronological gossip conjecture

Consider a hypothetical successful **minimum-call** n-participant gossip schedule with exactly \(2n-4\) **pairwise-distinct** calls, in which both original chronological halves are cyclic. Let \(r,s\ge3\) be their respective connected-component counts. Their prefix components \(P_1,\dots,P_r\) meet every suffix component \(Q_1,\dots,Q_s\) in a positive number of vertices, by the existing component-incidence lemma.

Every **prefix tree component** \(P_i\) must, at the original midpoint, have the original secrets of \(P_i\) collectively represented **inside each** of its s nonempty intersections with the suffix components: otherwise that secret could never subsequently reach all the vertices of that suffix component. This is the established cellwise-coverage lemma, not an added modelling assumption.

The local tree-cover theorem therefore forces

\[
|P_i|\ge 2^{s-1}.
\]

The prefix has n-2 calls and r components, so its total cycle rank is r-2; hence **at least two prefix components are trees**. Every other prefix component meets each suffix component and has at least s vertices. Summing sizes across the disjoint prefix components gives

\[
n\ge 2\cdot 2^{s-1}+(r-2)s
=\boxed{2^s+(r-2)s}.
\]

By reversing the complete bidirectional telephone-gossip chronology, which transposes temporal information reachability and preserves success, the suffix has at least two tree components and we similarly obtain \(n\ge2^r+(s-2)r\).

**Corollary (new necessary exponential incidence obstruction).**

\[
\boxed{
n\ge \max\!\left\{
2^s+(r-2)s,\;
2^r+(s-2)r
\right\}
}
\]

for all n and r,s as above. Combine this with the independent Stage 7 and Stage 8 inequalities:

\[
\boxed{
n\ge\max\left\{
rs+2(r+s)-8,\;
2rs-4\min(r,s)+4,\;
2^s+(r-2)s,\;
2^r+(s-2)r
\right\}.
}
\]

The local exponential bound needs **neither** the single-source entry lemma nor B/D compatibility, a SAT solver, classic kernel classification, or an assumption about chronological reorderings. The global step uses only the elementary positive-incidence and time-reversal lemmas.

### Consequences (necessary bounds; not realizability claims)

| Component incidence | Stage 7 | Stage 8 | New exponential bound | Combined minimum n |
|---|---:|---:|---:|---:|
| 3×3 | 13 | 10 | 11 | 13 |
| 3×4 | 18 | 16 | **20** | **20** |
| 3×5 | 23 | 22 | **37** | **37** |
| 3×6 | 28 | 28 | **70** | **70** |
| 3×7 | 33 | 34 | **135** | **135** |
| 4×4 | 24 | 20 | 24 | 24 |
| 5×5 | 37 | 34 | **47** | **47** |
| 6×6 | 52 | 52 | **88** | **88** |
| 8×8 | 88 | 100 | **304** | **304** |
| 10×10 | 132 | 164 | **1,104** | **1,104** |

This immediately proves that **no 3×4 or 4×3 both-cyclic original-midpoint chronology exists for n=18 or 19**. Consequently, together with the other displayed bounds, any hypothetical both-cyclic chronology on n=18 or 19 **must** have exactly r=s=3 components (this does NOT show that such a 3×3 chronology exists). Furthermore, since r,s>=3, the two exponential inequalities imply **r,s < log_2(n)**. Thus the number of components in each half of a hypothetical counterexample is O(log n), an unbounded but much smaller structural frontier than rs<=n alone. Stage 6 had established nonexistence of this rectangular geometry through n=17 with a different proof. The 3×3 geometry may still be structurally possible for n=18 or 19, so these conclusions do **not** settle the full n=18 or n=19 cases.

## 3. Independent executed verification

- [Tree-cover exhaustive C++ falsifier](check_tree_cover_small.cpp) enumerates **every labelled tree** on 4–7 vertices (Prüfer sequences) and every chronological permutation of its \(m-1\) distinct contacts. It checks a *necessary-and-sufficient* small-m condition for the existence of four disjoint collectively complete groups, based on full-information singleton collectors and disjoint covering pairs. It asserts no four-group tree-cover instance exists below eight vertices. The run covers **96 + 3,000 + 155,520 + 12,101,040 = 12,259,656** complete ordered tree histories, without inheriting the rooted-tree DP or the Stage 7 profile oracle.
- [Equality construction checker](construct_tree_cover_equality.py) builds explicit optimal \(s=1,\dots,8\) instances, checks tree edge counts, full-information group coverage, designated full root collectors, and the exact \(2^{s-1}\) sizes. In particular it constructs a valid eight-vertex, seven-call, four-group cover instance. The construction is *not* a successful full gossip schedule on its own.
- Both checks are CI-gated in [research-v26.yml](../../.github/workflows/research-v26.yml).

The universal conclusion rests on the **human induction**, not on extrapolating the finite tests.

## 4. What this does not prove

The general half-forest conjecture remains **OPEN**: 3×3 incidence already permits arbitrarily large n at the level of these necessary bounds. No finite bound on the minimal counterexample, no universal descending reduction preserving both original chronological cycle ranks and success, and no exhaustive classical-kernel consequence is established. The theorem is a significant **local exact extremal bound and global necessary condition**, not a universal exclusion of both-cyclic chronologies.

Historical novelty relative to earlier gossip/broadcast group-cover bounds has not yet been checked; do not claim first discovery or submit pending that audit. Maintain PR #1 DRAFT/UNMERGED.
