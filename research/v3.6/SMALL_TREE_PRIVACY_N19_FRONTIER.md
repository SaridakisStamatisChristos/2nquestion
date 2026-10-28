# Stage 19 — exact small-tree privacy filters the \(n=19\) original-midpoint frontier to ONE incidence orbit

**28 October 2026. Status:** a rigorously enumerated finite **necessary incidence reduction**, NOT a proof of the full original chronological half-forest conjecture for \(n=19\). Four labelled matrices remain, equivalent under renaming the two prefix-tree rows and two reverse-suffix-tree columns. No actual successful both-cyclic schedule has been constructed; no contradiction yet for the final orbit. Keep PR #1 **DRAFT / OPEN / UNMERGED**. External refereeing and formal-assistant proof checks have not been performed.

## Exact model, prior art, and prerequisites

Let a successful shortest pairwise-distinct two-way telephone-gossip chronology have its original fixed first and last \(n-2\) calls both cyclic. Bumby's 1981 Theorem 3 restricts the actual original midpoint to a \(3\times3\) incidence grid \(m_{ij}=|P_i\cap Q_j|\), where \(P_1,P_2\) are original prefix trees, \(P_3\) is a prefix unicyclic component, and \(Q_1,Q_2\) are *fully reverse-time* suffix trees and \(Q_3\) is a reverse-time unicyclic suffix component. All nine cells are positive, all four off-corner cells at least two. The **last original call** inside each \(P_i\) tree joins \(Q_1\) to \(Q_2\); the **last reverse-time call** inside each \(Q_j\) tree joins \(P_1\) to \(P_2\). See [Bumby source audit](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md).

