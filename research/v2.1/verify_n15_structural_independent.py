"""Independent n=13..15 incidence reduction using positive compositions.

The main v2.0 implementation uses combinations-with-replacement of extra
vertices; this checker instead enumerates all 8 divider positions among n-1.
"""
from collections import Counter
from itertools import combinations, permutations
from verify_n15_independent import requirements

PERM=tuple(permutations(range(3)))

def compositions(n):
    for cuts in combinations(range(1,n),8):
        points=(0,)+cuts+(n,)
        seq=[points[i+1]-points[i] for i in range(9)]
        yield tuple(tuple(seq[3*i:3*i+3]) for i in range(3))

def canonical(M,cr,cc):
    best=None
    for rp in PERM:
        for cp in PERM:
            for transposed in (False,True):
                mat=[[0]*3 for _ in range(3)]
                for r in range(3):
                    for c in range(3):
                        rr=rp[c] if transposed else rp[r]
                        col=cp[r] if transposed else cp[c]
                        mat[rr][col]=M[r][c]
                candidate=(tuple(tuple(row) for row in mat),
                           rp[cc] if transposed else rp[cr],
                           cp[cr] if transposed else cp[cc])
                if best is None or candidate<best:best=candidate
    return best

def legal(M,cr,cc,include_strong):
    forward,backward=requirements(M,cr,cc)
    if not include_strong:
        # Only singleton and two-singleton first-bridge obligations apply.
        forward=[[int(M[r][c]==1) for c in range(3)] for r in range(3)]
        backward=[[int(M[r][c]==1) for c in range(3)] for r in range(3)]
        for c in range(3):
            if c==cc:continue
            singles=[r for r in range(3) if M[r][c]==1]
            if len(singles)==2:
                other=next(r for r in range(3) if r not in singles)
                forward[other][c]=min(M[other][c],2) if M[other][c]<=3 else 0
        for r in range(3):
            if r==cr:continue
            singles=[c for c in range(3) if M[r][c]==1]
            if len(singles)==2:
                other=next(c for c in range(3) if c not in singles)
                backward[r][other]=min(M[r][other],2) if M[r][other]<=3 else 0
    for r in range(3):
        count=sum(forward[r]);size=sum(M[r])
        if r!=cr and count>2:return False
        if r==cr and size>=5 and count==size:return False
    for c in range(3):
        count=sum(backward[r][c] for r in range(3))
        size=sum(M[r][c] for r in range(3))
        if c!=cc and count>2:return False
        if c==cc and size>=5 and count==size:return False
    return True

def audit():
    from half_forest14_grid import run
    expectations={13:(1278,9,0,0),14:(4698,738,81,3),
                  15:(13680,4662,945,20)}
    for n in (13,14,15):
        eligible=basic=strong=0;orbit=Counter()
        for M in compositions(n):
            for cr in range(3):
                for cc in range(3):
                    if any(r!=cr and all(M[r][c]==1 for c in range(3))
                           for r in range(3)):continue
                    if any(c!=cc and all(M[r][c]==1 for r in range(3))
                           for c in range(3)):continue
                    eligible+=1
                    if not legal(M,cr,cc,False):continue
                    basic+=1
                    if not legal(M,cr,cc,True):continue
                    strong+=1
                    orbit[canonical(M,cr,cc)]+=1
        assert (eligible,basic,strong,len(orbit))==expectations[n],n
        assert orbit==run(n)[3],('independent orbit disagreement',n)
        print(f'PASS independent divider/composition enumeration n={n}: '
              f'{eligible}/{basic}/{strong} and {len(orbit)} orbits')
    return True

if __name__=='__main__':
    audit()
