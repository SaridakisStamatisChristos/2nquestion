# Universal small-cell hub forcing and a 28-person four-quadrant lower bound

**30 October 2026. Exact original-order, edge-once chronological trees; unbounded total size and arbitrary unassigned helpers.** This is a conditional structural theorem, not an all-width impossibility proof. It strengthens the earlier per-quadrant >=3 bound without changing that older historical checkpoint.

## Lemma U.15 — small crossed rooted cell forces the other tree's complete collector

Let A and B be finite original-order edge-once chronological trees with shared designated cell E = V(A) intersect V(B), with 1 <= |E| <= 4. Assume:

- A has a terminal complete collector r outside E;
- B has a terminal complete collector p outside E;
- for **every** original source a in A and b in B, their exact terminal E-recipient supports intersect.

Then **the second terminal complete collector of B belongs to E**. In particular B cannot have both actual last-edge complete endpoints outside E.

**Proof.** Every A original source has nonempty exact E support. Suppose instead that B's two complete last-edge endpoints are outside E.

If some A source has singleton exact E support {v}, exact crossing makes v a terminal complete collector of B: every B-original secret must be known by v. This contradicts the fact that the *only* complete collectors in an edge-once chronological tree with >=2 vertices are its two last-call endpoints, both assumed outside E.

Otherwise every A-original secret is held by at least TWO E people. In particular, A is doubly E-covered; by the universal small-recipient rigidity Lemma U.2 (ROOTED_SUPPORT_TRANSVERSAL.md), |E| is 3 or 4 and there exist two **distinct exact** original-source E supports {c,a} and {c,b}, where a,b,c are three different E people.

Delete B's ACTUAL last call. It separates B into two preceding independent original-order trees, each with its full last-edge endpoint as an outside-E root. Since those endpoints are outside E, no E person's knowledge changes at B's final call, and every B-original source has all its exact E recipients within its own preceding component.

The common E vertex c lies in one of the two components. Choose the *other* component H. Every original H source must have an exact E support avoiding c, yet intersect BOTH {c,a} and {c,b}. Therefore each H original secret is known by BOTH a and b. These two vertices must lie in H and are terminal complete collectors of H. But H's final-edge B endpoint is a THIRD complete collector of H and is outside E, contradicting the at-most-two-complete-collectors theorem for a chronological tree. (H cannot be a singleton, since it would then have no E recipient meeting both pairs.) Contradiction.

Thus B's second complete collector lies in E. QED.

This proof does **not** require A to be doubly covered as an input hypothesis: singleton E supports are handled separately. It does **not** use a finite-size enumeration; the only small constant is the recipient set size |E|<=4, while A and B may have arbitrarily many helpers.

## Theorem U.16 — every quadrant of a minimum-center crossed pair has at least SEVEN people

Assume an admissibly crossed pair P exists, in the precise sense of FOUR_HUB_MINIMAL_DESCENT.md, and choose one minimizing shared-center size. By Theorem U.14, its four local complete hubs occupy four distinct quadrants in alternating diagonals.

Fix a quadrant Q_ij = V(T_i) intersect V(U_j). Exactly one of its two rooted side trees has its local second full collector INSIDE Q_ij. Without loss of generality this is T_i, whose actual last local call is r-y with r outside X and y inside Q_ij. Both last-call full endpoints of U_j are outside Q_ij (its outside root and its second hub in the other row of column j).

Delete T_i's actual last local call r-y into two pre-final rooted chronological components A (with complete root r) and B (with complete root y). Delete U_j's actual last local call into two pre-final rooted components; let C be the one NOT containing y. Its complete root p is outside Q_ij. Define disjoint center cells

 E_A = V(A) intersect V(C),   E_B = V(B) intersect V(C).

These sets lie inside Q_ij minus {y}. Both are **NONEMPTY**: for every source in A (respectively B) and every original C source, the exact all-pairs support crossing of Lemma U.12 must occur inside E_A (respectively E_B). The deleted actual local last calls change knowledge only at their endpoints. In particular T_i's last call can move A-source knowledge to y, but y is outside C; U_j's last call has both endpoints outside Q_ij. Thus the original local A/C and B/C chronological histories still cross on their EXACT shared sets E_A,E_B.

The roots r of A and y of B both lie outside their corresponding E sets; y is outside C by definition. The root p of C lies outside both E sets. Therefore Lemma U.15 applies to **each** crossed pair (A,C) and (B,C) whenever its E cell has size at most four.

C has one outside-E complete root p and only ONE possible other terminal complete collector w. Because E_A,E_B are disjoint, **both cannot have size at most four**, or Lemma U.15 would require w to belong to both. At least one of E_A,E_B consequently has size >=5, and the other has size >=1. Since y is a different vertex in Q_ij, outside C,

 |Q_ij| >= 1 + |E_A| + |E_B| >= 1 + 5 + 1 = 7.

The argument is symmetric if U_j, rather than T_i, carries the quadrant's inside complete hub. It therefore applies to all four quadrants. They partition X and give

 **|Q_ij| >= 7 for all four i,j, and |X| >= 28.**

QED.

## Claim gates

- **Human-proved conditional lemmas U.15 and U.16**, assuming the previously documented U.2, U.12 and U.14 exactly as stated.
- The `hub_forcing_audit.py` finite adversarial checker independently replays small chronological trees and challenges the two-support forcing mechanism; a finite audit is **not** the reason the universal claim holds.
- **No unrestricted contradiction:** |X| >=28 leaves centers of arbitrary larger size possible. This theorem does NOT resolve P, the original-half-forest conjecture, or the distinct 2n-3 temporal-clique spanner existence conjecture.
- No external referee, Lean/Coq check or historical novelty validation is claimed. Keep manuscript HOLD and PR DRAFT.
