"""Stage 16 exact labelled 3x3 NECESSARY incidence counts.

Two independent implementations:
  (1) iterate all nine cell additions;
  (2) compress the four corners and two off-corner pairs to p,q,d,
      then weigh by (p+1)(q+1)*C(r+3,3).
These are not chronologically valid gossip-schedule counts.
"""
from math import comb


BASE=(1,1,2,1,1,2,2,2,1)


def compositions(k, width):
    if width == 1:
        yield (k,)
        return
    for x in range(k+1):
        for rest in compositions(k-x,width-1):
            yield (x,)+rest


def allowed(m, upgraded):
    # Off-corner pairs on either side equal 2,2?
    top = m[2] == m[5] == 2
    left = m[6] == m[7] == 2
    if (top or left) and m[8] < 9:
        return False
    if top and left and m[8] < 64:
        return False
    if upgraded and (m[2]+m[5]+m[8] < 8 or m[6]+m[7]+m[8] < 8):
        return False
    return True


def brute(n):
    count0 = count15 = count16 = 0
    for extra in compositions(n-13,9):
        m=tuple(a+b for a,b in zip(BASE,extra))
        count0+=1
        if not allowed(m,False):
            continue
        count15+=1
        if allowed(m,True):
            count16+=1
    return count0,count15,count16


def formula(n):
    k=n-13
    total15=total16=0
    for p in range(k+1):
        for q in range(k-p+1):
            for d in range(k-p-q+1):
                if (p==0 or q==0) and d<8:
                    continue
                if p==q==0 and d<63:
                    continue
                r=k-p-q-d
                ways=(p+1)*(q+1)*comb(r+3,3)
                total15+=ways
                if p+d>=3 and q+d>=3:
                    total16+=ways
    return comb(k+8,8),total15,total16


EXPECTED={
  13:(1,0,0),
  14:(9,0,0),
  15:(45,4,0),
  16:(165,32,0),
  17:(495,145,4),
  18:(1287,489,41),
  19:(3003,1365,221),
  20:(6435,3333,825),
  21:(12870,7359,2438),
  24:(75582,52293,28205),
}


def main():
    print("n raw_3x3 stage15 stage16")
    for n in range(13,26):
        a=brute(n)
        b=formula(n)
        assert a==b,(n,a,b)
        if n in EXPECTED:
            assert a==EXPECTED[n],(n,a,EXPECTED[n])
        print(n,*a)
    for n in (26,30,40,75,76):
        raw,prev,now=formula(n)
        assert 0<=now<=prev<=raw
        print(n,raw,prev,now,"closed-form only")
    # n=18 center can only have two, three, or four people.
    centers=set()
    for extra in compositions(18-13,9):
        m=tuple(a+b for a,b in zip(BASE,extra))
        if allowed(m,True):centers.add(m[8])
    assert centers=={2,3,4},centers
    print("PASS independent 9D enumeration vs compressed triple sum n=13..25")
    print("PASS n18 size-only center membership {2,3,4}")
    print("NO actual global gossip chronology is certified")


if __name__=="__main__":
    main()
