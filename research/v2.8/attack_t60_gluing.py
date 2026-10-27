"""Construct two genuine chronological 64-participant local tree covers on a
68-vertex union with a 60-person shared cell, then independently replay
their gossip-state transitions and refute ALL-pairs B/D compatibility.

This is a SEPARATE numerical falsifier of the naive idea that achieving
Stage 10's local lower bound on both sides produces a global solution.
It does NOT verify or disprove every possible 60-person assignment.
"""
from collections import defaultdict


def equality_arm():
    # Separate implementation; does not import Stage 9/10 code.
    edges, colors, root = [], [0], 0
    for _ in range(4):
        h = len(colors)
        edges = (edges + [(a + h, b + h) for a, b in edges]
                 + [(root, root + h)])
        colors = ([0 if x == 0 else x + 1 for x in colors] +
                  [1 if x == 0 else x + 1 for x in colors])
    assert len(colors) == 16 and [colors.count(c) for c in range(5)] == [1, 1, 2, 4, 8]
    return edges, colors, root


def construct_and_replay():
    edges, colors, root = equality_arm()
    sizes = {(i, j): 1 << ((i + j) % 4)
             for i in range(4) for j in range(4)}
    cells = {}
    next_id = 8
    for i in range(4):
        for j in range(4):
            count = sizes[i, j]
            cells[i, j] = list(range(next_id, next_id + count))
            next_id += count
    assert next_id == 68 and sum(sizes.values()) == 60

    def component(which):
        calls = []
        for arm in range(4):
            groups = defaultdict(list)
            for v, g in enumerate(colors):
                groups[g].append(v)
            loc = {groups[0][0]: arm if which == "A" else arm + 4}
            for group in range(1, 5):
                if which == "A":
                    indices = [j for j in range(4)
                               if sizes[arm, j] == len(groups[group])]
                    assert len(indices) == 1
                    vertices = cells[arm, indices[0]]
                else:
                    indices = [i for i in range(4)
                               if sizes[i, arm] == len(groups[group])]
                    assert len(indices) == 1
                    vertices = cells[indices[0], arm]
                for local, global_id in zip(groups[group], vertices):
                    loc[local] = global_id
            assert len(loc) == 16
            calls.extend((loc[a], loc[b]) for a, b in edges)
        base = 0 if which == "A" else 4
        calls.extend(((base, base+2), (base+1, base+3),
                      (base+2, base+3)))
        assert len(calls) == 63
        assert len(set(tuple(sorted(e)) for e in calls)) == 63
        knowledge = [1 << i for i in range(68)]
        for a, b in calls:
            knowledge[a] = knowledge[b] = knowledge[a] | knowledge[b]
        fullmask = (sum(1 << i for i in range(base, base+4)) |
                    sum(1 << i for i in range(8,68)))
        assert knowledge[base+2] == knowledge[base+3] == fullmask
        return knowledge, calls

    A, call_A = component("A")
    B, call_B = component("B")
    assert not (set(map(lambda e:tuple(sorted(e)),call_A)) &
                set(map(lambda e:tuple(sorted(e)),call_B))), (
                    "unexpected reuse of a contact across halves")

    # B's run is the time REVERSED suffix; every source index in B
    # represents a suffix TARGET, not an original A-source secret.
    sources_A = list(range(4)) + list(range(8,68))
    targets_B = list(range(4,8)) + list(range(8,68))
    missing = []
    for a in sources_A:
        for b in targets_B:
            if not any(((A[x] >> a) & 1) and ((B[x] >> b) & 1)
                       for x in range(8,68)):
                missing.append((a,b))
    assert len(missing) == 2176, len(missing)
    # Display one concrete secret/source and destination pair with no
    # common shared cell witness. Four size-two cells make the private
    # witness obstruction visible.
    assert (0,10) in missing
    for cell in cells.values():
        if len(cell)==2:
            x,y=cell
            assert any((A[x] & (1<<a)) and not (A[y] & (1<<a))
                       for a in sources_A)
            assert any((B[y] & (1<<b)) and not (B[x] & (1<<b))
                       for b in targets_B)

    print("PASS independent chronological 60-person shared-cell"
          " two-tree construction: two genuine 63-call component"
          " chronologies on 68 union vertices, 0 duplicate pairs;"
          " exactly 2176 incompatible source-target obligations",
          flush=True)
    print("PASS explicit incompatibility original source 0"
          " vs reversed-suffix target 10;"
          " all four size-two subcells exhibit private"
          " receiver obstructions", flush=True)
    print("LIMIT: this disproves a naive matched-equality construction,"
          " NOT every future-t interface and NOT the full all-n"
          " half-forest conjecture",flush=True)


if __name__ == "__main__":
    construct_and_replay()
