# v1.5 — minimal-order/chronology bridge audit

The full minimal event-order poset of a successful gossip schedule need not determine the component structure of the exact midpoint in its chronological linear extensions. An exact n8 example has **51,200** linear extensions, split between both-forest and one-cyclic-half outcomes. A proven two-call vertex extension produces two *same-poset* n13 schedules with differing half-forest shapes.

- [Proof and audit](RESEARCH_UPDATE_v1.5.md)
- [Executable finite verifier](minimal_order_bridge.py)

Run: \`python3 research/v1.5/minimal_order_bridge.py\`.

**Crucial limitation:** this is not a complete enumeration of all admissible Labahn p-grid kernels at n=13; without the original 1995 admissibility and fringe rules it cannot certify historical priority. The v1.4 n13 half-forest theorem and the original temporal-clique 2n−3 conjecture are unaffected.
