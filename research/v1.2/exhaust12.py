import itertools,sys,time,json
from collections import Counter
from double_cycles import find_case
cells=list(itertools.product(range(3),repeat=2))
perms=list(itertools.permutations(range(3)))
def orbit_rep(extras):
    possibilities=[]
    for rp in perms:
        for cp in perms:
            for sw in (False,True):
                tmp=sorted((rp[r],cp[c]) if not sw else (rp[c],cp[r]) for r,c in extras)
                possibilities.append(tuple(tmp))
    return min(possibilities)
allsets=set()
for extra in itertools.combinations_with_replacement(cells,3):
    rows=Counter(r for r,c in extra);cols=Counter(c for r,c in extra)
    if sum(rows[r]==0 for r in range(3))>1 or sum(cols[c]==0 for c in range(3))>1:continue
    allsets.add(orbit_rep(extra))
print('Isomorphism classes',len(allsets),[list(t) for t in sorted(allsets)],flush=True)
start=time.time();total=0
for ext in sorted(allsets):
    rows=Counter(r for r,c in ext);cols=Counter(c for r,c in ext)
    rr=[r for r in range(3) if rows[r]==0] or list(range(3))
    cc=[c for c in range(3) if cols[c]==0] or list(range(3))
    for i in rr:
      for j in cc:
        total+=1
        case=find_case(list(ext),i,j)
        print('CASE',ext,i,j,'found',bool(case),'elapsed',round(time.time()-start,2),flush=True)
        if case:
          print('FOUND_SCHEDULE',json.dumps(case));exit(1)
print('No both-cyclic shortest schedule for n12 in',total,'classes of component patterns')
