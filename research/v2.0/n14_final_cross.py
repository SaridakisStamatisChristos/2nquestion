"""Independent exact chronology obstruction for the final n14 incidence orbit."""
from itertools import combinations,permutations
M=((1,1,2),(1,2,2),(2,2,1))
V=tuple((r,c) for r in range(3) for c in range(3) for _ in range(M[r][c]))
N=len(V);P=tuple(v for v in range(N) if V[v][0]==1)
Q=tuple(v for v in range(N) if V[v][1]==2)
def connect(group,edges):
    p={v:v for v in group}
    def rt(x):
        while p[x]!=x:x=p[x]
        return x
    for x,y in edges:p[rt(x)]=rt(y)
    return len({rt(v) for v in group})==1
def gossip(orders,initial):
    z=list(initial)
    for x,y in orders:z[x]=z[y]=z[x]|z[y]
    return z
def orders(group,part,cyc,need,reverse):
    init=[0]*N
    for i,v in enumerate(group):init[v]=1<<i
    full=(1<<len(group))-1
    out=[]
    for E in combinations(tuple(combinations(group,2)),len(group)-1+cyc):
        if not connect(group,E):continue
        for seq in permutations(E):
            s=gossip(seq[::-1] if reverse else seq,init)
            okay=True
            for k in range(3):
                cell=[v for v in group if part(v)==k]
                union=0;complete=0
                for v in cell:union|=s[v];complete+=(s[v]==full)
                if union!=full or complete<need[k]:okay=False;break
            if okay:out.append(seq)
    return out
def run():
    pre=orders(P,lambda v:V[v][1],0,(1,1,0),False)
    post=orders(Q,lambda v:V[v][0],1,(2,1,1),True)
    assert (len(pre),len(post))==(48,288)
    start=[0]*N
    for i,v in enumerate(P):start[v]=1<<i
    clash=failed=valid=0
    for x in pre:
        state=gossip(x,start);ed={frozenset(e) for e in x}
        for y in post:
            if any(frozenset(e) in ed for e in y):clash+=1;continue
            out=gossip(y,state)
            if all(out[v]==31 for v in Q):valid+=1
            else:failed+=1
    assert (clash,failed,valid)==(0,13824,0)
    print('PASS n14 residual: 48 x 288 = 13824 pairs; all information-infeasible')
if __name__=='__main__':run()
