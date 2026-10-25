"""Find smallest ordered source-target test set ruling out all 2-tree spanners."""
import itertools, sys
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import lil_matrix
from independent_verify import N,TIMELINE,EDGES,TIDX,constructive_two_trees,connected

def reach_pairs(mask):
   misses=set()
   for s in range(N):
       R={s}
       for a,b in TIMELINE:
           if mask>>TIDX[tuple(sorted((a,b)))]&1:
               if a in R or b in R:R|={a,b}
       for t in range(N):
           if s!=t and t not in R:misses.add((s,t))
   return misses

p=[(s,t) for s in range(N) for t in range(N) if s!=t]
trees=sorted(constructive_two_trees(N))
misses=[reach_pairs(mask) for mask in trees]
assert all(misses)
mat=lil_matrix((len(trees),len(p)),dtype=np.float64)
for i,ms in enumerate(misses):
 for j,pair in enumerate(p):
  if pair in ms:mat[i,j]=1.
res=milp(np.ones(len(p)),integrality=np.ones(len(p)),bounds=Bounds(np.zeros(len(p)),np.ones(len(p))),
 constraints=LinearConstraint(mat.tocsr(),np.ones(len(trees)),np.full(len(trees),np.inf)),
 options={'time_limit':90,'mip_rel_gap':0})
print('status',res.status,'dual_bound',getattr(res,'mip_dual_bound',None),'gap',getattr(res,'mip_gap',None))
if res.x is not None:
 chosen=[pair for pair,x in zip(p,res.x) if x>0.5]
 print('certificate pair count',len(chosen),'pairs',chosen)
 assert all(any(q in failures for q in chosen) for failures in misses)
 with open('/mnt/data/Temporal_Clique_Research_v0.6/reachability_certificate.txt','w') as f:
  f.write(f'K6 chronology: {TIMELINE}\nWitness checked over 1215 spanning 2-trees\n')
  f.write(f'Targeted ordered pairs: {chosen}\n')
  f.write(f'cover status: {res.status} dual_bound:{getattr(res,"mip_dual_bound",None)}\n')
