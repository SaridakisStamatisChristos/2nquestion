from temporal_lab import edges_complete, temporal_reach,is_spanner
from itertools import permutations,combinations
import random,collections

def analyze(n,seq):
 m=len(seq); allmask=(1<<m)-1
 redundant=[i for i in range(m) if is_spanner(n,seq,allmask ^(1<<i))]
 pairconf=[]; tripleconf=[]
 for i,j in combinations(redundant,2):
  if not is_spanner(n,seq,allmask^(1<<i)^(1<<j)):
   pairconf.append((i,j))
 for i,j,k in combinations(redundant,3):
  mask=allmask^(1<<i)^(1<<j)^(1<<k)
  if not is_spanner(n,seq,mask) and all(is_spanner(n,seq,allmask^(1<<a)^(1<<b)) for a,b in [(i,j),(i,k),(j,k)]):
   tripleconf.append((i,j,k))
 return pairconf,tripleconf

if __name__=='__main__':
 for n in range(3,6):
  base=edges_complete(n); ctr=collections.Counter();first={}
  for seq in permutations(base):
   p,t=analyze(n,seq)
   ctr['total']+=1
   if p:
    ctr['pair_instances']+=1;ctr['pair_obstructions']+=len(p)
    for i,j in p:
     disjoint=set(seq[i]).isdisjoint(seq[j])
     key='disjoint_pair' if disjoint else 'adjacent_pair'
     ctr[key]+=1
     first.setdefault(key,(seq,(i,j)))
   if t:
    ctr['triple_instances']+=1;ctr['triple_obstructions']+=len(t)
    first.setdefault('triple',(seq,t[0]))
   if n==5 and ctr['total']>15000:break
  print(n,ctr,first,flush=True)
