# Universal quadrant recipient lower bound (human proof, 30 October 2026)

## Theorem (every quadrant of a minimal admissible four-hub pair has at least three people)

Assume the exact crossed-tree problem P and choose an admissible pair with minimum shared-center cardinality. By U.14, its four local second-last-edge complete collectors occupy complementary diagonals, exactly one per quadrant Q_ij. Then **|Q_ij| >= 3 for each i,j**, hence |X| >= 12.

**Proof.** Fix a quadrant Q = V(T_i) intersect V(U_j). Exactly one of the two local rooted side trees T_i and U_j has its second final-edge complete collector inside Q, because the four hubs occupy different quadrants. Without loss of generality, T_i has its hub in Q, whereas U_j has both of its actual last-edge full endpoints outside Q (its root is outside X and its second endpoint lies in the other quadrant of column j).

By U.12, every original U_j source has a nonempty exact Q-support and every T_i original source's exact Q-support intersects every U_j original source's exact Q-support. Delete the actual final local call of U_j. Its endpoints are both outside Q, so the two preceding independent components partition Q into Q_A and Q_B. Each component has original secrets with nonempty Q-support, hence Q_A and Q_B are nonempty. Choose one original source from each component; their exact Q-supports A and B are disjoint and nonempty.

The all-pairs crossing property means **each** of A and B collectively covers every original T_i secret: for each source a in T_i, some recipient in A and some recipient in B knows a. The outside full root r_i of T_i is a third disjoint complete recipient group {r_i}. Therefore T_i possesses three pairwise-disjoint collectively complete recipient groups A, B, {r_i}. The sharp helper-robust group-cover lower bound U.9 for s=3 gives |A|+|B|+1 >= 4. Since A,B are disjoint subsets of Q, |Q| >= |A|+|B| >= 3. The case where U_j has its hub inside Q is symmetric. All four quadrants have size at least three, so |X|>=12. QED.

## Scope and novelty gate

This is a valid all-width **conditional** consequence of U.9, U.12 and U.14, but the numerical conclusion |X|>=12 is WEAKER than the existing unconditional-for-P |X|>=14 from CROSSED_TREE_COVER_TRANSFER.md. Its only additional information is the per-quadrant restriction for a minimal counterexample. It is not an all-width impossibility theorem, not a counterexample, and not a resolution of either the original-half-forest or the distinct 2n-3 temporal-clique spanner conjecture. No claim of independent refereeing or historical novelty.
