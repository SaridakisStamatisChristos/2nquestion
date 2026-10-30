# Universal crossed-tree research gate — 30 October 2026

## Confirmed, not rediscovered

The sharp all-s recipient-group construction is already proved as U.9b in GENERAL_COVER_PACKING.md and implemented by `sharp_all_s_groups` in `general_group_cover_audit.py`. Its recurrence duplicates H(s-1), executes both copies, joins their full roots by one last call, and merges each nonroot group pair. It yields 2^(s-1) vertices and group sizes (1,1,2,...,2^(s-2)). Do not claim a new theorem or new verification run here.

## Exact unrestricted target

Find or rule out two original-order edge-once chronological trees T,U with intersection X such that (i) the actual final-call endpoints in each tree lie outside X and are full; (ii) each original secret has at least two distinct X carriers in its own tree; (iii) for every source a of T and b of U the exact X carrier supports intersect. Neither incidence-only supports nor reorderable calls suffice.

## Minimal obstruction (conditional U.14)

Choose an admissible pair with minimum |X|. Removing each actual last call yields four nonempty quadrants Q_ij. A quadrant whose T-side and U-side local last-call second endpoints both lie outside it inherits all three conditions, giving strict descent. Therefore four second endpoints must occupy the four quadrants in complementary diagonals. This is a reduction, not a contradiction.

## Next proof/falsification gate

For the alternating four-hub case, explicitly track for each quadrant (a) its T-side local last-edge full hub, (b) its U-side local last-edge full hub, (c) all exact source supports, and (d) which outside-root last contacts cannot alter X supports. A proposed impossibility proof must derive a contradiction from actual temporal causality for arbitrary quadrant sizes, not a fixed-width bound. A proposed counterexample must provide full vertex/edge/time lists, bitset replay, and exhaustive cross-pair checking.

## Evidence boundaries

The existing finite `general_group_cover_audit.py` exercises s=1..8; CI workflow `research-universal.yml` includes it. This document does not assert a fresh CI run, a formal proof assistant result, or a solution of the all-width crossing problem. The auxiliary original-half-forest conjecture and the primary 2n-3 exact temporal clique spanner conjecture remain separate and OPEN.
