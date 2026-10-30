"""Independent exhaustive two-carrier Boolean support crossing falsification.

Exact all-pairs supports model, 2- and 3-point cells, families of 1..3
nonempty source/target subsets. This does NOT enumerate gossip schedules.
"""
from itertools import product


def families(width):
    masks = range(1, 1 << width)
    for length in (1, 2, 3):
        yield from product(masks, repeat=length)


def crossing(a, b):
    return all(left & right for left in a for right in b)


def complete_points(family, width):
    return {x for x in range(width) if
            all(mask & (1 << x) for mask in family)}


def main():
    for width in (2, 3):
        f = list(families(width))
        checked = accepted = zero_opposite_full = 0
        for a in f:
            for b in f:
                checked += 1
                if not crossing(a, b):
                    continue
                accepted += 1
                if not complete_points(b, width):
                    zero_opposite_full += 1
                    assert all(mask.bit_count() >= 2 for mask in a), (width, a, b)
                if not complete_points(a, width):
                    assert all(mask.bit_count() >= 2 for mask in b), (width, a, b)
        print(f"PASS width={width}: {checked} source-target families, "
              f"{accepted} crossing, {zero_opposite_full} with no opposing complete")
        assert zero_opposite_full > 0
    triangle = (0b011, 0b101, 0b110)
    assert crossing(triangle, triangle)
    assert not complete_points(triangle, 3)
    assert all(mask.bit_count() == 2 for mask in triangle)
    # An allowed singleton source support can cross all targets exactly when
    # its singleton owner is a complete opposing collector.
    a = (0b001,)
    b = (0b001, 0b011, 0b101)
    assert crossing(a, b) and complete_points(b, 3) == {0}
    print("PASS 3-point triangle boundary and valid singleton with full opposing collector")
    print("LIMIT: finite support logic, not full original gossip chronology")


if __name__ == "__main__":
    main()
