"""Falsify the ALL-n conditional crossed-two-tree support theorem.

This checker is intentionally INDEPENDENT of earlier Stage25-34 filters:
- enumerates each labelled Prüfer tree + ALL chronological edge orders
  for rooted recipient sets with k=3/4/5, also helper cases;
- verifies exact two-carrier path subfamilies, and
- enumerates ALL abstract 2-disjoint-side pair-support patterns
  at center widths 6..8 and all 2-vertex transversals.

A finite checker DOES NOT itself prove any universal theorem.
The complete proof is ROOTED_SUPPORT_TRANSVERSAL.md.
"""
from collections import Counter
from itertools import combinations, permutations, product


def tree_edges(n, word):
    d=[1]*n
    for w in word:
        d[w]+=1
    result=[]
    for w in word:
        leaf=next(i for i in range(n) if d[i]==1)
        result.append((leaf,w))
        d[leaf]-=1
        d[w]-=1
    result.append(tuple(i for i in range(n) if d[i]==1))
    return result


def supports(n, chronological_calls, C):
    known=[1<<i for i in range(n)]
    for a,b in chronological_calls:
        merged=known[a]|known[b]
        known[a]=known[b]=merged
    if known[0] != (1<<n)-1:
        return None
    out=tuple(frozenset(x for x in C if (known[x]>>secret)&1)
              for secret in range(n))
    if any(len(q)<2 for q in out):
        return None
    return set(q for q in out if len(q)==2)


def has_path(pairs):
    for a,b in combinations(pairs,2):
        if len(a&b)==1:
            return True
    return False


def rooted_local_checks(k, helpers):
    n=1+k+helpers
    designated=tuple(range(1,1+k))
    total=0
    options=Counter()
    for word in product(range(n),repeat=n-2):
        for seq in permutations(tree_edges(n,word)):
            E=supports(n,seq,designated)
            if E is None:
                continue
            total+=1
            options[len(E)]+=1
            if k in (3,4):
                assert len(E)>=2 and has_path(E), (n,k,helpers,seq,E)
            elif k==5:
                assert len(E)>=1,(n,k,helpers,seq,E)
    if helpers==0:
        expect={3:12,4:288,5:8640}[k]
        assert total==expect,(k,total)
    if helpers<=1:
        assert total>0,(k,helpers)
    print(f"PASS chronological rooted C={k} helpers={helpers} "
          f"eligible={total} paircount_hist={dict(options)}")
    return total


def path_options(group):
    """Sharp rooted 3/4 group: two distinct 2-support edges, same center."""
    for triples in combinations(group,3):
        for y in triples:
            a,b=(x for x in triples if x!=y)
            yield frozenset((frozenset((y,a)),frozenset((y,b))))


def local_options(group):
    if len(group) in (3,4):
        yield from path_options(group)
    elif len(group)==5:
        # A rooted five-recipient side must supply >=1 2-support.
        for pair in combinations(group,2):
            yield frozenset((frozenset(pair),))
    else:
        raise ValueError("only critical support sizes 3,4,5")


def two_hit_transversals(c,E):
    return tuple(frozenset(pair) for pair in combinations(range(c),2)
                 if all(frozenset(pair)&edge for edge in E))


def crossing_support_checks():
    visited=Counter()
    for c in (6,7,8):
        for a in range(3,c-2):
            b=c-a
            A=tuple(range(a))
            B=tuple(range(a,c))
            # By vertex relabeling any split of size (a,b) is isomorphic
            # to this one: all labelled local path/edge supports checked.
            for ea in local_options(A):
                for eb in local_options(B):
                    E=ea|eb
                    hits=two_hit_transversals(c,E)
                    assert len(E)>=3
                    assert len(hits)<=2,(c,a,b,E,hits)
                    if c<=7 or (a,b)==(4,4):
                        assert len(hits)==1,(c,a,b,E,hits)
                    if c==8 and (a,b) in ((3,5),(5,3)):
                        assert len(hits)==2,(c,a,b,E,hits)
                    visited[(c,a,b)]+=1
    assert all(any(q[0]==c for q in visited) for c in (6,7,8))
    print("PASS all abstract critical 2-edge cross-transversal cases",
          dict(visited))
    print("PROOF BASIS: each hypothetical opposite T2 has >=3 DISTINCT "
          "two-carrier original target supports")
    print("PROOF CONSEQUENCE: every T1 permits at MOST 2 two-carrier "
          "target supports for center width <=8")


def main():
    for k,helpers in [(3,0),(4,0),(5,0),(3,1),(4,1),(3,2)]:
        rooted_local_checks(k,helpers)
    crossing_support_checks()
    print("LIMIT: mathematically ALL n only via independent human proof")
    print("LIMIT: for center >=9 no exclusion; all-n FOREST still OPEN")
    print("LIMIT: infinite incidence matrices are NOT gossip chronologies")


if __name__=="__main__":
    main()
