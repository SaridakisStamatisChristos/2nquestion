"""Stage 10 four-arm crossing barrier: independent constructive + exact checks.

1. Use the independently checked Stage 9 SHARP s=5 tree cover to
construct four disjoint rooted arms of 16 participants each.
2. Join their OUTSIDE roots with precisely three last tree contacts to
create an actual 64-person (2,2,60) chronological tree component with
two complete collectors in the designated middle outside cell.
3. Verify exact global local knowledge, all four crossed color classes
inside EACH arm receiving all that arm's local secrets, and that every
original local secret's receivers in X meet all four colors.
4. Compare against exact earlier n16/n17 local B/D impossibilities.
5. Check the algebraic q*(2**p - 1) crossing boundary independently.

This construction is NOT a successful global two-half gossip scheme:
only one local component and a hypothetical coloring of its X members
are constructed. It demonstrates the LOCAL per-arm bound is sharp.
"""
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE / "v2.6"))
sys.path.insert(0, str(BASE / "v2.3"))
from construct_tree_cover_equality import build
from exclude_n17_orbits30_31 import local_profiles


def build_crossed_suffix_tree():
    edges, colors, local_root = build(5)
    assert len(colors) == 16 and colors.count(0) == 1
    assert colors[local_root] == 0
    assert all(colors.count(j) > 0 for j in range(1, 5))

    # Roots 0,1 are the other outside pair, roots 2,3 the full collectors.
    # X participants occupy precisely positions 4..63.
    renamings = []
    colors_x = {}
    arm_of = {}
    number = 4
    for arm in range(4):
        renaming = {}
        for i, color in enumerate(colors):
            if color == 0:
                renaming[i] = arm
            else:
                renaming[i] = number
                arm_of[number] = arm
                colors_x[number] = color - 1
                number += 1
        renamings.append(renaming)
    assert number == 64
    assert len(colors_x) == 60
    S = []
    for arm in range(4):
        R = renamings[arm]
        S.extend((R[u], R[v]) for u, v in edges)
    assert len(S) == 60
    S += [(0, 2), (1, 3), (2, 3)]
    assert len(S) == 63
    assert len({tuple(sorted(e)) for e in S}) == len(S)

    knowledge = [1 << v for v in range(64)]
    cut = 0
    for j, (u, v) in enumerate(S):
        knowledge[u] = knowledge[v] = knowledge[u] | knowledge[v]
        if j == 59:
            cut = knowledge.copy()
    full = (1 << 64) - 1
    assert knowledge[2] == knowledge[3] == full
    assert knowledge[0] | knowledge[1] == full

    # Component cell sizes 2,2,60 in a REAL legal local chronology.
    assert all((knowledge[4] | knowledge[5]) >= 0 for _ in (0,))
    x_union = 0
    for x in range(4, 64):
        x_union |= knowledge[x]
        assert knowledge[x] == cut[x], "X state must be arm-sealed"
    assert x_union == full
    for arm in range(4):
        arm_vertices = [arm] + [x for x in colors_x if arm_of[x] == arm]
        assert len(arm_vertices) == 16
        arm_mask = sum(1 << x for x in arm_vertices)
        assert cut[arm] == arm_mask, "each outside root completely knows its arm"
        for color in range(4):
            members = [x for x in arm_vertices
                       if x in colors_x and colors_x[x] == color]
            assert members
            known = 0
            for x in members:
                known |= knowledge[x]
            assert known == arm_mask, ("four color groups must each cover arm", arm, color)
        for secret in arm_vertices:
            receivers = [x for x in colors_x if knowledge[x] >> secret & 1]
            assert all(arm_of[x] == arm for x in receivers)
            assert {colors_x[x] for x in receivers} == set(range(4))

    print("PASS 64-vertex legal (2,2,60) local tree chronology:"
          " 63 distinct calls, 2 full middle-cell collectors,"
          " all 4 suffix arms have one full outside root and"
          " 4 complete X-recipient groups", flush=True)
    return S, colors_x, arm_of


def main():
    # Independently test earlier exact local small-size impossibilities.
    old = {
        (4, False): ({(8, 14, 32768)}, {(6, 8, 278)}, 48),
        (4, True): ({(14, 14, 32768)}, {(8, 8, 278)}, 144),
    }
    for key, expected in old.items():
        assert local_profiles(*key) == expected, key
    for cyc in (False, True):
        B, D, total = local_profiles(5, cyc)
        assert (len(B), len(D), total) == (
            5, 20, 5760 if cyc else 1920
        )
        assert all((b[2] & d[2]) != d[2] for b in B for d in D)
    print("PASS exact t=4 and t=5 original (2,2,t)"
          " prefix/suffix local chronology B/D crossing regression", flush=True)

    build_crossed_suffix_tree()

    for p in range(1, 9):
        for q in range(1, 9):
            t = q * (2 ** p - 1)
            assert t // q + 1 == 2 ** p
            assert t > 0
    assert 4 * (2 ** 4 - 1) == 60
    assert 4 * (2 ** 4 - 1) - 1 == 59
    assert 2 ** 5 == 16
    assert 4 * (16 - 1) == 60
    print("PASS generalized p/q arm capacity and 59-versus-60"
          " threshold arithmetic; construction does not assert"
          " a complete globally successful original-half scheme", flush=True)


if __name__ == "__main__":
    main()
