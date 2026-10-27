# Stage 11 — Steiner-robust tree-cover and exact equality rigidity

**27 October 2026. Status: complete human proofs of two ALL-n LOCAL lemmas and a stronger conditional crossed-arm obstruction. This is NOT an all-n proof of the chronological half-forest conjecture. PR #1 remains DRAFT/UNMERGED; novelty vs classical work is UNRESOLVED.**

## Theorem A — Number of actual recipients, even with unused helpers

Let T be ANY chronological connected tree on m>=1 participants, with each of its m−1 unique edges called exactly once. Initially each participant knows only their own secret. Let G1,...,Gs be pairwise-disjoint nonempty subsets of participants, not necessarily covering the vertex set. They represent s *designated recipient groups*; the remaining u=m−Σ|Gj| participants are helpers belonging to no group. Suppose after all tree calls EVERY group collectively knows all m secrets. Then

\[
\boxed{\sum_{j=1}^{s}|G_j|\ge 2^{s-1},\qquad m\ge 2^{s-1}+u.}
\]

**Proof (all s; actual chronology, not reordered).** The s=1 case is immediate since G1 is nonempty. Let s>=2 and consider the chronologically LAST contact xy. Removing its edge partitions the tree into U and V with x in U, y in V; all previous calls took place within the respective sides. Put a=group index of x (if x is unassigned, use an arbitrary non-null sentinel a), b=group index of y (similarly). We may **not** assume x or y are assigned to a recipient group.

For every j≠b, the participants Gj∩U must collectively contain EVERY U-secret after the internal U calls: no member of Gj∩V can have received a U-secret after the final contact (only y on the V side can acquire one, and y∉Gj). Consequently all the s−1 sets Gj∩U for j≠b are nonempty and cover all U-secrets, provided b indexes one of the s designated groups. If y is unassigned, **choose any b∈{1,...,s}**: y is not in any group, so this same conclusion holds for all j≠b. Apply the induction hypothesis to the U subtree with these s−1 groups. The number of *designated recipients* in U among j≠b is at least 2^{s-2}.

Similarly, choosing a to be x's group or an arbitrary group if x is unassigned, the designated recipient count in V among j≠a is at least 2^{s-2}. These two counted sets are disjoint, so the TOTAL number of designated recipients is ≥2^{s-1}. Helpers cannot improve this bound. QED.

### Equality rigidity

Suppose there are no helpers and m=2^{s-1}, with s>=2. Then:

**(R1)** The last-edge endpoints x and y belong to two **different** designated groups Ga,Gb, respectively. The group Ga is confined to U; Gb is confined to V; each half of the tree has exactly 2^{s-2} vertices, with its own valid equality (s−1)-group tree cover.

**(R2)** Exactly two designated groups are singletons, namely Ga={x} and Gb={y}. They contain the tree's **only two complete collectors**.

**(R3)** Every designated recipient v∈Gj has a **private secret**: some original secret σ is known after all calls by v and by NO other member of Gj.

**Proof.** Tightness of the induction inequality forces equality in both U and V designated recipient counts. It also forces every designated participant in U to belong to one of the U counted groups j≠b, hence Gb∩U=∅, and likewise Ga∩V=∅. Since x∈Ga and y∈Gb (a≠b; equality rules out an unassigned endpoint), each group is confined to its own side. All 2^{s-1} participants are recipients, so |U|=|V|=2^{s-2} and both restricted (s−1)-group covers are equality cases.

Group Gb occurs only in V. For Gb to know each original U-secret after the final contact, x had to know every U-secret before it; likewise y knew every V-secret. Thus x and y are complete collectors of their respective side trees. Inductively, in an equality (s−1)-group tree cover, each full collector is a singleton recipient group; therefore Ga={x} and Gb={y}. All other groups Gj, j≠a,b, must have nonempty members in BOTH U and V (their knowledge must cover both sides and their vertices never participate in the last call), so |Gj|>=2. There are exactly two singleton groups. Since no third participant can gain all component secrets after the last edge, x,y are also the only full collectors of the whole tree.

For R3, use induction on s. Each singleton group is trivially private. For a non-singleton group Gj with j≠a,b, its U and V portions are separate recipient groups of the two equality subinstances. Every v in Gj∩U has by induction a secret originating in U that only v knows *within Gj∩U*. No Gj∩V participant learns a U-secret at the final contact (its V endpoint y belongs to Gb), so that same secret remains private within all of Gj. The V case is symmetric. QED.

**Important proof nuance:** Theorem A's induction works even with unassigned last-edge endpoints because we choose an arbitrary omitted group on the opposite side; for equality there are no helpers, so the last endpoints must belong to actual groups. Equality requires no omitted-group participants on the opposite side. It does NOT claim a partially covered tree, or a chronology with repeated edge contacts, has R1-R3.

