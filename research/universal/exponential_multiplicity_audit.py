"""All-n rooted tree receiver multiplicity: exact exponential sharp threshold.

Proof, universal quantifiers, and exclusion boundary:
  research/universal/EXPONENTIAL_MULTIPLICITY_AND_PAIR_RIGIDITY.md

The finite tests below NEVER certify universal validity by themselves.
They replay EXPLICIT parameterized sharp constructions for q=1..7 and
independently check the support-transversal bound on genuine two-root
chronological tree histories (including cases with one rooted side
having only a unique 2-carrier support).
"""
from itertools import combinations, permutations, product
from collections import Counter


def inside(q):
    """Root IN designated C; |C|=2^(q-1), every secret q-fold C-covered."""
    if q == 1:
        return 1, (), 0, frozenset((0,))
    n1, e1, r1, C1 = inside(q-1)
    n2, e2, r2, C2 = inside(q-1)
    off = n1
    return (n1+n2,
            tuple(e1)+tuple((a+off,b+off) for a,b in e2)+((r1,r2+off),),
            r1, C1|frozenset(v+off for v in C2))


def outside(q):
    """Root NOT in C; |C|=2^q-1, every secret q-fold C-covered."""
    if q == 1:
        return 2, ((0,1),), 0, frozenset((1,))
    n1, e1, r1, C1 = outside(q-1)
    n2, e2, r2, C2 = inside(q)
    off = n1
    return (n1+n2,
            tuple(e1)+tuple((a+off,b+off) for a,b in e2)+((r1,r2+off),),
            r1, C1|frozenset(v+off for v in C2))


def replay(n, contacts):
    info = [1<<i for i in range(n)]
    parent = list(range(n))
    seen = set()

    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v

    for a,b in contacts:
        edge=tuple(sorted((a,b)))
        assert 0 <= a < n and 0 <= b < n and a != b and edge not in seen
        seen.add(edge)
        ra, rb = root(a), root(b)
        assert ra != rb, "static contact graph must be a tree"
        parent[ra] = rb
        union = info[a] | info[b]
        info[a] = info[b] = union
    assert len(contacts)==n-1
    assert len({root(v) for v in range(n)}) == 1
    return info


def support_masks(n, info, C):
    return tuple(frozenset(v for v in C if (info[v]>>s)&1)
                 for s in range(n))


def certify_constructive_sharpness():
    for q in range(1,8):
        for label, maker, formula in (
            ("in",inside,2**(q-1)),("out",outside,2**q-1)):
            n, calls, r, C = maker(q)
            assert len(C)==formula
            assert (r in C) == (label=="in")
            info = replay(n,calls)
            assert info[r]==(1<<n)-1
            supports = support_masks(n,info,C)
            assert min(map(len,supports))==q, (q,label,supports)
            print(f"PASS q={q} root-{label}: vertices={n} recipients={len(C)} "
                  f"minimum exact original-secret carrier count={q}")


def rooted_five_single_pair():
    n=6
    calls=((3,0),(4,1),(1,0),(2,5),(0,2))
    C=frozenset(range(1,n))
    info=replay(n,calls)
    assert info[0]==(1<<n)-1
    s=support_masks(n,info,C)
    assert min(map(len,s))==2
    assert len({x for x in s if len(x)==2})==1
    return n,calls,0,C


def joined_two_roots(a,b):
    n1,e1,r1,C1=a
    n2,e2,r2,C2=b
    off=n1
    n=n1+n2
    seq=tuple(e1)+tuple((x+off,y+off) for x,y in e2)+((r1,r2+off),)
    C=C1|frozenset(v+off for v in C2)
    info=replay(n,seq)
    assert info[r1]==info[r2+off]==(1<<n)-1
    supports=support_masks(n,info,C)
    assert min(map(len,supports))>=2
    return n,seq,C,supports


def check_unique_two_support_transversal():
    source=Counter()
    cases=(
        ("3+3",outside(2),outside(2)),
        ("3+5",outside(2),rooted_five_single_pair()),
        ("5+7",rooted_five_single_pair(),outside(3)),
        ("7+7",outside(3),outside(3)),
    )
    for name,left,right in cases:
        n, seq, C, supports=joined_two_roots(left,right)
        # For a fixed T2, all T1 size-two supports compatible with every
        # original T2 source are exactly the 2-element transversals
        # of the actual T2 carrier-support hypergraph.
        hits=[frozenset(p) for p in combinations(sorted(C),2)
              if all(frozenset(p)&s for s in supports)]
        assert len(hits)<=1,(name,hits)
        p2={s for s in supports if len(s)==2}
        source[name]=(n,len(C),len(hits),len(p2))
        print("PASS crossed-tree two-support uniqueness template",name,
              "n=",n,"center=",len(C),"admissible 2-supports=",len(hits))
    return source


def local_tree_bound_regression():
    """Exhaust original orders on <=6 vertices; validate q=2,3 sharp bound."""
    for n in (3,4,5,6):
        qualified=Counter()
        for word in product(range(n),repeat=n-2):
            deg=[1]*n
            for z in word:deg[z]+=1
            edges=[]
            for z in word:
                leaf=next(i for i in range(n) if deg[i]==1)
                edges.append((leaf,z));deg[leaf]-=1;deg[z]-=1
            edges.append(tuple(i for i in range(n) if deg[i]==1))
            for seq in permutations(edges):
                info=replay(n,seq)
                if info[0] != (1<<n)-1:
                    continue
                # Enumerate ALL nonempty C from remaining vertices,
                # including arbitrary helpers NOT in C.
                for mask in range(1,1<<(n-1)):
                    C=frozenset(v+1 for v in range(n-1) if mask>>v&1)
                    q=min(map(len,support_masks(n,info,C)))
                    if q>0:
                        assert len(C)>=(1<<q)-1,(n,seq,C,q)
                        qualified[q]+=1
        assert qualified, n
        print("PASS exact n=",n,"unbounded-helper subset-bound regression",dict(qualified))


def main():
    certify_constructive_sharpness()
    check_unique_two_support_transversal()
    local_tree_bound_regression()
    print("HUMAN ALL-n theorem: rooted out-C q-fold cover requires >=2^q-1 C")
    print("HUMAN ALL-n theorem: crossed two-root trees permit <=1 exact two-carrier source support per side")
    print("CONSEQUENCE (CONDITIONAL): all-pairs crossed two-root trees require |X|>=12")
    print("LIMIT: all-width no-crossing theorem / original half-forest still OPEN")
    print("LIMIT: formal proof assistant and historical novelty check NOT done")


if __name__=="__main__":
    main()
