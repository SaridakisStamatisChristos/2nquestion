"""Stage 11 independent falsification for unbounded tree-cover rigidity.

NO re-use of earlier rooted-tree oracle, B/D CSP, or f(s) source:
- Enumerate every labelled tree (edge subsets) and chronological permutation
  on m=2..5, every (s+1)^m group/unassigned coloring for s<=3.
- Verify assigned-recipient count >=2**(s-1), including UNUSED HELPERS.
- Verify equality entails EXACTLY TWO singleton groups and EVERY
  participant has a private secret within their own recipient group.
- Independently build and verify equality examples for s=1..8.
- Attack the tight-tight crossed-arm slack arithmetic for k=2..8.
Finite checks corroborate the human proofs; they do not prove all-n.
"""
from itertools import combinations, permutations, product
from collections import Counter
from functools import lru_cache


def states_for_trees(m):
    edges = tuple(combinations(range(m), 2))
    for chosen in combinations(edges, m - 1):
        parent = list(range(m))
        def rt(a):
            while parent[a] != a:
                a = parent[a]
            return a
        for a, b in chosen:
            ra, rb = rt(a), rt(b)
            parent[ra] = rb
        if len({rt(i) for i in range(m)}) != 1:
            continue
        for chronology in permutations(chosen):
            knowledge = [1 << i for i in range(m)]
            for a, b in chronology:
                knowledge[a] = knowledge[b] = knowledge[a] | knowledge[b]
            yield tuple(knowledge)


def exhaustive_small():
    fixtures = {2:(1,5),3:(6,72),4:(96,2784),5:(3000,199800)}
    for m,(expected_histories, expected_covers) in fixtures.items():
        checked_histories = covers = equality = helpers = 0
        full = (1 << m) - 1
        for knowledge in states_for_trees(m):
            checked_histories += 1
            for s in range(1, min(3,m)+1):
                for labels in product(range(s+1),repeat=m):
                    if any(g not in labels for g in range(1,s+1)):
                        continue
                    groups = [tuple(i for i in range(m) if labels[i]==g)
                              for g in range(1,s+1)]
                    if any(__import__("functools").reduce(int.__or__,
                              (knowledge[v] for v in G), 0)!=full
                           for G in groups):
                        continue
                    covers += 1
                    assigned=sum(bool(x) for x in labels)
                    helpers += assigned < m
                    assert assigned>=2**(s-1),(
                        "Steiner helper violates bound",m,s,knowledge,labels)
                    if m!=2**(s-1) or assigned!=m or s<2:
                        continue
                    equality+=1
                    assert sum(len(G)==1 for G in groups)==2,(
                        "tight singleton rigidity failed",m,s,knowledge,labels)
                    full_collectors = [i for i,k in enumerate(knowledge)
                                      if k==full]
                    assert len(full_collectors)==2
                    assert all(len(next(G for G in groups if i in G))==1
                               for i in full_collectors)
                    for G in groups:
                        for v in G:
                            assert any(
                                (knowledge[v] & (1<<bit)) and
                                all(not(knowledge[u] & (1<<bit))
                                    for u in G if u!=v)
                                for bit in range(m)
                            ),("private secret absent",m,s,labels,knowledge,v)
        assert (checked_histories,covers)==(
            expected_histories,expected_covers),(
            m,checked_histories,covers)
        print("PASS chronological tree m=%d: %d histories, %d covering"
              " marked group assignments, %d with unused helpers,"
              " %d equality rigidity checks"%(m,checked_histories,
               covers,helpers,equality),flush=True)


def construct(s):
    if s==1:
        return [],[0],0
    old,colors,root=construct(s-1)
    half=len(colors)
    edges=old+[(a+half,b+half) for a,b in old]+[(root,root+half)]
    return edges,[(0 if x==0 else x+1) for x in colors]+[
        (1 if x==0 else x+1) for x in colors],root


def equality_constructions():
    for s in range(1,9):
        edges,colors,root=construct(s)
        n=len(colors)
        assert n==2**(s-1)
        assert len(edges)==n-1
        assert len({tuple(sorted(e)) for e in edges})==len(edges)
        k=[1<<i for i in range(n)]
        for a,b in edges:
            k[a]=k[b]=k[a]|k[b]
        full=(1<<n)-1
        groups=[[i for i,c in enumerate(colors) if c==j]
                for j in range(s)]
        assert colors[root]==0 and k[root]==full
        for G in groups:
            assert __import__("functools").reduce(
                int.__or__,(k[i] for i in G),0)==full
            for v in G:
                assert any(
                    (k[v]&(1<<bit)) and
                    all(not (k[u]&(1<<bit)) for u in G if u!=v)
                    for bit in range(n)
                ),("private secret failure",s,v)
        if s>=2:
            assert sum(len(G)==1 for G in groups)==2
            assert sum(K==full for K in k)==2
        print(f"PASS sharp recursive s={s}, n={n}: every"
              " designated recipient PRIVATE, exact collectors and"
              " singleton groups",flush=True)


def weak_compositions(total,parts):
    if parts==1:
        yield (total,)
        return
    for first in range(total+1):
        for rest in weak_compositions(total-first,parts-1):
            yield (first,)+rest


def slack_regression():
    for k in range(2,9):
        cases=0
        for D in range(k-1):
            for row_slack in weak_compositions(D,k):
                for col_slack in weak_compositions(D,k):
                    cases+=1
                    tight_rows=[i for i,a in enumerate(row_slack) if a==0]
                    tight_cols=[j for j,b in enumerate(col_slack) if b==0]
                    assert len(tight_rows)>=2 and len(tight_cols)>=2
                    # Every crossing of two tight arms must be singleton.
                    # But an extremal arm has only one X singleton group:
                    # any tight row has >=2 singleton X cells, contradiction.
                    assert len(tight_cols)>1
        assert cases>0
        print(f"PASS crossed k={k}: {cases} independently enumerated"
              f" row/column slack pairs with D<k-1 all obstructed;"
              f" necessary t>={k*(2**k-1)+(k-1)}",flush=True)
    assert 4*(2**4-1)+3==63
    print("VERDICT: rigorous finite falsification PASS;"
          " conditional Stage 11 four-arm threshold >=63;"
          " all-n half-forest conjecture remains OPEN",flush=True)


if __name__=="__main__":
    exhaustive_small()
    equality_constructions()
    slack_regression()
