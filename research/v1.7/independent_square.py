"""Independent, local-order exact n=13 exceptional-grid refutation."""
from itertools import combinations,permutations
V=[(i,j) for i in range(3) for j in range(3)]+[(0,0),(0,1),(1,0),(1,1)]
N=len(V)
R=[tuple(i for i,(r,c) in enumerate(V) if r==j) for j in range(3)]
C=[tuple(i for i,(r,c) in enumerate(V) if c==j) for j in range(3)]
def transfer(seq,starting):
    a=list(starting)
    for u,v in seq:
        x=a[u]|a[v];a[u]=x;a[v]=x
    return a
def tree_orders(group):
    for chosen in combinations(tuple(combinations(group,2)),4):
        parent={i:i for i in group}
        def root(i):
            while i!=parent[i]:i=parent[i]
            return i
        for u,v in chosen:parent[root(u)]=root(v)
        if len({root(v) for v in group})!=1:continue
        yield from permutations(chosen)
def prefix_orders(row):
    group=R[row];entry=next(v for v in group if V[v][1]==2)
    required=sum(1<<v for v in group)
    for seq in tree_orders(group):
        initial=[1<<v for v in range(N)]
        if transfer(seq,initial)[entry]==required:yield seq
def suffix_orders(column):
    group=C[column];src=next(v for v in group if V[v][0]==2)
    for seq in tree_orders(group):
        ini=[0]*N;ini[src]=1
        if all(transfer(seq,ini)[v]==1 for v in group):yield seq
def option_mask(r,c,prefix,suffix):
    begin=[0]*N
    for v in R[r]:begin[v]=1<<v
    needed=sum(begin);state=transfer(prefix,begin)
    used={frozenset(x) for x in prefix}
    valid=0
    for i,post in enumerate(suffix):
        if any(frozenset(x) in used for x in post):continue
        final=transfer(post,state)
        if all(final[v]==needed for v in C[c]):valid |=1<<i
    return valid
def run():
    pref=[list(prefix_orders(i)) for i in (0,1)]
    suff=[list(suffix_orders(i)) for i in (0,1)]
    assert list(map(len,pref))==[576,576]
    assert list(map(len,suff))==[576,576]
    masks={}
    for r in (0,1):
        for c in (0,1):
            masks[r,c]=[option_mask(r,c,seq,suff[c]) for seq in pref[r]]
            assert sum(bool(x) for x in masks[r,c])==288
    for r in (0,1):
        shared=sum(bool(masks[r,0][i] and masks[r,1][i]) for i in range(576))
        assert shared==0, (r,shared)
        print("row",r,"prefixes working independently for both columns:",shared)
    print("PASS: independent exact UNSAT for n=13 square exceptional configuration")
if __name__=="__main__":run()
