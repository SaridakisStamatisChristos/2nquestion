# Stage 14 — Causal four-arm bridge: a larger unconditional *conditional-family* exclusion

**28 October 2026. Human proof of an all-n necessary condition under the stated fixed-original-midpoint hypotheses, with independent finite falsification. The full original chronological half-forest conjecture remains OPEN; no global counterexample has been found.**

## Source and quantifiers

Use the *actual original order* of all \(2n-4\) pairwise-distinct successful bidirectional calls and its fixed \(n-2\)/\(n-2\) midpoint. Richard T. Bumby, *A Problem with Telephones*, SIAM J. Algebraic Discrete Methods **2** (1981), 13–18, Theorem 3, confines any both-cyclic midpoint to prefix components \(P_1,P_2\) closed trees and \(P_3\) unicyclic, and reversed-suffix components \(Q_1,Q_2\) closed trees and \(Q_3\) unicyclic. His proof also forces the original last contact in each \(P_i\) to join \(Q_1,Q_2\), and the original first suffix contact in each \(Q_j\) to join \(P_1,P_2\). See [the primary-source audit](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md).

Let \(m_{ij}=|P_i\cap Q_j|\), and in this stage assume **only**

\[
m_{13}=m_{23}=m_{31}=m_{32}=2.
\]

The other four corner sizes are arbitrary positive integers; the center is \(X=P_3\cap Q_3\), \(t=m_{33}\).

## Adversarial finding: the strict original-chronology Stage 10 bridge is false

[Stage 10](../v2.7/FOUR_ARM_CROSSING_THEOREM.md) defines *strict* four-arm rigidity to require **every internal arm call earlier than every inter-arm call**. Four full outside collectors do **not** imply that strict original-chronology condition. Consider a connected unicyclic 16-person local chronology with four tree arms

- root 0, others 2,3,4; contacts \((0,2),(3,4),(0,3)\);
- root 1, others 5,6,7; contacts \((1,5),(6,7),(1,6)\);
- root 8, others 10,11,12; contacts \((8,10),(11,12),(8,11)\);
- root 9, others 13,14,15; contacts \((9,13),(14,15),(9,14)\).

Execute the *first two* arms, call \((0,1)\), execute the *last two* arms, then call \((8,9),(0,8),(1,9)\). Exactly roots 0,1,8,9 become complete collectors; the other twelve participants never receive a secret from another arm. But inter-arm \((0,1)\) precedes internal calls on vertices 8–15. The core root-to-root graph is a four-cycle, so no different four-arm partition with exactly these four outside participants can reclassify \((0,1)\) as internal. This refutes *only the automatic strict-order bridge*, not the Stage 10 result **conditional on its stated strict assumptions**.

**Minimal local countermodel (five vertices, five distinct calls).** A smaller example suffices:
\[
(0,1),\ (2,4),\ (2,3),\ (0,2),\ (1,3).
\]
The connected static graph has five edges and one cycle, and after the last call precisely vertices \(0,1,2,3\) know all five secrets; vertex \(4\) knows only secrets \(2,4\). The rooted arms are \(\{0\},\{1\},\{2,4\},\{3\}\), with root-core calls forming a four-cycle \(01,23,02,13\). The inter-arm call \(01\) at position 1 precedes internal arm call \(24\) at position 2, but internal \(24\) precedes both incident root-2 core contacts \(23,02\). Thus causal sealing holds while strict global sealing fails. The independent all-graph enumeration finds **zero** strict failures with four collectors at \(v=4\) and **240** non-strict histories at \(v=5\); this demonstrates that five vertices is minimal for this local strict-order falsification.

The relevant weaker property is *causal sealing*: four rooted tree arms partition a local component; all other calls join roots; **every internal call of an arm precedes every root-to-root call incident to that arm's own root**. Unrelated other-root calls may interleave. Every non-root participant then retains information originating **only in their own arm**, because there are no further calls to them after their root participates in inter-arm communication.

## Lemma 1. Four full collectors in a unicyclic chronology force causal sealing

Let a connected component on \(v\) people have exactly \(v\) distinct chronological calls, and exactly four terminal complete collectors \(u,v',w,z\). A participant cannot know all \(v\) initial secrets before the \((v-1)\)st call: the calls so far would otherwise contain a connected graph on \(v\) vertices with fewer than \(v-1\) edges. A call makes at most two *new* complete collectors. Thus **two** collectors \(u,v'\) first become complete at contact \(v-1\), and the other **two**, \(w,z\), first become complete at the final call.

The first \(v-1\) calls form a spanning tree. Removing their last edge \(uv'\) splits it into two independently contacted trees \(U\ni u\), \(V\ni v'\). Before \(uv'\), the endpoints \(u,v'\) must know all original secrets of their respective sides. The final edge \(wz\) has no endpoint in \(\{u,v'\}\). Before it, \(w,z\) still know only secrets from their respective sides: neither was touched by \(uv'\). They must lie on **opposite** sides, otherwise neither could learn secrets from the other side on the last call. Thus (renaming) \(w\in U,z\in V\), and each already completely knows their own side.

In a tree contacted once per edge, there can be at most two terminal complete collectors, and these must be the endpoints of the tree's **last** call. Hence the last \(U\)-call is \(uw\), and the last \(V\)-call is \(v'z\). Delete those two edges and the global last two edges \(uv',wz\). The remaining graph splits into four tree arms, containing the **four distinct roots** \(u,w,v',z\), one per arm. Every arm's internal calls preceded its own root's first root-to-root call; the four deleted edges have only root endpoints. Each root had collected its arm secrets before the root links. This proves **causal**, but not necessarily strict global, sealing. QED.

