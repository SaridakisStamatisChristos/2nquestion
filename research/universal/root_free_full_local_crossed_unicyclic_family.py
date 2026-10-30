"""All-width pair of root-free cyclic histories crossing in X, each with q2 A/B/X.

LOCAL original/reverse component pair only; not full 3x3 successful gossip.
"""


def sharp(s):
    if s == 1:
        return 1, [], [{0}]
    n, E, G = sharp(s-1)
    H = [{next(iter(G[0]))}, {next(iter(G[0]))+n}]
    H += [G[i] | {v+n for v in G[i]} for i in range(1,s-1)]
    return 2*n, E + [(a+n,b+n) for a,b in E]+[(next(iter(G[0])),next(iter(G[0]))+n)], H


def family(k):
    assert isinstance(k,int) and k>=0
    n,E,G=sharp(6)
    assert n==32 and list(map(len,G)) == [1,1,2,4,8,16]
    centers={0,1,2,3}
    extra=set(range(124,124+k))
    X=centers|extra
    def make(kind):
        vnext=4 if kind=='P' else 64
        maps=[]
        owners={}
        for arm in (0,1):
            if kind=='P':
                endpoints=(2*arm,2*arm+1)
            else:
                endpoints=(arm,arm+2)
            mapping={next(iter(G[0])):endpoints[0],next(iter(G[1])):endpoints[1]}
            for old in range(n):
                if old not in mapping:
                    mapping[old]=vnext
                    vnext+=1
            for old, new in mapping.items():
                owners[new]=arm
            maps.append(mapping)
        assert vnext == (64 if kind=='P' else 124)
        A=set()
        B=set()
        for m in maps:
            A|={m[v] for v in G[2]|G[3]}
            B|={m[v] for v in G[4]|G[5]}
        C=[]
        for arm,m in enumerate(maps):
            if arm==0:
                r=(0 if kind=='P' else 2)
                C.extend((r,w) for w in sorted(extra))
            C.extend((m[a],m[b]) for a,b in E)
        e0=maps[0][min(G[4])]
        e1=maps[1][min(G[4])]
        a0=maps[0][min(G[2])]
        b1=maps[1][min(G[5])]
        assert len({e0,e1,a0,b1})==4
        C.append((e0,e1))  # nonfull--nonfull spanning-tree join
        C.append((a0,b1))  # A-to-B last static cycle edge
        for w in extra:
            owners[w]=0
        return A,B,C,owners
    A,B,P,pr=make('P')
    C,D,Q,qr=make('Q')
    assert (A|B)&(C|D)==set()
    assert (A|B|X)&(C|D|X)==X
    return X, (A,B,P,pr), (C,D,Q,qr)


def exact(V,calls):
    K={v:{v} for v in V}
    for a,b in calls:
        both=K[a]|K[b]
        K[a]=K[b]=both
    return K


def topology(V, calls):
    assert len(calls)==len(V)
    e=[frozenset(t) for t in calls]
    assert len(set(e))==len(e)
    parent={v:v for v in V}
    def root(v):
        while parent[v]!=v:
            v=parent[v]
        return v
    for a,b in calls[:-1]:
        ra,rb=root(a),root(b)
        assert ra!=rb
        parent[ra]=rb
    assert len({root(v) for v in V})==1
    assert e[-1] not in e[:-1]


def check(k):
    X,(A,B,P,pr),(C,D,Q,qr)=family(k)
    VP=A|B|X
    VQ=C|D|X
    assert len(VP)==len(VQ)==64+k
    assert len(A)==len(C)==12 and len(B)==len(D)==48
    topology(VP,P)
    topology(VQ,Q)
    assert {frozenset(e) for e in P}.isdisjoint(frozenset(e) for e in Q)
    assert P[-1][0] in A and P[-1][1] in B
    assert Q[-1][0] in C and Q[-1][1] in D
    kp0=exact(VP,P[:-1]); kp=exact(VP,P)
    kq0=exact(VQ,Q[:-1]); kq=exact(VQ,Q)
    for x in X:
        assert kp[x]==kp0[x] and kq[x]==kq0[x]
    for v in VP:
        assert kp[v]!=VP and kp0[v]!=VP
        assert all(sum(v in kp[x] for x in H)>=2 for H in (A,B,X))
        assert {2*pr[v],2*pr[v]+1}<={x for x in X if v in kp[x]}
    for v in VQ:
        assert kq[v]!=VQ and kq0[v]!=VQ
        assert all(sum(v in kq[x] for x in H)>=2 for H in (C,D,X))
        assert {qr[v],qr[v]+2}<={x for x in X if v in kq[x]}
    # Every row source crosses every column source AT THEIR CELL HUB.
    for u in VP:
        for v in VQ:
            z=2*pr[u]+qr[v]
            assert z in X and u in kp[z] and v in kq[z]
    return len(X),len(VP)*len(VQ)


def main():
    total=0
    for k in (0,1,2,4,8,16,32,64):
        width,pairs=check(k)
        total+=pairs
    print('PASS 8 full-local root-free crossed q2 A/B/X cyclic pairs; max center=68, total cross pairs=',total)


if __name__=='__main__':
    main()
