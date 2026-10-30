# v0.9 — exact incident-local MILP and n=10 falsification search

**Scientific status:** source-verified finite evidence and proof of an exact mathematical formulation; **no new universal spanner theorem and no demonstrated scholarly novelty.**

The local-time formulation in `incident_milp.py` uses only one binary decision per clique edge. For a fixed choice of edges, its continuous information states are forced to the exact Boolean gossip propagation. See [the research note](RESEARCH_UPDATE_v0.9.md) for the proof, benchmarks, and literature.

Reproduce from repo root:

```bash
python research/v0.9/verify_incident_milp.py
python research/v0.9/independent_check_v09.py
python research/v0.9/targeted_n10.py
```

Evidence files: `validation_results.json`, `nine_vertex_results.json`, `targeted_n10_results.json`. `targeted_n10.py` can overwrite its evidence JSON, so preserve the archived version when doing new experiments. Solver timeouts always mean UNKNOWN, **not counterexamples**.