By [Stage 18's global tree-versus-star obstruction](../v3.5/FOUR_LEAF_STAR_GLOBAL_EIGHT_EXCLUSION.md), in any such successful original chronology both cyclic components must have **at least nine vertices**. Stage 14 gives a **causal**, not globally strict, four-arm decomposition when one unicyclic component has four terminal complete collectors outside center \(X=P_3\cap Q_3\); the Stage 15 one-sided crossed-arm theorem then forces \(|X|\ge9\) even if only one cyclic component has four such outsiders. Do NOT use the historically falsified assumption that all arm-internal calls must precede unrelated inter-arm calls.

At \(n=19\), the existing necessary-incidence count leaves exactly **41** labelled positive matrices. None of those matrices is asserted to be realized by a complete chronological schedule.

## Lemma 19.1 — finite exact privacy of small chronological trees

Let \(T\) be a tree on \(a+b+c\) labelled people; each of its \(a+b+c-1\) distinct edges is called **once, in its specified chronological order**. Its participants are partitioned into THREE disjoint nonempty groups \(G_0,G_1,G_2\) of sizes \(a,b,c\), each group **collectively knowing every original tree secret** after the calls. Suppose the LAST chronological tree call joins \(G_0\) to \(G_1\), as forced by Bumby's spine in our application. A vertex \(z\in G_2\) is *private in \(G_2\)* if some original \(T\)-secret is known by \(z\) and by no other \(G_2\) participant.

Then the following exhaustive table gives **all** possibilities for the number of private \(G_2\) participants, for each size triple needed at \(n=19\):

| \((a,b,c)\) | Vertices | Exact histogram: private count → labelled chronological histories | Minimum private |
|---|---:|---|---:|
| (1,1,2) | 4 | 2 → 4 | **2** |
| (1,1,3) | 5 | 2 → 72 | **2** |
| (2,1,2) | 5 | 2 → 48 | **2** |
| (1,2,2) | 5 | 2 → 48 | **2** |
| (2,1,3) | 6 | 2 → 1,728; 3 → 192 | **2** |
| (1,2,3) | 6 | 2 → 1,728; 3 → 192 | **2** |
| (1,1,4) | 6 | 1 → 384; 2 → 1,344 | **1** |

The proof is **complete finite exhaustion**, not statistical sampling: [the standalone verifier](exact_small_tree_privacy.py) enumerates all \(v^{v-2}\) Prüfer codes (exactly all labelled trees on \(v=a+b+c\) vertices) and all \((v-1)!\) chronological edge orders, fixes the last call between the designated first two groups, replays the exact secret-union model, tests that each of all three groups collectively covers all initial secrets, then counts private individual recipients in the third group. All table entries are explicit expected counts; a discrepancy fails the check. Swapping the first two groups is NOT taken on faith: both directed size triples are enumerated where needed.

**Adversarial boundary:** It is FALSE that a 6-person tree with complete singleton first two groups and a 4-person third group must have at least two private members. The table has **384 counterexamples** with exactly ONE private member. Therefore a blanket extension of the \(n=18\) two-private argument would be unsound. This is the reason the final \(n=19\) incidence orbit does not collapse under the present theorem.

## Lemma 19.2 — four local private receivers on either side force large center (all \(n\))

Fix an original prefix tree \(P_i\) and suffix component \(Q_3\). A recipient \(z\in P_i\cap Q_3\) who uniquely knows some \(P_i\) secret among that intersection has a *singleton midpoint source support* \(\{z\}\) for that secret within \(P_i\cap Q_3\). Successful FULL gossip to every \(Q_3\) target requires \(\{z\}\) to meet every reversed-\(Q_3\) target support. Therefore \(z\) is a **complete reverse-chronological collector** of the unicyclic \(Q_3\) component. This is the exact original-chronology temporal crossing lemma and uses no event reordering.

Similarly a private reversed-suffix \(Q_j\) tree recipient in \(P_3\cap Q_j\) is a **complete original prefix \(P_3\) collector**.

Thus if the combined minimum number of private \(Q_3\)-recipients in the two prefix trees is at least FOUR, then \(Q_3\) has at least FOUR distinct full collectors **outside center \(X\)**. The cycle can have at most four; Stage 14's causal four-arm normal form applies, and Stage 15's one-sided theorem, using original prefix \(P_3\)'s final cycle-closing contact outside \(X\), forces \(|X|\ge9\). The dual statement holds when the two reversed-suffix trees force four prefix \(P_3\) outsiders. This implication is valid **for arbitrary \(n\)** once the private-recipient premise is established; the finite histogram applies only to the listed 4-, 5-, 6-person trees.

At \(n=19\), ALL 41 necessary-incidence candidates have \(|X|\le5\). Consequently **either** total of four private recipients gives a contradiction.

## Theorem 19.3 — exact \(n=19\) remaining incidence orbit

**Claim (proved, conditional necessary reduction).** Any hypothetical successful shortest 34-call bidirectional chronology on 19 people with BOTH its original first and last 17-call halves cyclic must have incidence matrix, after renaming the two *tree component indices* on each side, EXACTLY

\[
\boxed{M=\begin{pmatrix}1&1&2\\1&1&4\\2&4&3\end{pmatrix}.}
\]

This is **NOT** a construction of such a chronology, nor a proof that it exists.

**Proof.** Start with the exact **41** Stage 18 positive labelled incidence matrices at \(n=19\), independently reproduced by enumeration. For each tree prefix row \(i=1,2\), apply Lemma 19.1 with triple \((m_{i1},m_{i2},m_{i3})\) and obtain its minimum private recipients \(r_i\). For each reversed suffix tree column \(j=1,2\), apply the same lemma to triple \((m_{1j},m_{2j},m_{3j})\) and obtain minimum private recipients \(s_j\). All these triples belong to the exact finite table above. Any matrix with \(\sum_i r_i\ge4\) or \(\sum_j s_j\ge4\) contradicts Lemma 19.2 because center has at most five participants.

The [separate complete nine-cell integer enumeration](count_n19_privacy_profiles.py) generates all \(\binom{14}{8}=3003\) labelled positive matrices over the Bumby baseline \(M_0=[[1,1,2],[1,1,2],[2,2,1]]\), applies only the independently documented Stage 14/15/18 necessary cell-size restrictions and obtains 41. Exactly 37 of those have at least four minimum private off-corner recipients on one side, and are eliminated. Exactly FOUR matrices survive, each with minimum-private totals **(3,3)**. They are the four row/column-swapped copies of the displayed \(M\), a single orbit under \(S_2\times S_2\). The four matrices are NOT actual successful schedules; all information compatibility beyond the necessary conditions remains to be checked. QED.

Numerically the 41 are distributed by minimum collector totals:

| Min prefix private recipients | Min reversed-suffix private recipients | Labelled incidence matrices |
|---:|---:|---:|
| 4 | 4 | 25 |
| 4 | 3 | 6 |
| 3 | 4 | 6 |
| 3 | 3 | **4** |

So **37/41** Stage 18 necessary-incidence matrices are excluded, leaving FOUR labelled candidates in ONE orbit.

### The remaining obstruction, precisely stated

At \(n=19\), both \(P_3\) and reversed \(Q_3\) have NINE people, the center has THREE, and the off-corner sizes are \(2,4\) on each side. A corresponding 4-person tree with complete corner-singletons forces TWO private off-corner recipients; its 6-person counterpart with three recipient groups of sizes (1,1,4) can force only ONE (384 genuine local tree histories exist). Therefore exactly THREE outside-center complete collectors are forced on each cyclic component, **not the four required** by the Stage 14/15 center contradiction.

The unresolved task is whether the actual original and reverse chronological event orders can be joined across the 3×3 grid under this three-collector configuration. Any future assertion of a full \(n=19\) proof or actual counterexample requires an independently replayable successful 34-call original chronology or a further unconditional contradiction. Neither is provided here.

## Reproducibility, provenance and disposition

- [Complete labelled tree/history private-recipient falsifier](exact_small_tree_privacy.py).
- [Separate 3003-matrix exact n19 incidence counter](count_n19_privacy_profiles.py).
- [Stage 18 original-order global star theorem](../v3.5/FOUR_LEAF_STAR_GLOBAL_EIGHT_EXCLUSION.md).
- [Stage 14 causal arm theorem](../v3.1/CAUSAL_FOUR_ARM_BRIDGE.md) and [Stage 15 one-sided private-support implication](../v3.2/HELPER_EQUALITY_AND_ONE_SIDED.md).

All-n half-forest conjecture **OPEN**. The \(n=18\) case was proved in Stage 17B; the \(n=19\) case is reduced to ONE labelled-incidence orbit. Finite local enumeration is exact for its asserted domain but not a formal proof assistant certificate. Historical novelty and peer review remain **UNVERIFIED**. PR #1 stays **DRAFT / UNMERGED**, publication HOLD.
