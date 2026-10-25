import random,sys,time,collections
sys.path.insert(0,'/mnt/data/temporal_clique_lab')
from temporal_lab import *
from nonpivot import pivot_edges
for n, trials in [(6,200000),(7,100000),(8,100000),(9,100000)]:
 rng=random.Random(20261024+n)
 nonpivot=0; upper=collections.Counter(); suspects=[]
 tt=time.perf_counter()
 for j in range(trials):
  seq=edges_complete(n);rng.shuffle(seq)
  if not pivot_edges(n,seq):
   nonpivot+=1
   best=min(greedy(n,seq,k).bit_count() for k in range(12))
   upper[best]+=1
   if best>2*n-4:suspects.append(seq)
 print('n',n,'trials',trials,'nonpivot',nonpivot,'greedy',dict(upper),'suspects',len(suspects),'time',round(time.perf_counter()-tt,2),flush=True)
 if suspects:print('hard example:',suspects[0],flush=True)
