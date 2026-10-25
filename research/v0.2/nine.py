import sys,random,json,time
sys.path.insert(0,'/mnt/data/temporal_clique_lab')
from temporal_lab import *
for j in range(5):
 n=9;seq=edges_complete(n);random.Random(98009+j).shuffle(seq)
 result=exact_milp(n,seq,time_limit=12,k_bound=15)
 result.pop('mask',None);print(j,json.dumps(result),flush=True)
