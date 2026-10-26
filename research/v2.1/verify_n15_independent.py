"""Second implementation of all 20 profile compatibility checks.

Consumes the primary oracle's fully enumerated local domains; it does NOT
independently re-enumerate the seven-vertex local states. Small-size differential
tests and separate temporal semantics checks guard that remaining dependency.
"""
from itertools import combinations, permutations
from pathlib import Path
import re
from half_forest14_grid import run

def requirements(M,cr,cc):
    forward=[[int(x==1) for x in row] for row in M]
    backward=[[int(x==1) for x in row] for row in M]
    for col in range(3):
        if col==cc:continue
        singles=[row for row in range(3) if M[row][col]==1]
        if singles:
            for row in range(3):
                if row not in singles:forward[row][col]=max(1,forward[row][col])
        if len(singles)==2:
            other=({0,1,2}-set(singles)).pop()
            forward[other][col]=max(forward[other][col],2 if M[other][col]==2 else 1)
    for row in range(3):
        if row==cr:continue
        singles=[col for col in range(3) if M[row][col]==1]
        if singles:
            for col in range(3):
                if col not in singles:backward[row][col]=max(1,backward[row][col])
        if len(singles)==2:
            other=({0,1,2}-set(singles)).pop()
            backward[row][other]=max(backward[row][other],2 if M[row][other]==2 else 1)
    return forward,backward

def parse(text):
    lines=iter(text.splitlines());cases=[];domains={}
    for line in lines:
        if line.startswith('CASE '):
            cases.append(line)
            continue
        t=line.split()
        assert t[0]=='DOMAIN',line
        nums=list(map(int,t[1:]))
        g=tuple(nums[:3]);req=tuple(nums[3:6])
        cyclic,optimistic,nB,nD=nums[6:]
        B={tuple(map(int,next(lines).split()[1:])) for _ in range(nB)}
        D={tuple(map(int,next(lines).split()[1:])) for _ in range(nD)}
        assert next(lines)=='END'
        assert len(B)==nB and len(D)==nD
        key=(g,req,cyclic,optimistic)
        assert key not in domains
        domains[key]=(B,D)
    return cases,domains

def compatible(rows,cols):
    # Different from C++: repeatedly filter suffix choices row-by-row,
    # then select each suffix triple and independently satisfy all row variables.
    suffix=[list(x) for x in cols]
    for row in sorted(range(3),key=lambda r:len(rows[r])):
        for col in range(3):
            suffix[col]=[d for d in suffix[col]
                         if any((b[col]&d[row])==d[row] for b in rows[row])]
        if any(not x for x in suffix):return False
    for d0 in suffix[0]:
        for d1 in suffix[1]:
            for d2 in suffix[2]:
                if all(any(all((p[j] & (d0,d1,d2)[j][r]) ==
                               (d0,d1,d2)[j][r] for j in range(3))
                           for p in rows[r]) for r in range(3)):
                    return True
    return False

def simulate(order,m):
    know=[1<<v for v in range(m)]
    for u,v in order:know[u]=know[v]=know[u]|know[v]
    return know

def profile(state,group):
    full=(1<<len(state))-1
    b=d=0
    for mask in range(1<<len(group)):
        joined=0
        for i,v in enumerate(group):
            if mask>>i&1:joined|=state[v]
        if joined==full:b|=1<<mask
    for secret in range(len(state)):
        entry=sum(1<<i for i,v in enumerate(group) if state[v]>>secret&1)
        d|=1<<entry
    return b,d

def python_local(groups,required,cyclic):
    m=sum(groups)
    all_edges=list(combinations(range(m),2))
    parts=[];offset=0
    for g in groups:
        parts.append(tuple(range(offset,offset+g)));offset+=g
    bs=set();ds=set();full=(1<<m)-1
    for order in permutations(all_edges,m-1+cyclic):
        neighbors=[set() for _ in range(m)]
        for u,v in order:neighbors[u].add(v);neighbors[v].add(u)
        discovered={0};frontier=[0]
        for v in frontier:
            for w in neighbors[v]:
                if w not in discovered:discovered.add(w);frontier.append(w)
        if len(discovered)!=m:continue
        state=simulate(order,m)
        if any(sum(state[v]==full for v in part)<need or
               __import__('functools').reduce(int.__or__,(state[v] for v in part),0)!=full
               for part,need in zip(parts,required)):continue
        bs.add(tuple(profile(state,part)[0] for part in parts))
        ds.add(tuple(profile(state,part)[1] for part in parts))
    return bs,ds

def audit(output):
    reports,domains=parse(output)
    assert len(reports)==20 and len(domains)>=30
    eligible,basic,strong,orbits=run(15)
    assert (eligible,basic,strong,len(orbits))==(13680,4662,945,20)
    result=[]
    for index,((M,cr,cc),multiplicity) in enumerate(sorted(orbits.items())):
        forward,backward=requirements(M,cr,cc)
        rowkeys=[(tuple(M[r]),tuple(forward[r]),int(r==cr),
                  int(sum(M[r])>=7 and r!=cr)) for r in range(3)]
        colkeys=[(tuple(M[r][c] for r in range(3)),
                  tuple(backward[r][c] for r in range(3)),
                  int(c==cc),
                  int(sum(M[r][c] for r in range(3))>=7 and c!=cc))
                 for c in range(3)]
        rows=[domains[k][0] for k in rowkeys]
        cols=[domains[k][1] for k in colkeys]
        missing=any(not d for d in rows+cols)
        assert not compatible(rows,cols),('RELAXED_SAT',index)
        report=reports[index]
        assert re.match(r'CASE (\d+)',report).group(1)==str(index)
        assert f'mult={multiplicity}' in report
        assert ('status=LOCAL_UNSAT' in report)==missing
        assert ('status=PROFILE_UNSAT' in report)==(not missing)
        result.append({'orbit':index,'matrix':[list(row) for row in M],'cyclic_row':cr,
                       'cyclic_col':cc,'multiplicity':multiplicity,
                       'result':'LOCAL_UNSAT' if missing else 'PROFILE_UNSAT',
                       'optimistic':bool(any(k[3] for k in rowkeys+colkeys)),
                       'row_domains':[len(p) for p in rows],
                       'col_domains':[len(p) for p in cols]})
    assert sum(x['multiplicity'] for x in result)==945
    # Independently enumerate four small local component types and compare
    # both prefix sufficiency and reverse ancestry domain sets.
    keys=[((1,1,1),(1,1,1),1,0),((1,1,2),(1,1,0),0,0),
          ((1,2,2),(1,1,0),1,0),((2,1,2),(0,1,1),0,0)]
    for key in keys:
        assert key in domains,key
        assert python_local(*key[:3])==domains[key],('local differential',key)
    print('PASS: 4 independently enumerated local component domain types')
    print('PASS: second full compatibility implementation 20/20')
    return {'claim':'n15 both-cyclic original chronological halves excluded by a relaxed information-profile CSP',
            'scope':'computer-assisted finite exhaustive, not formal proof assistant or global novelty',
            'structural':{'allocations':3003,'eligible':13680,'basic':4662,
                          'strong':945,'orbits':20},
            'independent_semantics_tests':3200,
            'orbits':result}
