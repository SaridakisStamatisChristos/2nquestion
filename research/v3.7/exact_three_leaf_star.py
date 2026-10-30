"""Stage 20: independent complete three-leaf star original TREE falsifier.

Target: original six-person prefix tree P2 with last call joining singleton
Q1/Q2 corner participants 0,1, and third group B={2,3,4,5}. Every
original P2 source secret must cross each reverse target support
  {2,3}, {2,4}, {2,5}
inside B. This cannot happen, as verified by complete enumeration.

This enumerates ALL 6^4 labelled trees, and, for those containing edge
(0,1), ALL original chronologies with (0,1) as their final call. Independent
of Stage 18's seven-person FOUR-leaf checker and all previous modules.
"""
from itertools import permutations, product
from collections import Counter


def tree_edges(prufer, n):
    deg = [1] * n
    for z in prufer:
        deg[z] += 1
    out=[]
    for z in prufer:
        leaf=next(i for i in range(n) if deg[i]==1)
        out.append((leaf,z))
        deg[leaf]-=1
        deg[z]-=1
    a,b=[i for i in range(n) if deg[i]==1]
    out.append((a,b))
    return out


def replay(calls, n=6):
    knowledge=[1<<i for i in range(n)]
    for u,v in calls:
        knowledge[u]=knowledge[v]=knowledge[u]|knowledge[v]
    return knowledge


def check():
    n=6
    full=(1<<n)-1
    trees=chronologies=qualified=compatible=0
    star_supports=((2,3),(2,4),(2,5))
    for word in product(range(n),repeat=n-2):
        edges=tree_edges(word,n)
        if not any(set(e)=={0,1} for e in edges):
            continue
        trees+=1
        for order in permutations(edges):
            if set(order[-1])!={0,1}:
                continue
            chronologies+=1
            know=replay(order)
            if know[0]!=full or know[1]!=full:
                continue
            if (know[2]|know[3]|know[4]|know[5])!=full:
                continue
            qualified+=1
            success=all(
                any(know[u] & (1<<s) for u in target_support)
                for s in range(n)
                for target_support in star_supports
            )
            compatible+=success
    actual=(trees,chronologies,qualified,compatible)
    expected=(432,10368,1728,0)
    assert actual==expected,(actual,expected)
    print("PASS six-person labelled tree histories with prescribed final edge:",trees)
    print("PASS all chronological orders preserving that last edge:",chronologies)
    print("PASS complete two corner-singleton + four-cell group covers:",qualified)
    print("PASS incompatible three-leaf star tested, feasible count:",compatible)
    print("LIMIT: finite verification corroborates the all-n last-edge star lemma")


if __name__=="__main__":
    check()
