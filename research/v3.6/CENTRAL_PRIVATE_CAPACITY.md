# Stage 19 — Universal central private-support capacity and penultimate-call pinning

**28 October 2026. ALL-n necessary statement for the full unrestricted hypothetical both-cyclic ORIGINAL chronological 3×3 split.** Universal original half-forest conjecture remains OPEN. No schedule reordering.

## Setting

Under the original fixed midpoint and Bumby's 1981 Theorem 3 (see [historical source audit](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md)), let the prefix components be closed trees \(P_1,P_2\) and unicyclic \(P_3\), and let the fully reversed suffix components be closed trees \(Q_1,Q_2\) and unicyclic \(Q_3\). Let \(X=P_3\cap Q_3\), of arbitrary positive size.

For each \(a\in P_3\) set

\[
A_a=\{x\in X:x\text{ knows }a\text{ after the original prefix}\}.
\]

For each \(b\in Q_3\) set

\[
B_b=\{x\in X:x\text{ knows reverse label }b\text{ at the end of the fully reversed suffix}\}.
\]

Successful complete original gossip means \(\forall a,b,\ A_a\cap B_b\ne\varnothing\). Define the **distinct forward-private center positions**

\[
D_A=\{x\in X:\exists a\in P_3,\ A_a=\{x\}\}
\]

and the **distinct reverse-private center positions**

\[
D_B=\{x\in X:\exists b\in Q_3,\ B_b=\{x\}\}.
\]

Count distinct positions, not the number of secrets with singleton support.

## Theorem — At most TWO private positions in either direction, all n

\[
\boxed{|D_A|\le2,\qquad |D_B|\le2.}
\]

**Proof.** If \(x\in D_A\), choose \(a\) with \(A_a=\{x\}\). The exact midpoint crossing \(A_a\cap B_b\ne\varnothing\) for **every** \(b\in Q_3\) forces \(x\in B_b\) for all \(b\). Equivalently, \(x\) is a **complete reverse-time collector** of the entire unicyclic component \(Q_3\).

Bumby's original first/last call spine, applied to the original (unreordered) reversed suffix, says the **last reversed \(Q_3\) call** is the first original suffix call in \(Q_3\), connects the prefix-tree rows \(P_1,P_2\), and lies on \(Q_3\)'s unique static cycle. Consequently its two endpoints are both **outside** \(X\), and deleting it leaves a chronological spanning tree \(T_Q\) of \(Q_3\).

No \(X\) participant takes part in that final reversed call. Thus every complete reverse-time collector in \(X\) must already have become complete during the earlier \(v-1\) tree contacts. Nobody can know all \(v\) original \(Q_3\) labels before those \(v-1\) contacts, since fewer than \(v-1\) distinct edges cannot connect all vertices. The \((v-1)\)st tree contact can make at most its **two endpoints** complete. Thus at most two people of \(X\) can be reverse-complete, and \(|D_A|\le2\).

The symmetric argument runs on \(P_3\)'s actual original prefix chronology, whose last unicyclic on-cycle call connects reversed suffix tree columns \(Q_1,Q_2\), again outside \(X\). For every \(x\in D_B\), exact crossing makes \(x\) a complete original-prefix collector of \(P_3\), of which at most two can belong to \(X\). Hence \(|D_B|\le2\). QED.

### Stronger fixed-order positional conclusion

If \(|D_A|=2\), then the two distinct positions in \(D_A\) are **exactly the endpoints of the penultimate call in the fully reversed local \(Q_3\) chronology**, i.e. the **SECOND original suffix call within \(Q_3\)**. Likewise, if \(|D_B|=2\), those two positions are **exactly the endpoints of the penultimate original PREFIX call within \(P_3\)**.

This is because no person can become fully informed in the local tree before the last tree contact, and only that contact's endpoints can become complete before the final unicyclic contact (which touches no center position). This is a necessary original-order pin; it does **not** move or reorder any event.

## A concrete local countermodel to naive sufficiency

The following is an **isolated local unicyclic chronology**, not a full shortest gossip schedule. Its ten participants are partitioned into external groups

\[
D_1=\{0,1,2\},\quad D_2=\{3,4,5\},\quad X=\{6,7,8,9\}.
\]

Its ten pairwise-distinct chronological calls are

\[
(5,0),\ (1,9),\ (7,4),\ (0,9),\ (8,3),\
(4,0),\ (6,2),\ (3,2),\ (2,4),\ (0,3).
\]

The last call joins \(D_1,D_2\), is on the unique static cycle, and touches no center participant. **Every** original secret is carried by at least two people in \(D_1\) and at least two in \(D_2\), and \(X\) collectively covers every secret. These are strong, exactly replayable *one-sided* necessary conditions inherited from Stage 17.

However, the four center knowledge sets are:

\[
\begin{aligned}
K(6)&=\{2,6\},\\
K(7)&=\{4,7\},\\
K(8)&=\{3,8\},\\
K(9)&=\{0,1,5,9\}.
\end{aligned}
\]

Thus **every original secret has a singleton support in \(X\)**, and \(|D_A|=4\). The all-n theorem proves that this locally admissible \(P_3\) chronology **cannot** be paired with ANY \(Q_3\) reversed chronology satisfying the actual both-cyclic Bumby last-cycle spine and successful full original gossip. Its four singleton center positions would demand four complete reversed collectors in \(X\), whereas a unicyclic component with final edge outside \(X\) permits at most two.

The explicit local countermodel is an *adversarial example of why size-only and double-carrier-local tests are insufficient*: it is ruled out only when central cross-half temporal information is imposed. It is **not** a counterexample to the original half-forest conjecture.

## Reproducible independent verifier and next bottleneck

[central_private_capacity_check.py](central_private_capacity_check.py) independently replays the ten-contact witness, checks distinct edges, connected unicyclic static rank, the actual last-edge side assignment, two-fold secret coverage in both exterior cells, all-secrets collective center coverage, the four private center positions, and verifies the exact Boolean support implication by exhaustive enumeration for center width 2,3 and source/target support families of size up to three.

**Pruning rule for an exact chronology solver:** Reject any local \(P_3\) state with three distinct singleton-centered original secrets, and reject any reverse-local \(Q_3\) state with three distinct singleton-centered reverse-target supports. With exactly two such positions, the **second original suffix call in \(Q_3\)** or **penultimate prefix call in \(P_3\)** is forced between their two participants. This improves on the Stage 17 off-corner double-carrier filter without assuming any \((2,2)\) pair.

**Truth gate:** all-n human proof; finite executable regression; no universal half-forest proof, global counterexample, Lean/Coq certification, or external priority sign-off. Keep PR #1 DRAFT/UNMERGED.
