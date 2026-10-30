"""Explicit equality construction for the exact Stage 9 all-n tree-cover bound.

Build two disjoint optimal (s-1)-color rooted tree-call chronologies,
then join their two full root collectors with one LAST call. Preserve the
common colors in both sides, give distinct new colors to the roots.
This creates s collectively complete groups on 2**(s-1) vertices.
Independent from the tree-cover lower-bound proof and brute-force C++.
"""
def build(s):
    assert s >= 1
    if s == 1:
        return [], [0], 0
    edges, colors, root = build(s - 1)
    h = len(colors)
    left = [0 if c == 0 else c + 1 for c in colors]
    right = [1 if c == 0 else c + 1 for c in colors]
    contacts = edges + [(a+h, b+h) for a,b in edges] + [(root,root+h)]
    return contacts, left+right, root

def check(s):
    contacts, groups, root = build(s)
    n = len(groups)
    assert n == 2**(s-1) and len(contacts) == n-1
    assert len(set(tuple(sorted(e)) for e in contacts)) == len(contacts)
    knowledge = [1 << i for i in range(n)]
    for a,b in contacts:
        knowledge[a] = knowledge[b] = knowledge[a] | knowledge[b]
    full = (1 << n) - 1
    assert knowledge[root] == full
    for color in range(s):
        cover = 0
        for i,c in enumerate(groups):
            if c == color:
                cover |= knowledge[i]
        assert cover == full, (s,color)
    sizes = [groups.count(c) for c in range(s)]
    assert all(x>0 for x in sizes)
    print(f"PASS s={s} m={n} tree_calls={n-1} "
          f"complete_root=YES sizes={sizes}",flush=True)

def main():
    for s in range(1,9):
        check(s)
    print("LIMIT: these are tight isolated tree-cover examples; "
          "NOT globally successful gossip counterexamples")

if __name__=="__main__":
    main()
