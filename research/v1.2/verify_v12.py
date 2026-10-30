#!/usr/bin/env python3
"""Self-contained independent checks for 2nquestion v1.2. Requires Python 3.10+."""
import itertools
import json
from pathlib import Path

K8 = [(0,1),(4,5),(3,7),(2,6),(2,3),(1,5),(0,4),(1,2),(6,7),(4,6),(3,5),(0,7)]

def gossip(n, edges):
    state=[1<<u for u in range(n)]
    for a,b in edges:
        union=state[a] | state[b]
        state[a]=state[b]=union
    return all(x==(1<<n)-1 for x in state)

def dfs_reachable(n, edges, s, t):
    # Distinct contacts, direction can be either but indices must increase.
    reachable={s}
    for a,b in edges:
        olda=a in reachable; oldb=b in reachable
        if olda or oldb:
            reachable.add(a); reachable.add(b)
    return t in reachable

def all_pairs(n, edges):
    return all(dfs_reachable(n,edges,s,t) for s in range(n) for t in range(n) if s!=t)

def canonical_11():
    # Exactly two extra cells, in distinct prefix components and suffix components.
    labels=[(r,c) for r in range(3) for c in range(3)]+[(0,0),(1,1)]
    rows=[tuple(v for v,(r,c) in enumerate(labels) if r==i) for i in range(3)]
    cols=[tuple(v for v,(r,c) in enumerate(labels) if c==i) for i in range(3)]
    return labels,rows,cols

def options(group, cycle, singleton_required):
    edges=list(itertools.combinations(group,2))
    full=sum(1<<v for v in group)
    all_options=[]
    e_count=len(group) if cycle else len(group)-1
    for selected in itertools.combinations(edges,e_count):
        # Check static connectivity, independent of chronology.
        comp={v:v for v in group}
        def root(v):
            while comp[v]!=v:v=comp[v]
            return v
        for a,b in selected:
            comp[root(a)]=root(b)
        if len({root(v) for v in group})!=1:
            continue
        for seq in itertools.permutations(selected):
            bits={v:1<<v for v in group}
            for a,b in seq:
                merged=bits[a]|bits[b]
                bits[a]=bits[b]=merged
            if all(bits[v]==full for v in singleton_required):
                all_options.append(seq)
    return all_options

def test_canonical_n11():
    labels,rows,cols=canonical_11()
    ropts=[]; copts=[]
    for grp in rows:
        required=[u for u in grp if sum(labels[v][1]==labels[u][1] for v in grp)==1]
        ropts.append(options(grp,len(grp)==3,required))
    for grp in cols:
        required=[u for u in grp if sum(labels[v][0]==labels[u][0] for v in grp)==1]
        reverse_options=options(grp,len(grp)==3,required)
        copts.append([seq[::-1] for seq in reverse_options])
    assert [len(x) for x in ropts]==[12,12,6],tuple(map(len,ropts))
    assert [len(x) for x in copts]==[12,12,6],tuple(map(len,copts))
    tested=0
    for rowcombo in itertools.product(*ropts):
        state=[1<<v for v in range(11)]
        used=set()
        for seq in rowcombo:
            for a,b in seq:
                merged=state[a]|state[b]
                state[a]=state[b]=merged
                used.add(tuple(sorted((a,b))))
        for i,col in enumerate(cols):
            valid=False
            for seq in copts[i]:
                if any(tuple(sorted(e)) in used for e in seq):
                    continue
                local={v:state[v] for v in col}
                for a,b in seq:
                    union=local[a]|local[b]
                    local[a]=local[b]=union
                if all(local[v]==(1<<11)-1 for v in col):
                    valid=True
                    break
            if not valid:
                break
        else:
            raise AssertionError('Both-cyclic n=11 schedule found!')
        tested+=1
    assert tested==864
    return {'row_options': list(map(len,ropts)), 'column_options':list(map(len,copts)), 'prefix_profiles_tested':tested, 'simultaneous_cyclic_successes':0}

def test_n8():
    assert len(K8)==12 and len(set(tuple(sorted(e)) for e in K8))==12
    assert gossip(8,K8)
    assert all_pairs(8,K8)
    def cycle_count(es):
        parents=list(range(8)); cycle=0
        def root(v):
            while parents[v]!=v:v=parents[v]
            return v
        for a,b in es:
            a=root(a);b=root(b)
            if a==b:cycle+=1
            else:parents[a]=b
        return cycle
    assert cycle_count(K8[:6])==0
    assert cycle_count(K8[6:])==1
    return {'n':8,'contacts':12,'pairs_reached':56,'prefix_cycles':0,'suffix_cycles':1}

if __name__=='__main__':
    print(json.dumps({'witness_8':test_n8(),'excluded_11':test_canonical_n11()},indent=2))
