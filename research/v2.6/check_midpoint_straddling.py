"""Independent exhaustive verification of Stage 9 all-n midpoint straddling.

For all optimal successful n4/n5 chronologies, require every vertex to
occur in both original halves; every degree-two vertex must occur once
per half. Check EVERY insertion slot pair for three endpoint choices
per chronology. Only successful inserted schedules must preserve ranks.
This finite test does NOT prove the all-n theorem (proof in .md).
"""
from itertools import combinations, permutations

def gossip(n,schedule):
    k=[1<<i for i in range(n)]
    for a,b in schedule:
        k[a]=k[b]=k[a]|k[b]
    return all(x==(1<<n)-1 for x in k)

def rank(n,schedule):
    p=list(range(n));cyc=0
    def root(x):
        while p[x]!=x:
            x=p[x]
        return x
    for a,b in schedule:
        x,y=root(a),root(b)
        if x==y:cyc+=1
        else:p[x]=y
    return cyc

def main():
    for n,expected in ((4,(24,96,1080,216)),(5,(3240,9720,272160,49248))):
        count=degrees=trials=good=0
        m=2*n-4
        for S in permutations(tuple(combinations(range(n),2)),m):
            if not gossip(n,S):
                continue
            count+=1
            prefix,suffix=S[:n-2],S[n-2:]
            for v in range(n):
                assert any(v in e for e in prefix),("missing prefix",n,S,v)
                assert any(v in e for e in suffix),("missing suffix",n,S,v)
                if sum(v in e for e in S)==2:
                    degrees+=1
                    assert sum(v in e for e in prefix)==1
                    assert sum(v in e for e in suffix)==1
            original=(rank(n,prefix),rank(n,suffix))
            for a,b in ((0,1),(1,0),(0,n-1)):
                for i,j in combinations(range(m+2),2):
                    T=[];oldidx=0
                    for pos in range(m+2):
                        if pos==i:T.append((n,a))
                        elif pos==j:T.append((n,b))
                        else:
                            T.append(S[oldidx]);oldidx+=1
                    trials+=1
                    if not gossip(n+1,T):
                        continue
                    good+=1
                    assert i<n-1<=j,("new vertex failed to straddle",n,i,j,S)
                    assert (rank(n+1,T[:n-1]),rank(n+1,T[n-1:]))==original
        assert (count,degrees,trials,good)==expected,(
            n,(count,degrees,trials,good),expected
        )
        print(f"PASS n={n}: {count} optimal chronologies,"
              f" {degrees} degree2 vertices, {trials} insertion attempts,"
              f" {good} successful exact-rank-preserving insertions",flush=True)
    print("SCOPE: finite corroboration, NOT all-n half-forest proof",flush=True)

if __name__=="__main__":
    main()
