# Stage 31 — Universal last-cycle collector transfer

**28 October 2026. ALL-n conditional structural result; necessary-incidence consequences only. No global n22 original half-forest proof and no 2n−3 temporal-clique theorem. PR #1 DRAFT, UNMERGED; publication HOLD.**

## Fixed-original-order contract

In a hypothetical successful shortest **pairwise-distinct** 2n−4-contact bidirectional gossip chronology whose **ORIGINAL** first and last n−2 contacts are cyclic, Bumby's Theorem 3 gives two prefix trees P1,P2 and unicyclic P3, and two fully reverse-chronological suffix trees Q1,Q2 and unicyclic Q3, with positive cells m_ij=|Pi∩Qj|. Each unicyclic component U has an **ACTUAL LAST chronological call** e=ab joining its two exterior cells A,B and closing its unique cycle, outside center X=P3∩Q3. The preceding v−1 contacts form a chronological spanning tree. All four offcorner cells have ≥2 people.

A complete local U collector knows every original local U secret at U termination. Existing exact original midpoint crossing means that each private prefix/reversed-tree offcorner recipient becomes a full collector of the opposite cyclic component, with the exact Stage25 privacy lower bounds; unknown classes default to zero.

## Theorem 31.1 (all n; complete proof)

If **|A|=2 and BOTH participants of A are complete terminal U collectors**, then B contains a complete U collector, regardless of |B|, |X| and total n. Symmetrically for B.

**Proof.** The final original local call e=ab has a∈A and b∈B. Because A has exactly two people and both are complete, a is complete after e. A bidirectional call makes **both its endpoints' final knowledge sets equal**, so b is also complete. Time reversal on the WHOLE original suffix gives the same proof for Q3. This uses the ACTUAL last call; no reorder is permitted. QED.

**Essential sharp hypothesis.** This is FALSE if |A|≥3 and two (but not all) A people are known full. Take A={0,1,2}, B={3}, helper {4}, and local unicyclic chronological calls (2,0),(4,0),(3,1),(0,1),(2,3). The first four form a spanning tree and the last closes the unique static cycle. Exactly 0 and 1 know all five secrets; 3 does not. Since e touches only A member 2, having two full collectors in A does not force a B full collector. This is a LOCAL logic countermodel, not a full minimum-gossip 3×3 example; the executable exact bitset replay preserves this boundary.

## Corollary 31.2 — all-n exterior collector closure

Write upper pair (a,b)=(m13,m23) for reversed-Q3, with certified full-collector lower bounds (u,v) from the PREFIX trees. Analogously lower pair (m31,m32) for original P3, with certified lower bounds from the REVERSED suffix trees.

The condition

\[
\boxed{(u\ge1\land v\ge1)\ \lor\
 (a=2\land u\ge2)\ \lor\ (b=2\land v\ge2)}
\]

is sufficient to infer ≥1 complete U collector in EACH exterior cell. It is not asserted necessary. When additionally a+b≤8, the existing [Stage28 all-n collector obstruction](../v4.5/ALL_N_EIGHT_OUTSIDE_COLLECTOR_THEOREM.md) excludes a center complete U collector. Exact original-support crossing then excludes: center |X|=1 if either U side is blocked; center |X|=2,3 if both U sides are blocked (binary support trichotomy or three-person chronological-tree double-cover lemma). For |X|≥4, no such conclusion follows.

## Exact new incidence consequences, NOT global chronological realizability

[Executable checker](last_contact_transfer.py) enumerates all positive nine-cell matrices using the independent Stage27 generator and reruns the exact Stage25, Stage26, Stage28 necessary gates BEFORE the new gate. It checks collector transfer without extrapolating tree privacy classes:

| n | Stage28 survivors | Stage31 survivors | newly excluded | S2×S2 surviving orbits |
|---:|---:|---:|---:|---:|
| 21 | 0 | **0** | 0 | 0 |
| 22 | 104 | **92** | **12** | **24** |
| 23 | 1392 | **1348** | **44** | **346** |

All 12 newly removed n22 matrices have center width TWO, and represent 4 symmetry orbits. Remaining center-size histogram: center1=4, center2=28, center3=36, center4=20, center6=4.

Representative newly excluded n22 matrix:

\[
M=\begin{pmatrix}
1&1&2\\
1&1&6\\
4&4&2
\end{pmatrix}.
\]

In Q3 upper (2,6) pair the two people in C13 are BOTH complete reversed-Q3 collectors because the original prefix P1 has exact chronological tree cover (1,1,2), each C13 recipient private. By Theorem31.1, the ACTUAL reversed-Q3 last contact transfers full information to one C23 person. Both Q3 exterior cells have complete collectors and total occupancy eight, so Stage28 forbids any Q3 center complete collector.

In P3 lower (4,4) pair the reversed suffix Q1,Q2 groups each have (1,1,4) tree covers; the Stage29 exact universal privacy theorem forces ≥1 private recipient in C31 and in C32, hence complete P3 collectors in BOTH lower exterior cells. Total exterior occupancy eight; Stage28 forbids a P3 center full collector. The original two-person center X must have a complete collector on at least one side by exact binary midpoint crossing. Contradiction.

**All four** n22 Stage30 special (1,1,6) exact-path CSP applicability profiles are among these newly excluded matrices; none of the current 92 n22 necessary profiles uses that special case. At n23 the six-cell target registry reduces from 140 to 128 labelled profiles (33 orbits). These are **necessary-profile exclusions**, not enumeration of complete 40-call schedules.

## Evidence and epistemic boundary

- Human theorem 31.1: complete direct edge endpoint proof, for ALL n.
- Center exclusions: conditional on the previously written Stage28/Stage19 human all-n arguments and Bumby's original last-call spine; **not** independently formally verified.
- Executable falsification: Python script replays the |A|=3 countermodel, requires each earlier edge to make a spanning tree and final edge close cycle, recomputes n21/22/23 necessary profiles, verifies symmetry and Stage28-gate subsumption.
- CI: see [Stage31 workflow](../../.github/workflows/research-v48.yml). Never claim CI-VERIFIED before checking a matching latest revision.
- No global half-forest proof for n≥22; no exact 2n−3 spanner theorem, formal theorem prover, historically verified novelty or external refereeing. DRAFT/UNMERGED; publication HOLD.

Next target: general original-order information-support relations for center widths 2 and 3 that do not require exterior cell size exactly two, plus a separate direct temporal-clique spanner route.
