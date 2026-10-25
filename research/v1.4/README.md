# v1.4 — a first-bridge covering lemma and the finite n=13 half-forest theorem

A general information-flow necessary condition excludes 43 of 44 nominal double-cyclic 13-vertex gossip configurations; exact chronological enumeration rejects the sole remaining square incidence pattern. An unquotiented audit enumerates 1,278 candidate cycle placements and confirms that nine survivors are symmetric copies of that pattern.

**Run from repository root:**

```sh
python research/v1.4/half_forest13_reduction.py
python research/v1.4/verify_square.py
```

Read [RESEARCH_UPDATE_v1.4.md](RESEARCH_UPDATE_v1.4.md) for the proof, assumptions, exact finite-search coverage and limitations.

**Scope:** this is a finite result for shortest distinct-contact gossip schedules, **not** a proof of the universal 2n-3 temporal-clique spanner conjecture. Prior-art novelty unchecked. Keep PR draft pending independent review.
