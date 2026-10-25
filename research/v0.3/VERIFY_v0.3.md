# Reproduction — v0.3

Run from `temporal_clique_lab` using a C++17 compiler and Python 3:

```sh
c++ -O3 -std=c++17 extreme_exhaustive.cpp -o /tmp/extreme_exhaustive
/tmp/extreme_exhaustive 4
/tmp/extreme_exhaustive 5
c++ -O3 -std=c++17 extreme_degree_probe.cpp -o /tmp/extreme_degree_probe
/tmp/extreme_degree_probe 9 2000000
/tmp/extreme_degree_probe 12 300000
python check_counter_v03.py
```

The `critical_bound_v03.cpp` executable is intended to exit **nonzero** after finding a valid counterexample; it is **not** a passing test. It provides an explicit witness. No formal theorem checker was run. Numerical sample counts and seed values are recorded in `RESEARCH_UPDATE_v0.3.md`.
