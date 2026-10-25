# Temporal Clique 2n−3 Research Lab

`RESEARCH_NOTE.md` is the primary research handoff and evidence ledger. This is **not a proof of the open conjecture**.

## Dependencies

- Python 3.x, `numpy`, `scipy` (the exact solver uses `scipy.optimize.milp`/HiGHS)
- C++17 compiler (for independently exhaustive small cases and structural searches)

## Reproduction

From the package directory:

```sh
python validation.py

g++ -O3 -std=c++17 exhaustive_small.cpp -o exhaustive_small
./exhaustive_small 4
./exhaustive_small 5

g++ -O3 -std=c++17 star_tree.cpp -o star_tree
./star_tree 6 300000 2177
python verify_witness.py
python verify_nonpivot.py
python n8_verify.py
```

`verify_nonpivot.py` performs the seeded n6..n9 survey and exact adjudication of initially hard cases, while `n8_verify.py` completes the n8 hard cases. `nonpivot_survey.json` contains the recorded data from those runs, including n9 follow-on multi-start greedy outcomes. Some MILP runs take longer than others; a time-limit status is not a certificate of infeasibility or optimality.

`nonpivot_long.py` was exploratory; it reuses the helper module with top-level survey execution, so prefer `verify_nonpivot.py` for deterministic replay. Verification results in the note use only real executed searches and exact checks.
