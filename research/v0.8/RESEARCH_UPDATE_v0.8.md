# v0.8: Hard-instance POD falsification campaign (25 October 2026)

**Scope:** undirected `K_n`, globally unique edge times, strictly increasing journeys, all-pairs temporal reachability. **Status:** executable certificates for selected `K9` cases; no universal theorem; no novelty claim.

## Target

- Main question (still open): Must every temporal clique contain a spanner with at most `2n-3` edges?
- Stronger working conjecture, **Pivot–Optimal Dichotomy (POD)**: If no pivot contact exists, does a spanner with `2n-4` edges exist?
- We do **not** assume POD follows from established pivotability theorems; it is unproved and might be false.

## Results obtained and independently verified

1. Parsed all **14** non-pivotable `K9` schedules in `../v0.2/hard_seeds9.txt`. The script `certify_pod9.py` generated an explicit 14-edge witness for **each** input, recording selected contact indices, deterministic greedy seeds, and the full chronology in `certificates_pod9.json`.
2. `independent_verify_v08.py` independently verified every witness and each schedule's lack of pivots; additionally checked time-reversal and vertex-renaming invariance on those schedules. It exhaustively compared two reachability algorithms across all `6! * 2^6 = 46,080` chronology/subgraph pairs for `K4`.
3. An exploratory 60,000-iteration deterministic pair-swap local search (`adversarial_nonpivot9.cpp`, `seed=2100825`) produced a non-pivotable `K9` chronology on which *24 predetermined greedy deletion orders* required at least 15 edges. **This was not a counterexample.** The independent Python greedy challenge found a valid 14-edge witness with random seed **3**, and the result is recorded in `adversarial_certificate.json`. An exact MILP was not necessary to refute this putative obstruction.
4. For the 14 instances and the adversarial example, the known universal gossip lower bound `2n-4=14` and the explicit validated witnesses yield **instance-specific optimality**. This is not a proof of POD for all n=9, let alone all n.

## Insight / failure mode

A heuristic that minimizes success among a fixed, small collection of greedy deletion orders can produce **false computational hardness** even when another deletion order finds a minimum spanner immediately. A failed greedy search is not a lower-bound certificate. To search for a true POD counterexample, use a complete exact solver to establish infeasibility at `2n-4`; do not infer infeasibility from restart counts, 3-tree enumerations, or pivots alone.

## Reproduction

Run from repo root with Python 3.10+ and `scipy`, `numpy`, C++17 `g++` for the optional annealer:

```bash
python research/v0.8/certify_pod9.py --max-cases 14 --starts 1000 --seconds 6
python research/v0.8/challenge_best9.py --greedy-starts 25000 --seconds 35
python research/v0.8/independent_verify_v08.py
# Optional re-generate the adversarial chronology:
g++ -std=c++17 -O3 -Wall -Wextra research/v0.8/adversarial_nonpivot9.cpp -o /tmp/nonpivot9
/tmp/nonpivot9 60000 2100825 > research/v0.8/adversarial_best9.txt 2> research/v0.8/adversarial_run.log
```

The optional annealer output is the chronology referenced by the challenge script. Re-generating it overwrites the checked schedule; verify `adversarial_certificate.json` afterwards.

### What the scripts certify

- `WITNESS_14`: a concrete feasible 14-edge subset; optimum 14 follows using the **established** universal gossip lower bound for n>=4.
- `CERTIFIED_NO_14`: intended only when the MILP returns a certified infeasibility (would refute POD on a nonpivotable input); no such result occurred in this campaign.
- `UNKNOWN`: time or optimization resource limits; **never** a counterexample.
- Neither exhaustive checks at `K4` nor 14 selected `K9` schedules imply an unbounded result.

## Prior art and scholarly integrity

- Casteigts, open temporal clique spanner question, updated 22 September 2026: https://arnaudcasteigts.net/blog/open-problems.html
- Baligács, *Temporal Cliques Admit Linear Spanners* (2026): https://arxiv.org/abs/2606.05156 (general `7n` upper bound).
- Carnevale, Casteigts, Corsini, *Dismountability in Temporal Cliques Revisited* (SAND 2025): https://doi.org/10.4230/LIPIcs.SAND.2025.6 (pivotability/dismountability; known `2n-3` subfamilies).
- Bumby, *A Problem with Telephones*, 1981: https://doi.org/10.1137/0602002 (minimum `2n-4` gossip lower bound and four-cycle theorem).
- Kleitman & Shearer, *Further Gossip Problems*, 1980: https://doi.org/10.1016/0012-365X(80)90116-8.
- Göbel, Cerdeira, Veldman, *Label-connected graphs and the gossip problem*, 1991: https://doi.org/10.1016/0012-365X(91)90068-D (graph-labelability and structural context, **not** fixed chronology).

## Next mathematical bottleneck

We need either (A) a certified non-pivotable `K_n` instance with no `2n-4` spanner, (B) a universally valid constructive proof of POD, or (C) a universal `2n-3` construction independent of POD. The present results accomplish none. Prefer a certified exact `n>=9` search for genuine counterexamples and a theory-backed structural invariant rather than larger unfiltered random surveys.
