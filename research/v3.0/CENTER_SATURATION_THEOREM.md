# Stage 13 — Center saturation in the original chronological 3×3 split

**28 October 2026. Status: proved, strictly conditional all-n necessary lemma. Stronger saturated-center bound m33>=12 (supersedes preliminary >=3). The original chronological half-forest conjecture remains OPEN. No original both-cyclic gossip schedule or global counterexample has been constructed.**

## Historical dependencies and precise model

Source: Richard T. Bumby, *A Problem with Telephones*, *SIAM J. Algebraic Discrete Methods* 2 (1981), 13–18, [author scan](https://sites.math.rutgers.edu/~bumby/telephone.pdf), Theorem 3 and proof (printed pages 16–17). See [source-checked Stage 12 reduction](../v2.9/BUMBY_1981_UNIVERSAL_GEOMETRY.md).

Suppose a shortest successful **fixed, unreordered** schedule of \(2n-4\) pairwise-distinct bidirectional calls has **both** original \(n-2\)-call halves cyclic. By Bumby, the prefix has closed tree components \(P_1,P_2\) and unicyclic component \(P_3\); the reversed suffix has closed tree components \(Q_1,Q_2\) and unicyclic component \(Q_3\). Define \(m_{ij}=|P_i\cap Q_j|\).

The first original suffix contact inside **each** \(Q_j\) joins \(P_1\) to \(P_2\), because it is minimal in the post-prefix contact ideal and Bumby's closed-tree lemma forces all such minimal contacts between the two closed prefix trees. By reversal, the last original prefix contact inside each \(P_i\) joins \(Q_1\) to (Q_2). Consequently the only complete reversed-suffix collectors in each tree \(Q_j\) (\(j=1,2\)) lie in \(P_1,P_2\); the only complete prefix collectors in each tree \(P_i\) (\(i=1,2\)) lie in \(Q_1,Q_2\). This conclusion concerns **actual original first/last contacts**, not rearranged schedules.

A connected component with \(v-1\) chronological calls in a tree has at most two complete collectors: only endpoints of the last call can newly know all \(v\) secrets. A unicyclic component has exactly \(v\) calls, so at most four complete collectors: nobody can know all secrets before the first \(v-1\) calls; at the (\(v-1\))st call at most two can, and at the final call at most two more may become complete. This is a valid upper bound even if the earlier \(v-1\) edges were disconnected.

## Lemma — exact two-point temporal crossing

Fix a cell \({x,y}=P_i\cap Q_j\) of size two. For each original secret \(a\) of \(P_i\), let \(A_a\subseteq\{x,y\}\) be its terminal prefix carriers inside the cell. For each participant \(b\) of \(Q_j\), let \(B_b\subseteq\{x,y\}\) be the vertices from which \(b\) is reachable by chronological suffix calls inside \(Q_j\); equivalently these are its reverse-time suffix carriers. Full successful gossip implies \(A_a\cap B_b\ne\varnothing\) for **every** \(a,b\): every path from \(a\) to \(b\) must cross the original midpoint inside this component intersection.

If **neither** \(x\) nor \(y\) is a complete reverse collector of all \(Q_j\) targets, some \(B_b\) equals \({x}\) and some (possibly different) \(B_{b'}\) equals \({y}\). Both are nonempty by global success. Every (A_a) must meet both, so \(A_a=\{x,y\}\) for every \(a\). Therefore **both** \(x\) and \(y\) are complete prefix collectors of \(P_i\). The symmetric conclusion follows by exchanging \(A,B\).

The full two-point criterion is: either both vertices are A-complete, or both are B-complete, or one of them is A- and B-complete. This is equivalent to all nonempty support pairs intersecting and is also exhaustively checked independently.

## Theorem — saturated off-corners force at least three central people

**Claim.** Under the above hypothetical both-cyclic chronological split, if

\[
m_{13}=m_{23}=m_{31}=m_{32}=2,
\]

then

\[
\\boxed{m_{33}\\ge3}.
\]

**Proof.** By the closed-tree first suffix-contact spine, neither vertex of \(P_3\cap Q_1\) is a complete reverse collector of the tree \(Q_1\). The two-point lemma forces **both** vertices to be complete prefix collectors of \(P_3\). The same is true for the disjoint two-vertex cell \(P_3\cap Q_2\). Thus four distinct vertices of unicyclic \(P_3\) are already complete, saturating its absolute capacity of four. No vertex in \(P_3\cap Q_3\) can be a complete prefix collector.

Reverse the argument using the last prefix-contact spine. All four distinct vertices of \(P_1\cap Q_3\) and \(P_2\cap Q_3\) are complete reversed-suffix collectors of unicyclic \(Q_3\), saturating its capacity. Hence no vertex in \(P_3\cap Q_3\) can be a complete reverse collector.

The central cell \(P_3\cap Q_3\) cannot be empty, since an original secret in \(P_3\) must reach every suffix target of \(Q_3\). If it were a singleton, successful crossing requires that participant to be complete on **both** sides. If it had size two, the two-point lemma requires at least one complete collector on one side (indeed, if neither point is B-complete, both must be A-complete). Both possibilities contradict the exhausted capacities. Therefore \(m_{33}\ge3\). QED.

This is an **unbounded conditional obstruction**; it does not imply all hypothetical schedules have four size-two off-corners. In particular, no reduction to this narrow saturation hypothesis has been established.

## Strong sharpening — the central cell has at least TWELVE vertices

The preceding \(m_{33}\ge3\) statement can be improved using the actual **last two contacts**, rather than merely collector counts.

### Tree double-cover lemma, one outside complete collector

Let \(T\) be a chronological tree with each edge called once. Let \(C\) be a designated recipient set and \(u\notin C\) a **complete collector** of all secrets of \(T\). Suppose every original secret of \(T\) is known by at least two **distinct** vertices of \(C\). Then

\[
\boxed{|C|\ge3}.
\]

**Proof.** The complete collector \(u\) must be an endpoint of the last contact \(uv\). Remove that edge, splitting the underlying tree into \(U\ni u\) and \(V\ni v\). Prior contacts stay within their respective sides. After the last contact the **only** person in \(U\) who can have learned a \(V\)-secret is \(u\), which is outside \(C\). Hence \(C\cap V\) contains at least two carriers of each \(V\)-secret, so \(|C\cap V|\ge2\). For any \(U\)-secret, the only possible recipient in \(V\) after the last contact is \(v\); to have two distinct designated carriers, \(C\cap U\) must be nonempty. Thus \(|C|\ge2+1=3\). QED.

The bound is sharp: on vertices \(u,a,b,c\), call \(ua,bc,ub\) in that order. Vertex \(u\) is complete, and each of the four secrets is known by at least two members of \(C=\{a,b,c\}\).

### Tree double-cover lemma, two outside complete collectors

Under the same model, if **two** distinct vertices \(u,w\notin C\) are complete and every original secret has at least two \(C\)-carriers, then

\[
\boxed{|C|\ge6}.
\]

**Proof.** A tree with its \(v-1\) edge contacts has at most two complete collectors, which must be the endpoints \(u,w\) of the last contact. Delete it, obtaining two chronological subtrees \(U,V\). No designated recipient in either side can learn an original secret from the other side at the final call, since both endpoints are outside \(C\). Therefore every secret in each side already has at least two \(C\)-carriers in that same side. Before the last contact, \(u\) is complete for \(U\) and \(w\) complete for \(V\). The one-root lemma applies to **each** subtree, giving at least three recipients on each side, for six in total. QED.

Sharpness is given by two disjoint four-person one-root constructions, with a final call joining their outside roots. This has eight vertices, seven distinct tree contacts, two complete outsiders and six double-cover designated recipients.

### Unicyclic double-cover lemma, four outside complete collectors

Let \(T\) be any chronological, connected unicyclic graph on \(v\) people, with exactly \(v\) distinct calls. Let \(C\) be a set of designated vertices, suppose **four distinct complete collectors lie outside \(C\)**, and suppose every original \(T\)-secret is known by at least two vertices of \(C\). Then

\[
\boxed{|C|\ge12}.
\]

**Proof.** Four complete collectors is the maximum possible after \(v\) calls. Immediately before the final call, there were exactly two complete collectors \(u,v'\), since at most two additional people can become complete in one call. They first became complete at the penultimate call \(uv'\) (no one can become complete earlier than contact \(v-1\)). The first \(v-1\) distinct edges must therefore be a spanning tree and \(uv'\) is its last chronological edge. Removing \(uv'\) partitions the prior history into separate tree histories \(U,V\). The final contact \(wz\) has endpoints distinct from \(u,v'\), otherwise there could not be four complete collectors. These four endpoints lie outside \(C\).

The two final endpoints \(w,z\) did not participate in \(uv'\), and immediately before the final contact their information is entirely from their own respective side of \(U,V\). To become complete in the final contact they must lie on **opposite** sides, say \(w\in U,z\in V\), and \(w\) already knows every original \(U\)-secret while \(z\) knows every original \(V\)-secret. Likewise, for \(u,v'\) to become complete at \(uv'\), \(u\) and \(v'\) already knew every original secret of \(U\) and \(V\), respectively.

Thus **each** chronological subtree has two complete outside-\(C\) collectors: \(u,w\) for \(U\), \(v',z\) for \(V\). No vertex in \(C\) takes part in either of the final two calls. Therefore a secret originating in \(U\) can have its designated carriers **only in \(C\cap U\)**, and similarly for \(V\). Each side inherits the two-fold cover hypothesis. By the two-root tree lemma each side requires at least six recipients, hence \(|C|\ge6+6=12\). QED.

The one-sided bound is attained in an explicit **local** 16-vertex unicyclic chronology: build one sharp eight-person two-root tree on vertices \(0,\ldots,7\) with outside roots \(0,1\), and another on vertices \(8,\ldots,15\) with outside roots \(8,9\). Then call \((0,8)\) and finally \((1,9)\). All calls are distinct. Exactly \(0,1,8,9\) become complete, while the other 12 people doubly cover every original secret. The precise replay is [construct_saturated_center.py](construct_saturated_center.py). This construction does **not** realize a full 3×3 two-half schedule.

### Improved original-half 3×3 consequence

When \(m_{13}=m_{23}=m_{31}=m_{32}=2\), the earlier proof showed that **all four** full prefix collectors of unicyclic \(P_3\) lie outside \(C=P_3\cap Q_3\), and all four full reversed-suffix collectors of \(Q_3\) likewise lie outside \(C\).

No vertex of \(C\) is a complete reversed-suffix collector of \(Q_3\). For **each** original \(P_3\)-secret \(a\), its support \(A_a\subseteq C\) is nonempty by full gossip. If \(A_a\) were a singleton \(\{x\}\), then every reversed-target support \(B_b\) would have to contain \(x\); this would make \(x\) a complete reversed-suffix collector of \(Q_3\), contradiction. Therefore every \(P_3\)-secret is carried by **at least two** distinct central participants.

Apply the unicyclic double-cover lemma to the original chronological \(P_3\) calls:

\[
\boxed{m_{13}=m_{23}=m_{31}=m_{32}=2\quad\Longrightarrow\quad m_{33}\ge12.}
\]

This supersedes the preliminary \(m_{33}\ge3\) consequence and, since each of the four corner cells is nonempty, yields \(n\ge4+8+12=24\) **for this saturated off-corner subfamily alone**. It does not establish the global conjecture or assert that the locally sharp 12-person construction satisfies the dual \(Q_3\) compatibility constraints.


## Independent falsification and sharpness boundary

[check_center_saturation.py](check_center_saturation.py) uses only small bitset support sets, not the Stage 11 implementation or a solver. It exhaustively verifies the two-vertex crossing equivalence for **14,400** pairs of nonempty source/target support families (each side 1–4 members). It checks **196** admissible one- and two-point central support-family pairs under zero remaining full collectors and finds no crossing pair. Locally a three-point cell *can* cross without complete collectors: take \(A\) and \(B\) both to be the three two-element subsets ({x,y},{x,z},{y,z}). Every \(A\)-set meets every \(B\)-set, but neither side has a universal collector.

This latter pattern establishes only **sharpness of the abstract support-set argument**, not realizability as a tree or cycle contact chronology, let alone a successful complete schedule.

## Proof frontier after this result

To prove the original half-forest statement for arbitrary \(n\), one must exclude **all** positive 3×3 chronological incidence sizes and all valid local event orders, not merely small or saturated cells. The natural remaining obstacle is the unconstrained large-center information-flow family and unsaturated larger off-corner cells; the 12-person bound holds ONLY when all four off-corner sizes equal two. The Stage 12 conditional sealed-four-arm bound \(t\ge64\) survives unchanged; none of these local statements is a universal contradiction. PR remains DRAFT, unmerged. Historical priority unresolved.