Commuting unrelated disjoint calls within the same original half could create a strict representative, but **this argument never replaces the actual original midpoint**.

## Lemma 2. Two crossed *causally sealed* four-arm components require \(t\ge64\)

Suppose a prefix connected component \(A\) and fully reversed-suffix component \(B\) have exactly four outside-\(X\) vertices each, and each admits a causally sealed four-arm decomposition \(A_1,\ldots,A_4\), \(B_1,\ldots,B_4\). Assume \(A\cap B=X\) and the entire **fixed original** chronology succeeds.

For any \(A_i\)-source \(a\) and \(B_j\)-target \(b\), the successful information path must cross the original midpoint at a vertex in \(A\cap B=X\). Causal sealing confines all \(X\)-carriers of \(a\) to \(A_i\) and all reversed-\(X\)-carriers of \(b\) to \(B_j\). Consequently this crossing lies in \(X_{ij}=A_i\cap B_j\cap X\), and every \(A_i\)-secret (and every \(B_j\)-secret) has a recipient there. **All sixteen \(X_{ij}\) are nonempty.**

Each arm \(A_i\) is a chronological tree whose five disjoint nonempty recipient groups comprise its full-information singleton outside root and its four \(X_{ij}\), all collectively covering its secrets. The all-n exact tree-cover theorem in [Stage 11](../v2.8/STEINER_COVER_RIGIDITY.md) gives \(|A_i|\ge2^4=16\). Equality cannot hold: its rigidity states *every recipient* \(x\in X_{ij}\) has a secret private to \(x\) within that group. Crossing every \(B_j\) target forces such \(x\) to be a complete reversed collector of \(B_j\). Yet each tree \(B_j\) has at most **two** complete collectors, one already its outside root, hence at most **one** in \(X\). Tightness would force \(|X_{ij}|=1\) for all four \(j\), and \(|A_i|=1+4=5\), contradicting 16.

So \(|A_i|\ge17\) for all four arms. Exactly one participant per arm is outside \(X\), giving

\[
\boxed{t=|X|=\sum_i(|A_i|-1)\ge4\cdot16=64.}
\]

No globally ordered arm/core-phase hypothesis was used. QED.

## Theorem. Stronger saturated-off-corner 3×3 obstruction

**If both fixed original halves are cyclic and \(m_{13}=m_{23}=m_{31}=m_{32}=2\), then \(m_{33}\ge64\), even with arbitrary positive corner multiplicities.**

Proof: Bumby's last-prefix/first-suffix spine places the two complete collectors of each reversed-suffix tree \(Q_1,Q_2\) in prefix rows \(P_1,P_2\), and the two complete collectors of each prefix tree \(P_1,P_2\) in reversed-suffix columns \(Q_1,Q_2\). Therefore neither participant of the size-two cell \(P_3\cap Q_j\) (\(j=1,2\)) can be a complete reversed collector of \(Q_j\). The exact two-point crossing lemma forces **both** participants to be complete prefix collectors of \(P_3\). Four distinct outsiders of \(X\) are thus complete in unicyclic \(P_3\), its absolute maximum. Reversing the argument, all four participants in \(P_1\cap Q_3\) and \(P_2\cap Q_3\) are complete reversed collectors of unicyclic \(Q_3\), all outside \(X\). Apply Lemma 1 to both **originally oriented local chronologies** and Lemma 2 to their crossing. QED.

In particular this family requires \(n\ge 4+8+64=76\), but **this is only a necessary condition in the stated subfamily**; it is not a global bound on a possible original both-cyclic schedule. The previous Stage 13 \(m_{33}\ge12\) bound remains valid, but is superseded for this family. The Stage 12 conditional \(t\ge64\) result itself is unchanged; this stage repairs the unjustified strict-order *applicability* step and removes the old fixed-(1,1,1,1)-corner restriction.

## Independent falsification, not an all-n certificate

[exhaustive_four_collector.cpp](exhaustive_four_collector.cpp) independently enumerates every **connected** labelled unicyclic \(v\)-edge graph and every permutation of its distinct edges for \(v=4,5,6\). For each chronology with four complete collectors it reconstructs the four arms from the last edges, tests one root per arm, exact causal precedence and absence of leaked arm secrets, and counts the failures of *strict* global precedence. It never imports Stage 10–13 oracle code. Passing these finite checks tests but does **not** prove Lemmas 1–2.

**Open:** general unrestricted 3×3 cell multiplicities and all possible local chronologies; outside peer review; formal proof assistant; prior-art originality. PR #1 must remain **DRAFT/UNMERGED**; manuscript publication HOLD.
