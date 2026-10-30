"""Exact necessary-condition n13-15 grid filter; NOT a satisfiability checker."""
from itertools import combinations_with_replacement, permutations, product
from collections import Counter
CELLS=tuple(product(range(3),repeat=2))
S3=tuple(permutations(range(3)))
def mat(extra):
    c=Counter(extra)
    return tuple(tuple(1+c[r,j] for j in range(3)) for r in range(3))
def orbit(extra):
    return min(tuple(sorted((p[j],q[i]) if t else (p[i],q[j]) for i,j in extra))
               for p in S3 for q in S3 for t in (False,True))
def admissible(M,cr,cc):
    dp=[sum(M[r][c]==1 for c in range(3)) for r in range(3)]
    dq=[sum(M[r][c]==1 for r in range(3)) for c in range(3)]
    for c in range(3):
        if c==cc:continue
        singleton=[r for r in range(3) if M[r][c]==1]
        if len(singleton)==2:
            r=next(r for r in range(3) if r not in singleton)
            k=M[r][c]
            if k==1:return False
            if k==2:dp[r]+=2
            if k==3:dp[r]+=1
    for r in range(3):
        if r==cr:continue
        singleton=[c for c in range(3) if M[r][c]==1]
        if len(singleton)==2:
            c=next(c for c in range(3) if c not in singleton)
            k=M[r][c]
            if k==1:return False
            if k==2:dq[c]+=2
            if k==3:dq[c]+=1
    for r in range(3):
        m=sum(M[r])
        if r!=cr and dp[r]>2:return False
        if r==cr and m>=5 and dp[r]==m:return False
    for c in range(3):
        m=sum(M[r][c] for r in range(3))
        if c!=cc and dq[c]>2:return False
        if c==cc and m>=5 and dq[c]==m:return False
    return True
def run(n):
    eligible=0;surviving=[];orbits=Counter()
    allocations=0
    for extra in combinations_with_replacement(CELLS,n-9):
        allocations+=1
        M=mat(extra)
        for cr in range(3):
            for cc in range(3):
                if any(r!=cr and all(M[r][c]==1 for c in range(3)) for r in range(3)):continue
                if any(c!=cc and all(M[r][c]==1 for r in range(3)) for c in range(3)):continue
                eligible+=1
                if admissible(M,cr,cc):
                    surviving.append((extra,cr,cc))
                    orbits[orbit(extra)]+=1
    print(f"n={n} allocations={allocations} eligible={eligible} survivors={len(surviving)} matrix_orbits={len(orbits)}")
    return allocations,eligible,len(surviving),len(orbits)
if __name__=="__main__":
    assert run(13)==(495,1278,9,1)
    assert run(14)==(1287,4698,738,11)
    assert run(15)==(3003,13680,4662,42)
    print("PASS: necessary-condition enumeration; no existence claim for n>=14")
