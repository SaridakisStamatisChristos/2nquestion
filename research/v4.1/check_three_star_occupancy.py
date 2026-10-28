"""Independent finite occupancy falsifier for Stage24 all-n k-arm lemma.

The mathematical proof rests on exact original-time causal sealing,
double carriers and the three-star vs chronological-tree obstruction.
These finite integer compositions are an adversarial check of the
remaining sharp pigeonhole step, NOT completed gossip schedules.
"""


def compositions_positive(total, slots):
    if slots == 1:
        if total >= 1:
            yield (total,)
        return
    for first in range(1, total - slots + 2):
        for tail in compositions_positive(total - first, slots - 1):
            yield (first,) + tail


def test():
    total_checks = 0
    for k in range(3, 9):
        for nonroots in range(k, 2 * k - 1):
            for occupancy in compositions_positive(nonroots, k):
                total_checks += 1
                singleton_arms = sum(c == 1 for c in occupancy)
                if nonroots < 2 * k - 2:
                    assert singleton_arms >= 3, (k, occupancy)
                if singleton_arms <= 2:
                    assert nonroots >= 2 * k - 2, (k, occupancy)
        exact = (1, 1) + (2,) * (k - 2)
        assert len(exact) == k
        assert sum(exact) == 2*k - 2
        assert sum(z == 1 for z in exact) == 2
        print(f"PASS k={k}: B must have >= {2*k-1} total participants;"
              f" pure occupancy boundary={exact}")
    assert total_checks > 15000
    print(f"PASS {total_checks} exact positive integer arm occupancy assignments")
    print("LIMIT: arithmetic support-falsification only; chronological "
          "three-star impossibility has separate independent n6/n7 tests")


if __name__ == "__main__":
    test()
