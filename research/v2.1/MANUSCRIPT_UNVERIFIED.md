> **ARCHIVAL DRAFT — UNSAT CLAIMS UNVERIFIED AFTER UI INTERRUPTION.** The solver source files and certificates cited below were not preserved. Read STATUS.md before interpreting the finite n15 conclusions. Do NOT cite this text as a verified theorem.

# Original-Chronology Half-Forest Restrictions in Optimal Telephone Gossip

## A Computer-Assisted Classification Through Fifteen Participants Using Temporal Information Profiles

**Working mathematical manuscript — 25 October 2026.** Not externally peer reviewed or submitted. Historical priority beyond the sources below remains under investigation.

### Abstract

A successful minimum-call telephone-gossip schedule on \(n\ge4\) participants consists of exactly \(2n-4\) bidirectional calls, each transmitting all information currently known by either endpoint. We require the unordered contact pairs to be distinct and split the **original unchanged chronological sequence** into two halves of length \(n-2\). We investigate whether at least one half is a forest. Extending a structural information-flow argument and the independently checked finite classifications for \(n\le14\), we establish a computer-assisted finite theorem for \(n=15\). An incidence-and-collector filter reduces 13,680 eligible cycle placements to 945 placements in 20 equivalence classes. Seven classes have locally infeasible components. Ten more have incompatible **exact** compressed prefix/suffix information profiles. The remaining three are still infeasible after permitting vertices in a large prefix tree to know additional secrets—a conservative relaxation. Two independently organized compatibility searches, independent local-order checks and randomized semantic tests verify the certificate. Thus every successful 26-contact gossip schedule on 15 participants has a forest in its first or last 13 original contacts. This is **not** a universal result for arbitrary \(n\), nor a proof of the fixed-label temporal-clique \(2n-3\) conjecture. Its historical originality remains a separate open scholarly question.

### 1. Model and precise statement

Let \(V=\{1,\ldots,n\}\). Each participant \(v\) initially knows just the secret \(v\). A *call* \(uv\) replaces both endpoints' known-secret sets by their union. We consider an ordered sequence \((e_1,\ldots,e_{2n-4})\) of **pairwise different unordered pairs**, successfully disseminating all secrets to every participant. Define the prefix \(L=(e_1,\ldots,e_{n-2})\) and suffix \(R=(e_{n-1},\ldots,e_{2n-4})\), in their original orders. The underlying static contact graphs of the two halves may have disconnected components.

**Theorem A (finite half-forest classification).** Every such successful schedule on \(4\le n\le15\) has at least one half whose static contact graph is acyclic. At \(n=15\), the assertion follows from the complete, reproducible finite reduction developed below; the smaller instances are covered by the previously proved/certified \(n\le14\) result and the classical vertex-extension principle.

### 2. Structural reduction and classical dependencies

Write \(P_0,\ldots,P_{r-1}\) for the connected components of \(L\), and \(Q_0,\ldots,Q_{s-1}\) for those of \(R\). Every \(P_i\cap Q_j\) is nonempty: otherwise, secrets originating in \(P_i\) could never enter \(Q_j\) after the cut. Hence \(rs\le n\). Since each half has \(n-2\) edges, its cycle rank is respectively \(r-2\) or \(s-2\). If **both** halves are cyclic then \(r,s\ge3\).

The earlier *rectangular-grid bound* states that if \(r=3\) and \(s\ge4\), then \(n\ge5s-4\), and conversely with the two halves reversed. It uses two tree components on the three-component side, at most two complete information collectors in each contact tree, and the fact that a singleton cell needs its own collector. Thus, for \(n\le15\), a hypothetical both-cyclic schedule necessarily has **\(r=s=3\)**. Each half then contains precisely one unicyclic component and two tree components. The \(3\times3\) intersection matrix \(M=(|P_i\cap Q_j|)\) has all entries positive and sums to \(n\).

We use these previously established necessary constraints:

1. **Cell coverage:** for every \(P_i,Q_j\), the union of midpoint knowledge at \(P_i\cap Q_j\) contains every original \(P_i\)-secret. The same holds under reversal for \(Q_j\)-secrets.
2. **Tree collector budget:** only endpoints of a tree component's last internal call can know all its secrets. Each singleton cell therefore forces one collector at its only vertex.
3. **First-bridge restriction:** if a suffix tree has two singleton intersections from different prefix rows, its first contact must join those entries, and a third row's secrets must be represented on both sides of that contact. A third-row cell of size two therefore forces **both** vertices to be prefix collectors.
4. **Single-source entry lemma:** if a suffix tree has even one singleton prefix-row entry, each other prefix row must supply a complete collector in its intersection with the tree. There is a reverse-time dual for a prefix tree.
5. **Known lower bound:** a unicyclic component on \(m\ge5\) participants with exactly \(m\) local calls cannot make all \(m\) participants fully informed, because optimal all-to-all gossip requires \(2m-4>m\) calls.

These structural arguments and the independent n=13,14 certificates appear in the research record `research/v1.4` through `research/v2.0`. The minimum-call bound, kernel theory, static forest decompositions, and reordering techniques are historical prior art (see References).

### 3. Temporal-profile lemma: separating sources from destinations

The main compression reduces each potentially enormous contact-order domain to a small family of exact information profiles.

Fix a prefix component \(P\), a suffix component \(Q\), and their nonempty intersection \(X=P\cap Q\), of cardinality \(k\). For each \(x\in X\), let \(K(x)\subseteq P\) be the secrets of \(P\) known by \(x\) **at the original midpoint**. Define the *prefix sufficiency profile*

\[
 B(S)=1\quad\Longleftrightarrow\quad\bigcup_{x\in S}K(x)=P,\qquad S\subseteq X.
\]

Now execute the suffix component's local contact order **backwards**, starting with one artificial, distinct token at every vertex of \(Q\). Let \(T(x)\subseteq Q\) be the set of backwards tokens reaching \(x\in X\). For each suffix vertex \(v\in Q\), define

\[
 A_v=\{x\in X\colon v\in T(x)\}.
\]

A temporal path from \(x\) to \(v\) through the original suffix exists precisely when its reverse is a temporal path from \(v\) to \(x\) through the reversed suffix. Consequently, the original suffix delivers all \(P\)-secrets to **every** vertex of \(Q\) if and only if

\[
 \boxed{B(A_v)=1\quad\text{for every }v\in Q.}
\]

Store \(B\) as the bitmask of subsets \(S\subseteq X\) for which \(B(S)=1\), and store \(D\) as the bitmask of all subsets \(A_v\) required by the suffix. Then the condition is exactly

\[
 \boxed{B\mathbin{\&}D=D.}
\]

**Proof of equivalence.** At the midpoint, a \(P\)-secret can enter \(Q\) only through a member \(x\in X\) already carrying it. The final suffix vertex \(v\) receives precisely those entry secrets carried at \(x\)'s for which a nondecreasing-time path from \(x\) to \(v\) exists. The reverse-token experiment identifies exactly that set \(A_v\). The required union of entry knowledge sets is therefore all of \(P\) if and only if \(B(A_v)=1\). \(\square\)

Since different prefix components use disjoint participants, their internal calls commute; the same holds for different suffix components. Hence the family of component-local chronological orders suffices to describe **all global information-transfer possibilities**. We choose one prefix profile for each \(P_i\) and one reversed-suffix profile for each \(Q_j\), requiring compatibility in every cell \((i,j)\).

**Sound relaxation.** We do *not* impose disjointness between edges chosen in the prefix and suffix; allowing the same unordered pair to occur in both halves only **enlarges** the set of profile assignments. Therefore **UNSAT under this relaxation proves UNSAT under the required distinct-edge model**. A relaxed SAT assignment would not, by itself, be a valid gossip schedule.

### 4. Optimistic two-side tree lemma

