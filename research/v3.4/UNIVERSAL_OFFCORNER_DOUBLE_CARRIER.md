> **Stage 18 application (28 October 2026):** The at-least-two-carriers property **survives deleting the touched final cycle endpoint**: the remaining members of each off-corner cell are separate full-cover recipient groups of the earlier chronological spanning tree. Together with four center arm groups this gives six complete recipient groups and, via equality rigidity, **`|P3|>=35`** whenever the opposite off-corner pair is (2,2). See [Stage 18](../v3.5/SIX_GROUP_35_PERSON_OBSTRUCTION.md). The global conjecture remains OPEN.

# Stage 17 — Universal off-corner double-carrier principle

**28 October 2026. All-\(n\), original chronological, NECESSARY information-flow invariant for the FULL unrestricted 3×3 both-cyclic hypothetical family.** This is a conceptual strengthening of the simple off-corner size lower bounds. The full original half-forest conjecture remains **OPEN**.

## Model and historically verified premises

Take the **original**, unreordered first \(n-2\) distinct bidirectional calls and original last \(n-2\) calls of a shortest successful schedule. By Richard T. Bumby's 1981 Theorem 3 and its closed-tree spine (source checked in [Stage 12](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md)), if both halves are cyclic, the prefix components are \(P_1,P_2\) (closed trees) and \(P_3\) (unicyclic), and the **fully time-reversed** suffix components are \(Q_1,Q_2\) (closed trees) and \(Q_3\) (unicyclic).

The last original prefix contact within *each* \(P_i\) joins reversed suffix tree columns \(Q_1,Q_2\). Hence the only possible complete original-prefix collectors of tree \(P_1\) or \(P_2\) are outside \(Q_3\). Dually, the first original suffix contact within *each* \(Q_j\) joins prefix tree rows \(P_1,P_2\). Hence the only possible complete **reverse-time suffix** collectors of tree \(Q_1\) or \(Q_2\) are outside \(P_3\).

Let \(C_{ij}=P_i\cap Q_j\) and \(m_{ij}=|C_{ij}|\). Full temporal information propagation from an original \(P_i\) secret \(a\) to any final \(Q_j\) target \(b\) requires a midpoint participant in \(C_{ij}\) who is simultaneously a terminal original-prefix carrier of \(a\) and a terminal **reverse-time** \(Q_j\)-carrier of \(b\). This is the precise source-target support intersection condition, not a reordering statement.

## Universal four-cell double-carrier theorem (ALL n)

**Every original \(P_3\) secret is held at the fixed midpoint by AT LEAST TWO DIFFERENT people in each of \(C_{31}\) and \(C_{32}\). Moreover, for every \(Q_3\) target \(b\), in the fully reversed original suffix chronology that target's label is carried by AT LEAST TWO DIFFERENT people in each of \(C_{13}\) and \(C_{23}\).**

In symbols, with \(K_{P_3}(x)\) the original prefix local knowledge of \(x\) and \(K^{\mathrm{rev}}_{Q_3}(x)\) the fully reversed suffix local knowledge of \(x\),

\[
\boxed{\begin{aligned}
&\forall a\in P_3,\ \forall j\in\{1,2\}:&
|\{x\in C_{3j}:a\in K_{P_3}(x)\}|&\ge2,\\
&\forall b\in Q_3,\ \forall i\in\{1,2\}:&
|\{x\in C_{i3}:b\in K^{\mathrm{rev}}_{Q_3}(x)\}|&\ge2.
\end{aligned}}
\]

### Proof

Fix \(j\in\{1,2\}\). By the Bumby spine, the only complete reverse-time collectors of the suffix **tree** \(Q_j\) are endpoints of its *last reversed* call, i.e. its *first original suffix* call, whose endpoints lie in prefix rows \(P_1\) and \(P_2\). Thus **NO** person in \(C_{3j}\subseteq P_3\) is reverse-complete for \(Q_j\).

