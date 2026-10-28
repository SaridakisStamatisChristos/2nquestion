# Stage 20 — The ORIGINAL chronological half-forest conjecture holds for \(n=19\)

**28 October 2026. Status: COMPLETE HUMAN PROOF for \(n=19\) using explicit historically grounded, all-\(n\) local lemmas and independently exhaustive small-tree enumerations.** This does **NOT** prove the universal all-\(n\) conjecture. No Lean/Coq theorem assistant execution, independent referee report, or global schedule counterexample is claimed. PR #1 stays **DRAFT / OPEN / UNMERGED**; publication remains HOLD.

## 0. Exact model, dependencies and historical boundary

Let \(S=(e_1,\ldots,e_{2n-4})\) be a successful shortest **pairwise-distinct** bidirectional gossip call chronology. The target concerns its **original, fixed** first and last \(n-2\) calls, with no substitution by any other ordering of commuting events.

Richard T. Bumby, *A Problem with Telephones*, *SIAM J. Algebraic Discrete Methods* **2** (1981), 13–18, Theorem 3, applies to the original temporal midpoint. As [source-checked in Stage 12](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md), if both original halves were cyclic, prefix \(P_1,P_2\) would be closed trees and \(P_3\) unicyclic, and the fully reversed original suffix \(Q_1,Q_2\) would be closed trees and \(Q_3\) unicyclic. The original last contact of every prefix component joins \(Q_1,Q_2\); the reverse-last contact in each suffix component joins \(P_1,P_2\). For the unicyclic components these last contacts close their unique cycles. All nine cells \(m_{ij}=|P_i\cap Q_j|\) are positive and all four off-corner sizes \(\ge2\).

Critical established necessary results:
1. [Stage 18](../v3.5/FOUR_LEAF_STAR_GLOBAL_EIGHT_EXCLUSION.md): each unicyclic component has at least **nine** people in any globally successful hypothetical both-cyclic original schedule; this relies on global crossing with a tree, NOT the originally false local-only eight-person classification.
2. [Stage 14](../v3.1/CAUSAL_FOUR_ARM_BRIDGE.md): exactly four full collectors in a connected chronological unicyclic component force four **causally sealed** rooted tree arms (not the false globally strict arm order).
3. [Stage 15](../v3.2/HELPER_EQUALITY_AND_ONE_SIDED.md): in a chronological tree \(T\), \(s\) disjoint designated complete-cover recipient groups with arbitrarily many helpers require at least \(2^{s-1}\) total designated recipients. **At equality**, every designated recipient has an original secret private relative to its own group. This includes unused helpers. If a unicyclic component has **four complete collectors outside** a center crossing another prefix/reverse unicyclic component with last cycle call outside that center, the *one-sided* causal four-arm theorem forces that center to contain **at least nine** people.
4. [Stage 19](../v3.6/SMALL_TREE_PRIVACY_N19_FRONTIER.md): an exhaustive labelled chronological-tree privacy table for all relevant four-, five-, and six-person trees reduces the 41 Stage-18 positive \(n=19\) incidence matrices to **exactly four labelled matrices in one \(S_2\times S_2\) row/column orbit**, represented by

\[
\boxed{
M=\begin{pmatrix}
1&1&2\\
1&1&4\\
2&4&3
\end{pmatrix}.
}
\]

The numerical table and matrix enumeration are exact finite necessary-condition checks, NOT a global schedule generator. We now reject this sole orbit by an additional all-\(n\) structural contradiction.

## 1. Mandatory three-complete-collector configuration inside \(Q_3\)

Assume hypothetically the above sole \(n=19\) matrix is realized by a successful original both-cyclic 34-call schedule. Work within the **actually reverse-chronological** suffix component \(Q_3\), which has

\[
A=P_1\cap Q_3,\quad |A|=2;\qquad
B=P_2\cap Q_3,\quad |B|=4;\qquad
C=P_3\cap Q_3,\quad |C|=3.
\]

This is a connected NINE-person unicyclic local chronology of exactly nine distinct calls, and its last reverse-time call closes the cycle joining \(A\) to \(B\).

By the prefix-tree privacy forcing:

