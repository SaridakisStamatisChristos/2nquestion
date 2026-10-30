"""Independent, source-wise reachability and butterfly verifier for finite gossip cores."""
from itertools import combinations, permutations
import random

def connected_dfs(n, seq):
    for source in range(n):
        reached={source}
        for a,b in seq:
            a_old=a in reached; b_old=b in reached
            if a_old or b_old:reached.update((a,b))
        if len(reached)<n:return False
    return True

def four_cycle_core(seq):
    n=max(max(a,b) for a,b in seq)+1
    for a,b,c,d in combinations(range(n),4):
        for cyc in (((a,b),(b,c),(c,d),(d,a)),((a,b),(b,d),(d,c),(c,a)),((a,c),(c,b),(b,d),(d,a))):
            # Independent orientation-normalized edge/position lookup
            times={frozenset(pair):t for t,pair in enumerate(seq)}
            if not all(frozenset(e) in times for e in cyc):continue
            chrono=sorted((times[frozenset(e)],set(e)) for e in cyc)
            if chrono[0][1].isdisjoint(chrono[1][1]) and chrono[2][1].isdisjoint(chrono[3][1]):
                return True
    return False

def main():
    all_e=list(combinations(range(5),2))
    valid=0
    for remaining in permutations([e for e in all_e if e!=(0,1)],5):
        seq=[(0,1)]+list(remaining)
        if connected_dfs(5,seq):
            valid+=1
            assert four_cycle_core(seq)
    assert valid==324,(valid,324)
    print('K5 independently checked: 15,120 orders, 324 optimum gossip schedules, 0 butterfly-free')
    rng=random.Random(20261025)
    # Differential test of independent oracle versus bitset implementation.
    def bitset_oracle(n, edges, chosen):
        knowledge=[1<<v for v in range(n)]
        for i,(u,v) in enumerate(edges):
            if i not in chosen:continue
            combined=knowledge[u]|knowledge[v]
            knowledge[u]=knowledge[v]=combined
        return all(k==(1<<n)-1 for k in knowledge)
    for n in range(4,12):
        edges=list(combinations(range(n),2))
        for _ in range(1000):
            rng.shuffle(edges)
            k=rng.randrange(0,len(edges)+1)
            subset=rng.sample(range(len(edges)),k)
            sample=[edges[i] for i in sorted(subset)]
            assert connected_dfs(n,sample)==bitset_oracle(n,edges,set(subset))
    print('8,000 independent source-wise/bitset reachability differential tests passed')

if __name__=='__main__':main()
