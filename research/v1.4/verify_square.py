"""Exhaustive n=13 square-pattern chronological gossip feasibility check.

P0,P1: prefix trees of 5 vertices each; P2: triangle.
Q0,Q1: suffix trees of 5 vertices each; Q2: triangle.
Contact pairs must be distinct in both halves.
"""
from itertools import combinations, permutations

V = [(i,j) for i in range(3) for j in range(3)] + [(0,0),(0,1),(1,0),(1,1)]
N = len(V)
ROWS = [[v for v, (r,c) in enumerate(V) if r==i] for i in range(3)]
COLS = [[v for v, (r,c) in enumerate(V) if c==j] for j in range(3)]

def gossip(edges, initial):
    k=list(initial)
    for a,b in edges:k[a]=k[b]=k[a]|k[b]
    return k

def connected(group, seq):
    parent={i:i for i in group}
    def root(i):
        while i != parent[i]:i=parent[i]
        return i
    for a,b in seq:parent[root(a)] = root(b)
    return len({root(i) for i in group}) == 1

def orders(group, m, collectors=()):
    E=list(combinations(group,2))
    for selected in combinations(E,m):
        if not connected(group,selected): continue
        for seq in permutations(selected):
            if collectors:
                mask=sum(1<<v for v in group)
                state=gossip(seq, [1<<v if v in group else 0 for v in range(N)])
                if any(state[v]!=mask for v in collectors):continue
            yield seq

def masks_for_source(row_id,col_id,prefixes,suffixes):
    source=ROWS[row_id];target=COLS[col_id]
    initial=[1<<v if v in source else 0 for v in range(N)]
    full=sum(initial)
    d=[]
    for pre in prefixes:
        state=gossip(pre,initial)
        pre_edges=set(pre)
        valid=0
        for j,post in enumerate(suffixes):
            if any(edge in pre_edges for edge in post):continue
            end=gossip(post,state)
            if all(end[v]==full for v in target):valid|=1<<j
        d.append(valid)
    return d

def run():
    prefix=[]
    for i in range(3):
        singleton=[v for v in ROWS[i] if sum(V[w][1] == V[v][1] for w in ROWS[i]) == 1]
        prefix.append(list(orders(ROWS[i],len(ROWS[i]) if i==2 else len(ROWS[i])-1,
                                  singleton if i!=2 else ())))
    suffix=[list(orders(COLS[j],len(COLS[j]) if j==2 else len(COLS[j])-1)) for j in range(3)]
    print('row options',list(map(len,prefix)),'col options',list(map(len,suffix)),flush=True)
    assert list(map(len,prefix))==[576,576,6]
    assert list(map(len,suffix))==[3000,3000,6]
    for seq in prefix[2]:
        state=gossip(seq,[1<<v for v in range(N)])
        assert all(state[v] & sum(1<<w for w in ROWS[2]) == sum(1<<w for w in ROWS[2])
                   for v in ROWS[2])
    valid={}
    for c in (0,1):
        p2=masks_for_source(2,c,prefix[2][:1],suffix[c])[0]
        assert p2
        for r in (0,1):
            valid[r,c]=[v & p2 for v in masks_for_source(r,c,prefix[r],suffix[c])]
            print('source',r,'target',c,'feasible rows',sum(bool(v) for v in valid[r,c]),flush=True)
    for i in range(len(prefix[0])):
        if not valid[0,0][i] or not valid[0,1][i]:continue
        for j in range(len(prefix[1])):
            if (valid[0,0][i]&valid[1,0][j]) and (valid[0,1][i]&valid[1,1][j]):
                raise AssertionError(('candidate found! Must direct-verify',i,j))
    print('EXACT_UNSAT square K13 given component and half assumptions',flush=True)

if __name__=='__main__':run()
