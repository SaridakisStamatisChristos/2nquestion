# Temporal Clique Research Campaign — v0.4

**Date:** 24 October 2026. **Target:** universal `2n-3` temporal-clique spanner conjecture. **Status:** still open. This checkpoint develops a verified simultaneous-deletion obstruction and explicitly **does not** claim a solution, an original algorithm, or established publication-level novelty.

## 1. Model

All `n(n−1)/2` undirected edges of `K_n` appear exactly once, at distinct integer times. A journey uses edges in strictly increasing time order. A spanner is an edge subset retaining all ordered-pair temporal reachability. A deletion set `D` is **feasible** if `K_n \ D` is temporally connected. It is an **inclusion-minimal infeasible deletion set** if `D` is infeasible and each `D\{e}` is feasible. By monotonicity, every proper subset of such a `D` is feasible.

Call such a deletion obstruction **temporally pure** when its complement `K_n\D` remains *statically connected*.

## 2. Quadratic-order temporally pure deletion obstructions: proved proposition

**Proposition.** For every integer `d≥3`, let `s=2^d`, `n=2s`. There is an injectively timed `K_n` and a deletion set `D` of size `s²−1=n²/4−1` such that:

1. `K_n \ D` is NOT temporally connected;
2. `K_n \ D` IS connected as an ordinary graph;
3. for every `e∈D`, `K_n \ (D\{e})` IS temporally connected.

In particular, the size of a temporally pure inclusion-minimal infeasible deletion set can be `Ω(n²)`, which is asymptotically maximal because `K_n` has only `O(n²)` edges. No fixed order of local compatibility checks can certify arbitrary simultaneous deletions: for any fixed `r`, the constructed `D` can have `|D|>r` while all its subsets of size at most `r` are feasible.

### Explicit construction

Identify the two vertex classes `A` and `B` with disjoint copies of the group `F₂^d`. For a nonzero vector `v`, define the perfect matching `M_v={{x,x⊕v}:x∈F₂^d}` (each undirected edge occurs once).

Choose two disjoint ordered bases `P=(e₁,...,e_d)` and `Q=(e₁+e₂, e₂+e₃, ..., e_{d−1}+e_d, e₁+e₂+e₃)`. Here `e_i` are coordinate vectors and `+` denotes XOR. The first `d−1` vectors of `Q` are linearly independent and span the even-parity subspace; the last has odd parity, so `Q` is a basis. All members of `Q` have weight 2 or 3 and hence no member equals a coordinate vector; matching supports of `P` and `Q` are edge-disjoint.

Order the time-labelled edges of the full clique in five consecutive phases:

- `T₀`: one early bridge `e₀={0_A,0_B}`;
- `T₁`: within BOTH A and B, process the `d` matchings `M_{e₁},...,M_{e_d}` in that order, using distinct times for every edge;
- `T₂`: ALL the other `s²−1` A–B cross edges, in arbitrary order. Set `D` equal to this entire phase;
- `T₃`: within BOTH A and B, process the `d` matchings associated with `Q`, in their listed order, using distinct timestamps;
- `T₄`: any remaining intra-class clique edges in arbitrary order.

Every edge appears exactly once because P/Q matching families are disjoint and all other edges are allocated to the final phase.

### Proof of proposition

**Hypercube gossip invariant.** For any ordered basis `v₁,...,v_d` of `F₂^d`, processing its perfect matchings successively causes every vertex to know every initial item from its own class: after stage `j`, the information at `x` contains items from all vertices in the affine coset `x+span(v₁,...,v_j)`. The proof is by induction: the `j`-th matching merges two cosets of the previous span into a coset of the extended span. Furthermore, if a message is available at one vertex before these `d` matchings, the same schedule propagates that message to every vertex.

**Deletion of entire D is infeasible.** The only edge of `K_n\D` crossing between A and B is `e₀`, and it occurs before every internal communication event. Take any source `a∈A\{0_A}`. Its information cannot traverse `e₀` because it has not yet contacted `0_A`, and cannot cross between groups later. Hence `a` cannot reach any vertex of B, so temporal connectivity fails.

**Static connectivity of complement.** In both classes, the early P-matchings collectively form a connected d-dimensional hypercube. Edge `e₀` joins the two components, making the retained static graph connected.

**Restoring any one edge in D repairs temporal connectivity.** Let `e={a,b}` be the restored edge with `a∈A,b∈B`. At the end of phase `T₁`, every vertex in each class knows all original information from its own class (the early bridge can only add information). When `e` occurs in `T₂`, both endpoints learn all `n` initial items. The subsequent `T₃` communication rounds use an independent basis Q and distribute the complete information from `a` to all A and from `b` to all B. Consequently all ordered pairs have strictly increasing journeys. QED.

### Interpretation

The feasible-deletion family is hereditary, but its minimal forbidden sets can have quadratic cardinality even when no static cut is broken. Therefore pairwise, triple-wise, and every other fixed-arity consistency oracle can falsely approve a deletion batch.

