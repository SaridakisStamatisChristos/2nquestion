"""Adversarial induction counterexample: optimal gossip NEED NOT have a degree-2 vertex.

This refutes a tempting *universal* deletion premise, not the target
original chronological half-forest conjecture.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "v1.5"))
from minimal_order_bridge import W8, cyclerank, edge, extend_to, gossip


def check(schedule, n):
    degrees = [0] * n
    for a, b in schedule:
        degrees[a] += 1
        degrees[b] += 1
    assert len(schedule) == 2 * n - 4
    assert len({edge(e) for e in schedule}) == len(schedule)
    assert gossip(n, schedule)
    return tuple(degrees)


def main():
    degrees = check(W8, 8)
    assert degrees == (3,) * 8, degrees
    assert cyclerank(8, W8[:6]) == 0
    assert cyclerank(8, W8[6:]) == 0
    print("PASS W8 optimal distinct-contact n8 schedule: every vertex "
          "has degree three, NONE has degree two; proposed universal "
          "degree-two-deletion premise REFUTED", flush=True)
    for n in (9, 17, 18):
        extended = extend_to(W8, n)
        d = check(extended, n)
        assert all(d[v] == 2 for v in range(8, n))
        print(f"PASS classical two-contact extension n={n}: "
              f"{n - 8} degree-two fringe participants; "
              "persistent irreducible 8-vertex core", flush=True)
    print("LIMIT: this does not refute a hypothetical deletion lemma "
          "restricted to MINIMAL BOTH-CYCLIC counterexamples", flush=True)


if __name__ == "__main__":
    main()