A large tree component would make exhaustive contact-order enumeration expensive. The remaining large cases all contain a prefix tree with **one mandatory full collector in each of two different cells**. Since at most the two endpoints of a tree's final call can be complete collectors, the final edge must join some \(x\) and \(y\) in those two cells. Deleting \(xy\) partitions that prefix tree into sides \(A\ni x\) and \(C\ni y\).

Before the final call, all contacts occur separately inside \(A\) and \(C\). Immediately afterwards only \(x,y\) can have received secrets from both sides. Hence every non-endpoint vertex in \(A\) knows **at most** the original \(A\)-secrets, and every non-endpoint in \(C\) knows **at most** the original \(C\)-secrets. Give the two endpoints *all* secrets and optimistically give **every other vertex all secrets on its own side**, irrespective of what it could truly know. Enumerate every possible bipartition and choice of endpoint vertices.

The resulting sufficiency profiles dominate the actual profiles *pointwise*. For each potential actual prefix profile \(B\) there is an optimistic profile \(B^+\) with \(B(S)\le B^+(S)\) for every subset \(S\). Thus an UNSAT profile compatibility test using all optimistic possibilities excludes even more generous information distributions than any real tree chronology and **is a sound impossibility certificate**.

This is an over-approximation, not a claim to have generated every real eight-vertex tree order.

### 5. Complete finite computation for fifteen participants

With \(r=s=3\), exactly six extra participants beyond the nine mandatory intersections must be distributed into the \(3\times3\) grid: \(\binom{14}{6}=3003\) allocations. For each possible position of the unique prefix and suffix cycles, the structural filters give:

| Necessary-condition stage | Placements remaining |
|---|---:|
| Initial eligible cycle placements | 13,680 |
| Classical first-bridge and collector filters | 4,662 |
| Single-source entry and its dual | 945 |
| Cycle-position-aware orbits under row/column relabeling and time reversal | **20** |

All twenty orbits are then adjudicated as follows:

| Exclusion method | Orbits | Individual placements represented |
|---|---:|---:|
| Local component contact-order impossibility | 7 | 333 |
| Exact compressed global profiles, small components | 10 | 432 |
| Global profiles with optimistic large-tree information | 3 | 180 |
| **Total excluded** | **20** | **945** |

For components of at most six vertices, a C++ oracle enumerates *all ordered distinct contact sequences* of length \(m-1\) (tree) or \(m\) (unicyclic), checking graph connectivity, local cellwise secret coverage, and mandatory collectors. It records the resulting exact forward and reversed temporal profiles. For the relevant seven-vertex components, a second exhaustive local oracle prunes duplicate \((\text{used-edge set},\text{knowledge state})\) pairs, a provably semantics-preserving quotient, and certifies the locally infeasible cases. Its largest relevant UNSAT computation explores 55,208,475 distinct terminal state visits. No seven- or eight-vertex component requiring unsupported exhaustive profile enumeration is silently declared infeasible: the surviving large-tree cases are addressed by the optimistic lemma above.

The global finite constraint program chooses profiles \(B_i\) and \(D_j\) for each of three prefix and three suffix components. Every actual schedule induces a feasible choice, so absence of a choice excludes it. A second implementation **enumerates all suffix-profile triples first**, then independently checks for a compatible prefix profile in every row. It agrees on UNSAT for all 13 globally resolved orbits (ten exact-profile cases and three optimistic-tree cases). The other seven orbits have independently recorded local-order obstructions.

**Adversarial checks.** The forward/reversed temporal-profile equivalence was checked against direct information propagation on 3,200 randomized pairs of contact schedules. The C++ exact local-profile domain generator agrees with a separate Python exhaustive generator on four small component types. Finally, actual eligible random tree chronologies were compared against independently constructed optimistic side-information profiles: each genuine profile was contained in an optimistic one. These tests are validation of implementation invariants, not substitutes for the proofs above.

All twenty orbit statuses, their representative matrices, cyclic positions, multiplicities, reason categories and profile-domain sizes are recorded in machine-readable `N15_CERTIFICATE.json`. The entire deterministic computation is runnable without optional SAT/SMT dependencies.

