"""Independent cross-check of exchange obstructions using source-bitset gossip."""
from itertools import combinations, permutations
import random, sys, time
from v04_exchange_obstructions import make_schedule, is_connected_via_arrivals, verify_small

def alternate_gossip(n,seq):
    info=[1<<v for v in range(n)]
    for a,b in seq:
        old_a=info[a]; old_b=info[b]
        info[a]=info[b]=old_a|old_b
    return all(x == (1<<n)-1 for x in info)

def connected_static(n,seq):
    adj=[[] for _ in range(n)]
    for u,v in seq:adj[u].append(v);adj[v].append(u)
    vis={0};todo=[0]
    for u in todo:
        for v in adj[u]:
            if v not in vis: vis.add(v);todo.append(v)
    return len(vis)==n

def run():
    tic=time.monotonic(); rng=random.Random(20261024)
    count=0
    for n in range(3,9):
        base=list(combinations(range(n),2))
        for _ in range(400):
            rng.shuffle(base)
            mask=[rng.random()<0.5 for i in base]
            seq=[x for x,keep in zip(base,mask) if keep]
            assert is_connected_via_arrivals(n,seq)[0] == alternate_gossip(n,seq)
            count+=1
    print('Random independent oracles agree:',count,'cases')
    for d in [3,4,5]:
        n,events,D,_,_ = make_schedule(d)
        H=[e for e in events if e not in D]
        assert connected_static(n,H)
        assert not alternate_gossip(n,H)
        restored=0
        for e in D:
            ev=[edge for edge in events if edge not in D or edge==e]
            assert alternate_gossip(n,ev)
            restored+=1
        print(f'd={d}, n={n}, edges={len(events)}, |D|={len(D)}, single restoration checks={restored}, static complement connected=True, temporal complement connected=False')
    schedule=((0,1),(0,2),(1,3),(0,3),(2,3),(1,2)); n=4
    m=len(schedule);mini={}
    for mask in range(1<<m):
        e=[schedule[i] for i in range(m) if mask & (1<<i)]
        if alternate_gossip(n,e) and all(not alternate_gossip(n,[schedule[j] for j in range(m) if mask & (1<<j) and i!=j]) for i in range(m) if mask&(1<<i)):
            mini.setdefault(mask.bit_count(),e)
    assert sorted(mini)==[4,5]
    print('Non-equicardinal minimal spanners on K4:',mini)
    print('Elapsed:',round(time.monotonic()-tic,3),'sec')
if __name__=='__main__':run()
