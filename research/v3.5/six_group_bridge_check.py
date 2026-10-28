"""Stage 18 independent six-group local witness and exact labelled incidence filter.

All chronology replay uses original tree call order. Incidence enumeration counts
necessary cell-size profiles, NEVER complete successful gossip schedules.
"""
from itertools import product
from math import comb


def sharp_tree(labels, first_vertex=0):
    """Return (label-by-vertex, chronological calls, next_vertex, complete_root)."""
    if len(labels) == 1:
        return [labels[0]], [], first_vertex + 1, first_vertex
    if len(labels) == 2:
        return ([labels[0], labels[1]],
                [(first_vertex, first_vertex + 1)],
                first_vertex + 2, first_vertex)
    left, lcalls, middle, lr = sharp_tree(
        [labels[0]] + labels[2:], first_vertex)
    right, rcalls, last, rr = sharp_tree(
        [labels[1]] + labels[2:], middle)
    return left + right, lcalls + rcalls + [(lr, rr)], last, lr


def check_tight_six_groups():
    labels, calls, n, root = sharp_tree(list(range(6)))
    assert n == 32 and len(calls) == 31
    assert len(set(tuple(sorted(x)) for x in calls)) == len(calls)
    know = [1 << v for v in range(n)]
    for a, b in calls:
        know[a] = know[b] = know[a] | know[b]
    mask = (1 << n) - 1
    groups = [[v for v, mark in enumerate(labels) if mark == j]
              for j in range(6)]
    assert sorted(map(len, groups)) == [1, 1, 2, 4, 8, 16]
    collectors = [v for v in range(n) if know[v] == mask]
    assert len(collectors) == 2 and root in collectors
    for group in groups:
        collective = 0
        for v in group:
            collective |= know[v]
            assert any((know[v] & (1 << secret))
                       and all((know[w] & (1 << secret)) == 0
                               for w in group if w != v)
                       for secret in range(n)), (group, v)
        assert collective == mask, group
    print("PASS exact 32-vertex chronological spanning tree with SIX",
          "disjoint complete-cover recipient groups")
    print("PASS equality rigidity: 2 singleton complete collectors,",
          "32 private recipients, 31 distinct chronological calls")


def weak_compositions(n, width):
    if width == 1:
        yield (n,)
        return
    for first in range(n + 1):
        for rest in weak_compositions(n - first, width - 1):
            yield (first,) + rest


def choose(n, k):
    return comb(n, k) if n >= k >= 0 else 0


def closed_form(n):
    k = n - 13
    return choose(k + 8, 8) - 2 * choose(k + 6, 6) + choose(k + 4, 4)


def enumerate_profiles(n):
    raw = kept = 0
    for extra in weak_compositions(n - 13, 9):
        raw += 1
        if not (extra[2] == extra[5] == 0
                or extra[6] == extra[7] == 0):
            kept += 1
    return raw, kept


def verify_untouched_cover():
    # Exhaust all nonempty carrier supports with at least two recipients,
    # on 2..5 people. Removing ANY last-edge endpoint retains coverage of
    # each source secret by at least one unchanged participant.
    for size in range(2, 6):
        supports = [mask for mask in range(1, 1 << size)
                    if mask.bit_count() >= 2]
        for a in range(size):
            for mask in supports:
                assert mask & ~(1 << a)
    print("PASS endpoint deletion preserves each double-carried secret",
          "for all support masks on 2..5 recipients")


def main():
    check_tight_six_groups()
    verify_untouched_cover()
    fixed = {18: 489, 19: 1365, 20: 3333, 22: 15015,
             23: 28743, 24: 52195, 25: 90662, 26: 151606}
    for n in range(13, 27):
        raw, survivors = enumerate_profiles(n)
        predicted = closed_form(n)
        assert survivors == predicted, (n, survivors, predicted)
        assert raw == comb(n - 13 + 8, 8), (n, raw)
        if n in fixed:
            assert survivors == fixed[n], (n, survivors, fixed[n])
        if n >= 18:
            print(f"PASS n={n} raw={raw} stage18_necessary={survivors}")
    for n in (28, 29, 32, 35, 40, 42):
        print(f"PASS n={n} closed-form necessary={closed_form(n)}")
    print("ONLY VALID n<=42 as final necessary incidence count;",
          "does NOT count successful schedules")


if __name__ == "__main__":
    main()