**Proof of Theorem A for \(n=15\).** Suppose both chronological halves contain a cycle. Section 2 reduces the case to a positive \(3\times3\) incidence matrix with one cyclic prefix component and one cyclic suffix component. The collector and single-source restrictions reduce the possibilities to the twenty representative cases enumerated above, with symmetry preserving success and the forest property. Every representative is impossible, by exhaustive local-order checks or UNSAT in a sound global information-profile relaxation. Hence no both-cyclic successful schedule exists for \(n=15\). Together with the previous finite results for \(n\le14\), the stated range follows. \(\square\)

### 6. Reproducibility and independent verification

From the repository root:

```bash
python3 research/v2.1/prove_n15.py
python3 research/v2.1/verify_profile_semantics.py
python3 research/v2.1/verify_n15_independent.py
```

The first command compiles two self-contained C++17 oracles with `g++ -O3 -std=c++17`; no third-party runtime dependencies are required. Both verification scripts require only standard-library Python. GitHub Actions CI executes the commands on a fresh Linux runner. Every UNSAT check is deterministic, with no search-depth timeout treated as success.

The proof is **computer-assisted** and its implementation has undergone two independent verification approaches. It is not a Lean/Coq machine-formally checked proof and has not undergone external mathematical peer review. If a future checker errors or times out, the correct status is **unverified**, not automatically UNSAT.

### 7. Historical context, significance and limitations

Classical \(2n-4\) optimal call bounds, successful-edge-order characterizations, four-cycle and static forest decompositions and the two-contact vertex extension predate this work (Göbel, Cerdeira and Veldman 1991). Labahn (1995) classified minimum-call gossip kernels, admissible permutation structures and linear extensions. Krumme (1996) proved powerful *existential reordering* theorems. These results concern static or re-orderable structure, rather than explicitly asserting that the **original unmodified two equal-length halves** obey our finite invariant. The complete supplied originals of Labahn and Krumme were examined in `research/v1.8/`. No verbatim duplicate was located there; **historical priority or mathematical nonderivability from all prior results is not certified**.

The finite theorem through fifteen participants does **not** settle the conjecture for all \(n\), provide a counterexample, or prove the separate \(2n-3\) sparse subgraph conjecture for an adversarially fixed edge-order temporal clique. The present \(r=s=3\) reduction ceases to be exhaustive at \(n=16\), where \((r,s)=(3,4)\) can become feasible under the rectangular-grid bound. The finite \(n=15\) result is therefore a rigorously delimited stopping point, not an extrapolated asymptotic breakthrough.

### References

1. F. Göbel, J. O. Cerdeira, and H. J. Veldman, “Label-connected graphs and the gossip problem,” *Discrete Mathematics*, 87 (1991), 29–40. DOI: 10.1016/0012-365X(91)90068-D.
2. R. Labahn, “Kernels of minimum size gossip schemes,” *Discrete Mathematics*, 143 (1995), 99–139. DOI: 10.1016/0012-365X(94)00031-D.
3. D. W. Krumme, “Reordered gossip schemes,” *Discrete Mathematics*, 156 (1996), 113–140. DOI: 10.1016/0012-365X(94)00302-Y.
4. D. B. West, “A class of solutions to the gossip problem, Part I,” *Discrete Mathematics*, 39 (1982), and “Part II,” *Discrete Mathematics*, 40 (1982). See: https://dwest.web.illinois.edu/pubs/gossip1.pdf and https://dwest.web.illinois.edu/pubs/gossip2.pdf.
5. M. Renken, *Algorithmic and Structural Aspects of Temporal Graphs*, doctoral thesis, 2023. https://d-nb.info/1289610584/34.

**Repository evidence:** The complete prior experiments, exact finite reductions, independently implemented scripts, literature audit and the relevant CI logs are maintained in the draft research PR for `SaridakisStamatisChristos/2nquestion`.