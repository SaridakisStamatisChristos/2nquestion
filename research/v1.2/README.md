# Checkpoint v1.2 (2026-10-25)

- `RESEARCH_UPDATE_v1.2.md`: complete human proof through n=11, complete finite n=12 reduction, methodological caveats, and research objectives.
- `double_cycles.py`: exact local-order enumerator for proposed simultaneous cyclic halves.
- `exhaust12.py`: enumerates 3x3 component-grid isomorphism classes, cycle placements and all possible constrained contact orders at n=12.
- `exhaust12.log`: complete output from the n=12 run.
- `verify_v12.py`: independent n=8 gossip oracle and n=11 canonical necessary-configuration check.

Run (Python 3.10+, no dependencies):

```sh
python research/v1.2/verify_v12.py
python research/v1.2/exhaust12.py
```

Status: human proof n<=11; finite machine enumeration n=12; **NO solution to the general temporal clique 2n-3 conjecture; POD remains open.** Scholarly originality not established. No CI/formal-prover claim.
