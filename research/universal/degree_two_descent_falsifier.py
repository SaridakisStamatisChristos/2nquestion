"""Universal-INDUCTION falsifier: degree-two temporal contraction is NOT sound.

A shortest distinct-edge n9 gossip schedule has a vertex with exactly two
contacts in each original chronological half. Suppressing the vertex in
each half by replacing its incident two-edge path with a direct contact
at the LATER of those two original timestamps gives an n8 schedule
with 12 distinct calls, but the latter FAILS exact all-to-all reachability.

This invalidates a tempting general induction without asserting anything
about the restricted BOTH-CYCLIC case (our example has no such promise).
"""
from collections import Counter

W8 = ((0,1),(4,5),(3,7),(2,6),(2,3),(1,5),
      (0,4),(1,2),(6,7),(4,6),(3,5),(0,7))


def replay(n,contacts):
    k=[1<<v for v in range(n)]
    for a,b in contacts:
        k[a]=k[b]=k[a]|k[b]
    return k


def suppress_later(half,x):
    times=[i for i,e in enumerate(half) if x in e]
    assert len(times)==2
    peers=[next(v for v in half[i] if v != x) for i in times]
    out=[]
    for i,e in enumerate(half):
        if i==times[0]:
            continue
        out.append(tuple(peers) if i==times[1] else e)
    assert len(out)==len(half)-1
    return out


def main():
    S=((8,0),)+W8+((8,1),)
    assert len(S)==2*9-4
    assert len(set(map(lambda e:tuple(sorted(e)), S)))==len(S)
    assert all(v==(1<<9)-1 for v in replay(9,S))
    x=1
    halves=(S[:7],S[7:])
    assert all(sum(x in edge for edge in half)==2 for half in halves)
    contracted=suppress_later(halves[0],x)+suppress_later(halves[1],x)
    remaining=[v for v in range(9) if v!=x]
    remap={v:i for i,v in enumerate(remaining)}
    S8=tuple((remap[a],remap[b]) for a,b in contracted)
    assert len(S8)==2*8-4
    assert len(set(map(lambda e:tuple(sorted(e)), S8)))==len(S8)
    information=replay(8,S8)
    missing={i:[source for source in range(8)
                if not (information[i]>>source)&1]
             for i in range(8) if information[i]!=(1<<8)-1}
    assert missing=={1:[3,4],7:[3,4]},missing
    print("PASS original n9: successful 14 distinct calls, x=1 degree2 in EACH half")
    print("PASS naive degree-two compression: 12 distinct calls, n8")
    print("REFUTED general induction: omitted sources",missing)
    print("SCOPE: not a counterexample to the half-forest conjecture")
    print("SCOPE: an unsound naive contraction cannot be a universal proof step")


if __name__=="__main__":
    main()
