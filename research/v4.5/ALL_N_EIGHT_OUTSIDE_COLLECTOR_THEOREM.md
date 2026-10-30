# Stage 28 — an all-\(n\) eight-outside collector obstruction

**28 October 2026. A conditional but genuinely UNBOUNDED original-order theorem. It holds for any number of participants when its *local collector hypotheses* hold. It is NOT a proof of the universal original-half forest conjecture. PR #1 stays DRAFT/UNMERGED; submission HOLD.**

## Research question and precise setting

Work with a hypothetical successful shortest distinct-call two-way gossip chronology whose ORIGINAL first and last \(n-2\) calls are both cyclic. [Bumby 1981, Theorem 3 and fixed-order spine](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md) imply exactly two closed prefix trees \(P_1,P_2\), an original unicyclic \(P_3\), two reverse-suffix closed trees \(Q_1,Q_2\), and a reverse-suffix unicyclic \(Q_3\), for **every n**. A fixed midpoint compatibility relation requires each prefix-secret support \(S_a\) to meet every reverse-target support \(T_b\) in the cell \(P_i\cap Q_j\). Neither calls nor the midpoint are reordered.

Take **either** original \(P_3\) or reversed \(Q_3\) as the chronological unicyclic component \(U\). Its three disjoint participant groups are outside-center \(A,B\) and center \(X=P_3\cap Q_3\). Its ACTUAL last component contact \(e=ab\), with \(a\in A,b\in B\), closes the unique static cycle and touches no center vertex. Its preceding \(v-1\) distinct contacts form a chronological spanning tree \(T\). By the [universal off-corner double-carrier lemma](../v3.4/UNIVERSAL_OFFCORNER_DOUBLE_CARRIER.md), **every U-secret has at least two terminal U-carriers in EACH of \(A,B\)**. By the same fixed-order spine, the opposite chronological tree \(T_A\) (or \(T_B\)) crossing cell \(A\) (or \(B\)) has its last contact entirely OUTSIDE the cell.

**Additional premise, NOT inferred from sizes:** at U termination there is at least ONE fully informed U collector inside \(A\) and at least ONE inside \(B\). This can sometimes be forced by original-order privacy lemmas on the adjacent prefix/reversed suffix trees, but is **not** automatic for arbitrary 3-, 4-, or larger-person cells.

## Theorem 28.1 — no center collector below the eight-outside threshold

**Theorem (ALL n, conditionally quantified).** Under the above genuine original-schedule, double-carrier, spine, and exterior-collector premises, if

\[
\boxed{ |A|+|B|\le 8,}
\]

then **NO** center participant \(x\in X\) is a complete terminal U collector, irrespective of \(|X|\), the four corner-cell sizes, or total \(n\).

### Proof: four terminal full collectors

A connected unicyclic chronology with one contact per edge has at most **four** terminal complete collectors, by the [Stage 14 causal four-arm decomposition](../v3.1/CAUSAL_FOUR_ARM_BRIDGE.md). Suppose there is at least one full root in A, one in B, and one in X. There are therefore three or four in total.

If there are **four**, their distribution across A,B,X has ≥1 root in each. As only one extra root is available, **at least one** outside cell \(D\in\{A,B\}\) contains **exactly one** complete root. Moreover all four outside-center cells have size ≥2, so \(|D|\le 8-2=6\). By the [Stage 24 original-order k=4 three-star occupancy theorem](../v4.1/THREE_STAR_ARM_OCCUPANCY.md), a singly rooted outside cell that doubly carries every U-secret and crosses an opposite chronological tree whose last edge is outside the cell must have **at least seven** people. Contradiction. The invoked Stage 24 theorem uses the actual per-arm causal sealing, not the invalid strictly globally separated arm-phase shortcut.

### Proof: exactly three terminal full collectors

There must now be exactly one full collector \(a\in A\), one \(b\in B\), and one \(x\in X\).

The last unicyclic contact is \(e=a_0b_0\), outside X. Since x is terminally complete and unaffected by e, x is already complete after the preceding spanning tree T. A chronological tree has at most two complete collectors, which, when any exist, are the two endpoints of its ACTUAL last tree contact. Thus T's two full collectors are \(x\) and some \(t\ne x\).

At least three people are complete after e but only two after T. At least one terminal U collector is newly completed by e, so **BOTH e-endpoints are complete** (they finish a bidirectional call with identical knowledge). Consequently \(a_0=a,\ b_0=b\), and the second full T collector \(t\) must equal one of \(\{a,b\}\); otherwise at least four people would be complete at U termination.

Delete T's last contact \(xt\), separating the preceding chronological tree history into two connected sides \(W_1,W_2\). Their respective roots \(r_1=x,r_2=t\) already know all ORIGINAL secrets of their own sides before xt.

Let \(H_A=A\setminus\{a\}\), \(H_B=B\setminus\{b\}\). Every U-secret has at least two terminal carriers in A and in B; e touches only a,b. Therefore H_A and H_B separately collectively cover EVERY U-secret before e, already at the end of T. Furthermore **neither H group contains either endpoint of xt**. No H recipient receives secrets from the other tree side through xt. Thus for each \(W_i\), the three nonempty pairwise disjoint groups
\[
\{r_i\},\qquad H_A\cap W_i,\qquad H_B\cap W_i
\]
already collectively cover ALL original \(W_i\)-secrets immediately after W_i's internal tree contacts.

The [Stage 11 helper-robust chronological tree-cover inequality](../v2.8/STEINER_COVER_RIGIDITY.md), applied separately to each side with s=3, requires
\[
1+|H_A\cap W_i|+|H_B\cap W_i|\ge 2^{3-1}=4.
\]
Summing gives
\[
\boxed{|A|+|B|
=2+|H_A|+|H_B|\ge8.}
\]
If \(|A|+|B|<8\), contradiction immediately.

