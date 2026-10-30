"""Stage 20 chronological-tree falsifier and sharpness boundary.

All labelled chronological trees n4..6, with disjoint groups {root},{h},
{p,q} each complete. Falsify an extra complete fourth group of size <=2.
This checks the finite core of the all-n root-cut proof, not full gossip.
"""
from itertools import combinations, permutations, product
from functools import reduce

def prufer(code, n):
    d = [1] * n
    for v in code: d[v] += 1
    edges = []
    for v in code:
        leaf = next(i for i in range(n) if d[i] == 1)
        edges.append((leaf,v))
        d[leaf] -= 1
        d[v] -= 1
    edges.append(tuple(i for i in range(n) if d[i] == 1))
    return edges

def replay(n, calls):
    knowledge = [1 << i for i in range(n)]
    used = set()
    for a,b in calls:
        edge = tuple(sorted((a,b)))
        assert a != b and edge not in used
        used.add(edge)
        knowledge[a] = knowledge[b] = knowledge[a] | knowledge[b]
    return knowledge

def covered(knowledge, group):
    return reduce(int.__or__, (knowledge[i] for i in group), 0) == (1 << len(knowledge)) - 1

def small_falsification():
    result = {}
    for n in (4,5,6):
        seen = 0
        for code in product(range(n), repeat=n-2):
            for chronology in permutations(prufer(code,n)):
                know = replay(n,chronology)
                complete = [i for i in range(n) if know[i] == (1 << n) - 1]
                for root in complete:
                    for h in complete:
                        if h == root: continue
                        rem = [i for i in range(n) if i not in (root,h)]
                        for pair in combinations(rem, 2):
                            if not covered(know,pair): continue
                            seen += 1
                            extras = [i for i in rem if i not in pair]
                            for length in (1,2):
                                for e in combinations(extras,length):
                                    assert not covered(know,e), (
                                        n,chronology,root,h,pair,e)
        result[n] = seen
    assert result == {4:48,5:1440,6:51840}, result
    print("PASS ordered n4,n5,n6 trees:", result)
    print("PASS no fourth disjoint complete-cover group of size <=2")

def sharp(groups, start=0):
    if len(groups) == 1:
        return [(start,groups[0])],[],start+1,start
    if len(groups) == 2:
        return [(start,groups[0]),(start+1,groups[1])],[(start,start+1)],start+2,start
    L,a,m,u = sharp([groups[0]]+groups[2:], start)
    R,b,end,v = sharp([groups[1]]+groups[2:], m)
    return L+R,a+b+[(u,v)],end,u

def explicit_regressions():
    marks,calls,n,root=sharp(list(range(4)))
    know=replay(n,calls)
    groups=[[v for v,m in marks if m==i] for i in range(4)]
    assert (n,len(calls)) == (8,7)
    assert sorted(map(len,groups)) == [1,1,2,4]
    assert all(covered(know,g) for g in groups)
    assert know[root] == 255
    print("PASS sharp 8-person tree with four complete groups")
    # This locally refutes inferring four causally sealed arms from
    # two disjoint 2-person collective complete groups.
    calls=((0,1),(2,0),(3,0),(1,4))
    masks=replay(5,calls)
    assert masks == [15,19,7,15,19]
    assert covered(masks,(0,1)) and covered(masks,(3,4))
    assert all(z != 31 for z in masks)
    # root (0) calls root (1) BEFORE its own arm-internal (2,0).
    print("PASS five-person original-order falsifier to naive four-arm inference")

if __name__ == "__main__":
    small_falsification()
    explicit_regressions()
    print("LIMIT: no global 2n-4 both-cyclic schedule is constructed")
