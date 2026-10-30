# Stage 33 — exact all-n zero-privacy feasibility in a TWO-person recipient group

**28 October 2026. New all-n helper-robust chronological TREE theorem with an explicit infinite family of exact constructions. It improves the original n22 necessary 3×3-incidence frontier, not a global 2n−4 minimum-gossip schedule theorem or 2n−3 temporal-clique spanner solution. Manuscript HOLD and PR #1 DRAFT/UNMERGED.**

## Theorem 33.1 — exact sharp zero-private threshold for group sizes (a,b,2)

Let T be an edge-once chronological spanning tree with original secret at each participant and three nonempty **pairwise disjoint** designated recipient groups \(G_1,G_2,C\) of sizes \((a,b,2)\). Other people, if any, are unassigned helpers. Assume EACH group *collectively* covers all original T secrets after all edge contacts. Call a member \(z\in C\) private if some original T secret is known by z but not by the other member of C.

Then

\[
\boxed{\exists\text{ such a chronology with ZERO private C members}\quad
\Longleftrightarrow\quad a\ge2,\ b\ge2,\ a+b\ge6.}
\]

The necessity is true even with **arbitrarily many helpers**; the matching sufficiency constructions use **zero helpers**, and the graph is always a genuine edge-once tree. Therefore the lower bound

\[
p_C\ge1
\quad\text{whenever }a=1\text{ or }b=1\text{ or }a+b\le5
\]

is a sound all-n *universal* private-recipient forcing rule for every already-admissible chronological tree with the stated group sizes.

### Proof — necessity

Suppose C={u,v} collectively covers all original secrets and **neither u nor v is private**. Since any original secret has ≥1 C carrier and neither has a unique carrier, **BOTH** u and v know every original secret: they are two terminal complete tree collectors.

In an edge-once chronological tree, two complete collectors must be the endpoints of its **actual last chronological contact uv**. Deleting uv gives two disjoint chronological tree histories \(U\ni u\) and \(V\ni v\), with no earlier call between them. Because neither endpoint of uv lies in G1 or G2, **every G1/G2 participant's knowledge remains unchanged at this final call** and depends only on secrets from its own side. Consequently the nonempty groups \(G_1\cap U,G_2\cap U\) collectively cover all U secrets; likewise \(G_1\cap V,G_2\cap V\) cover all V secrets. The side roots u,v are complete within their own sides before uv (otherwise they could not be globally complete afterward).

In each side W, the three nonempty pairwise disjoint complete-cover recipient groups
\[
\{r_W\},\quad G_1\cap W,\quad G_2\cap W
\]
have **at least four designated recipients** by the helper-robust 3-group chronological tree-cover bound [Stage11](../v2.8/STEINER_COVER_RIGIDITY.md). Therefore
\[
|G_1\cap W|+|G_2\cap W|\ge3\qquad(W=U,V).
\]
In particular each G1 and G2 must meet BOTH sides; hence \(a,b\ge2\). Summing yields \(a+b\ge6\). The proof holds for arbitrarily many helper participants and preserves all actual last-edge order constraints. QED.

### Proof — sufficiency with an exact infinite construction

For any \(a,b\ge2\) and \(a+b\ge6\), split the two designated groups across two disjoint side trees so that **each side has ≥1 member of each group and total ≥3**, possible exactly under these inequalities. One explicit choice: if b≥3, place (aU,bU)=(1,2) and (aV,bV)=(a−1,b−2); if b=2, use (2,1) and (a−2,1), feasible since a≥4.

Build each side on root r (eventually the C member u or v). Let H be whichever of its G1/G2 recipient sets contains ≥2 people; let g be one member of the opposite recipient group. Select distinct h1,h2∈H. For every additional recipient z in either group, make the early call (z,r), then make exactly the three contacts
\[
(r,h_1),\quad(g,h_2),\quad(r,g).
\]
The root r and the opposite designated singleton g become full collectors of **every side-local original secret**, and H collectively covers every side-local secret via h1,h2; any extra designated leaf already knows its own original secret and passes it to the root early. No repeated edges or static cycle arise. Both opposite side recipient groups therefore collectively cover all side-local secrets.

Finally make ONE contact (u,v) joining the two disjoint side trees. Now u and v become full collectors of ALL global original secrets and C={u,v} has zero private recipients. The G1 and G2 participants do not take part in (u,v) but each group has recipients in BOTH sides, and each side subset collectively covers that side's secrets, so both groups globally cover ALL secrets. There are precisely N−1 distinct calls, and their graph is connected and acyclic. This construction works for every allowed a,b, with no helpers. QED.

**Scientific distinction:** This theorem characterizes whether **ZERO private recipients** can occur. It does NOT compute the entire minimum private count in forbidden classes, which may be >1. The sound inference used below is only ≥1 when zero privacy is impossible.

## Application to the true fixed ORIGINAL 3×3 midpoint

Let an opposite-chronology closed chronological TREE have recipient groups of sizes (a,b,c), with c its offcorner crossing cell, and let its TWO other groups be disjoint corner cells. By exact original-source / reverse-target support intersection, a C-private source must be a full collector of the opposite unicyclic local component. Thus Theorem33.1 adds the genuinely all-n conservative privacy bound
\[
\boxed{c=2,\ [\,a=1\ \lor\ b=1\ \lor\ a+b\le5\,]\quad
\Longrightarrow\quad
\text{at least ONE full opposite-cyclic collector in C}.}
\]

This complements [Stage29's exact (1,1,c) theorem](../v4.6/PRIVATE_THRESHOLD_THEOREM.md). It never overrules or weakens the 16 prior exact small-tree minima; unknown types without this proven new condition still contribute ZERO.

Combine only with the [Stage32 center-root bootstrap](../v4.9/CENTER_ROOT_BOOTSTRAP.md), not with an unjustified general sufficiency assumption about incidence.

## Executed matrix counts (necessary conditions only)

[Stage33 independent checker](two_recipient_zero_privacy.py) provides a construction factory for every \(2\le a,b\le11\), a+b≥6: 97 actual distinct-edge tree chronologies, each replayed with exact bitsets to prove C's two people full and both other groups collectively complete. It imports the exact earlier Stage25/26/28/32 predicates, applies the *proven* new privacy lower bound only when its assumptions hold, and checks classification monotonicity.

| n | Stage32 labelled survivors | Stage33 labelled survivors | excluded now | surviving tree-row/column orbits |
|---:|---:|---:|---:|---:|
| 21 | 0 | 0 | 0 | 0 |
| 22 | 32 | **24** | **8** | **7** |
| 23 | 804 | **732** | **72** | **191** |

All remaining **24** n22 necessary-profile matrices have **center size at least FOUR**, with size distribution center4:20 and center6:4. They occupy just seven legal S2×S2 orbits, not seven fully realized 40-call gossip schedules. A new real original-order impossibility argument is still necessary for those seven orbits.

The central exact claim is a HUMAN all-n proof plus finite independent falsification, **not formal Lean/Coq verification**. CI source: [Stage33 workflow](../../.github/workflows/research-v50.yml); check actual run status at the matching current commit before claiming passed. Novelty against Bumby/Labahn/Krumme remains UNVERIFIED. Primary 2n−3 spanner conjecture remains OPEN; PR OPEN, DRAFT, UNMERGED.