For every \(P_3\)-source secret \(a\) define its fixed-midpoint carrier set

\[
A_a=\{x\in C_{3j}:x\text{ knows }a\text{ after the original prefix}\}.
\]

Global successful gossip implies \(A_a\ne\varnothing\). If \(A_a=\{x\}\) were a singleton, then temporal compatibility with **every** \(Q_j\)-target \(b\) would force \(x\) to lie in **every** reversed suffix support \(B_b\subseteq C_{3j}\). But then \(x\) would be a complete reversed collector of \(Q_j\), contradiction. Therefore \(|A_a|\ge2\), for every \(a\in P_3\). This proves the first two cells, irrespective of how large they are.

For \(i=1,2\), repeat the reasoning with roles reversed. The only complete original-prefix collectors of the tree \(P_i\) are endpoints of its *last original prefix* call, which lie in suffix-tree columns \(Q_1,Q_2\), not \(Q_3\). Thus **NO** \(x\in C_{i3}\) is prefix-complete for \(P_i\). If a reverse suffix target label \(b\in Q_3\) had singleton reverse support \(B_b=\{x\}\subseteq C_{i3}\), crossing every original \(P_i\) source \(a\) would force \(x\) to belong to every \(A_a\), making \(x\) prefix-complete for \(P_i\), contradiction. Thus \(|B_b|\ge2\) for all \(b\). QED.

### Consequences / exact limitations

1. Every off-corner cell has size at least two (recovering Stage 12's simple numerical bound), but this theorem additionally forbids **any private local source or target support** in the specified unicyclic-side orientation, even when a cell has 3, 4, or many recipients.
2. If \(|C_{31}|=2\), both people must carry *every* \(P_3\)-secret; they are full prefix collectors of \(P_3\). Similarly for \(C_{32}\), and dually for \(C_{13},C_{23}\) on reversed \(Q_3\). This recovers the crucial saturated two-point collector step used by Stages 14–16 **without limiting the theorem to size-two cells**.
3. If \(|C_{31}|=3\), the supports of different \(P_3\)-secrets may be \(\{x,y\},\{x,z\},\{y,z\}\). Every secret has two carriers, but **nobody need be a full collector**. Thus a size-three cell does *not* generally force two full collectors. The same abstract support example works dually. This is an information-theoretic **support-family witness**, not a contact chronology and not a global 2n−4-call counterexample.
4. The opposite orientation is **not** asserted: an arbitrary \(P_3\) secret need not have two original-prefix carriers within \(C_{13}\), since \(P_3\not\subseteq P_1\). Likewise no new double-carrier condition is claimed within the center \(C_{33}\) absent the additional collector saturation hypotheses of Stages 13–16.
5. The property is **local and algorithmically testable**: any future exact 3×3 counterexample search can reject an original prefix/suffix component pair as soon as an off-corner cell has a single source/target carrier in the appropriate orientation. It is stronger than pruning by \(m_{ij}\ge2\) alone, especially in the still-open all-unsaturated families.

## Exact independent finite falsification

[double_carrier_support_falsifier.py](double_carrier_support_falsifier.py) independently exhausts all nonempty support-family assignments on cells of size \(2\) and \(3\), with 1–3 sources and 1–3 targets per side, under the exact all-pairs intersection and absence of full opposing collectors, and checks the two-carrier inference in both orientations. It separately exhibits the three-point triangle-support family with no complete collector, and pins a singleton-support falsifier where an opposing full collector is allowed. The experiment checks the finite Boolean lemma, **not** universal shortest-schedule existence, and uses no pre-existing oracle.

**Historical priority:** The elementary singleton-intersection principle is not claimed as a new external discovery; its four-cell chronological application derives from Bumby's historical spine. **Global original-half conjecture:** OPEN. **Independent global counterexample:** NONE. **PR #1:** DRAFT/UNMERGED.
