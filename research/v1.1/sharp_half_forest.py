"""Standalone exact certificate for a sharp first/last-half structural obstruction.

The schedule is a list of distinct contacts, with n=8 and 2n-4=12 calls.
No external dependencies. Intended for independent audit.
"""
from itertools import combinations
from collections import Counter

SEQUENCE = [
    (0,1), (4,5), (3,7), (2,6), (2,3), (1,5),
    (0,4), (1,2), (6,7), (4,6), (3,5), (0,7),
]

def gossip(n, seq):
    known = [1 << i for i in range(n)]
    for a,b in seq:
        union = known[a] | known[b]
        known[a] = known[b] = union
    return known

def components_and_cycles(n, seq):
    parent = list(range(n))
    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v
    cyclerank=0
    for a,b in seq:
        x,y=root(a),root(b)
        if x==y:
            cyclerank+=1
        else:
            parent[x]=y
    groups={}
    for v in range(n):
        groups.setdefault(root(v),[]).append(v)
    return sorted(tuple(g) for g in groups.values()),cyclerank

def butterfly_count(n,seq):
    pos={tuple(sorted(e)):i for i,e in enumerate(seq)}
    num=0
    for a,b,c,d in combinations(range(n),4):
        cycles=[((a,b),(b,c),(c,d),(d,a)),((a,b),(b,d),(d,c),(c,a)),((a,c),(c,b),(b,d),(d,a))]
        for cy in cycles:
            if all(tuple(sorted(e)) in pos for e in cy):
                z=[pos[tuple(sorted(e))] for e in cy]
                if max(z[0],z[2])<min(z[1],z[3]) or max(z[1],z[3])<min(z[0],z[2]):
                    num+=1
    return num

def extend(seq, n, u=0, v=1):
    """Extend shortest n-gossip to (n+1)-gossip in two new distinct contacts."""
    assert u!=v and u<n and v<n
    return [(n,u)]+list(seq)+[(n,v)]

def verify(n, seq, desired_cycle=True):
    assert len(seq)==2*n-4
    assert len({tuple(sorted(e)) for e in seq})==len(seq)
    assert all(0<=a<n and 0<=b<n and a!=b for a,b in seq)
    assert all(x==(1<<n)-1 for x in gossip(n,seq))
    left,lcycle=components_and_cycles(n,seq[:n-2]);right,rcycle=components_and_cycles(n,seq[n-2:])
    assert len(left)>=2 and len(right)>=2
    assert all(set(a)&set(b) for a in left for b in right)
    if desired_cycle:assert rcycle>=1
    return {'n':n,'calls':len(seq),'first_half_components':left,'last_half_components':right,
            'first_half_cycle_rank':lcycle,'last_half_cycle_rank':rcycle,
            'butterflies':butterfly_count(n,seq)}

if __name__=='__main__':
    import json
    for n in range(8,25):
        if n==8:s=SEQUENCE
        else:s=extend(s,n-1)
        proof=verify(n,s)
        if n in (8,9,12,16,24):print(json.dumps(proof))
    # chronology reversal preserves gossip and exchanges half-positions
    assert verify(8,list(reversed(SEQUENCE)),desired_cycle=False)['first_half_cycle_rank']==1
    print('PASS: n=8..24 extension and reversal independently checked')
