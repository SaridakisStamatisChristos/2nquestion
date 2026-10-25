"""Exact bridge audit: event-poset linear extensions vs chronological halves.

Enumerates all linear extensions of the 8-vertex example, extends two
contrasting extensions to 13 vertices, and checks Labahn's necessary kernel
cardinality equalities on EVERY optimal distinct-edge K4/K5 chronology.

Not a complete Labahn p-grid classifier (not all old admissibility rules
are available in the public reconstruction).
"""
from collections import Counter
from itertools import combinations, permutations
import json

W8=((0,1),(4,5),(3,7),(2,6),(2,3),(1,5),
    (0,4),(1,2),(6,7),(4,6),(3,5),(0,7))


def edge(e):
    return tuple(sorted(e))


def gossip(n, s):
    info=[1<<i for i in range(n)]
    for a,b in s:
        info[a]=info[b]=info[a]|info[b]
    return all(x==(1<<n)-1 for x in info)


def cyclerank(n, s):
    p=list(range(n));cycle=0
    def rt(x):
        while p[x]!=x:x=p[x]
        return x
    for a,b in s:
        x,y=rt(a),rt(b)
        if x==y:cycle+=1
        else:p[x]=y
    return cycle


def incident_orders(n,s):
    return tuple(tuple(edge(e) for e in s if v in e)
                 for v in range(n))


def pred(s):
    seen={};out=[]
    for i,(a,b) in enumerate(s):
        bits=0
        for v in (a,b):
            if v in seen:bits|=1<<seen[v]
            seen[v]=i
        out.append(bits)
    return out


def reaches(s):
    m=len(s);reach=[0]*m;vertices=[0]*m
    for i in range(m-1,-1,-1):
        a,b=s[i];mask=1<<i;v=(1<<a)|(1<<b)
        for j in range(i+1,m):
            if a in s[j] or b in s[j]:
                mask|=reach[j];v|=vertices[j]
        reach[i]=mask;vertices[i]=v
    return reach,vertices


def poset(s):
    reach,_=reaches(s)
    return {edge(s[i]):tuple(sorted(edge(s[j]) for j in range(len(s))
                      if (reach[i]>>j)&1))
            for i in range(len(s))}


def kernel(n,s):
    R,V=reaches(s);m=len(s)
    I={i for i in range(m) if V[i]==(1<<n)-1}
    Imax={i for i in I if not any(j!=i and (R[i]>>j)&1 for j in I)}
    F={i for i in range(m) if all((R[j]>>i)&1 for j in I)}
    Fmin={i for i in F if not any(j!=i and (R[j]>>i)&1 for j in F)}
    K=set(range(m))-(I-Imax)-(F-Fmin)
    return {'kappa_initial':len(Imax),'kappa_final':len(Fmin),
            'kernel_contacts':len(K)}


def extensions(n,seq):
    m=len(seq);deps=pred(seq);full=(1<<m)-1
    histogram=Counter();examples={};total=0
    def dfs(mask,ids):
        nonlocal total
        if mask==full:
            s=tuple(seq[i] for i in ids)
            assert gossip(n,s)
            key=(cyclerank(n,s[:n-2]),cyclerank(n,s[n-2:]))
            histogram[key]+=1;examples.setdefault(key,s);total+=1
            return
        for i in range(m):
            if not(mask>>i&1) and (deps[i]&mask)==deps[i]:
                dfs(mask|(1<<i),ids+(i,))
    dfs(0,())
    return histogram,examples,total


def extend_to(s,n):
    current=1+max(max(e) for e in s)
    while current<n:
        s=((current,0),)+tuple(s)+((current,1),)
        current+=1
    return tuple(s)


def run():
    assert gossip(8,W8) and len(set(map(edge,W8)))==12
    hist,examples,count=extensions(8,W8)
    assert dict(hist)=={(0,0):12800,(0,1):19200,(1,0):19200}
    assert count==51200
    A,B=examples[(0,1)],examples[(0,0)]
    assert incident_orders(8,A)==incident_orders(8,B)==incident_orders(8,W8)
    assert poset(A)==poset(B)==poset(W8)
    for n in range(8,14):
        a,b=extend_to(A,n),extend_to(B,n)
        assert len(a)==len(b)==2*n-4 and gossip(n,a) and gossip(n,b)
        assert len(set(map(edge,a)))==len(a)
        assert len(set(map(edge,b)))==len(b)
        assert incident_orders(n,a)==incident_orders(n,b)
        assert poset(a)==poset(b)
        assert (cyclerank(n,a[:n-2]),cyclerank(n,a[n-2:]))==(0,1)
        assert (cyclerank(n,b[:n-2]),cyclerank(n,b[n-2:]))==(0,0)
        assert kernel(n,a)==kernel(n,b)
    checked={}
    for n in (4,5):
        E=list(combinations(range(n),2));success=0
        for s in permutations(E,2*n-4):
            if not gossip(n,s):continue
            k=kernel(n,s);success+=1
            assert k['kappa_initial']==k['kappa_final']
            assert k['kernel_contacts']==4*k['kappa_initial']-4
        checked[n]=success
    assert checked=={4:24,5:3240}
    result={'n8_linear_extensions':count,
            'histogram':{str(k):v for k,v in sorted(hist.items())},
            'n13_schedule_A':[list(e) for e in extend_to(A,13)],
            'n13_schedule_B':[list(e) for e in extend_to(B,13)],
            'n13_half_cycles_A':[0,1], 'n13_half_cycles_B':[0,0],
            'same_n13_minimal_order':True,
            'k4_k5_exhaustive_success_counts':checked,
            'novelty_conclusion':'No equivalence/novelty claim: kernel order alone does not determine one chronological midpoint split.'}
    print(json.dumps(result,indent=2))
    return result


if __name__=='__main__':
    run()