## Theorem B — Crossed-arm rigidity cannot be simultaneously tight

Assume the [Stage 10 sealed-rooted-arms interface](../v2.7/FOUR_ARM_CROSSING_THEOREM.md) with the SAME integer number k>=2 of A arms and B arms, with one outside-X full root per arm, and all inter-arm contacts occurring later solely between outside roots. Assume the actual complete bidirectional gossip schedule succeeds, so exact cross-half B/D information compatibility holds. Let X be the shared cell with t=|X| participants. Then

\[
\boxed{ t \ge k(2^k-1) + (k-1).}
\]

In particular for FOUR crossed arms,

\[
\boxed{t\ge 4(2^4-1)+3=\mathbf{63}.}
\]

This strengthens Stage 10's earlier conditional t>=60. It is a lower bound under exactly the same **local arm decomposition** assumptions, not an assertion that every both-cyclic chronology has four-arm rigidity.

### Complete proof (arbitrary k>=2)

Write A1,...,Ak for first-half arms and B1,...,Bk for reversed-second-half arms. Every X vertex belongs to one A arm and one B arm. Let Xij=Ai∩Bj∩X and m_ij=|Xij|. Stage 10's exact B/D argument proves that every Xij is **nonempty**, and in each Ai the singleton outside root plus the k disjoint groups Xi1,...,Xik collectively cover ALL Ai original secrets. The same is true for each Bj with X1j,...,Xkj.

Every arm has tree contacts. By Theorem A with s=k+1 and no helpers, every arm has at least 2^k vertices. Therefore every A-row and B-column satisfies

\[
 \sum_j m_{ij} \ge 2^k-1,\qquad
 \sum_i m_{ij} \ge 2^k-1.
\]

Set δ_i = (Σ_j m_ij)−(2^k−1)>=0 and ε_j similarly. Both total \(\sum_i δ_i=\sum_j ε_j=t-k(2^k-1)=D\).

Call an A arm *tight* when δ_i=0 and a B arm *tight* when ε_j=0. For a tight arm, Theorem A's equality rigidity R2 says its (k+1) recipient groups have exactly two singleton groups. One is its outside root; hence **exactly one** Xij in that arm is singleton. Rigidity R3 says **every** participant of ANY Xij in a tight arm has a private secret from that arm, relative to all other participants in Xij.

**Cross-cell lemma:** If Ai and Bj are both tight, then m_ij=1. Otherwise choose two distinct participants x,y∈Xij. Equality rigidity provides an Ai-arm original secret α known within Xij only to x, and a Bj-arm original secret β known within Xij only to y (the latter is a *reversed suffix recipient secret*). Because X members in Ai cannot acquire A secrets from different A arms after their internal calls, the set of X carriers of α lies within Ai. Likewise the set of X reverse carriers of β lies within Bj. Thus any X vertex jointly carrying α at the original midpoint and β under reversed suffix chronology would have to belong to Xij, but the private-witness supports inside Xij are the DISJOINT singleton sets {x} and {y}. This contradicts exact full-information temporal reachability B/D compatibility. Hence every tight-tight cell is singleton.

Suppose for contradiction D<=k−2. Since every non-tight arm has integer δ>=1, there are at least k−D>=2 **tight A arms** and at least k−D>=2 **tight B arms**. Choose one tight A arm Ai and two distinct tight B arms Bj,Bℓ. By the crossed-cell lemma both Xij and Xiℓ are singleton X-recipient groups. But equality rigidity R2 for Ai allows **only one** singleton X group (the other singleton group is the outside root). Contradiction. Thus D>=k−1, giving t>=k(2^k−1)+(k−1). QED.

### Why this is not a universal forest proof

The theorem neither proves every 3x3 incidence includes k=4 sealed-crossing components, nor excludes t>=63 inside this rigid family. In particular, large-t arms have positive slack and R1–R3 need not apply to them. The successful existence of a local rooted equality tree is not the same as successful global two-half gossip.

## Independent falsification checks

[rigid_cover_check.py](rigid_cover_check.py) is a separate small-tree exhaustive checker and constructor. It:
- exhaustively enumerates every ordered labelled tree on m=2,3,4,5 vertices and all assignments of each participant to s nonempty recipient groups OR unused helper status, for s<=3; verifies the robust **number of assigned recipients** lower bound for every valid cover;
- tests equality rigidity, exact two singleton groups and **private-secret witnesses** for all enumerated equality instances;
- constructs and validates recursively sharp equality covers for s=1,..,8, confirming singleton counts and explicit private witnesses;
- tests the exact integer D>=k−1 statement by independently scanning nonnegative row/column slack compositions for k=2,..,7 and computing the tight×tight cell contradiction, and pins k=4 boundary 60..62 as impossible within the full-information crossed-arm model.

These computations corroborate—but cannot replace—the universally quantified human proofs. The half-forest conjecture remains OPEN.
