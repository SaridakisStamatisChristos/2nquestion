"""Test exactly what classical kernel-poset data does, and does NOT, decide.

This audit uses the old Labahn 6.1 p-grid verification, plus an explicit
same-event-poset sequence family where separate original-midpoint cycle ranks
differ for every n=8..16. Importantly this does NOT prove logical
independence of the "at least one half is a forest" conclusion from the
complete Labahn theory: all our witnesses satisfy that weaker conclusion.
"""
from pathlib import Path
import sys
BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE/"v1.5"))
sys.path.insert(0,str(BASE/"v1.8"))
from minimal_order_bridge import (
    W8,extensions,extend_to,gossip,cyclerank,poset,incident_orders,
    kernel,edge,
)
from verify_labahn61 import run as check_pgrid

def main():
    hist,examples,total=extensions(8,W8)
    assert total==51200
    assert dict(hist)=={(0,0):12800,(0,1):19200,(1,0):19200}
    A=examples[(0,1)]
    B=examples[(0,0)]
    checked=[]
    for n in range(8,17):
        a=extend_to(A,n); b=extend_to(B,n)
        assert len(a)==len(b)==2*n-4
        assert gossip(n,a) and gossip(n,b)
        assert len({edge(e) for e in a})==2*n-4
        assert len({edge(e) for e in b})==2*n-4
        assert incident_orders(n,a)==incident_orders(n,b)
        assert poset(a)==poset(b)
        assert kernel(n,a)==kernel(n,b)
        halfn=n-2
        ar=(cyclerank(n,a[:halfn]),cyclerank(n,a[halfn:]))
        br=(cyclerank(n,b[:halfn]),cyclerank(n,b[halfn:]))
        assert ar==(0,1) and br==(0,0)
        checked.append(n)
    print("PASS 51200 linear extensions of one optimal n8 event poset",flush=True)
    print("PASS distinct original midpoint ranks of same event poset"
          " at n=8..16:",checked,flush=True)
    check_pgrid()
    print("PASS Labahn 1995 Theorem 6.1 p-grid admissibility"
          " comparison for p=3..7",flush=True)
    print("LIMIT: this falsifies midpoint cycle rank DETERMINACY by"
          " the abstract event poset, but does NOT test all possible"
          " Labahn kernels/fringes or prove that n<=16 half-forest"
          " cannot be a corollary of full classical theory.",flush=True)

if __name__=="__main__":main()
