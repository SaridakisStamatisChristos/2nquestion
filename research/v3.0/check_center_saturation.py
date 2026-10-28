"""Exact finite falsifier for two-carrier temporal supports and 3x3 center capacity.

This validates the two-point logical lemma by enumeration, NOT an all-n
gossip theorem or existence of a complete global chronology.
"""
from itertools import product


def crossing(a, b):
    return all(x & y for x in a for y in b)


def classified(a, b):
    ax = all(x & 1 for x in a)
    ay = all(x & 2 for x in a)
    bx = all(x & 1 for x in b)
    by = all(x & 2 for x in b)
    return (ax and ay) or (bx and by) or (ax and bx) or (ay and by)


def check_two_carriers():
    count = 0
    for na in range(1, 5):
        for nb in range(1, 5):
            for a in product((1, 2, 3), repeat=na):
                for b in product((1, 2, 3), repeat=nb):
                    count += 1
                    assert crossing(a, b) == classified(a, b), (a, b)
    assert count == sum(3**i for i in range(1, 5)) ** 2
    return count


def check_saturated_center():
    # Given all four off-corner cell sizes equal 2, the Bumby spine
    # excludes complete collectors from the opposing TREE side of each
    # off-corner cell. Two-point crossing then consumes four collectors
    # of P3 and four of reversed Q3; both have capacity at most four.
    a_used = b_used = 4
    count = 0
    for center_size in (1, 2):
        choices = tuple(range(1, 1 << center_size))
        for na in range(1, 4):
            for nb in range(1, 4):
                for a in product(choices, repeat=na):
                    for b in product(choices, repeat=nb):
                        full_a = sum(
                            all(mask & (1 << i) for mask in a)
                            for i in range(center_size)
                        )
                        full_b = sum(
                            all(mask & (1 << i) for mask in b)
                            for i in range(center_size)
                        )
                        if a_used + full_a <= 4 and b_used + full_b <= 4:
                            count += 1
                            assert not crossing(a, b), (center_size, a, b)
    assert count == 196
    # Independent abstract three-carrier boundary: all two-subsets on
    # each side cross, though neither side has any complete collector.
    # These masks are NOT claimed to be realizable gossip components.
    triangle = (0b011, 0b101, 0b110)
    assert crossing(triangle, triangle)
    for point in range(3):
        assert not all(mask & (1 << point) for mask in triangle)
    return count


if __name__ == "__main__":
    count = check_two_carriers()
    center_cases = check_saturated_center()
    print(f"PASS {count} exhaustive pairs of nonempty 2-point support families")
    print(f"PASS {center_cases} collector-free center patterns at m33=1,2: no crossing")
    print("PASS 3-point abstract crossing without complete collectors (not a schedule)")
    print("CONDITIONAL: m13=m23=m31=m32=2 in both-cyclic 3x3 implies m33>=3")
