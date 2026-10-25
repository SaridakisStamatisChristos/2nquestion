import sys,time,random,collections
sys.path.insert(0,'/mnt/data/temporal_clique_lab')
from temporal_lab import *
for n in [6,7,8,9,10,12]:
    start=time.perf_counter(); rng=random.Random(161803*n);counts=collections.Counter();samples=[]
    for trial in range(500):
        seq=edges_complete(n);rng.shuffle(seq)
        candidates=[greedy(n,seq,i).bit_count() for i in range(8)]
        best=min(candidates);counts[best]+=1
        if best>=2*n-2: samples.append((best,seq))
    print(n,sorted(counts.items()),'hard',len(samples),'time',round(time.perf_counter()-start,2),flush=True)