- Prefix \(P_1\) has four people and disjoint complete-cover groups of sizes \((1,1,2)\). Its TWO vertices in \(A\) each have a private original \(P_1\) secret inside \(A\), by Stage 11 tree-cover equality rigidity. Every such private prefix recipient must be a **complete reverse-chronological collector of \(Q_3\)**, to deliver that secret to all \(Q_3\) targets. Thus **BOTH A participants are full reverse-\(Q_3\) collectors**.
- Prefix \(P_2\) has six people and groups \((1,1,4)\). The exact independent Stage 19 tree enumeration proves **at least one** vertex in \(B\) has a private prefix \(P_2\) secret inside \(B\). Thus **at least one** \(B\) participant is a complete reverse-\(Q_3\) collector.
- By Stage 16, **each** original \(Q_3\) secret has at least **two** terminal reversed carriers in \(B\) and **at least one** in \(C\). This is a property of the carriers of each *reverse-time target secret*, not the unrelated statement that every participant's reverse knowledge meets each group. Confusing these two matrix orientations would invalidate the argument.

A connected unicyclic \(v\)-person chronology with \(v\) calls has at most FOUR complete terminal collectors. We split into the only possible cases: exactly four or exactly three.

## 2. Lemma 20.1 — four full collectors are IMPOSSIBLE in the \((2,4,3)\) group sizes

If \(Q_3\) had four full collectors, its required two in \(A\) and at least one in \(B\) leave only two possibilities:

**Case (i): two full collectors in A and two in B.** All four are outside center \(C\). Stage 14 constructs its four causally sealed arms; Stage 15's *one-sided* crossing theorem forces \(|C|\ge9\), contradicting \(|C|=3\). This does **not** assume all arm calls globally precede all inter-arm calls.

**Case (ii): two full collectors in A, one in B and one in C.** Let the full B collector be \(y\). Stage 14's causal four-arm decomposition has exactly FOUR roots \(A_0,A_1,y,C_0\). They lie in four different tree arms. Every **non-root** vertex retains knowledge only of secrets originating in its own arm; none participates in the later root-root communication. The B group contains only THREE non-root recipients \(z_1,z_2,z_3\) in addition to the full root \(y\).

For **each** of the four arm roots \(r\), its own original secret must have at least TWO B-group carriers after \(Q_3\)'s reverse chronology. The root \(y\) is already one such B carrier because \(y\) is full. A B non-root in an arm OTHER than \(r\)'s cannot know \(r\)'s original secret, by causal sealing. Therefore **each of the four distinct arms must contain at least one of the three B nonroots**. This is impossible by pigeonhole. Contradiction.

Thus \(Q_3\) has **exactly three** complete collectors: the two in A and **one** in B; no center collector is complete.

The pigeonhole subcase has an independent 64-assignment check in [local_nine_collector_boundary.py](local_nine_collector_boundary.py); the human proof is universal.

## 3. Lemma 20.2 — three full collectors force THREE reverse target star supports

Let \(e=(a_0,b_0)\) be the LAST reverse-time \(Q_3\) call, where \(a_0\in A,b_0\in B\), and \(a_1\) the other vertex in \(A\). The edge \(e\) closes the unique cycle by Bumby's case-II proof. Its first eight calls therefore form a chronological **spanning tree** \(T\) on all NINE original Q3 people.

Because both A people are fully informed after all nine calls and \(a_1\) does **not** participate in the final call, \(a_1\) is **already complete after the first eight tree calls**. In a chronological spanning tree with each edge called once, no participant can be complete before its last (eighth) edge, and a complete participant after that edge must be an endpoint of that edge. In fact **both endpoints of that eighth tree call are complete**, since each endpoint must already have accumulated all secrets of its own side to make either one complete after their joining contact. Let these two full T collectors be \(a_1\) and \(t\).

Bidirectional calls give the **same final knowledge to both endpoints**. Since \(a_0\) is full after \(e\), its partner \(b_0\) is also full after \(e\). The only three full Q3 collectors are \(a_0,a_1,b_0\). Thus \(t\in\{a_0,b_0\}\), and \(b_0\) is the **unique** full collector in \(B\).

