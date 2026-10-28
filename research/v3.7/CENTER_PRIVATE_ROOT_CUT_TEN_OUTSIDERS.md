> **Stage 25 all-n quantifier clarification (28 October 2026):** The root-cut proof below actually requires only that **TWO distinct center participants are already complete collectors at the end of the spanning-tree portion of an original/reversed unicyclic component whose final on-cycle call is outside the center**, plus the existing universal two-fold off-corner condition. The premise \(|D_A|=2\) is a **sufficient way to force** those two collectors (by Stage 19), but it is **NOT necessary** for the ten-outsider conclusion. No unproved converse from complete collectors to private center positions is used. The general hypothesis is needed by the [Stage 25 n21 two-person-center pruning](../v4.2/N21_CONSERVATIVE_77_PROFILE_FRONTIER.md), which independently verifies it via the exact binary crossing lemma. The original global theorem remains OPEN.

# Stage 20 — Two central-private positions force ten outside people

**28 October 2026. ALL-n conditional necessary theorem for the ORIGINAL fixed chronological 3×3 both-cyclic midpoint. No calls are reordered.** The full original-half-forest conjecture remains OPEN; the result does **not** assert that an admissible local profile extends to a global gossip schedule.

## Canonical setup and evidence dependencies

Let an optimal successful schedule of \(2n-4\) **distinct** bidirectional calls have both **original** halves cyclic. By Bumby 1981 Theorem 3 and its first/last-call spine ([Stage 12](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md)), prefix components are closed trees \(P_1,P_2\) and unicyclic \(P_3\); fully reversed original suffix components are closed trees \(Q_1,Q_2\) and unicyclic \(Q_3\). Write \(m_{ij}=|P_i\cap Q_j|\) and \(X=P_3\cap Q_3\).

As [Stage 19](../v3.6/CENTRAL_PRIVATE_CAPACITY.md) proves, if there are **two distinct forward-private central positions** \(D_A=\{x,y\}\), then \(x,y\in X\) are the **only complete reversed-\(Q_3\) collectors before its final reversed call**. They are precisely the endpoints of its penultimate reversed call. The final reversed call is the FIRST original suffix call of \(Q_3\); Bumby's spine forces it to join one person \(a\in C_{13}=P_1\cap Q_3\) to one person \(b\in C_{23}=P_2\cap Q_3\), entirely **outside** \(X\), and lies on the unique static cycle.

Thus the first \(v-1\) chronological reversed calls of \(Q_3\) are a spanning tree \(T\), whose last edge is \(xy\). Removing \(xy\) splits the earlier original-order history into two chronological trees \(U\ni x\) and \(V\ni y\); \(x\) was already complete for \(U\) and \(y\) complete for \(V\) before \(xy\).

[Stage 17](../v3.4/UNIVERSAL_OFFCORNER_DOUBLE_CARRIER.md) proves a separate essential requirement: **every original \(Q_3\) target secret is held by at least two different final reversed carriers in EACH of \(C_{13},C_{23}\)**. The final reversed call \(ab\) affects only \(a,b\).

## Root-cut lemma — at least four untouched outsiders on EACH side

Define \(D_1=C_{13}\), \(D_2=C_{23}\), \(H_1=D_1\setminus\{a\}\), \(H_2=D_2\setminus\{b\}\). By the two-fold property and the fact the final reversed contact touches only \(a,b\), **each \(H_i\) individually collectively covers all original \(Q_3\) secrets already at the end of spanning tree \(T\)**.

For \(W\in\{U,V\}\), let \(r_W=x\) or \(y\), and \(H_i^W=H_i\cap W\). Since only central vertices \(x,y\), neither belonging to either \(H_i\), participate in the last tree call \(xy\), no \(H_i\)-recipient acquires any secrets from the other side at that call. Consequently **each** \(H_i^W\) nonempty and collectively covers every secret originating in \(W\).

Thus the chronological tree \(W\) has **three disjoint, nonempty, complete-cover recipient groups** \(\{r_W\},H_1^W,H_2^W\). By the helper-robust exact chronological tree-cover bound (Stage 11), their recipient count obeys

\[
1+|H_1^W|+|H_2^W|\ge2^{3-1}=4.
\]

Suppose, seeking a contradiction, \(|H_1^W|+|H_2^W|=3\). After exchanging labels if needed, \(H_1^W=\{h\}\) and \(|H_2^W|=2\). Since \(\{h\}\) completely covers the original \(W\)-secrets, \(h\) alone knows **every** \(W\)-secret before the last tree edge \(xy\).

After the final reversed cycle call \(ab\), every \(W\)-secret must have **at least two** distinct carriers in the *full* off-corner cell \(D_1\) (Stage 17). But among \(H_1\), the **sole** possible \(W\)-carrier is \(h\), because \(H_1\setminus W\) was untouched by \(xy\) and cannot know \(W\)-secrets. Hence the excluded designated endpoint \(a\) must obtain **every** \(W\)-secret at the final call \(ab\).

