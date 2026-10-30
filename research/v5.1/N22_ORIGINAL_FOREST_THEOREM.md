# Stage 34 — candidate n=22 ORIGINAL chronological half-forest theorem

**28 October 2026. Complete human proof GIVEN the cited earlier all-n fixed-original-order lemmas and the exact finite incidence oracle; machine-executed finite checks are required separately. Not a Lean/Coq-certified theorem, independent referee finding, universal half-forest result or proof of the original 2n−3 temporal-clique spanner conjecture. Novelty unverified. PR #1 DRAFT, UNMERGED; manuscript submission HOLD.**

## Precise statement

**Theorem 34.1 (conditional human proof, n22).** Let \(S=(e_1,\ldots,e_{40})\) be a successful bidirectional telephone gossip chronology on **exactly 22 people**, with **40 pairwise-distinct unordered calls**. Then at least one of the two **ORIGINAL** fixed halves
\[
(e_1,\ldots,e_{20}),\qquad(e_{21},\ldots,e_{40})
\]
has an acyclic undirected static contact graph, provided the cited original chronological structure and tree-cover lemmas hold as stated. Calls are not reordered, commuted, relabelled across their chronological slots or extended. The full theorem for unrestricted n≥23 is OPEN.

**Historical scope warning:** Bumby 1981, Labahn 1995, Krumme 1996 and more recent literature may imply comparable results, but external originality has NOT been established. This is a repository research theorem, not a priority announcement.

## Canonical contrary structure

Assume both ORIGINAL 20-call halves cyclic. By [Bumby 1981 Theorem 3 and original last-contact spine](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md), the original prefix has exactly two closed chronological trees P1,P2 and a unicyclic component P3, while the **fully reversed actual suffix** has two chronological trees Q1,Q2 and a unicyclic component Q3. They form nine positive intersection cells \(m_{ij}=|P_i\cap Q_j|\), with all four offcorner cells ≥2. Every P3 local original secret support in center \(X=P_3\cap Q_3\) meets EVERY Q3 reverse-target support there, and likewise for the four other crossings. The ACTUAL final local calls of P3 and reversed Q3 join their respective exterior cells and never touch X; deleting them gives original-ordered spanning chronological trees TP,TQ. Neither original half is cyclic by mere recolouring or event rearrangement: this is a fixed midpoint contradiction argument.

The exact independent Stage27 stars-and-bars oracle enumerates all
\[
\binom{22-13+8}{8}=24,310
\]
labelled necessary positive 3×3 incidence matrices. Each earlier rejection uses a cited **all-n original-chronology** necessary lemma, not mere size intuition. The proof dependency DAG (all in repo) is:

Bumby fixed-order 3×3 spine
→ Stage11 helper-robust tree recipient cover + Stage15 equality rigidity
→ Stage17 all-n offcorner double carrier
→ Stages19–26 original small-center and exact tree privacy exclusions
→ Stage28 eight-exterior center-root exclusion
→ Stage32 two-outside-collector center-root bootstrap
→ Stage33 exact (a,b,2) zero-private threshold
→ Stage34 dual tree-cover/private-support lemmas below
→ n22 zero-incidence census.

**Each imported historical/source theorem and human proof remains a separate verification obligation.** A CI check validates finite predicates, not the validity of every imported mathematical hypothesis.

## New key lemma 34.2 — untouched exterior collector forces two *tree* collectors (ALL n)

Let U be an edge-once chronological unicyclic local component whose LAST local call e=ab lies between exterior cells A,B, outside center X. Suppose some terminally complete U collector \(r\notin X\) does **not** participate in e.

Then r was already a complete U collector at the end of the preceding spanning edge-once chronological tree T=U−e. A tree with at least one complete terminal collector has **exactly two**: the endpoints of its ACTUAL last tree call, because both acquire the same terminal knowledge and no other person could have acquired every original secret before the final tree edge that first connects the static graph. If U has **no complete center collector**, both of T's last-call endpoints lie OUTSIDE X.

**Critical nuance:** a chronological tree need NOT have ANY complete collector (an arbitrary edge order can leave zero). We infer the pair of tree collectors **only because the untouched r is explicitly known full**. This avoids the invalid shortcut of treating every final-tree edge as universally informative.

A sufficient way to obtain r is **two distinct terminal U complete collectors in a SINGLE exterior cell A**, since the final local e touches at most one A participant. This property is exact and does NOT require |A|=2. QED.

## New lemma 34.3 — no zero-private center with ≤5 people (ALL n)

Assume an actual successful both-cyclic fixed-original split, and suppose **neither P3 nor reversed Q3 has any complete terminal center collector**. Let U be one of these cyclic components, with an untouched full exterior participant r (thus two outside full collectors in its preceding tree T by Lemma34.2).

For every original U secret \(\sigma\), its midpoint support inside X is **nonempty** by the all-pairs cross-half success condition. If \(\sigma\) were held in X by exactly one participant x, exact success for all targets of the OPPOSITE cyclic component would force x to be a complete collector of that opposite cyclic component, contradicting the premise. Hence EVERY original U secret has **at least TWO distinct terminal X carriers**. Since the final U cycle-closing edge is OUTSIDE X, this same double cover already holds at the end of T.

