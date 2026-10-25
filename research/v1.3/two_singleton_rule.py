"""Two-singleton tree-contact lemma: exhaustive finite regression.

For a shortest pairwise-distinct gossip schedule split at n-2 contacts,
if a suffix contact component is a tree and meets two DIFFERENT prefix
components in singleton vertices u,v, then its first contact is uv.
Similarly, if a prefix component is a tree and meets two suffix
components in singleton vertices u,v, then its last contact is uv.

Can be used on any successful schedule, not only shortest, provided
component is a tree and the cut is arbitrary.
"""
from itertools import combinations, permutations
import random,json,sys

def gossip(n,schedule):
    info=[1<<i for i in range(n)]
    for u,v in schedule:
        info[u]=info[v]=info[u]|info[v]
    return all(x==(1<<n)-1 for x in info)

def components(n,edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    seen=set();parts=[];label=[None]*n
    for v in range(n):
        if v in seen:continue
        component=set([v]);stack=[v];seen.add(v)
        while stack:
            x=stack.pop()
            for y in adj[x]:
                if y not in seen:seen.add(y);component.add(y);stack.append(y)
        k=len(parts)
        for w in component:label[w]=k
        parts.append(component)
    return parts,label

def check(n,schedule,at=None):
    if at is None:at=n-2
    pre=schedule[:at];post=schedule[at:]
    P,pr=components(n,pre);Q,qr=components(n,post)
    checked=0
    for j,q in enumerate(Q):
        edges=[e for e in post if e[0] in q and e[1] in q]
        if len(edges)!=len(q)-1:continue
        singleton=[next(iter(q & p)) for p in P if len(q & p)==1]
        if len(singleton)>=2:
            assert len(singleton)==2, (n,schedule,j,singleton)
            assert set(edges[0])==set(singleton), ('suffix failed',n,schedule,j,singleton)
            checked+=1
    for i,p in enumerate(P):
        edges=[e for e in pre if e[0] in p and e[1] in p]
        if len(edges)!=len(p)-1:continue
        singleton=[next(iter(p & q)) for q in Q if len(p & q)==1]
        if len(singleton)>=2:
            assert len(singleton)==2, (n,schedule,i,singleton)
            assert set(edges[-1])==set(singleton), ('prefix failed',n,schedule,i,singleton)
            checked+=1
    return checked

def full_check(n):
    all_edges=list(combinations(range(n),2));length=2*n-4
    count=successful=restrictions=0
    for seq in permutations(all_edges,length):
        count+=1
        if gossip(n,seq):
            successful+=1;restrictions+=check(n,seq)
    return {'n':n,'all_distinct_edge_schedules':count,'successful_schedules':successful,'two_singleton_constraints_checked':restrictions}

def random_check(n=6,count=30000,seed=1701):
    rng=random.Random(seed);edges=list(combinations(range(n),2));success=restrictions=0
    for i in range(count):
        seq=rng.sample(edges,2*n-4)
        if gossip(n,seq):
            success+=1;restrictions+=check(n,seq)
    return {'n':n,'sampled':count,'successes':success,'constraints_checked':restrictions,'seed':seed}

if __name__=='__main__':
    out={'full':[full_check(4),full_check(5)],'sample':[random_check(6)]}
    print(json.dumps(out,indent=2))
    open(str(__import__('pathlib').Path(__file__).with_name('rule_results.json')),'w').write(json.dumps(out,indent=2)+'\n')
