import json,time,sys
from temporal_lab import exact_milp
p='/mnt/data/temporal_clique_lab/nonpivot_survey.json'
data=json.load(open(p));obj=next(x for x in data if x['n']==8)
for i,x in enumerate(obj['hard']):
 if 'milp' in x:continue
 res=exact_milp(8,x['sequence'],time_limit=12,k_bound=12)
 x['milp']={k:v for k,v in res.items() if k not in ('mask','indices')}
 print(i,'trial',x['trial'],'status',res['status'],'size',res.get('size'),'elapsed',res['time'],flush=True)
 with open(p,'w') as f:json.dump(data,f,indent=2)
print('all n8',len(obj['hard']),'successful',sum(x.get('milp',{}).get('size')==12 for x in obj['hard']))
