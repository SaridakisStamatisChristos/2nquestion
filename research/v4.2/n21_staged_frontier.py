"""Stage 25 conservative n20/n21 ORIGINAL-chronology incidence necessary conditions.

All 9-cell matrices enumerated; unknown tree group privacy classes contribute ZERO.
Does NOT enumerate globally successful gossip schedules or prove n21 half-forest.
"""
from collections import Counter
from itertools import permutations
from math import comb

BASE = (1,1,2,1,1,2,2,2,1)
EXACT_PRIVATE = {
    (1,1,2):2,(1,1,3):2,(1,1,4):1,(1,1,5):1,
    (2,1,2):2,(1,2,2):2,(2,1,3):2,(1,2,3):2,
    (1,2,4):1,(2,1,4):1,(1,3,2):2,(3,1,2):2,
    (1,3,3):2,(3,1,3):2,(2,2,2):2,(2,2,3):2,
}

def composition(n,s):
    if s == 1:
        yield (n,)
        return
    for v in range(n+1):
        for rest in composition(n-v,s-1):
            yield (v,)+rest

def canonical(m):
    variants=[]
    for rr in permutations((0,1)):
        for cc in permutations((0,1)):
            z=[]
            for i in range(3):
                for j in range(3):
                    row=rr[i] if i<2 else 2
                    col=cc[j] if j<2 else 2
                    z.append(m[3*row+col])
            variants.append(tuple(z))
    return min(variants)

def private(m):
    f=lambda a,b,c: EXACT_PRIVATE.get((a,b,c),0)
    q=(f(m[0],m[1],m[2]),f(m[3],m[4],m[5]))
    p=(f(m[0],m[3],m[6]),f(m[1],m[4],m[7]))
    return q,p

def three_outside(cell_sizes,private_minima):
    a,b=cell_sizes
    x,y=private_minima
    return ((a<=3 and x>=2 and b<=6 and y>=1) or
            (b<=3 and y>=2 and a<=6 and x>=1))

def classify(m):
    p=m[2]+m[5]-4
    q=m[6]+m[7]-4
    d=m[8]-1
    # Exact globally necessary lower bounds for both cyclic components.
    if p+d<4 or q+d<4:return "component"
    # At n<=42 a (2,2) off-corner pair is impossible.
    if p==0 or q==0:return "saturated"
    q_priv,p_priv=private(m)
    # Four complete outsiders would force nine center vertices.
    if sum(q_priv)>=4 or sum(p_priv)>=4:return "privacy4"
    # Combined Stage23 + Stage24: exactly 3 outside collectors, no center.
    q3=three_outside((m[2],m[5]),q_priv)
    p3=three_outside((m[6],m[7]),p_priv)
    if m[8]<=5 and q3 and p3:return "dual3"
    # Single center vertex must be complete on BOTH cyclic sides.
    if m[8]==1 and (q3 or p3):return "singleton4"
    # Width-two crossing with zero complete central collectors on one side
    # forces BOTH center people complete on the other. Stage20 generalized
    # root-cut requires >=10 total off-corner vertices on THAT other side.
    if m[8]==2:
        if q3 and m[6]+m[7]<10:return "binary_rootcut"
        if p3 and m[2]+m[5]<10:return "binary_rootcut"
    return "survive"

def direct(n):
    counters=Counter()
    survivors=[]
    for xs in composition(n-13,9):
        m=tuple(v+d for v,d in zip(BASE,xs))
        label=classify(m)
        counters[label]+=1
        if label=="survive":survivors.append(m)
    return counters,survivors

def independent_baseline(n):
    # Alternative arithmetic enumeration in aggregated p/q/d coordinates.
    k=n-13
    component=non_saturated=0
    for p in range(k+1):
        for q in range(k-p+1):
            for d in range(k-p-q+1):
                if p+d<4 or q+d<4:continue
                ways=(p+1)*(q+1)*comb(k-p-q-d+3,3)
                component+=ways
                if p>0 and q>0:non_saturated+=ways
    return component,non_saturated

def run():
    for n in (20,21):
        counts,remaining=direct(n)
        component=sum(v for key,v in counts.items() if key!="component")
        non_saturated=component-counts["saturated"]
        assert (component,non_saturated)==independent_baseline(n)
        assert sum(counts.values())==comb(n-13+8,8)
        if n==20:
            assert (component,non_saturated)==(354,221)
            assert counts["privacy4"]==169
            assert counts["dual3"]==52
            assert remaining==[]
        if n==21:
            assert (component,non_saturated)==(1200,850)
            assert counts["privacy4"]==529
            assert counts["dual3"]==184
            assert counts["singleton4"]==12
            assert counts["binary_rootcut"]==48
            assert len(remaining)==77
            assert len({canonical(m) for m in remaining})==22
            assert Counter(m[8] for m in remaining)=={1:9,2:4,3:48,4:16}
        print("PASS n=",n,"raw=",sum(counts.values()),
              "component=",component,"nonsaturated=",non_saturated,
              "gates=",dict(counts),"survivors=",len(remaining),
              "orbits=",len({canonical(m) for m in remaining}))
    print("PASS all unknown n8+ tree privacy classes are assigned minimum ZERO")
    print("LIMIT: size-only necessary matrices, not actual 2n-4-call schedules")

if __name__=="__main__":run()
