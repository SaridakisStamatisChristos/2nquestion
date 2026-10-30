# v1.0 — butterfly-core finite classification

Exact finite computer-assisted result: BF(n) holds for shortest simple-contact gossip schedules at n=4,5,6. No general proof, novelty, or 2n-3 breakthrough claimed.

- `RESEARCH_UPDATE_v1.0.md` — definitions, finite theorem, scope, prior art, and proof obligations
- `exhaustive_kernel.cpp` — all first-edge-normalized distinct-contact shortest schedules n=4,5,6
- `independent_kernel_verify.py` — independent n=5 enumeration and 8,000 reachability differential checks
- `kernel_walk.cpp` — explicitly heuristic n=6..10 falsification walks; no negative result can imply truth
- `results.json` — deterministic enumerations and seeded search summaries
- `INCIDENCE_WINDOW_LEMMA.md` — universal elementary proved necessary condition on the first/last calls of each vertex

Reproduce via commands in the mathematical note. The `n=6` enumeration has 17,297,280 normalized orders, of which 83,808 are valid and all contain a chronological butterfly.