Immediately before the final call, the **one or two endpoints of \(ab\) belonging to \(W\)** must therefore collectively know all original \(W\)-secrets. There must be at least one such endpoint: no outside-\(W\) endpoint knew any \(W\)-secret before the final call. Let \(E_W=\{a,b\}\cap W\), so \(1\le|E_W|\le2\). The four disjoint designated recipient groups

\[
\{r_W\},\quad H_1^W,\quad H_2^W,\quad E_W
\]

are all collectively complete in the **unchanged chronological tree \(W\)**, with arbitrary unused helpers. Their total number of recipients is \(1+1+2+|E_W|\le6\), contradicting the Stage 11 lower bound \(2^{4-1}=8\) for **four disjoint groups**.

Therefore \(|H_1^W|+|H_2^W|\ge4\) for each \(W\in\{U,V\}\). In fact, if either \(H_i^W\) is singleton, the same four-group inequality gives \(|H_{3-i}^W|\ge4\) when \(|E_W|=2\), or \(\ge5\) when \(|E_W|=1\), so a one-plus-two arrangement is impossible.

The argument uses exact information support, the original two last local contacts, and the helper-robust tree theorem; it **does not** posit a globally strict ordering of separate arms.

## Main theorem — ten off-corner participants

Since \(H_1,H_2\) partition the untouched off-corner participants between \(U\) and \(V\),

\[
|H_1|+|H_2|=\sum_{W\in\{U,V\}}\bigl(|H_1^W|+|H_2^W|\bigr)\ge8.
\]

Exactly two excluded endpoints \(a\in D_1\), \(b\in D_2\) were removed, hence

\[
\boxed{|D_A|=2\quad\Longrightarrow\quad m_{13}+m_{23}\ge10.}
\]

By reversing the **entire original** shortest schedule (not rearranging it) and exchanging the roles of prefix and suffix, the symmetric theorem holds:

\[
\boxed{|D_B|=2\quad\Longrightarrow\quad m_{31}+m_{32}\ge10,}
\]

where \(D_B\) are the distinct reverse-private central positions.

**Additional geographic refinement.** If the last reversed cycle call \(ab\) has *both endpoints in one of the two penultimate-tree sides*, say \(U\), then in the untouched opposite side \(V\) every local \(V\)-secret must have at least two carriers in **each** \(H_1^V,H_2^V\) (no final contact touches \(V\)). The one-root three-recipient double-cover lemma of Stage 13 then forces \(|H_1^V|,|H_2^V|\ge3\) separately. Combined with the universal \(|H_1^U|+|H_2^U|\ge4\), this yields

\[
\boxed{\text{both cycle endpoints in one tree side}\quad\Longrightarrow\quad m_{13}+m_{23}\ge12.}
\]

The **uniform** bound \(10\) permits the last reversed call \(ab\) to cross the \(U/V\) cut. The bound 10 is only **necessary**, not known sharp for real local chronologies, and certainly not claimed realizable in a successful both-cyclic complete gossip scheme.

### New finite-state exclusions, using previously proved universal off-corner minima

For a hypothetical both-cyclic 3×3, all four off-corners are at least two, all four corners are positive, and \(m_{33}=|X|\ge2\) if \(|D_A|=2\) or \(|D_B|=2\). Therefore

- If \(|D_A|=2\), then \(n\ge(10+4+4+2)=20\).
- If \(|D_B|=2\), likewise \(n\ge20\).
- If **both** \(|D_A|=|D_B|=2\), both off-corner pairs sum to at least 10, so \(n\ge 10+10+4+2=26\).

In particular every hypothetical counterexample with \(n=18\) or \(19\) has \(|D_A|\le1\) and \(|D_B|\le1\). For \(n\le25\), the two private-direction capacities **cannot simultaneously attain two**. These are chronology-state pruning rules **in addition to**, not replacements for, the stronger Stage 18 size-only condition forbidding an exact \((2,2)\) off-corner pair for \(n\le42\).

## Independent adversarial checks and an invalid shortcut

[stage20_root_cut_probe.py](stage20_root_cut_probe.py) independently enumerates labelled chronological trees through six people, validates that no FOUR disjoint complete-cover groups of total size 5 or 6 exist even when arbitrary helpers are allowed, and replays a five-person chronological tree with two *disjoint two-person collectively complete groups* but a **non-causally sealed** four-root partition. That explicit local counterexample blocks an attractive but invalid attempt to generalize Stage 14's four-arm rigidity to arbitrary size-three off-corner cells solely from a pair of size-two *collective covers*. The four-root counterexample does **not** violate Stage 17's double-carrier requirement for genuine hypothetical midpoint chronologies because it is only an isolated tree instance.

**Limitations:** no formal proof-assistant certificate; independent local testing is finite; the all-n claim rests on the complete tree-cover and original fixed chronology proofs; historical novelty not certified (Labahn 1995/Krumme 1996). PR #1 remains DRAFT, OPEN and UNMERGED. The original chronological half-forest conjecture remains OPEN.
