from temporal_lab import edges_complete,is_spanner
from collections import Counter
import random

def circs(n,seq):
 m=len(seq); F=(1<<m)-1
 ok=[is_spanner(n,seq,F^d) for d in range(1<<m)]
 rank=0;count=Counter();samples={}
 for d in range(1,1<<m):
  if ok[d]:continue
  # if all 1-removals are good then no smaller subset bad by upward-closed badness
  if all(ok[d^(1<<i)] for i in range(m) if d>>i&1):
   r=d.bit_count();count[r]+=1
   if r>rank:rank=r
   samples.setdefault(r,[seq,[seq[i] for i in range(m) if d>>i&1]])
 return rank,count,samples

if __name__=='__main__':
 for n,trial in [(4,720),(5,350),(6,25)]:
  if n==6:trial=5
  base=edges_complete(n);rng=random.Random(2026+n)
  hi=0
  for k in range(trial):
   seq=base[:] ; rng.shuffle(seq)
   r,c,s=circs(n,seq)
   if r>hi:
    print('NEW max',n,k,r,s[r],flush=True)
    hi=r
  print('sample',n,k,r,c if k==0 else '',flush=True) if k==0 else None
