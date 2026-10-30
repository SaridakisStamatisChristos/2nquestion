"""Exact n17 orbit 30 and 31 local exclusions; independent n16 regression.

n17 canonical matrix ((1,1,2),(1,1,2),(2,2,5)).
Orbit 30 has cyclic row/column 0 and exact tree (2,2,5) groups with
required collectors (0,2,0) in row2 and column2. Orbit 31 has
cyclic row/column 2 and requires four collectors (2,2,0) in both.

For a connected tree with two specified full collectors the final
internal call joins them. For a connected unicyclic contact component
with four specified full collectors, the final two cross-component
calls join two tree components using four different endpoints: before
those calls the four endpoints must each know their side completely.
This enumerates *all* possible internal tree histories, including
each temporal order, and both final crossing matchings.

The mandatory inter-half information transfer in third cell fails
for all B/D profile pairs. Valid for just these two marked n17 classes,
NOT an all-n theorem or full n17 proof.
"""
from functools import lru_cache
from itertools import combinations, permutations


def local_profiles(t, cyclic):
    n = t + 4
    full = (1 << n) - 1
    groups = ((0, 1), (2, 3), tuple(range(4, n)))

    @lru_cache(None)
    def side_histories(side, pair):
        vertices = tuple(v for v in range(n) if side >> v & 1)
        a, b = pair
        h = len(vertices)
        assert a in vertices and b in vertices and h >= 2
        choices = tuple(e for e in combinations(vertices, 2)
                        if e != (a, b))
        histories = set()
        for before in permutations(choices, h - 2):
            parent = list(range(n))

            def root(v):
                while parent[v] != v:
                    v = parent[v]
                return v

            okay = True
            for u, v in before:
                ru, rv = root(u), root(v)
                if ru == rv:
                    okay = False
                    break
                parent[ru] = rv
            if not okay or root(a) == root(b):
                continue
            k = [1 << v for v in range(n)]
            for u, v in before:
                k[u] = k[v] = k[u] | k[v]
            k[a] = k[b] = k[a] | k[b]
            if k[a] == side:
                histories.add(tuple(k[v] for v in vertices))
        return tuple(sorted(histories))

    def profile(k):
        B, D = [], []
        for group in groups:
            b = 0
            for subset in range(1 << len(group)):
                know = 0
                for j, v in enumerate(group):
                    if subset >> j & 1:
                        know |= k[v]
                if know == full:
                    b |= 1 << subset
            d = 0
            for secret in range(n):
                recv = 0
                for j, v in enumerate(group):
                    if k[v] >> secret & 1:
                        recv |= 1 << j
                d |= 1 << recv
            B.append(b)
            D.append(d)
        return tuple(B), tuple(D)

    B, D = set(), set()
    terminal = 0
    for partner in ((1, 2, 3) if cyclic else (0, 1)):
        # The large third cell must meet both sides, since its vertices
        # never participate in the last cross-component contacts.
        for extra in range(1, (1 << t) - 1):
            if cyclic:
                side = (1 << 0) | (1 << partner) | (extra << 4)
                left = tuple(x for x in range(4) if side >> x & 1)
                right = tuple(x for x in range(4) if not (side >> x & 1))
                assert len(left) == len(right) == 2
            else:
                side = (1 << 2) | (1 << partner) | (extra << 4)
                left = (2, partner)
                right = (3, 1 - partner)
            other = full ^ side
            lm = tuple(x for x in range(n) if side >> x & 1)
            rm = tuple(x for x in range(n) if other >> x & 1)
            for l in side_histories(side, left):
                for r in side_histories(other, right):
                    k = [0] * n
                    for v, s in zip(lm, l):
                        k[v] = s
                    for v, s in zip(rm, r):
                        k[v] = s
                    for flip in ((0, 1) if cyclic else (0,)):
                        state = k.copy()
                        if cyclic:
                            for j in range(2):
                                a, b = left[j], right[j ^ flip]
                                state[a] = state[b] = state[a] | state[b]
                            assert all(state[q] == full for q in range(4))
                        else:
                            state[2] = state[3] = state[2] | state[3]
                            assert state[2] == state[3] == full
                        b, d = profile(state)
                        if all(v & (1 << ((1 << len(g)) - 1))
                               for v, g in zip(b, groups)):
                            B.add(b)
                            D.add(d)
                            terminal += 1
    return B, D, terminal


def main():
    # Regression against independent earlier, fully enumerated n16 files.
    historic = {
        (4, False): ({(8, 14, 32768)}, {(6, 8, 278)}, 48),
        (4, True): ({(14, 14, 32768)}, {(8, 8, 278)}, 144),
    }
    for (t, cyclic), expected in historic.items():
        result = local_profiles(t, cyclic)
        assert result == expected, (t, cyclic, result)
        print("PASS n16 historical exact local regression",
              t, cyclic, flush=True)

    for cyc, orbit, mult in ((False, 30, 36), (True, 31, 9)):
        B, D, terminal = local_profiles(5, cyc)
        assert len(B) == 5 and len(D) == 20
        assert terminal == (5760 if cyc else 1920)
        assert all((b[2] & d[2]) != d[2] for b in B for d in D)
        print(f"PASS n17 orbit {orbit} / {mult} placements:",
              "exact (2,2,5)", "cyclic" if cyc else "tree",
              "B=5 D=20; histories=", terminal,
              "; all 100 B/D pairs contradict group2 compatibility",
              flush=True)
    print("LIMIT: other n17 classes remain OPEN; not all-n.", flush=True)


if __name__ == "__main__":
    main()
