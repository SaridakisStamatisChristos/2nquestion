> **Stage 14 chronology scope clarification (28 October 2026):** The inequality t>=64 proven below is valid under its stated strictly sealed-arm assumption. Four full outside-X collectors alone do **not** force strict global all-arm-before-all-core ordering in the original chronology. The [Stage 14 causal sealing proof](../v3.1/CAUSAL_FOUR_ARM_BRIDGE.md) derives the same inequality from the weaker per-arm chronological property actually forced by four collectors. It then proves an expanded original 3×3 necessary condition m33>=64 with all four off-corner cells of size two and *unrestricted corner sizes*. Universal half-forest remains OPEN.

# Stage 12 — No-tight-arm theorem and universal private-recipient bottleneck

**28 October 2026 — proved conditional ALL-n LOCAL structural result. Original chronological half-forest conjecture OPEN; no universal contradiction or actual counterexample obtained.**

## Scope and definitions

Assume the precise Stage 10 sealed-arm interface: p>=2 prefix (A) rooted tree arms, q>=2 reverse-suffix (B) rooted tree arms, each arm contains **exactly one outside-X participant, its full-information root**, all its remaining vertices belong to shared cell X, and all other inter-arm calls occur later exclusively between outside-X roots. Suppose the entire unreordered full gossip chronology is successful, so for each prefix arm Ai and reverse suffix arm Bj, every Ai-source and Bj-target has an intersecting pair of information supports in Xij=Ai∩Bj∩X. All q recipient groups Xij in Ai, and all p recipient groups Xij in Bj, collectively cover the original secrets of their respective arms, as proved in Stage 10.

A participant x of Xij is **A-private in this cell** if there exists an original Ai-secret a whose ONLY terminal recipient in Xij (within the Ai internal chronology) is x. Analogously, x is B-private if a reversed-Bj secret has only x as a recipient in Xij.

## Proposition 1 — private support forces an opposing full collector (ALL n)

If x is A-private in Xij, then x must be a **complete reverse-suffix collector of Bj**. Likewise if x is B-private, x must be a complete prefix collector of Ai.

**Proof.** Choose the Ai-secret a whose support inside Xij is exactly {x}. Since the full gossip schedule succeeds, there is a time-respecting information path from a's originating participant to EVERY Bj target b. The path passes through the original cut at some v∈Ai∩Bj=Xij: a can leave the prefix component Ai only along the suffix, and in reverse Bj target information is confined to Bj. Thus for each b, a's prefix support and b's reversed-suffix support intersect in Xij. Because its prefix support within Xij is only {x}, x must belong to every reversed-suffix support; equivalently x knows all Bj original target secrets in Bj's reversed local chronology. QED.

A tree arm with m-1 contacts has at most two complete collectors, the endpoints of its last internal contact. Its outside-X root is already one collector. Therefore **AT MOST ONE** participant in Xij can be A-private, and likewise at most one can be B-private. This restriction is valid for EVERY shared subcell size, and does NOT require either arm to attain any exponential equality threshold.

## Theorem 2 — no tree arm can be tight

For any Ai, consider its q+1 disjoint complete-cover recipient groups: its outside full root as singleton, and the q intersections Xi1,...,Xiq. By the Stage 11 helper-robust exact chronological tree-cover theorem, the total number of participants in the tree arm is at least 2^q.

**The equality case is impossible in a fully successful crossed interface whenever q>=2.** Indeed Stage 11's equality rigidity says EVERY member of EVERY recipient group has a private original secret within that group. Therefore every x∈Xij is A-private, and by Proposition 1 must be a complete collector of Bj. But Bj already has its full outside root and can have only ONE complete collector inside X. Consequently each nonempty Xi1,...,Xiq would have to be a singleton. Hence Ai would have 1+q total participants; for q>=2 this is strictly smaller than 2^q. Contradiction.

Thus |Ai|>=2^q+1, i.e. its X share is at least 2^q. Summing over the p disjoint A arms,

\[
 \boxed{t=|X|\ge p\,2^q}.
\]

Time reversal gives the complementary bound t>=q 2^p. In full generality:

\[
\boxed{t\ge\max\{\,p\,2^q,\;q\,2^p\,\}\qquad(p,q\ge2).}
\]

For symmetric k-arm interfaces this is

\[
\boxed{t\ge k\,2^k.}
\]

At k=4 it strengthens Stage 11's threshold from t>=63 to **t>=64**. In the original marked 3×3 (1,1,2)/(1,1,2)/(2,2,t) four-arm rigid family, n=12+t, so the specified subfamilies are excluded up to **n=75** (t<=63). The stronger bound is NECESSARY ONLY and does not show t=64 is attainable globally.

## Crucial adversarial boundary

A tempting next claim would be: any rooted tree cover with s=3 recipient groups (outside singleton root and two groups inside X) and m=2^(s-1)+1=5 participants must have at least two privately informed recipients in one non-root group. That holds for m=5 in complete small-tree enumeration. BUT it is **false by m=6**, where an exact five-call chronological tree on participants 0..5 with root 0 and groups G1={4}, G2={1,2,3,5} has terminal local knowledge masks

\[
(63,43,20,10,63,33)
\]

for call order

\[
(2,4),\ (3,1),\ (0,5),\ (1,0),\ (4,0).
\]

Here root 0 and vertex 4 are complete, both other recipient groups collectively know all six secrets, and only one recipient in each nonroot group has a private secret. This demonstrates that unbounded slack can remove the **multiple-private** obstruction; no all-n contradiction follows from assuming it always persists.

## Independent verification

[no_tight_arm_probe.cpp](no_tight_arm_probe.cpp) independently enumerates every ordered labelled tree contact chronology with 4, 5, and 6 vertices, checks singleton outside-root and two other complete-cover recipient groups, and computes the exact minimum number of private members per group. It confirms **zero** root covers with ≤1 private member in each group at m=4,5, then checks the exact explicit m=6 six-vertex witness. It additionally evaluates the universal p/q numeric thresholds against the Stage 11 bound, deliberately retaining the **weaker** Stage 11 inequality as a separate regression fixture.

The written proof is the basis for the all-n necessary theorem; the executable evidence is falsification, not a formal proof assistant. The universal half-forest conjecture, historical novelty against the classical literature and independent refereeing remain unresolved. Keep PR #1 DRAFT/UNMERGED and submission HOLD.
