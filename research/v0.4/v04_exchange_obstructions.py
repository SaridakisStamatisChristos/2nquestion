"""Standalone temporal edge-deletion dependency constructions with independent checks."""
from itertools import combinations


def is_connected_via_arrivals(n, events):
    """Independent source-specific earliest-arrival dynamic programming."""
    for source in range(n):
        seen = [False] * n
        seen[source] = True
        for u, v in events:
            before_u, before_v = seen[u], seen[v]
            if before_u or before_v:
                seen[u] = seen[v] = True
        if not all(seen):
            return False, source, next(i for i, q in enumerate(seen) if not q)
    return True, None, None


def make_schedule(d):
    """n=2^(d+1) temporal clique and a large inclusion-minimal deletion obstruction.

    Within each side, early and late perfect matchings are bases in (F_2)^d.
    Earliest cross contact remains; every other cross contact belongs to D.
    """
    assert d >= 3
    s = 1 << d
    n = 2 * s
    side = (list(range(s)), list(range(s,2*s)))
    early_basis = [1 << i for i in range(d)]
    late_basis = [(1 << i) | (1 << (i+1)) for i in range(d-1)] + [7]
    assert len(set(early_basis + late_basis)) == 2*d
    # GF(2) rank check
    def rank(vecs):
        pivots = {}
        for v in vecs:
            while v:
                j=v.bit_length()-1
                if j in pivots: v ^= pivots[j]
                else: pivots[j]=v;break
        return len(pivots)
    assert rank(early_basis) == rank(late_basis) == d
    events = [(0, s)]  # unusably early cross edge: keeps ordinary graph connected
    for basis in [early_basis]:
        for delta in basis:
            for offset in [0,s]:
                for x in range(s):
                    y=x^delta
                    if x<y: events.append((offset+x,offset+y))
    deleted = [(x,s+y) for x in range(s) for y in range(s) if (x,s+y)!=(0,s)]
    events.extend(deleted)
    for delta in late_basis:
        for offset in [0,s]:
            for x in range(s):
                y=x^delta
                if x<y: events.append((offset+x,offset+y))
    already = {tuple(sorted(e)) for e in events}
    events.extend((a,b) for a,b in combinations(range(n),2) if (a,b) not in already)
    assert len(events) == n*(n-1)//2 and len(set(tuple(sorted(e)) for e in events))==len(events)
    return n,events,set(deleted),early_basis,late_basis


def verify(d):
    n, seq, D, be, bl = make_schedule(d)
    # all other edges remain; this is the smallest retained subgraph 
    retain = [e for e in seq if e not in D]
    assert not is_connected_via_arrivals(n,retain)[0]
    # complement static graph connected (retained cross edge plus connected half-hypercubes)
    seen={0}
    while True:
        extra={v for u,v in retain if u in seen}|{u for u,v in retain if v in seen}
        new=seen|extra
        if new==seen:break
        seen=new
    assert len(seen)==n
    for e in D:
        ok,s,t=is_connected_via_arrivals(n,[v for v in seq if v not in D or v==e])
        assert ok, (d,e,s,t)
    return {'n':n,'m':len(seq),'obstruction_size':len(D),'early_basis':be,'late_basis':bl,'all_single_edge_reinsertions_pass':True,'complement_static_connected':True,'complement_temporally_connected':False,'unreachable_example':is_connected_via_arrivals(n,retain)[1:]}


def verify_small(n,seq,deleted):
    def r(D):return is_connected_via_arrivals(n,[e for e in seq if e not in D])
    assert not r(deleted)[0]
    for e in deleted:
        assert r(deleted-{e})[0]
    # check static complement
    keep=[e for e in seq if e not in deleted];seen={0}
    while True:
        new=seen|{v for u,v in keep if u in seen}|{u for u,v in keep if v in seen}
        if new==seen:break
        seen=new
    return {'n':n,'obstruction_size':len(deleted),'complement_static_connected':len(seen)==n,'unreachable_example':r(deleted)[1:]}

if __name__=='__main__':
    x4 = [(0,1),(0,2),(0,3),(1,3),(1,2),(2,3)]
    x5 = [(0,1),(0,2),(0,3),(0,4),(1,2),(1,4),(1,3),(2,4),(2,3),(3,4)]
    x6 = [(0,5),(0,4),(4,5),(0,3),(1,2),(1,3),(1,5),(3,4),(0,2),(1,4),(2,5),(2,4),(2,3),(0,1),(3,5)]
    for n,seq,idx in [(4,x4,[4,5]),(5,x5,[6,8,9]),(6,x6,[1,2,3,6,8,10])]:
        assert len(seq)==n*(n-1)//2
        print('SMALL',verify_small(n,seq,{seq[i] for i in idx}))
    for d in [3,4,5]:
        print('FAMILY',verify(d),flush=True)