Set \(B^\ast=B\setminus\{b_0\}\), consisting of exactly three vertices \(z_1,z_2,z_3\). Examine the first EIGHT calls' chronological tree \(T\), with the following FOUR pairwise disjoint designated recipient groups:

\[
G_1=\{a_1\},\qquad
G_2=\{t\},\qquad
G_3=B^\ast=\{z_1,z_2,z_3\},\qquad
G_4=C.
\]

One of \(a_0,b_0\), not in the first two singleton groups, is an unassigned helper. **EVERY group collectively covers ALL NINE original \(Q_3\) secrets already after the first eight tree contacts**:

- \(a_1,t\) are full T collectors.
- Each \(Q_3\) secret has at least TWO terminal B carriers. The last contact \(e\) changes **only** \(b_0\) inside B. Thus after deleting \(b_0\), at least one of \(B^\ast\) already carried the secret at the end of \(T\).
- Every \(Q_3\) secret has a terminal carrier in C. No C person participates in the final \(e\), so C already collectively covers all secrets at the end of T.

The FOUR designated groups contain precisely \(1+1+3+3=8=2^{4-1}\) people, attaining equality in the Stage 15 **helper-robust chronological tree-cover** theorem (with one helper). Its all-\(n\) equality rigidity forces **EACH** \(z_i\in B^\ast\) to have some original \(Q_3\) secret \(\sigma_i\) private within \(B^\ast\): of the three \(z_j\), ONLY \(z_i\) knows \(\sigma_i\). This persists past the final \(e\), since no \(z_i\) participates in it.

But \(b_0\) is a complete reverse-time Q3 collector after \(e\), so among the four B recipients the support of \(\sigma_i\) is **EXACTLY**

\[
\boxed{
\mathrm{Supp}_{B}(\sigma_i)=\{b_0,z_i\},\qquad i=1,2,3.
}
\]

The three \(\sigma_i\) are necessarily distinct (a secret cannot be private to two different recipients of the same group). These sets are **reverse-time carrier supports of original \(Q_3\) targets**. Their orientation is precisely the one needed for chronological cross-half source-target compatibility; no reverse-knowledge transpose is assumed.

This is an all-\(n\) *deduced three-leaf star*, not an assertion that every local 9-person chronology must have four full collectors. An independently replayable LOCAL nine-person Q3 example with exactly three complete collectors and precisely these three star supports appears in [local_nine_collector_boundary.py](local_nine_collector_boundary.py); it shows why this lemma alone is not a global contradiction.

## 4. Lemma 20.3 — the ORIGINAL \(P_2\) tree cannot cross those three supports

The original prefix \(P_2\) has SIX people: its two corner cells in suffix-tree columns \(Q_1,Q_2\) are singletons, and its cell \(B=P_2\cap Q_3\) has four members. By Bumby's original last-prefix-contact spine, the LAST chronological call in the tree \(P_2\) joins the two corner cells, so BOTH endpoints lie **outside B**.

By full gossip, the four B recipients collectively know all original \(P_2\) secrets at the fixed original midpoint; each original \(P_2\) secret must reach each target in \(Q_3\), so the exact crossing across the B cell is necessary.

For each original P2 source secret \(a\) and each of the three original Q3 target secrets \(\sigma_i\), successful original information transfer requires
\[
\mathrm{Supp}_{B}^{\rm prefix}(a)\cap
\{b_0,z_i\}\ne\varnothing
\quad (i=1,2,3).
\]

**Last-edge contradiction:** Remove P2's last tree edge, which separates P2 into two chronological subtrees \(U,V\). No B vertex participates in that final call, so its terminal knowledge remains confined to the original secrets of its own side. Because B collectively covers all P2 secrets, it meets BOTH U and V. Put \(b_0\in U\). Choose any original P2 secret \(a\) from the other side V; \(b_0\) cannot know \(a\). For the singleton-pair crossing \(\{b_0,z_i\}\) to succeed, **each** of the three distinct \(z_1,z_2,z_3\) must know \(a\). Apply this for EVERY original secret in V: all three \(z_i\) lie in V and each individually knows every original V secret after the P2 tree calls.

