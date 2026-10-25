"""Independent, unquotiented n=13 both-cyclic half reduction."""
from itertools import product,combinations_with_replacement,permutations
from collections import Counter
cells=tuple(product(range(3),repeat=2))
perms=tuple(permutations(range(3)))
def canon(e):
    return min(tuple(sorted((p[j],q[i]) if sw else (p[i],q[j]) for i,j in e))
               for p in perms for q in perms for sw in (False,True))
def grid(e):
    count=Counter(e)
    return [[1+count[i,j] for j in range(3)] for i in range(3)]
def possible(M,r,c):
    if any(all(M[i][j]==1 for j in range(3)) for i in range(3) if i!=r):return False
    if any(all(M[i][j]==1 for i in range(3)) for j in range(3) if j!=c):return False
    prow=[sum(M[i][j]==1 for j in range(3)) for i in range(3)]
    qcol=[sum(M[i][j]==1 for i in range(3)) for j in range(3)]
    for j in range(3):
        if j==c:continue
        singles=[i for i in range(3) if M[i][j]==1]
        if len(singles)==2:
            k=next(i for i in range(3) if i not in singles)
            if M[k][j]==1:return False
            if M[k][j]==2:prow[k]+=2
            if M[k][j]==3:prow[k]+=1
    for i in range(3):
        if i==r:continue
        singles=[j for j in range(3) if M[i][j]==1]
        if len(singles)==2:
            k=next(j for j in range(3) if j not in singles)
            if M[i][k]==1:return False
            if M[i][k]==2:qcol[k]+=2
            if M[i][k]==3:qcol[k]+=1
    for i in range(3):
        size=sum(M[i])
        if i!=r and prow[i]>2:return False
        if i==r and size>=5 and prow[i]==size:return False
    for j in range(3):
        size=sum(M[i][j] for i in range(3))
        if j!=c and qcol[j]>2:return False
        if j==c and size>=5 and qcol[j]==size:return False
    return True
def run():
    all_extras=list(combinations_with_replacement(cells,4))
    orbit={canon(e) for e in all_extras};raw=0;survivors=[]
    for e in all_extras:
        M=grid(e)
        for r in range(3):
            for c in range(3):
                if any(all(M[i][j]==1 for j in range(3)) for i in range(3) if i!=r):continue
                if any(all(M[i][j]==1 for i in range(3)) for j in range(3) if j!=c):continue
                raw+=1
                if possible(M,r,c):survivors.append((e,r,c))
    assert len(all_extras)==495 and len(orbit)==16
    assert raw==1278 and len(survivors)==9
    assert {canon(e) for e,_,_ in survivors}=={((0,0),(0,1),(1,0),(1,1))}
    print("PASS: 495 assignments, 16 orbits, 1278 eligible placements, 9 survivors in one orbit")
if __name__=="__main__":run()
