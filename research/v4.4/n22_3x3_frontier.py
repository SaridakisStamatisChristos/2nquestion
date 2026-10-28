"""Stage 27: independent n=22 3x3 incidence frontier (NECESSARY, not sufficient).

Uses only size/collector predicates whose hypotheses are valid at arbitrary n.
Independently enumerates 9-cell compositions using stars-and-bars dividers,
then differentially checks the prior Stage25 and Stage26 implementations when
run inside the repository. Does NOT examine 3x4/4x3 or chronological schedules.
"""
from collections import Counter
from itertools import combinations
from math import comb
from pathlib import Path
import sys

BASE = (1, 1, 2, 1, 1, 2, 2, 2, 1)
PRIV = {
    (1, 1, 2): 2, (1, 1, 3): 2, (1, 1, 4): 1, (1, 1, 5): 1,
    (2, 1, 2): 2, (1, 2, 2): 2, (2, 1, 3): 2, (1, 2, 3): 2,
    (1, 2, 4): 1, (2, 1, 4): 1, (1, 3, 2): 2, (3, 1, 2): 2,
    (1, 3, 3): 2, (3, 1, 3): 2, (2, 2, 2): 2, (2, 2, 3): 2,
}


def matrices(n):
    """Independent separator-based weak-composition enumeration."""
    k = n - sum(BASE)
    if k < 0:
        return
    for dividers in combinations(range(k + 8), 8):
        vals = []
        previous = -1
        for div in dividers:
            vals.append(div - previous - 1)
            previous = div
        vals.append(k + 8 - previous - 1)
        yield tuple(x + y for x, y in zip(BASE, vals))


def canonical(m):
    return min(tuple(m[3 * r + c] for r in rows for c in cols)
               for rows in ((0, 1, 2), (1, 0, 2))
               for cols in ((0, 1, 2), (1, 0, 2)))


def privacy(m):
    f = lambda a, b, c: PRIV.get((a, b, c), 0)
    return ((f(m[0], m[1], m[2]), f(m[3], m[4], m[5])),
            (f(m[0], m[3], m[6]), f(m[1], m[4], m[7])))


def has_three_outside(cells, mins):
    return any(cells[i] <= 3 and mins[i] >= 2 and
               cells[1-i] <= 6 and mins[1-i] >= 1 for i in (0, 1))


def small_pair(cells):
    return min(cells) == 2 and max(cells) <= 6


def stage25(m):
    p = m[2] + m[5] - 4
    q = m[6] + m[7] - 4
    d = m[8] - 1
    if p + d < 4 or q + d < 4:
        return 'component'
    if p == 0 or q == 0:
        return 'saturated'
    qm, pm = privacy(m)
    if sum(qm) >= 4 or sum(pm) >= 4:
        return 'privacy4'
    qa = has_three_outside((m[2], m[5]), qm)
    pa = has_three_outside((m[6], m[7]), pm)
    if m[8] <= 5 and qa and pa:
        return 'dual3'
    if m[8] == 1 and (qa or pa):
        return 'singleton4'
    if m[8] == 2 and ((qa and m[6] + m[7] < 10) or
                      (pa and m[2] + m[5] < 10)):
        return 'binary_rootcut'
    return 'survive'


def stage26(m):
    qm, pm = privacy(m)
    up, down = (m[2], m[5]), (m[6], m[7])
    x = m[8]
    qa = has_three_outside(up, qm)
    pa = has_three_outside(down, pm)
    if x == 1 and (small_pair(up) or small_pair(down)):
        return 'L26_single'
    if x == 2 and small_pair(up) and small_pair(down):
        return 'L26_double'
    if x == 3 and ((qa and small_pair(down)) or (pa and small_pair(up))):
        return 'L26_triple'
    if x < 6 and small_pair(up) and small_pair(down):
        return 'L26_twice'
    for cells, minima in ((up, qm), (down, pm)):
        if x == 3 and sorted(cells) == [2, 4]:
            i = 0 if cells[0] == 2 else 1
            if minima[i] >= 2 and minima[1-i] >= 1:
                return 'L22_243'
    if m == (1, 1, 4, 1, 1, 4, 4, 4, 1):
        return 'L26_last'
    return 'survive'


def run(n):
    earlier, newer = Counter(), Counter()
    remaining = []
    all_m = list(matrices(n))
    assert len(all_m) == comb(n - 13 + 8, 8)
    assert len(set(all_m)) == len(all_m)

    # Differential oracle: prior implementations are imported only if present;
    # neither provides input to this generator or classifier.
    research = Path(__file__).resolve().parent.parent
    v42, v43 = research / 'v4.2', research / 'v4.3'
    if v42.is_dir() and v43.is_dir():
        sys.path[:0] = [str(v42), str(v43)]
        from n21_staged_frontier import classify as reference25
        from n21_staged_frontier import canonical as reference_canonical
        from n21_final import classify_final as reference26
        for m in all_m:
            assert stage25(m) == reference25(m), ('Stage25 mismatch', m)
            assert canonical(m) == reference_canonical(m), ('canonical mismatch', m)
            if stage25(m) == 'survive':
                ours = stage26(m)
                orig = reference26(m)
                # Label conventions differ; only surviving states must agree.
                assert (ours == 'survive') == (orig == 'UNRESOLVED'), (m, ours, orig)
        print(f'PASS differential Stage25+26 branch-source oracle n={n}')
    else:
        print('NOTE standalone run: repository differential oracle UNVERIFIED')

    for m in all_m:
        a = stage25(m)
        earlier[a] += 1
        if a != 'survive':
            continue
        b = stage26(m)
        newer[b] += 1
        if b == 'survive':
            remaining.append(m)
    return earlier, newer, remaining


def main():
    a21, b21, surviving21 = run(21)
    assert a21['survive'] == 77 and not surviving21
    assert b21 == {'L26_single': 8, 'L26_double': 4, 'L26_triple': 40,
                   'L26_twice': 20, 'L22_243': 4, 'L26_last': 1}, b21
    print('PASS n21 finite necessary-incidence regression 77 -> 0')

    a, b, surviving = run(22)
    assert a == {'component': 20914, 'saturated': 798, 'privacy4': 1209,
                 'dual3': 328, 'singleton4': 56, 'binary_rootcut': 244,
                 'survive': 761}, a
    assert b == {'L26_single': 72, 'L26_double': 40, 'L26_triple': 168,
                 'L26_twice': 264, 'L22_243': 80, 'survive': 137}, b
    assert len(surviving) == 137
    assert len({canonical(m) for m in surviving}) == 42
    assert Counter(m[8] for m in surviving) == {1: 28, 2: 41, 3: 44, 4: 20, 6: 4}
    print('PASS n22 3x3 raw=24310 Stage25=761 Stage26=137 orbits=42')
    print('PASS center histogram', dict(sorted(Counter(m[8] for m in surviving).items())))
    print('SCOPE: 3x3 ONLY; 3x4/4x3 unexamined; NO n22 proof')
    print('SCOPE: necessary incidence filters, not chronologies; novelty OPEN')


if __name__ == '__main__':
    main()
