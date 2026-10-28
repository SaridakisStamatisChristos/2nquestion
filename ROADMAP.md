# Research roadmap: pursue universal novelty, not incremental tuning

## 28 October 2026 — Evidence-gated SOTA route after Stages 29–30

**Principal target** is still the all-labelings exact \(2n-3\) temporal clique reachability spanner, NOT the different multiplicative-hop-stretch 3-spanner problem. Current best prominently published unconditional reachability upper bound is 7n (Baligács 2026); the author's September 2026 open-problem summary notes a same-algorithm 6n analysis refinement. Neither is 2n-3. Treat new title similarity as an adversarial priority/model-semantics risk.

**Auxiliary conditional route:** original fixed-chronology half-forest human arguments cover n<=21 with finite evidence; n>=22 OPEN. Universal both-cyclic incidence geometry reduces to 3x3 by Bumby Theorem 3, but the n22 necessary-size/profile frontier still has **104** labelled survivors in **28** symmetry orbits. An incidence survivor does not construct a full successful 2n−4-contact chronology.

**New reusable exact all-n results:**
1. Stage 29 p(c) exact privacy threshold, including **zero privacy already possible for c>=6**. NEVER extrapolate the earlier c<=5 positive privacy oracle to large c.
2. Stage 30 when (1,1,6) off-corner tree privacy is zero: four exact support pairs form two disjoint 3-vertex paths, forcing each opposing target's six-bit support into a **25-of-63 upward-closed mask domain** (four binary pair-hitting clauses). This is a **conditional exact-information CSP gate**. It does not prove that the opposite unicyclic chronology must also have this special shape.
3. Stage 30 pairwise incompatibility for **TWO** such privacy-free six-cell chronological TREES; do not invoke for a TREE vs UNICYCLIC pair without additional proof.

**Next evidence-producing actions, ranked:**
1. **Implement an exact original-order information-profile solver** for Stage30-eligible n22 incidence orbits. Branch explicitly on whether the sharp off-corner tree has ≥1 private recipient (which forces an opposite collector) or zero private recipients (which forces the four-edge 2P3 support system). The zero-private branch must add the four Boolean hitting clauses per target; branch coverage must be exhaustive, not chosen by convenience. Compare to a separate faithful chronology oracle and report UNSAT only after independent confirmation.
2. **Resolve n22 only if every 104 incidence-necessary survivor is excluded by a sound proof/oracle** or supply a fully replayable 40-contact both-cyclic schedule. Avoid promoting local SAT/UNSAT or matrix rejection to a theorem without complete coverage and verified certificates.
3. **Generalize support-transfer inequalities beyond center width 6** (arbitrary receiver groups, arbitrary helpers, unicyclic last-edge spine). Seek a global obstruction not dependent on bounded numerical sizes, or a genuine chronology-preserving descent; actively try to falsify any overstrong claim with c>=6 Stage29 witnesses.
4. **Maintain a distinct direct temporal-clique track:** run exact POD adversarial searches / reachability MILP n>=9 and exploit newly proved constraints only where source-target contact semantics transfer. A proof that every existing shortest gossip schedule has a forest half does NOT logically imply existence of a 2n−4/2n−3 schedule in every time-labelled clique.
5. **Independent scientific gate:** compare mechanisms/hypotheses against Bumby (1981), Labahn (1995), Krumme (1996), Baligács (2026), Casteigts et al. (2025), and the September 2026 temporal 3-spanner paper while preserving the distinction between exact reachability and stretch. Formal checker execution and outside referee review remain missing.

**Release/claim gate:** Stage29/30 = human-proved conditional/local all-n lemmas with executable boundary checks; not machine-formal proof, external peer review, established historical novelty, global half-forest solution, or SOTA 2n−3 construction. Keep PR #1 DRAFT, UNMERGED and publication HOLD.



**Primary objective:** prove or refute that every distinct-time temporal clique has a `2n-3`-edge spanner. A known published construction attains only a larger linear bound; consult [REFERENCES](REFERENCES.md) for priority anchors.

## Highest-information tasks

1. **Adversarial structural generation.** Generate non-pivotable and non-dismountable chronologies; naive uniform shuffles frequently have a pivot at n=7,8 and waste search time. Preserve actual chronological edge order and random seeds.
2. **Certified n>=9 optimization.** Combine the v0.5 exact frontier-cut formulation with an independent time-expanded MILP formulation. For a suspected counterexample to `2n-3`, require a certified infeasibility result for every size-`2n-3` selection, not only a heuristic failure. Record solver logs, versions, time limits, and model files.
3. **Challenge treewidth 3.** Try constructing a temporal clique with **no spanning 3-tree**; require full independent 3-tree enumeration or an equivalent exact solver proof. If no counterexample emerges, attempt a universal 3-tree construction with a complete inductive invariant.
4. **Global exchange conditions.** Study whether the v0.4 unbounded simultaneous-deletion obstruction can be circumvented using constrained global information-flow invariants. Local pairwise tests alone are provably insufficient.
5. **Research-priority audit.** Compare proposed new structural statements against historical minimum-gossip, dismountability, 2-arch/2-degeneracy, temporal reachability sparsification and treewidth literature. Distinguish temporal stretch-3 from static treewidth 3.

## Gating criteria

A **breakthrough** requires either (a) a complete human-checkable universal proof with independent adversarial audit, (b) a minimal counterexample with a certified nonexistence result, or (c) another universal theorem plus verified scholarly-priority search showing genuinely new substance. A small instance or numerical pattern is a research artifact, not a paper-worthy novelty declaration by itself.

## Next target after v0.8: exact non-pivotable n >= 9 obstruction search

1. Do not optimize for failure of a fixed set of greedy permutations: v0.8 demonstrates this metric can declare a readily solvable schedule difficult.
2. Generate non-pivotable, non-1/2/3-hop-dismountable chronologies and separate instance generation from exact witness/infeasibility validation.
3. To refute POD, produce an order with **certified infeasibility** under cardinality bound `2n-4`; an exact solver timeout is UNKNOWN.
4. To refute the primary `2n-3` conjecture, prove no temporal spanner with <=`2n-3` exists for a particular chronology.
5. For any positive universal result, write and adversarially audit the complete proof; compare exact hypotheses with Bumby (1981), Göbel–Cerdeira–Veldman (1991), SAND 2025, and Baligács (2026).

## v1.1 research direction: chronology and kernel compatibility

- **PROVED boundary:** for shortest gossip schedules n<=7 both halves are forests; for n>=8 a cyclic half is possible by an explicit infinite construction; n<=10 at least one half is always a forest.
- **OPEN beyond n=10:** Is at least one chronological half always a forest in a minimum gossip schedule? An adversarial walk n=11..14 produced no counterexample, but may be biased.
- **NEXT:** Investigate implications for nonpivotable fixed-time cliques and compare all half-component results against Labahn (1995) and Krumme (1996) before novelty claims.
- **CRITICAL:** The central `2n-3` conjecture and the stronger POD conjecture remain open; this structural boundary neither proves nor refutes them.
