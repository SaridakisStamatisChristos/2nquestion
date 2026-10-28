# Universal research track — why finite incidence filters cannot solve the conjecture

**28 October 2026. This directory is the all-n research track. STOP progressing by running n=23,24,25,... incidence censuses. The goal is a theorem or counterexample with a quantifier over EVERY n, preserving the ORIGINAL fixed midpoint, and separately the original exact 2n-3 temporal-clique spanner problem.**

## Theorem U.1 — infinite counterfamily to the entire Stage25–34 size-filter strategy

For **each integer n>=23**, set t=n−16>=7 and define the positive labelled 3×3 matrix

\[
M_n=\begin{pmatrix}
1&1&2\\
1&1&4\\
2&4&t
\end{pmatrix}.
\]

**Then \(M_n\) satisfies ALL the previously implemented sound necessary-incidence rejection rules** of Stages25,26,28,32,33 and34. In particular their **complete aggregate filtering process never proves inconsistency for any of the infinitely many values \(n\ge23\)**.

### Completely symbolic proof (for ALL n; not numerical extrapolation)

The four corner cells are 1,1,1,1, and the four off-corner sizes are 2,4,2,4. Their sum is 16, so \(\sum M_n=n\) for all n≥23. Both off-corner pairs are (2,4), so the Stage25 excess parameters are p=q=2, while d=t−1≥6. Therefore the Stage25 component obstruction p+d<4 or q+d<4 fails, neither p nor q is saturated, and the exact two opposite-chronology tree private-recipient minima for groups (1,1,2) and (1,1,4) are (2,1). Their sum is only 3<4, so the privacy4 obstruction fails. The earlier three-outside and binary-rootcut cases require *center size ≤5 or 2*, so they also fail for t≥7.

Every Stage26 incidence exclusion requires center ≤6 (with one special exact center-one configuration). Stages28/32/33 reject only center one/two/three based on their full-collector restrictions. Stage34's new tree-double-cover / crossed-path exclusions require center≤5 or center exactly6. Because t≥7, **none** can reject \(M_n\). QED.

[Executable exact predicate regression](infinite_incidence_barrier.py) independently checks scattered values up to one million; **the proof is the symbolic argument above, not those finite samples**.

### What this does and does NOT mean

- **PROVED unbounded statement:** No proof whose final step is only one of these already implemented Stage25–34 *incidence/size* predicates can settle the full original-half forest conjecture. Counting ever higher n will never close this gap.
- **NOT proved:** The matrices \(M_n\) need not arise from any successful chronological 2n−4 call schedule! There is NO constructed counterexample to the conjecture. They expose a logical gap in current NECESSARY conditions, not in the conjecture.
- The original-half forest conjecture remains **OPEN for arbitrary n**; the all-n temporal-clique \(2n-3\) spanner conjecture is also **OPEN**, a DIFFERENT statement.

## The actual structural bottleneck

Each hypothetical both-cyclic original midpoint has Bumby's two closed trees plus one unicyclic component in each half, and the two unicyclic components share center \(X=P_3\cap Q_3\). The latest human arguments produce *two distinct* preceding chronological spanning trees \(T_P=P_3-e_P\) and \(T_Q=Q_3^{\mathrm{rev}}-e_Q\), with exact center source/target support families \(\{S_a\},\{T_b\}\). The TRUE original order requires

\[
\forall a\in P_3\quad\forall b\in Q_3,\qquad
S_a\cap T_b\ne\varnothing.
\]

When neither cyclic side has a center full collector and each has an untouched full exterior collector, each chronological tree has TWO complete last-edge endpoints outside \(X\), while **every** source/target secret is received by at least TWO center participants. The center therefore has a double-cover tree/tree crossing with **arbitrary** width |X|.

The new [universal rooted-support theorem](ROOTED_SUPPORT_TRANSVERSAL.md) pushes its unavoidable width lower bound to |X|≥9 with an actual unbounded human proof, not an n-specific census. But it **does not establish impossibility for arbitrary |X|**. The first open configuration in this reduced model is width9; to prove the true forest conjecture for every n, a new scale-free invariant must rule out crossing at *ALL* widths, or a valid global both-cyclic chronology must be constructed.

## General-theorem target, not a list of larger n

**Target A — complete crossed-tree obstruction for every center width.** For any two chronological edge-once spanning trees on intersecting vertex sets U,V with common designated cell X, assume each has its only two complete terminal collectors outside X and X doubly covers every original secret. Can their two center source-support families cross for *every* a∈U,b∈V? This is an independent general conjecture; proving or refuting it would close an important formerly bounded support-compatibility gap. **DO NOT assert it is true: first seek a real counterexample for large X.**

**Target B — make exterior-root hypotheses universal, or replace them.** In a hypothetical both-cyclic original schedule, large off-corner cells need not have private recipients (exact Stage29/33 witnesses). Even a full proof of Target A would not cover the cases where no pair of exterior full collectors is forced. A scale-free transfer from *collective* tree covers to crossed center support is also required.

**Target C — primary spanner conjecture.** The original \(2n-3\) exact temporal-clique reachability bound is not implied merely by a property of existing optimal 2n−4 call histories. Maintain a separate constructive/dismountability track.

## Scientific truth gate

Labahn (1995) completely characterized kernels of minimal gossip scheme partial orders, while Krumme (1996) gave a *reordering* theorem. Neither automatically supplies a claim about these **unaltered original chronological halves**. Verify exact theorem hypotheses and priority before declaring novelty. No all-n original-half proof, no 2n−3 solution, no Lean/Coq checker and no independent referee are asserted. Keep PR #1 DRAFT/UNMERGED and manuscript publication HOLD.
