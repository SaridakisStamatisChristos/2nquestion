# Reproducibility guide

Run tests from **each checkpoint directory** because local modules sometimes use same-directory imports. Examples assume a POSIX shell, Python 3.10+, a C++17 compiler, and installed `numpy` and `scipy` (the MILPs use `scipy.optimize.milp` / HiGHS).

```bash
python -m pip install -r requirements.txt
cd research/v0.4 && python v04_independent_verify.py && cd ../..
cd research/v0.5 && python verify_v05.py && cd ../..
cd research/v0.6 && python independent_verify.py && cd ../..
cd research/v0.7/code && python independent_v07.py && python two_tree_probe_np7.py && cd ../../..
```

For C++ investigations (example v0.7):

```bash
cd research/v0.7/code
g++ -std=c++17 -O3 probe_3trees.cpp -o probe_3trees
./probe_3trees 7 100 42
./probe_3trees 8 100 42

g++ -std=c++17 -O3 nonpivot_3trees.cpp -o nonpivot_3trees
./nonpivot_3trees 7 10000 42
./nonpivot_3trees 8 600 42
```

Some C++ loops are CPU-intensive; study each version's note before running large `exhaustive_small.cpp`, `trace_classes.cpp`, or annealing experiments. Number of samples, seeds, ordering conventions, and compile flags are documented in individual research notes.

**Verification during repository import:** Ran local Python `v04_independent_verify.py`, `verify_v05.py`, `independent_verify.py` (v0.6), and `independent_v07.py` (v0.7); each completed successfully. This verifies selected executable claims, **not** the entire source tree and **not** the universal conjecture. GitHub CI status is separate and must be inspected after publication.
