from temporal_lab import edges_complete,is_spanner
from itertools import permutations
from collections import Counter
for n in (4,5):
 m=n*(n-1)//2
 for it,seq in enumerate(permutations(edges_complete(n))):
  goods=[]
  for mask in range(1<<m):
   if is_spanner(n,seq,mask) and all(not is_spanner(n,seq,mask^(1<<i)) for i in range(m) if mask>>i&1):goods.append(mask)
  counts=Counter(g.bit_count() for g in goods)
  if len(counts)>1:
   print('found n',n,'i',it,'schedule',seq,'minimal_sizes',counts,'examples',[(k,[[seq[i] for i in range(m) if mask>>i &1] for mask in goods if mask.bit_count()==k][0]) for k in sorted(counts)]);break
  if n==5 and it>=5000:break
 else:print('no found n',n)
