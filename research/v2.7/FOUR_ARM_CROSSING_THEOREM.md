> **28 October 2026 Stage 14 adversarial correction:** The *strict original chronology* claim that four complete outside-X collectors automatically imply ALL arm-internal calls precede ALL inter-arm calls is **FALSE**. A 16-vertex connected unicyclic counterexample interleaves the first root-root call before an unrelated arm finishes. The strict four-arm crossing theorem remains valid **if its strict hypotheses hold**, but the unconditional Type C applicability paragraph below is overstrong. [Stage 14](../v3.1/CAUSAL_FOUR_ARM_BRIDGE.md) proves a sufficient **causal sealing** condition directly, including a corrected four-collector decomposition and the stronger original 3×3 implication m33>=64 when all four off-corner cells equal two. The explicit countermodel is independently CI-checked. Do not use the unqualified Type C-to-strict-rigidity inference.

> **27 October 2026 Stage 11 refinement:** The t≥60 conditional necessary inequality here has been **strictly improved** for symmetric four-arm interfaces to **t≥63**, using a new [Steiner-robust exact-cover rigidity theorem](../v2.8/STEINER_COVER_RIGIDITY.md). An additional [two-person crossing lemma](../v2.8/TWO_VERTEX_CROSSING.md) rules out certain small cells and gives a separate k×k bound. The older t≥60 proof remains valid as a historical, weaker result; none of these proves the all-n original-half forest conjecture.

# Stage 10 — Four-arm crossing obstruction (all component sizes)

**27 October 2026. All-n conditional structural theorem, human proof with exact independent small-case regression. Original chronological half-forest conjecture OPEN.** This is a local incompatibility for a specific rigid two-component crossing pattern, not a universal exclusion for every r×s grid. No external proof-assistant or refereed verification is claimed.

## The four-arm interface

Consider two chronological connected local gossip components A and B that meet in a common set X of t participants. All other participants in either component are outside X; in each component there are **exactly four** outside-X participants.

A component is *four-arm rigid relative to X* if its contact chronology admits a partition into four connected **tree arms**, each containing exactly one of its outside-X participants (called the arm root) plus some X members, such that:

1. all contacts within every arm happen before all inter-arm contacts;
2. all inter-arm contacts have both endpoints outside X (so X members never acquire information from other arms); and
3. the root in each arm has learned **every original secret originating in that arm** by the end of the arm-internal calls.

The definition refers to the **original local chronological calls**, not an arbitrarily reordered graph. The outside-root singleton group and all groups inside X can be used as disjoint recipient groups.

In the original-half gossip interpretation, A is a connected component of the first half; B is a connected component of the *fully time-reversed second half*. Assume the complete schedule succeeds. Denote the four A arms by A1,...,A4 and the four B arms by B1,...,B4.

## Universal theorem: exponential crossing barrier

**Theorem (four-arm crossed-tree incompatibility).** If both A and B have the four-arm rigidity property and they intersect in the same t-person cell X, then successful original full gossip requires

\[
   \boxed{t\ge 4(2^4-1)=60.}
\]

More generally, if the first component has p such tree arms and the reversed second component has q such tree arms, the same argument proves

\[
 t\ge q(2^p-1).
\]

Because reversing any successful full bidirectional gossip schedule remains successful, reversing the roles gives the further bound \(t\ge p(2^q-1)\), so for an actual successful original chronology:

\[
\boxed{t\ge\max\{q(2^p-1),\ p(2^q-1)\}.}
\]

### Proof

Fix an original secret \(\sigma\) belonging to any B arm \(B_j\). Before/after that component's arm-to-arm contacts, **no X member changes knowledge across B arms**, because all inter-arm contacts have outside-X endpoints. Consequently the set \(D_X(\sigma)\subseteq X\) of X participants who know \(\sigma\) after B's local chronological calls is contained entirely in \(B_j\cap X\).

By the full gossip requirement across the original midpoint, **every subset of X receiving a particular secret from B must collectively possess ALL original secrets of the A component at the original midpoint**. This is the established exact cellwise B/D necessary condition: \(B_A(D_X(\sigma))=1\). In particular, the set \(D_X(\sigma)\) must meet **each A arm**. Indeed the A arm root's original secret is outside X, and no member of X outside that A arm can learn it during A's local calls: the only later links between arms have endpoints outside X. A subset of X that misses one A arm therefore cannot collectively contain all A secrets.

For each fixed B arm \(B_j\) and each A arm \(A_i\), the X members in \(B_j\cap A_i\cap X\) consequently collectively know **every original secret of \(B_j\)** after B's arm-local calls. They must be nonempty. Moreover the B arm root (outside X) knows all B-arm secrets after its internal calls by condition (3).

Thus the participants in the B arm can be partitioned into **p+1 disjoint, nonempty, collectively complete recipient groups**: the singleton outsider root, plus its p intersections with the A arms within X. Since internal B-arm contacts form a tree using exactly \(|B_j|-1\) pairwise distinct calls, Stage 9's sharp all-n chronological-tree cover theorem gives

