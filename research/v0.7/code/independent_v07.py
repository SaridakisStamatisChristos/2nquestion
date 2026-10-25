"""Independent temporal reachability, pivotability, and size-10/11 certificate.
Python >=3.10, standard library; exact elimination-order treewidth for <=7 vertices.
"""
from itertools import combinations, permutations
from collections import Counter

PIVOT=[(3,6),(1,6),(0,6),(5,6),(0,3),(2,6),(4,6),(0,1),(3,5),(0,5),(1,2),(1,5),(0,2),(0,4),(1,3),(2,3),(1,4),(2,5),(4,5),(2,4),(3,4)]
NONPIVOT=[(3,6),(5,6),(4,6),(3,4),(1,4),(0,6),(2,3),(3,5),(0,3),(2,5),(2,4),(1,6),(4,5),(0,5),(1,3),(1,5),(0,4),(2,6),(0,1),(1,2),(0,2)]
n=7

def tc(x):
    xset=set(x)
    for source in range(n):
        r={source}
        for a,b in timeline:
            if (a,b) in xset and (a in r or b in r): r.add(a);r.add(b)
        if len(r)!=n:return False
    return True

def tw(edges):
    best=n
    adj=[set() for _ in range(n)]
    for a,b in edges:adj[a].add(b);adj[b].add(a)
    for order in permutations(range(n)):
        nodes=[set(x) for x in adj]
        alive=set(range(n));width=0
        for v in order:
            nei=nodes[v]&alive
            width=max(width,len(nei))
            if width>=best:break
            for u in nei:nodes[u].update(nei-{u})
            alive.remove(v)
        else:best=min(best,width)
    return best

def pivots(timeline):
    found=[]
    for at,(a,b) in enumerate(timeline):
        early=timeline[:at]
        late=timeline[at+1:]
        # Every source can arrive at at least one endpoint before the pivot.
        gathers=True
        for source in range(n):
            r={source}
            for c,d in early:
                if c in r or d in r:r.add(c);r.add(d)
            if not (a in r or b in r):gathers=False;break
        if not gathers:continue
        # Both endpoints can disseminate information to all vertices after pivot.
        r={a,b}
        for c,d in late:
            if c in r or d in r:r.add(c);r.add(d)
        if len(r)==n:found.append(at+1)
    return found

for name,timeline in [('pivot',PIVOT),('nonpivot',NONPIVOT)]:
    assert len(timeline)==21 and len({tuple(sorted(e)) for e in timeline})==21
    temporal_spanners=[]
    for k in (10,11):
        for indices in combinations(range(21),k):
            x=[timeline[i] for i in indices]
            if tc(x):temporal_spanners.append((k,indices,tw(x)))
        if temporal_spanners:break
    print(name,'pivots at times',pivots(timeline), 'optimal k',temporal_spanners[0][0], 'optimal count',len(temporal_spanners),'treewidths',[row[2] for row in temporal_spanners])
    for k,ids,width in temporal_spanners:
        print('  ',k,[i+1 for i in ids],width)
