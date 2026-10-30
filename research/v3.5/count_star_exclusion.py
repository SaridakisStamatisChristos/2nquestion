"""Stage 18 exact necessary 3x3 incidence count after the all-n star obstruction.

Two independent methods: fully enumerate nine labelled cell occupancies;
and sum compressed off-corner pair extras p,q, center d, corner combinations.
These are NEVER counts of successful chronological gossip schedules.
"""
from itertools import product
from math import comb

BASE=(1,1,2,1,1,2,2,2,1)
FIXED={18:(1287,489,41,4),19:(3003,1365,221,41),
       20:(6435,3333,825,221),21:(12870,7359,2438,850),
       24:(75582,52293,28205,15517)}


def compositions(k,d):
    if d==1:
        yield (k,)
    else:
        for a in range(k+1):
            for rest in compositions(k-a,d-1):
                yield (a,)+rest


def predicates(m):
    upper=(m[2]==m[5]==2)
    lower=(m[6]==m[7]==2)
    if (upper or lower) and m[8]<9:
        return False,False,False
    if upper and lower and m[8]<64:
        return False,False,False
    s16=(m[2]+m[5]+m[8]>=8 and m[6]+m[7]+m[8]>=8)
    s18=(m[2]+m[5]+m[8]>=9 and m[6]+m[7]+m[8]>=9)
    return True,s16,s18


def full_enumeration(n):
    raw=stage15=stage16=stage18=0
    for extra in compositions(n-13,9):
        m=tuple(a+b for a,b in zip(BASE,extra))
        raw+=1
        p15,p16,p18=predicates(m)
        stage15+=p15
        stage16+=p15 and p16
        stage18+=p15 and p18
    return raw,stage15,stage16,stage18


def compressed(n):
    k=n-13
    s15=s16=s18=0
    for p in range(k+1):
        for q in range(k-p+1):
            for d in range(k-p-q+1):
                if (p==0 or q==0) and d<8:
                    continue
                if p==q==0 and d<63:
                    continue
                r=k-p-q-d
                weight=(p+1)*(q+1)*comb(r+3,3)
                s15+=weight
                if p+d>=3 and q+d>=3:
                    s16+=weight
                if p+d>=4 and q+d>=4:
                    s18+=weight
    return comb(k+8,8),s15,s16,s18


def main():
    for n in range(13,26):
        direct=full_enumeration(n)
        summed=compressed(n)
        assert direct==summed,(n,direct,summed)
        if n in FIXED:
            assert direct==FIXED[n],(n,direct,FIXED[n])
        print("PASS n",n,"raw, stage15, stage16, stage18:",*direct)
    for n in (26,30,40,75,76):
        raw,s15,s16,s18=compressed(n)
        assert 0<=s18<=s16<=s15<=raw
        print("PASS compressed n",n,raw,s15,s16,s18)
    print("PASS sound all-n size filter after global tree/star obstruction")
    print("NO global gossip schedule certified")


if __name__=="__main__":
    main()