\[
 |B_j|\ge 2^{(p+1)-1}=2^p.
\]

Every B arm contains exactly one outside-X root, so its own share of X has size at least \(2^p-1\). Summing the q disjoint B arms yields \(|X|=t\ge q(2^p-1)\). Reverse the successful full schedule to obtain the symmetric bound, which proves the theorem. QED.

This is a **necessary-condition theorem**. There is no claim that t=60 is globally attainable; additional incompatibilities may make these configurations impossible at every t.

## Rigidity of the two actual local types (2,2,t)

Let a component have two designated outside-X cells of size two each, and a large intersection cell X of size t, so its group sizes are (2,2,t).

**Type T (connected tree; two complete collectors in one outside two-cell).** The final tree contact must join the two collectors. Just before it, the tree has two disjoint sides. The *other* outside two-cell has two members collectively knowing the entire component at termination and is not touched by the final contact; therefore those two vertices lie in different sides and each already knows every secret of their own side. Together with the designated final collector on each side, they are two complete collectors within each side tree; hence the final internal call of each side joins those two outside-X vertices. Delete the final global edge and two side-tree final edges. This leaves **four rooted arms**, each with one outside-X member, with all inter-arm calls later and outside X. The local roots are complete for their arms, so Type T is four-arm rigid.

**Type C (connected unicyclic m-contact component; all FOUR outside-X participants are complete collectors).** Before its last two calls the used contact graph must consist of exactly two disjoint trees, since otherwise no vertex can become complete before the last call and at most its two endpoints become complete. The last two calls must involve all four designated collector participants; the first joins the two pre-existing sides, and both first-call endpoints must already know all information within their own side. Likewise the other two collectors, to become complete at the end, must already know their respective side. Both trees therefore have two complete outside-X collectors, and their last internal call joins those collectors. Deleting these two internal final contacts leaves **four rooted arms**, with all subsequent links exclusively between outside-X participants. Type C is four-arm rigid.

The first reduction uses the extra *cellwise coverage* premise for the other size-two cell and cannot be applied to a generic tree with only two collectors. The second uses **all four** outside-X vertices being full collectors and cannot be applied to a generic unicyclic component merely because it has a cycle.

Thus **any pair of Type T/C components** sharing the same t-person cell X and satisfying the original successful-gossip profile-compatibility condition must have t>=60. This includes tree/tree, tree/four-collector-cycle, and four-collector-cycle/four-collector-cycle crossed pairs. It subsumes the exact n16 and n17 small-t obstruction mechanisms in the (2,2,t) subfamily.

## Application to an infinite matrix family

For the original 3×3 incidence matrix

\[
M=\begin{pmatrix}
1&1&2\\
1&1&2\\
2&2&t
\end{pmatrix}\quad(t\ge1),
\]

the third prefix row and third reversed-suffix column both have local groups (2,2,t), sharing their large cell X of size t. Whenever both are of Type T or Type C with the stated **exact** collector requirements, the crossed-tree theorem forces \(t\ge60\). In particular the marked subclasses with both first row/first column cyclic and the third row/column being the forced two-collector trees (the family previously represented by n17 orbit 30), or both third row and column cyclic with all four outside X collectors forced (previously orbit 31), are impossible whenever t<=59, corresponding to n=12+t<=71.

**Do not generalize this to every cyclic-row/cyclic-column marking or every 3×3 matrix.** The special four-arm premises are essential. The conclusion does not imply all-n half-forest, even though it eliminates a parameterized family of candidate obstructions.

## Executable adversarial corroboration

- [crossing_barrier_check.py](crossing_barrier_check.py) constructs sharp **root-excluded five-group** chronological tree-cover examples on sixteen vertices (one full collector outside X, four disjoint nonempty X groups covering every arm secret). The construction proves the derived per-B-arm lower bound |B_j|>=16 is attained as an isolated local tree property, without suggesting four such arms can be globally assembled into gossip.
- The same program independently checks the exact Type T / Type C small-t chronological local B/D domain contradictions already recorded for t=4,5 using the preserved exact oracle module, and exhaustively verifies finite arm-intersection capacity identities and the t=59/60 boundary.
- [research-v27.yml](../../.github/workflows/research-v27.yml) is a fail-closed CI gate for these boundary/equality/local regressions.

## Status and gap

**Four-arm crossed-tree necessary bound:** human proof with explicitly stated hypotheses; CI can corroborate sample regimes but not mathematically quantify over all t. External peer review/formal-assistant certification not performed. **Universal original-half forest conjecture:** OPEN. **Novelty vs historical gossip/kernel results:** UNRESOLVED. **PR:** DRAFT, UNMERGED. **Publication:** HOLD.

The next universal bottleneck is proving that *every* both-cyclic hypothetical chronology contains an incompatible crossed pair, or producing a valid counterexample whose local components avoid this four-arm rigidity. Neither is established here.