**This does not imply the 2n−3 conjecture is false, nor does it yield a tighter spanner bound.** It describes the obstruction structure of a plausible proof route.

## 3. Small certified temporal-only witnesses

These witnesses are illustrative, *not* claims about the minimum obstruction size for each order of clique.

**K4** chronology: `01,02,03,13,12,23`, D=`{12,23}`. Each singleton deletion feasible; joint deletion infeasible (3 cannot reach 2), although the static complement is connected.

**K5** chronology: `01,02,03,04,12,14,13,24,23,34`, D=`{13,23,34}`. Every proper subset feasible, all three infeasible (4 cannot reach 3), static complement connected. Pairwise compatibility does not entail triple compatibility.

**K6** chronology: `05,04,45,03,12,13,15,34,02,14,25,24,23,01,35`, D=`{04,45,03,15,02,25}`. Every proper subset feasible, the set itself infeasible (0 cannot reach 2), static complement connected.

## 4. Additional obstruction: minimum spanners do not have matroid uniformity

For K4 chronology `01,02,13,03,23,12`, exhaustive subset enumeration independently checks two inclusion-minimal temporally connected edge sets, of sizes 4 and 5 respectively:

- 4-edge spanner: `{02,13,03,12}`.
- 5-edge spanner: `{01,02,03,23,12}`.

Each is irreducible, yet the cardinalities differ; therefore the minimal spanners are not the bases of a matroid. This is a small illustrative example, not an independently novel theorem; it cautions against importing static spanning-tree basis exchange axioms.

## 5. Positive exchange rule, but limited

**Phase-bridge exchange lemma:** Suppose two disjoint vertex sets A and B each have an internal *early* interval of temporal all-to-all reachability and a separate internal *late* interval of temporal all-to-all reachability. All cross edges of interest occur between those intervals. Keeping any ONE intermediate cross edge suffices for global all-to-all temporal reachability. Thus any two intermediate cross edges may be exchanged while preserving connectivity **when the early/late certificates remain retained**.

This is an elementary proved sufficient condition (a variant of gossiping / pivotable exchange), not a new general algorithm. It is deliberately restricted to a situation where time order makes exchange sound.

## 6. Executed verification

Two independent algorithms:

1. Source-by-source chronological reachability, with in-place endpoint update from pre-event states (`v04_exchange_obstructions.py`).
2. Source-bitset simultaneous information propagation (`v04_independent_verify.py`).

- 2,400 seeded random subgraph schedules, n=3..8: exact agreement between algorithms.
- Explicit K4, K5, K6 witnesses: every single-edge restoration tested, all complements statically connected, and all complements temporally disconnected.
- Family d=3, n=16: all 63 single-edge restorations tested.
- Family d=4, n=32: all 255 single-edge restorations tested.
- Family d=5, n=64: all 1023 single-edge restorations tested.
- K4 matroid obstruction: enumerate all 64 edge subsets, find inclusion-minimal 4- and 5-edge spanners.

The proof is *human-checkable but not formalized*; the finite tests do not establish the infinite theorem (its proof does).

Run `python v04_exchange_obstructions.py` and `python v04_independent_verify.py` using Python 3.10+, standard library only; no solver or internet needed.

## 7. Prior art and originality boundaries

Directly relevant established work:

- Akrida, Gąsieniec, Mertzios & Spirakis, *The Complexity of Optimal Design of Temporally Connected Graphs*, Theory of Computing Systems 2017, https://doi.org/10.1007/s00224-017-9757-x. Uses temporal hypercube matching schedules and studies label deletion / minimal temporal designs. **The hypercube gossip invariant is not new.**
- Kurita, Marino, Schoeters & Uno, *Spanner Enumeration for Temporal Graphs*, SAND 2025, https://doi.org/10.4230/LIPIcs.SAND.2025.9. Treats minimal spanners and dual-hardness of all-to-all enumeration. **Minimal spanner/nonmatroid phenomena should not be claimed original without deeper review.**
- Casteigts, Peters & Schoeters, *Temporal Cliques Admit Sparse Spanners*, JCSS 2021, https://doi.org/10.1016/j.jcss.2021.04.004.
- Casteigts, *Open questions in temporal graphs*, last updated 22 Sep 2026, https://arnaudcasteigts.net/blog/open-problems.html. The universal 2n−3 bound remains open.

**Novelty status:** the specific quadratic-size temporally pure deletion obstruction was not located in this targeted search but is a straightforward composition of known temporal-hypercube gossip schedules, so **do not present this as a validated significant novelty**. No claim is made that its formulation is new in the literature.

## 8. Research decision and next attack

**Negative finding:** A naive exchange principle of the type “if every small subset of deletions is safe, then the entire batch is safe” is refuted at maximum possible asymptotic order. Greedy matroid-style proof strategies are also blocked by unequal-size minimal spanners.

**Promising unrestricted problem:** identify a new *global replacement invariant* that captures temporal path interactions even when no single time-local pivot or bounded-arity exchange exists. It must certify constructive size `≤2n−3`, or lead to an independently checkable counterexample with `n≥9`. The present work does not solve that challenge.
