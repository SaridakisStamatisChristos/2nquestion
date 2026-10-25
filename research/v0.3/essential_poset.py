"""Temporal precedence and compulsory-edge lemmas for injectively timed cliques.

All computational tests check finite instances only. The universal statements
in the accompanying note have independent human-checkable proofs.
"""
from itertools import combinations, permutations
import random


def edge_sequence_lex(n):
    return list(combinations(range(n), 2))


def info_at_end(n, sequence, omitted=None):
    info = [1 << i for i in range(n)]
    for i, (u, v) in enumerate(sequence):
        if i == omitted:
            continue
        x = info[u] | info[v]
        info[u] = info[v] = x
    return info


def connected(n, sequence, omitted=None):
    return all(mask == (1 << n) - 1 for mask in info_at_end(n, sequence, omitted))


def time_matrix(n, sequence):
    times = [[-1] * n for _ in range(n)]
    for t, (u, v) in enumerate(sequence):
        times[u][v] = times[v][u] = t
    return times


def precedence_matrix(n, sequence):
    assert n >= 3
    times = time_matrix(n, sequence)
    return [[u != v and all(times[u][w] < times[v][w]
                              for w in range(n) if w not in (u, v))
             for v in range(n)] for u in range(n)]


def compulsory(n, sequence):
    assert connected(n, sequence)
    return [(t, u, v) for t, (u, v) in enumerate(sequence)
            if not connected(n, sequence, omitted=t)]


def has_edge_pivot(n, sequence):
    allbits = (1 << n) - 1
    past = [1 << i for i in range(n)]
    before = []
    for u, v in sequence:
        before.append(past[:])
        both = past[u] | past[v]
        past[u] = past[v] = both
    for t, (u, v) in enumerate(sequence):
        if before[t][u] | before[t][v] != allbits:
            continue
        reached = (1 << u) | (1 << v)
        for a, b in sequence[t + 1:]:
            if (reached >> a & 1) or (reached >> b & 1):
                reached |= (1 << a) | (1 << b)
        if reached == allbits:
            return True
    return False


def verify_lemmas(n, sequence):
    p = precedence_matrix(n, sequence)
    # Strict partial-order property, including antisymmetry and transitivity.
    for a in range(n):
        assert not p[a][a]
        for b in range(n):
            assert not (p[a][b] and p[b][a])
            for c in range(n):
                if p[a][b] and p[b][c]:
                    assert p[a][c], ('transitivity', n, sequence)
    for index, u, v in compulsory(n, sequence):
        assert p[u][v] or p[v][u], ('comparability', n, sequence, index)
        lower, upper = (u, v) if p[u][v] else (v, u)
        predecessors = [x for x in range(n) if p[x][lower]]
        successors = [y for y in range(n) if p[upper][y]]
        assert not (predecessors and successors), ('detour', n, sequence, index)
    bottoms = [u for u in range(n) if all(u == v or p[u][v] for v in range(n))]
    tops = [v for v in range(n) if all(u == v or p[u][v] for u in range(n))]
    if bottoms and tops:
        assert has_edge_pivot(n, sequence), ('pivot', n, sequence)


def main():
    assert all(connected(n, edge_sequence_lex(n)) for n in range(3, 16))
    for n in range(4, 16):
        seq = edge_sequence_lex(n)
        f = compulsory(n, seq)
        expected = {tuple(sorted(e)) for e in seq if 0 in e or (n - 1) in e}
        actual = {tuple(sorted((u, v))) for _, u, v in f}
        assert actual == expected and len(f) == 2*n - 3
        verify_lemmas(n, seq)
    # Full permutations K4, followed by seeded randomized larger instances.
    tested = 0
    edges = edge_sequence_lex(4)
    for seq in permutations(edges):
        verify_lemmas(4, seq)
        tested += 1
    rng = random.Random(20261024)
    for n, count in [(5, 1500), (6, 1500), (7, 1500), (8, 1500), (9, 1500)]:
        base = edge_sequence_lex(n)
        for _ in range(count):
            seq = base[:]
            rng.shuffle(seq)
            verify_lemmas(n, seq)
            tested += 1
    print('PASS:', tested, 'edge orderings; lex extremal family 4..15')

if __name__ == '__main__':
    main()