Thus T has **two disjoint singleton complete recipient groups outside X** and a disjoint collectively complete recipient group X of size c, containing NO private X participant. [Stage29's exact all-n \((1,1,c)\) privacy theorem](../v4.6/PRIVATE_THRESHOLD_THEOREM.md) proves such an edge-once chronological tree is **impossible for \(c\le5\)** (valid with arbitrary unassigned helpers). Consequently
\[
\boxed{c=|X|\ge6.}
\]
This is a genuinely all-n original-order, conditional crossing obstruction. QED.

## New lemma 34.4 — two untouched exterior collectors on opposite cyclic sides force c≥7 (ALL n)

Retain absence of complete center collectors in BOTH U=P3 and V=Q3(reversed), and assume EACH of U and V has ≥2 distinct terminal full collectors in **one of its exterior cells**, so in each cyclic side an exterior full collector r is untouched by that side's last cycle-closing contact.

By Lemma34.2 both original-ordered spanning trees TP,TQ each have **two complete terminal recipients outside X**. By the previous argument, X **doubly covers EVERY original TP and TQ secret**, with no private X recipient. If c≤5, Lemma34.3 already gives a contradiction. Suppose c=6.

The [Stage30 all-n sharp six-recipient double-path theorem](../v4.7/DOUBLE_PATH_RIGIDITY.md) now applies **separately** to TP and TQ. Their original center knowledge supports equal the supports within the preceding trees, because each final U/V cycle-closing contact touches ONLY exterior participants, leaving EVERY X person's knowledge unchanged. Stage30 forces each of TP and TQ to have **four distinct exact 2-point center supports forming two disjoint three-vertex paths**. All-pairs original source-target midpoint crossing across the shared center X therefore requires the four P3 source supports to intersect ALL four reversed-Q3 target supports.

This is combinatorially impossible: for any two disjoint 3-vertex paths on six people, the **ONLY** two-person set meeting all four path edges is the pair of their two path centers. Yet the opposite side supplies FOUR DISTINCT two-person sets, so they cannot all equal the unique transversal. This is Stage30's exact 90-pattern / 8,100-pair independent finite check, backed by the complete all-n human transversal proof. Hence
\[
\boxed{c=|X|\ge7}
\]
whenever both sides have the stipulated untouched full exterior collectors and no center full collector. QED.

**Scope honesty:** Theorem34.4 is **not** a blanket impossibility for every pair of unicyclic components. Its application to TP and TQ is justified ONLY because their center knowledge is unchanged by the actual last cycle contacts and both preceding TREE histories meet the two-singleton-full-collector and double-cover hypotheses. This explicit transport is the new bridge missing in Stage30's original standalone TREE-versus-TREE theorem.

## Completion of n22 fixed-midpoint proof by exact finite incidence coverage

Run the [Stage34 reason-partition auditor](n22_final_center_support.py) from the repository root. It independently enumerates the exact 24,310 labelled positive matrices and applies previous all-n necessary filters in explicit order. The decisive ledger:

| Filter stage, conditional on cited human proofs | n22 still possible necessary-incidence matrices |
|---|---:|
| Raw positive 3×3 shapes | 24,310 |
| Stages25/26 necessary gates | 137 |
| Stage28 exterior root obstruction | 104 |
| Stage32 two-exterior root bootstrap | 32 |
| Stage33 exact two-recipient zero-privacy theorem | 24 |
| Lemma34.3, center width four | **4** |
| Lemma34.4, center width six | **0** |

At the last stage, every one of the **24** residual labelled matrices has BOTH cyclic sides certified to have NO full center collector by Stage32's all-n exterior occupancy≤8/root-capacity theorem. Of these:

- **20 labelled, center c=4:** at least ONE cyclic side has at least two certified complete exterior collectors in the SAME offcorner cell, by exact opposite tree private support minima. Its final cycle edge touches at most one of them, so Lemmas34.2–34.3 contradict double center coverage at c=4.
- **4 labelled, center c=6:** EACH cyclic side has at least two certified complete exterior collectors in one offcorner cell. Both preceding original-order spanning trees have two complete exterior collectors and double-cover center X. Lemma34.4 prohibits their exact all-pairs 2P3 supports.

These 24 labelled matrices form **seven** row/column two-tree symmetry orbits, exhaustively checked. The 20/4 reason partition is independent of the Stage34 proof prose; the executable classifier also asserts all no-center and collector premises for EVERY final matrix before rejecting it.

Thus no successful 40-contact distinct-call both-original-cyclic schedule on 22 vertices can exist **IF** the earlier imported all-n theorems are correct. Therefore at least one of its two original 20-contact halves is a forest. QED.

## Evidence and limitations

The checker is an **executable finite exhaustive necessary-incidence audit**, not 40-contact chronology enumeration; source and earlier human structural lemmas matter. Rerun all earlier exact privacy and support tests in [Stage34 CI workflow](../../.github/workflows/research-v51.yml) and **observe matching head-run success** before claiming verified finite census. Stage30 independent exactly enumerates all 90 labelled 2P3 systems and their 8,100 pairs, as well as exact original n4–6 tree chronologies; Stage32 separately enumerates all n4/5 unicyclic local histories and A/B/X partitions. No Lean/Coq/Isabelle proof checker or external referee has validated the full mathematical dependency chain, and source-level historical priority remains unverified.

**Do not misreport this as SOTA solution of the main project.** The primary conjecture that every properly labelled temporal clique admits an EXACT reachability-preserving 2n−3-edge spanner remains OPEN. Existence of an optimal \(2n-4\)-contact gossip chronology cannot be assumed for arbitrary time-labelled cliques. The global original chronological half-forest claim for n≥23 also remains OPEN.

Next highest-information task is independent proof adversarial review of the Stage14, Stage19, Stage28, Stage29, Stage30 dependencies; then original n23 396 necessary profiles with a larger c=7 or a new unbounded descent. Preserve DRAFT/UNMERGED and publication HOLD until an external novelty/referee or formal assurance gate is satisfied.
