"""Primary-source crosscheck for Labahn (1995), Theorem 6.1.

Build each p-grid candidate directly from the published chains and covers.
Compare the independent reachability check for (K2) to the subset-union
admissibility predicate. No dependency on v1.4/5/6/7.
"""
from itertools import permutations

def f(x):
    return frozenset(i for i in range(1,len(x))
                     if set(x[:i])==set(range(1,i+1)))

def inv(x):
    y=[0]*len(x)
    for i,v in enumerate(x,1):y[v-1]=i
    return tuple(y)

def build(p,rho,sigma):
    k=p-2; edges={}
    def add(u,v):
        edges.setdefault(u,set()).add(v)
        edges.setdefault(v,set())
    paths=(
        [('c',0)]+[('a',i) for i in range(1,k+1)]+[('d',p-1)],
        [('c',p-1)]+[('b',i) for i in range(k,0,-1)]+[('d',0)])
    for path in paths:
        for u,v in zip(path,path[1:]):add(u,v)
    add(('c',0),('d',0))
    add(('c',p-1),('d',p-1))
    for i in range(1,k+1):
        add(('c',i),('a',i))
        add(('c',i),('b',rho[i-1]))
        add(('a',i),('d',i))
        add(('b',sigma[i-1]),('d',i))
    return edges

def k2(poset,p):
    for i in range(p):
        seen=set();todo=[('c',i)]
        while todo:
            u=todo.pop()
            if u in seen:continue
            seen.add(u);todo.extend(poset[u]-seen)
        if any(('d',j) not in seen for j in range(p)):
            return False
    return True

def run():
    grand_total=0
    grand_valid=0
    for p in range(3,8):
        k=p-2
        all_perms=permutations(range(1,k+1))
        rhos=[r for r in all_perms if all(x>=i-1 for i,x in enumerate(r,1))]
        sigmas=[s for s in permutations(range(1,k+1))
                if all(x<=i+1 for i,x in enumerate(s,1))]
        valid=0;total=0
        for rho in rhos:
            for sig in sigmas:
                total+=1
                P=build(p,rho,sig)
                accepted=k2(P,p)
                expected=(f(rho)|f(inv(sig))==frozenset(range(1,k)))
                assert accepted==expected,(p,rho,sig)
                if accepted:
                    valid+=1
                    assert len(P)==4*p-4
                    indeg={v:0 for v in P}
                    for u,following in P.items():
                        assert len(following)<=2
                        for v in following:indeg[v]+=1
                    assert max(indeg.values())<=2
                    assert {u for u in P if indeg[u]==0}=={('c',j) for j in range(p)}
                    assert {u for u in P if not P[u]}=={('d',j) for j in range(p)}
        assert total==4**(p-3),(p,total)
        assert valid==3**(p-3),(p,valid)
        grand_total+=total
        grand_valid+=valid
        print("PASS: p=%d, candidate pairs=%d, admissible=%d"%(p,total,valid))
    assert grand_total==341 and grand_valid==121
    print("PASS: 341 independently checked ordered permutation pairs, 121 admissible")

if __name__=="__main__":run()
