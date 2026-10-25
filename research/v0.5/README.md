# Temporal Clique v0.5 research checkpoint

This is an independently verifiable exploration of the global `2n−3` temporal clique spanner conjecture. **It does not resolve the conjecture or establish a publication-level novel result.**

## Contents

- `RESEARCH_UPDATE_v0.5.md`: precise chronological frontier theorem, rigorous proof, global 0–1 formulation, fractional LP counterexample, and scientific limitations.
- `frontier_solver_v05.py`: exact iterative cut-generation solver. Reports `PROVED_OPTIMUM` only after a MILP optimality certificate and independently checked temporal connectivity. Runs slowly at n>=7.
- `baseline_time_expanded_milp.py`: independent MILP formulation for cross-checking.
- `verify_v05.py`: deterministic exhaustive K3/K4 temporal frontier verification, global-validity checks including 50 K5 schedules, LP gap on K4, and selected MILP comparisons.

Python 3.10+ with numpy/scipy. Run `python verify_v05.py` (typically under a minute on modest hardware).

The program's elapsed times vary by hardware and solver; none of these experiments demonstrates superior performance or proves the conjecture. Consult the note for literature priority boundaries.
