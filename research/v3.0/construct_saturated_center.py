"""Standalone exact replay of sharp local two-fold cover constructions.

These are only LOCAL tree / unicyclic chronologies, not full gossip schedules
with 3x3 prefix/suffix component intersections.
"""


def replay(n, calls):
    knowledge = [1 << i for i in range(n)]
    edges = set()
    for a, b in calls:
        assert a != b
        edge = tuple(sorted((a, b)))
        assert edge not in edges
        edges.add(edge)
        combined = knowledge[a] | knowledge[b]
        knowledge[a] = knowledge[b] = combined
    return knowledge


def rooted_four(vertices):
    root, a, b, c = vertices
    return [(root, a), (b, c), (root, b)]


def two_root_eight(vertices):
    u, w, a, b, c, d, e, f = vertices
    return rooted_four((u, a, b, c)) + rooted_four((w, d, e, f)) + [(u, w)]


def double_coverage(knowledge, recipients):
    return all(
        sum(bool(knowledge[x] & (1 << secret)) for x in recipients) >= 2
        for secret in range(len(knowledge))
    )


def main():
    t4 = rooted_four((0, 1, 2, 3))
    k4 = replay(4, t4)
    assert k4[0] == 15 and double_coverage(k4, (1, 2, 3))
    print("PASS one full outside root; 3 designated double-cover recipients")

    t8 = two_root_eight(tuple(range(8)))
    k8 = replay(8, t8)
    assert k8[0] == k8[1] == 255
    assert double_coverage(k8, tuple(range(2, 8)))
    print("PASS two full outside roots; 6 designated double-cover recipients")

    # Two eight-vertex rooted tree pieces, penultimate join, final extra
    # edge: precisely 16 calls on 16 people, with one static cycle.
    t16 = (
        two_root_eight(tuple(range(8)))
        + two_root_eight(tuple(range(8, 16)))
        + [(0, 8), (1, 9)]
    )
    k16 = replay(16, t16)
    assert len(t16) == 16
    full = (1 << 16) - 1
    assert {x for x in range(16) if k16[x] == full} == {0, 1, 8, 9}
    center = tuple(range(2, 8)) + tuple(range(10, 16))
    assert len(center) == 12 and double_coverage(k16, center)
    print("PASS unicyclic 16-contact chronology: 4 full outsider collectors, 12 double-cover recipients")
    print("LIMIT: local necessity is sharp; no two-half global schedule is produced")


if __name__ == "__main__":
    main()
