# Stage 8 — exact original-midpoint fringe extension for all n

**27 October 2026. All-n elementary reduction: proved; independently checked on all optimal n=4 and n=5 schedules. It does not settle the half-forest conjecture.**

## Statement

Let S=(e_1,...,e_{2n-4}) be ANY successful shortest bidirectional telephone gossip chronology of **pairwise-distinct unordered contacts** on n>=4 labelled participants. Let a and b be any **two distinct existing participants**, and let v be new. Define

\[
S^+ := ((v,a),\,e_1,\ldots,e_{2n-4},\,(v,b)).
\]

Then S^+ is a shortest successful distinct-contact schedule on n+1 participants, and the static cycle ranks of its **original** two (n-1)-call halves are **identical** to those of the original two (n-2)-call halves of S, coordinate by coordinate.

In particular a both-cyclic minimum-call counterexample at size n, if one exists, generates a both-cyclic counterexample at EVERY size n'>n.

## Complete proof

The new initial call (v,a) supplies the new v-secret to a and a's then-current secret to v. Along the original S chronology, the information of a propagates to every original vertex because S is successful. Adding a further secret to a at time zero cannot invalidate existing propagation; by induction on the original call sequence, every vertex's new knowledge contains their original S knowledge plus the v-secret wherever the a-secret would travel. Since S completes gossip, every original vertex has all n old secrets and the v-secret at the end of S. In particular participant b knows all n+1 secrets.

The final call (v,b) then gives v everything. Thus S^+ completes full information gossip. Its contact pairs are distinct because S was distinct and a!=b, and both new pairs contain v, which was absent from S. It has length (2n-4)+2=2(n+1)-4, the known optimal bound for n+1>=5.

The original prefix half of S^+ has length (n+1)-2=n-1 and consists of (v,a) plus the original prefix S[1:n-2]. The new edge meets the original prefix graph **at exactly one existing endpoint**, so v is a leaf. Adding a leaf preserves the number of independent cycles, so its cycle rank equals the old prefix rank. Similarly the original suffix half of S^+ consists of the old suffix S[n-1:2n-4] followed by (v,b), adding a leaf and preserving the suffix cycle rank. QED.

## Significance and limitations

This gives a **sound upward closure** of hypothetical counterexamples. By contrapositive, proving the half-forest property at size N also proves it for every smaller size 4<=n<=N. It does NOT establish the converse that every (n+1)-participant counterexample can be reduced to an n-participant one: its final and initial edges may not have a disposable common participant, and removing an arbitrary degree-two vertex may destroy successful information flow or change the chronological midpoint. The optimal eight-person cubic W8 fixture in [Stage 7](../v2.4/adversarial_induction_obstruction.py) already refutes universal existence of a degree-two vertex.

This closure is an instance of the standard two-call participant-extension idea; it is not claimed as historical novelty. The result does NOT imply any counterexample exists.

## Independent verification

[test_fringe_extension.py](test_fringe_extension.py) independently enumerates every ordered distinct-contact gossip-successful schedule for n=4 and n=5 (24 and 3,240 respectively), tests three choices of distinct participants (a,b) per schedule, checks that the extension succeeds with distinct contacts at the minimum length, and compares BOTH original cycle ranks before/after. No event reordering or relaxed information profile is involved.

Research direction: any hoped-for all-n proof by descent needs an additional theorem that every **minimal both-cyclic counterexample** has a midpoint-compatible removal or a bounded classical kernel. The extension here alone is not such a theorem.
