import random,sys,time,collections,itertools,json
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

results=[]
for n, trials in [(6,200000),(7,100000),(8,100000),(9,100000)]:
 rng=random.Random(20261024+n)
 nonpivot=0; good=0; hard=[]
 for j in range(trials):
  seq=edges_complete(n);rng.shuffle(seq)
  if not pivot_edges(n,seq):
   nonpivot+=1
   upper=min(greedy(n,seq,k).bit_count() for k in range(12))
   if upper<=2*n-4:good+=1
   else:hard.append({'trial':j,'sequence':seq,'greedy':upper})
 print('n',n,'nonpivot',nonpivot,'good',good,'hard',len(hard),flush=True)
 results.append({'n':n,'trials':trials,'nonpivot':nonpivot,'good':good,'hard':hard})
for obj in results:
  n=obj['n']
  # Only all n=6 difficult cases and up to 9 n=7 difficult cases exact
  if n==6:
   for item in obj['hard']:
    seq=item['sequence']; sol=[]
    for ii in itertools.combinations(range(len(seq)),2*n-4):
      mask=sum(1<<v for v in ii)
      if is_spanner(n,seq,mask): sol.append(ii)
    item['exact_2n4_exists']=bool(sol);item['sol_count']=len(sol)
   print('n6 brute hard:',[(x['trial'],x['exact_2n4_exists'],x['sol_count']) for x in obj['hard']],flush=True)
  if n==7:
   for item in obj['hard'][:9]:
    r=exact_milp(n,item['sequence'],time_limit=6,k_bound=2*n-4)
    item['milp']={k:v for k,v in r.items() if k not in ('mask','indices')}
   print('n7 MILP hard:', [(x['trial'],x.get('milp',{}).get('status'),x.get('milp',{}).get('size')) for x in obj['hard']],flush=True)
  if n==8:
   for item in obj['hard'][:2]:
    r=exact_milp(n,item['sequence'],time_limit=16,k_bound=2*n-4)
    item['milp']={k:v for k,v in r.items() if k not in ('mask','indices')}
   print('n8 MILP hardest2:', [(x['trial'],x.get('milp',{}).get('status'),x.get('milp',{}).get('size')) for x in obj['hard'][:2]],flush=True)
with open('/mnt/data/temporal_clique_lab/nonpivot_survey.json','w') as f:json.dump(results,f,indent=2)
