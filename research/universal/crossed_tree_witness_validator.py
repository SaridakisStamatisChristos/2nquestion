"""Exact original-order crossed-tree witness verifier. Run with JSON path or --selftest."""
import json
import sys

def replay(tree):
    V=list(map(str,tree["vertices"]))
    assert V and len(V)==len(set(V))
    E=[(str(a),str(b)) for a,b in tree["calls"]]
    assert len(E)==len(V)-1
    idx={v:i for i,v in enumerate(V)}
    parent=list(range(len(V)))
    def root(i):
        while parent[i]!=i:i=parent[i]
        return i
    info={v:1<<i for i,v in enumerate(V)}
    used=set()
    for a,b in E:
        assert a in idx and b in idx and a!=b
        e=frozenset((a,b))
        assert e not in used
        used.add(e)
        ra,rb=root(idx[a]),root(idx[b])
        assert ra!=rb
        parent[ra]=rb
        info[a]=info[b]=info[a]|info[b]
    assert len({root(i) for i in range(len(V))})==1
    return V,E,info

def verify(data):
    T=replay(data["T"]);U=replay(data["U"])
    X=set(T[0])&set(U[0])
    assert X
    def supports(tree):
        V,E,info=tree
        assert E
        a,b=E[-1]
        assert a not in X and b not in X
        assert info[a]==info[b]==(1<<len(V))-1
        out=[]
        for j,v in enumerate(V):
            S={x for x in X if (info[x]>>j)&1}
            assert len(S)>=2,("double coverage",v,S)
            out.append((v,S))
        return out
    A=supports(T);B=supports(U)
    for a,sa in A:
        for b,sb in B:
            assert sa&sb,("crossing",a,b,sa,sb)
    return {"center_size":len(X),"cross_pairs":len(A)*len(B)}

def selftest():
    t={"vertices":[0,1,2,3],"calls":[[0,1],[2,3],[1,2]]}
    V,E,K=replay(t)
    assert K["1"]==K["2"]==15 and K["0"]==3 and K["3"]==12
    try:verify({"T":t,"U":t})
    except AssertionError:pass
    else:raise AssertionError("invalid crossed witness accepted")
    print("PASS exact chronology and negative witness selftest")

if __name__=="__main__":
    if len(sys.argv)==2 and sys.argv[1]=="--selftest":selftest()
    elif len(sys.argv)==2:
        with open(sys.argv[1],encoding="utf8") as f:
            print(json.dumps(verify(json.load(f)),sort_keys=True))
    else:raise SystemExit("usage: validator.py --selftest|witness.json")
