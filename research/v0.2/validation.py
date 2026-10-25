"""Independent temporal-path witness checker + cross validation."""
import random,itertools,sys,json
from temporal_lab import *

def independent_reach(n,seq,mask):
    """DFS over increasing contact times; no gossip-state propagation."""
    adj=[[] for _ in range(n)]
    for i,(u,v) in enumerate(seq):
        if mask>>i & 1:
            adj[u].append((i,v));adj[v].append((i,u))
    all_reach=[]
    for source in range(n):
        seen=set();stack=[(source,-1)];targets={source}
        while stack:
            v,t=stack.pop()
            if (v,t) in seen:continue
            seen.add((v,t));targets.add(v)
            for ti,w in adj[v]:
                if ti>t and (w,ti) not in seen:stack.append((w,ti))
        all_reach.append(targets)
    return all_reach

def check(n,seq,mask):
    reach=temporal_reach(n,seq,mask)
    dst=independent_reach(n,seq,mask)
    for s in range(n):
        inferred={v for v in range(n) if reach[v]>>s & 1}
        assert inferred==dst[s],(n,seq,mask,s,inferred,dst[s])

rng=random.Random(161803)
count=0
for n in range(2,9):
    for trial in range(200):
        seq=edges_complete(n);rng.shuffle(seq)
        mask=rng.getrandbits(len(seq))
        check(n,seq,mask)
        count+=1
print('dfs-vs-gossip differential cases passed:',count)
# full exhaustive all labelled cliques n<=4 and all subsets for each
cases=0
for n in [2,3,4]:
  for seq in itertools.permutations(edges_complete(n)):
    for mask in range(1<<len(seq)):
      check(n,seq,mask);cases+=1
print('fully exhaustive n<=4 pair checks passed:',cases)
