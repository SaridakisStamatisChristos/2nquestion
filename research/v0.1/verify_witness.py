import sys,itertools,random
sys.path.insert(0,'/mnt/data/temporal_clique_lab')
from temporal_lab import *
seq=[(2,3),(0,2),(0,1),(2,5),(1,2),(3,4),(0,3),(1,5),(0,4),(3,5),(2,4),(0,5),(4,5),(1,3),(1,4)]
n=6
print('complete connected:',is_spanner(n,seq))
from itertools import combinations
for k in [8,9]:
 sol=[]
 for idxs in combinations(range(15),k):
  keep=sum(1<<i for i in idxs)
  if is_spanner(n,seq,keep): sol.append(idxs)
 print('k',k,'valid-spanners',len(sol),'one',sol[:1])
 if sol:break

def star_tree(S):
 for h in range(n):
  star={(min(h,u),max(h,u)) for u in range(n) if u!=h}
  if not star.issubset(S):continue
  leafE=S-star
  if len(leafE)!=4: continue
  seen={next(iter(range(n))) if h!=0 else 1}
  changed=True
  while changed:
   changed=False
   for u,v in leafE:
    if u in seen and v not in seen:seen.add(v);changed=True
    if v in seen and u not in seen:seen.add(u);changed=True
  if len(seen)==n-1:return True
 return False
cnt=0
for idxs in combinations(range(15),9):
 S={tuple(sorted(seq[i])) for i in idxs}
 if star_tree(S):
  cnt+=1
  if is_spanner(n,seq,sum(1<<i for i in idxs)):
   print('Unexpected found star+tree!');break
print('enumerated star-tree candidates',cnt)
