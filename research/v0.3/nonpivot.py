import sys,random,time,collections,json,itertools
sys.path.insert(0,'/mnt/data/temporal_clique_lab')
from temporal_lab import *
def pivot_edges(n,seq):
 m=len(seq); allbits=(1<<n)-1
 pre=[(1<<v) for v in range(n)]; prefix=[]
 for i,(u,v) in enumerate(seq):
  prefix.append(pre.copy());b=pre[u]|pre[v];pre[u]=pre[v]=b
 ans=[]
 for i,(u,v) in enumerate(seq):
  if (prefix[i][u]|prefix[i][v]) != allbits:continue
  active=[0]*n;active[u]=active[v]=1
  for a,b in seq[i+1:]:
   q=active[a]|active[b];active[a]=active[b]=q
  if all(active):ans.append(i)
 return ans

rng=random.Random(71091)
for n in (5,6,7,8):
 samples=0; tally=collections.Counter(); nonpivot=[]
 t=time.perf_counter()
 for j in range(10000):
  seq=edges_complete(n);rng.shuffle(seq)
  if not pivot_edges(n,seq):
   samples+=1
   heur=min(greedy(n,seq,i).bit_count() for i in range(30))
   tally[heur]+=1
   if heur>2*n-4:nonpivot.append(seq)
 print('n',n,'nonpivot',samples,'bestgreedy',dict(tally),'hard',len(nonpivot),'secs',round(time.perf_counter()-t,2),flush=True)
 if n==6:
  verified=collections.Counter();bad=None
  for seq in nonpivot:
   result=exact_milp(n,seq,6)
   verified[result.get('size')]+=1
   if result.get('size',100)>2*n-4:bad=seq
  print('  exact hard cases',dict(verified),'counterexample?',bad,flush=True)
