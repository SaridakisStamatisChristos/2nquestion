"""Stage30 n22/n23 source-target exact-support target registry.

NO size-only UNSAT exclusion is claimed. This lists profiles in the sound
Stage28 frontier for which an exact local chronological solver can impose
the new six-cell 2P3 mandatory source-support condition IF that tree's
six-person recipient group has zero private recipients.
"""
from collections import Counter, defaultdict
from pathlib import Path
import sys

research = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(research / "v4.5"))
sys.path.insert(0, str(research / "v4.4"))
from unbounded_eight_outside_audit import classify_new  # noqa: E402
from n22_3x3_frontier import canonical  # noqa: E402


def exact_six_tree_cells(m):
    """The applicable tree row/column, not the unicyclic center itself."""
    return tuple(
        [("prefix-P1", "C13")] if m[0] == m[1] == 1 and m[2] == 6 else []
    ) + tuple(
        [("prefix-P2", "C23")] if m[3] == m[4] == 1 and m[5] == 6 else []
    ) + tuple(
        [("reverse-Q1", "C31")] if m[0] == m[3] == 1 and m[6] == 6 else []
    ) + tuple(
        [("reverse-Q2", "C32")] if m[1] == m[4] == 1 and m[7] == 6 else []
    )


def run(n):
    _, _, survivors, _ = classify_new(n)
    found = []
    seen = defaultdict(set)
    for m in survivors:
        targets = exact_six_tree_cells(m)
        if not targets:
            continue
        found.append((m, targets))
        seen[canonical(m)].add(m)
    selected = {canonical(m) for m, _ in found}
    # Target eligibility is stable under legal swaps of the two TREE rows
    # and two TREE columns; never swap chronological call positions.
    canonical_selected = {canonical(m) for m in survivors
                          if exact_six_tree_cells(m)}
    assert selected == canonical_selected
    assert all(len(cells) >= 1 for _, cells in found)
    return survivors, found, seen


def main():
    for n in (22, 23):
        survivors, selected, by_orbit = run(n)
        labels = Counter(label for _, targets in selected for label, _ in targets)
        print("n=", n, "Stage28 necessary survivors=", len(survivors))
        print("  exact (1,1,6) eligible matrices=", len(selected),
              "orbits=", len(by_orbit), "tree-label multiplicity=", dict(labels))
        print("  symmetry representatives and applicable exact-support cells:")
        reps = {}
        for m, targets in selected:
            key = canonical(m)
            reps.setdefault(key, targets)
        for m, targets in sorted(reps.items()):
            print(" ", m, sorted(set(c for _, c in targets)))
        print("LIMIT: These are applicability targets, NOT excluded matrices.")
    print("PASS Stage30 exact-support CSP target registry")
    print("NEXT: enumerate original prefix tree order and reverse suffix target")
    print("supports, requiring four forced 2P3 source edges and all-pairs crossing.")


if __name__ == "__main__":
    main()
