"""Independent earliest-arrival and n=7 half-cover structural audit.

No reference to the bitset recurrence implementation used by sharp_half_forest.py.
"""
from itertools import combinations
from math import comb

CONTACTS = [(0,1),(4,5),(3,7),(2,6),(2,3),(1,5), (0,4),(1,2),(6,7),(4,6),(3,5),(0,7)]

def path_exists(src,dst,edges):
    # Check every strictly time-increasing simple path, via DFS on used vertices.
    n=max(max(e) for e in edges)+1
    def dfs(cur,next_time,used):
        if cur==dst:return True
        for time in range(next_time,len(edges)):
            a,b=edges[time]
            if a==cur and not (used & (1<<b)):
                if dfs(b,time+1,used|1<<b):return True
            if b==cur and not (used & (1<<a)):
                if dfs(a,time+1,used|1<<a):return True
        return False
    return dfs(src,0,1<<src)

def cycle_exists(n,edges):
    p=list(range(n))
    def rt(a):
        while p[a]!=a:a=p[a]
        return a
    for a,b in edges:
        x,y=rt(a),rt(b)
        if x==y:return True
        p[x]=y
    return False

if __name__=='__main__':
    assert len({tuple(sorted(e)) for e in CONTACTS})==12
    for u in range(8):
        for v in range(8):
            if u!=v: assert path_exists(u,v,CONTACTS),(u,v)
    assert cycle_exists(8,CONTACTS[6:])
    assert not cycle_exists(8,CONTACTS[:6])
    print('PASS: 56 ordered pairs admit a strictly increasing simple path on K8 witness')

    E=list(combinations(range(7),2))
    all_cover_cycle=[]
    for S in combinations(E,5):
        if len({v for edge in S for v in edge})==7 and cycle_exists(7,S):
            all_cover_cycle.append(S)
            # Only a 3-cycle plus two independent K2 can cover all 7 with 5 edges.
            cdeg=[sum(i in e for e in S) for i in range(7)]
            assert sorted(cdeg)==[1,1,1,1,2,2,2],(S,cdeg)
    assert all_cover_cycle
    print(f'PASS: all {comb(21,5)} 5-edge graphs on 7 vertices checked; '
          f'{len(all_cover_cycle)} with full vertex cover and cycle have triangle + two K2 structure')