But a chronological tree V with each edge called once has **at most TWO** terminal full collectors: only endpoints of its final internal contact can first collect all V secrets. THREE distinct complete V collectors are impossible. Contradiction.

This is the \(r=3\) specialization of the independently proved all-\(n\) [Stage 18 tree-versus-star lemma](../v3.5/FOUR_LEAF_STAR_GLOBAL_EIGHT_EXCLUSION.md), which required only \(r\ge3\). [exact_three_leaf_star.py](exact_three_leaf_star.py) independently checks every original six-person labelled tree chronology whose last contact joins its two corner singleton recipients: 432 labelled trees with that edge, 10,368 original chronologies, 1,728 valid three-group full covers, and **ZERO** crossing all three target star supports. This finite check is separate from the Stage 18 seven-person four-star checker.

## 5. THEOREM 20.4 — \(n=19\) original fixed-half forest, complete contradiction

**Theorem.** Every successful shortest bidirectional gossip schedule of exactly \(2\cdot19-4=34\) DISTINCT calls has a **forest** among its **ORIGINAL first or last \(19-2=17\)** calls.

**Proof.** If both original halves were cyclic, Bumby's 1981 Theorem 3 and the previously verified stages would confine their 3×3 incidence sizes to the sole Stage 19 orbit \(M\). Applying the originally oriented component-tree privacy results forces Q3 to have at least two A-side and one B-side full collectors. Lemma 20.1 excludes four full collectors (the only other possible collector count), so exactly three exist. Lemma 20.2 forces three distinct reversed-Q3 target supports \(\{b_0,z_i\}\) inside the shared B cell. Lemma 20.3 proves that the actual ORIGINAL chronological P2 tree cannot carry its own secrets across all those supports. This contradicts success of the originally ordered 34-call schedule. Therefore both original halves cannot be cyclic. At least one is a forest. QED.

**Scope:** This is a human-checkable proof with fully specified finite exact underlying tree enumerations. It is NOT a Lean/Coq/Isabelle formal verification, an independently refereed manuscript, a global all-\(n\) theorem, or a counterexample.

## 6. Independent adversarial boundary and evidence contract

The three-full-collector local nine-person cycle truly **exists** in isolation; [the independent local replay](local_nine_collector_boundary.py) pins these original reverse-time calls on vertices 0,..,8:

\[
(0,1),(1,6),(3,7),(1,3),(2,4),(8,5),(2,8),(1,2),(0,2).
\]

It has A=\{0,1\}, B=\{2,3,4,5\}, C=\{6,7,8\}; the last edge closes a cycle from A to B; exactly people 0,1,2 know all nine secrets; every secret has two A and two B carriers and at least one C carrier. The three B support pairs are \(\{2,3\},\{2,4\},\{2,5\}\). **This is not a successful full 34-call schedule**, because the adjacent original six-person tree required by the unique n19 incidence matrix cannot cross those supports. Do not mistake local feasibility for a counterexample.

Computational checks, all independent in mechanism:
- [Stage 19 exhaustive small-tree privacy histograms](../v3.6/exact_small_tree_privacy.py) for each required 4-, 5-, and 6-person cell group triple, including the real \((1,1,4)\) one-private boundary cases; [independent 3×3 n19 incidence enumeration](../v3.6/count_n19_privacy_profiles.py).
- [Stage 20 independent original six-person tree / three-leaf star exclusion](exact_three_leaf_star.py).
- [Stage 20 real local three-full-collector unicyclic boundary replay](local_nine_collector_boundary.py).
- [Stage 18 all-n four-leaf star and independent chronology oracle](../v3.5/FOUR_LEAF_STAR_GLOBAL_EIGHT_EXCLUSION.md), with GitHub Stage 18 CI run 40685277971 observed **SUCCESS**.

The Stage 20 new human proof remains subject to external peer review and formal proof-assistant translation. The original half-forest conjecture for **arbitrary \(n\ge20\) remains OPEN**, with no valid global both-cyclic counterexample. No priority claim is made without a full literature comparison. PR #1 remains **DRAFT / OPEN / UNMERGED**; manuscript submission HOLD.
