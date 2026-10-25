"""Exact incidence reduction for n=13 and n=14 optimal gossip schedules."""
from collections import Counter
from itertools import product, permutations, combinations_with_replacement
CELLS=tuple(product(range(3),repeat=2))
S3=tuple(permutations(range(3)))
def matrix(extra):
    d=Counter(extra)
    return tuple(tuple(1+d[r,c] for c in range(3)) for r in range(3))
def canonical(M,cr,cc):
    out=[]
    for a in S3:
        for b in S3:
            for flip in (False,True):
                N=[[0]*3 for _ in range(3)]
                for r in range(3):
                    for c in range(3):
                        N[a[c] if flip else a[r]][b[r] if flip else b[c]]=M[r][c]
                out.append((tuple(map(tuple,N)),a[cc] if flip else a[cr],
                            b[cr] if flip else b[cc]))
    return min(out)
def counts(M,cr,cc,strong):
    # Minimum required forward prefix collectors and reverse suffix collectors.
    row=[[int(M[r][c]==1) for c in range(3)] for r in range(3)]
    col=[[int(M[r][c]==1) for c in range(3)] for r in range(3)]
    for c in range(3):
        if c==cc:continue
        singles=[r for r in range(3) if M[r][c]==1]
        if strong:
            for r in range(3):
                if singles and r not in singles:row[r][c]=max(row[r][c],1)
        if len(singles)==2:
            r=next(r for r in range(3) if r not in singles)
            if M[r][c]==2:row[r][c]=2
            if M[r][c]==3:row[r][c]=max(row[r][c],1)
    for r in range(3):
        if r==cr:continue
        singles=[c for c in range(3) if M[r][c]==1]
        if strong:
            for c in range(3):
                if singles and c not in singles:col[r][c]=max(col[r][c],1)
        if len(singles)==2:
            c=next(c for c in range(3) if c not in singles)
            if M[r][c]==2:col[r][c]=2
            if M[r][c]==3:col[r][c]=max(col[r][c],1)
    for r in range(3):
        need=sum(row[r]);size=sum(M[r])
        if r!=cr and need>2:return False
        if r==cr and size>=5 and need==size:return False
    for c in range(3):
        need=sum(col[r][c] for r in range(3))
        size=sum(M[r][c] for r in range(3))
        if c!=cc and need>2:return False
        if c==cc and size>=5 and need==size:return False
    return True
def run(n):
    eligible=old=new=0;orbits=Counter()
    for ex in combinations_with_replacement(CELLS,n-9):
        M=matrix(ex)
        for cr in range(3):
            for cc in range(3):
                if any(r!=cr and all(M[r][c]==1 for c in range(3)) for r in range(3)):continue
                if any(c!=cc and all(M[r][c]==1 for r in range(3)) for c in range(3)):continue
                eligible+=1
                if not counts(M,cr,cc,False):continue
                old+=1
                if counts(M,cr,cc,True):
                    new+=1
                    orbits[canonical(M,cr,cc)]+=1
    return eligible,old,new,orbits
def main():
    e,o,s,d=run(13);assert (e,o,s,len(d))==(1278,9,0,0)
    print('PASS n13:',e,o,s,len(d))
    e,o,s,d=run(14);assert (e,o,s,len(d))==(4698,738,81,3)
    assert sorted(d.values())==[9,36,36]
    print('PASS n14:',e,o,s,len(d))
    for k,v in sorted(d.items()):print('orbit',v,k)
    return d
if __name__=='__main__':main()