If \(|A|+|B|=8\), both W_i are **exact equality cases**, even if arbitrary other helper vertices (including arbitrarily many in X) exist. The [Stage 15 helper-equality private-secret rigidity theorem](../v3.2/HELPER_EQUALITY_AND_ONE_SIDED.md) implies every recipient in H_A and H_B has a secret originating in its own W_i that is *private within its own designated recipient group*. Since the other W-side H recipients do not participate in xt, and no H recipient participates in final e=ab, each \(z\in H_B\) has a distinct U-secret \(\sigma_z\) whose exact final support in B is
\[
\operatorname{Supp}_B(\sigma_z)=\{b,z\},
\]
because b is fully informed. Analogously, each \(z\in H_A\) yields the star support \(\{a,z\}\) inside A.

Since \(|A|+|B|=8\), at least one cell D of A,B has size **≥4**, so it contributes **at least THREE** such distinct two-point star pairs \(\{y,z_1\},\{y,z_2\},\{y,z_3\}\). The [Stage 20 original chronological tree-versus-three-star obstruction](../v3.7/N19_ORIGINAL_CHRONOLOGY_THEOREM.md) applies to the adjacent opposite chronological tree with last contact OUTSIDE D: deleting its actual last tree edge places y on one side; every original secret of the other side would have to be known by all three \(z_i\). But an edge-once chronological tree side has **at most two** complete collectors, an impossibility. This uses ORIGINAL source-target support intersections, not an event exchange. Therefore the equality case is impossible too.

No complete center collector can exist. QED.

## Corollary 28.2 — low-width center obstruction, all n

Apply Theorem 28.1 symmetrically to \(U=P_3\) and reversed \(U=Q_3\). Assume that **on each unicyclic component** its two exterior cells sum to at most eight AND each contains at least one full terminal collector. Then neither component can have a complete collector inside \(X\).

If **\(|X|=1\)**, full original gossip across the singleton forces that participant to be complete on BOTH cyclic sides, contradiction.

If **\(|X|=2\)**, exact pairwise-support crossing on two participants requires a complete center collector on at least one cyclic side (indeed, the Stage 11 [two-person crossing trichotomy](../v2.8/TWO_VERTEX_CROSSING.md)). Contradiction.

If **\(|X|=3\)**, no reversed-Q3 center collector means every P3 source-secret center support has at least TWO people: otherwise a singleton would force its sole carrier to be a complete reversed-Q3 collector. The final P3 call is outside X, so its preceding chronological spanning TREE already has the same doubly covering three-person center set. The [Stage 19 exact all-n three-recipient doubly-covering chronological-tree lemma](../v3.6/CENTRAL_PRIVATE_CAPACITY.md) forces at least one COMPLETE original-P3 collector in X. Contradiction.

Hence
\[
\boxed{\text{Both outside pairs collector-qualified and sum}\le8
\quad\Longrightarrow\quad |X|\ge4.}
\]

**Important asymmetry:** For \(|X|=1\), blocking just ONE cyclic side suffices. For \(|X|=2,3\), this corollary requires both sides to be blocked. No claim is made when outside collector forcing is unknown.

## Stage 27 numerical consequences, NOT a new n=22 theorem

Run [independent Stage 28 audit](unbounded_eight_outside_audit.py) against the **entire** 137-profile Stage 27 necessary-incidence frontier using only the 16 PREVIOUSLY exact, size-bounded tree-privacy minima. Whenever the privacy lower bound for either exterior group is unknown, it is zero and does NOT satisfy the gate.

| Additional all-n gate | n=22 labelled cases excluded |
|---|---:|
| Center 1; at least one cyclic side blocked | 24 |
| Center 2; both cyclic sides blocked | 1 |
| Center 3; both cyclic sides blocked | 8 |
| **Total** | **33** |

Thus **137 → 104** labelled n22 necessary matrices, **28** tree-row/tree-column swap orbits. Remaining center histogram: \(1:4,\ 2:40,\ 3:36,\ 4:20,\ 6:4\). Example newly excluded (previously survived) is
\[
M=\begin{pmatrix}1&1&4\\1&1&4\\4&4&2\end{pmatrix};
\]
the four (1,1,4) adjacent chronological tree group triples each have at least one exact certified private recipient, forcing one complete U collector into each corresponding outside cell.

As a second arithmetic cross-check the same universally quantified gate reduces **n23 1,505 → 1,392** necessary profiles (**360** row/column orbits). This does **not** prove an n23 forest theorem, nor a statement about historical novelty.

## Why this still does not solve the original all-n conjecture

- The outside-collector premise is **not automatically true** when adjacent cells become large; arbitrarily extrapolating small-tree privacy lower bounds would be unsound.
- The argument rules out center **FULL collectors** for exterior sum ≤8 but does not rule out configurations where information in X is redundantly shared among four or more participants with no full collector.
- Entire infinite families still survive all declared size/privacy/center gates. For example \(\begin{psmallmatrix}1&1&4\\1&1&4\\4&4&t\end{psmallmatrix}\) for integer \(t\ge4\) passes the size-only Stage 25–28 predicates; this is a **formal incidence survivor**, NOT a successful gossip chronology or a counterexample.
- A universal forest proof must produce a global restriction valid for arbitrary \(m_{ij}\): a new receiver-cover vs source-cover inequality, chronology-preserving minimal-counterexample descent, or a genuine global schedule counterexample.
- The present proof is human-checkable conditional reasoning based on the cited prior repo lemmas; **no formal proof assistant or external referee has certified it**. Historical novelty against Bumby/Labahn/Krumme is UNVERIFIED. Preserve PR DRAFT/UNMERGED and publication HOLD.
