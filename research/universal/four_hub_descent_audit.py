"""Independent combinatorial audit of the ALL-n four-hub minimal descent.

Proof in FOUR_HUB_MINIMAL_DESCENT.md. This enumeration is ONLY of
FOUR possible hub placements, not a finite-n gossip chronology census.
No actual crossed-tree example is assumed to exist.
"""
from itertools import product


def all_hub_assignments():
    # Each second local last-call endpoint is one vertex:
    # outside X or in ONE of its own TWO row/column quadrants.
    choices = (
        (None,(0,0),(0,1)),  # y0 terminal complete in T0
        (None,(1,0),(1,1)),  # y1 terminal complete in T1
        (None,(0,0),(1,0)),  # z0 terminal complete in U0
        (None,(0,1),(1,1)),  # z1 terminal complete in U1
    )
    return product(*choices)


def analyze(assignment):
    y0,y1,z0,z1=assignment
    covered={x for x in assignment if x is not None}
    allquadrants={(0,0),(0,1),(1,0),(1,1)}
    free=allquadrants-covered
    return covered,free


def main():
    configurations=list(all_hub_assignments())
    assert len(configurations)==81
    fully_covered=[]
    with_free=[]
    for c in configurations:
        covered,free=analyze(c)
        if free:with_free.append((c,free))
        else:fully_covered.append(c)
    # There are precisely 2 possible deranged four-corner assignments:
    expected={
        ((0,0),(1,1),(1,0),(0,1)),
        ((0,1),(1,0),(0,0),(1,1)),
    }
    assert set(fully_covered)==expected,(fully_covered,expected)
    assert len(with_free)==79
    for c in fully_covered:
        y0,y1,z0,z1=c
        assert len(set(c))==4
        assert y0[0]!=y1[0] and y0[1]!=y1[1]
        assert z0[1]!=z1[1] and z0[0]!=z1[0]
        print("PASS unavoidable minimal four-hub assignment",c)
    for c,free in with_free:
        assert len(free)>=1
    print("PASS 81 possible original-side hub placements: 79 admit a strict"
          " hub-free quadrant, precisely 2 force alternate diagonals")
    print("HUMAN ALL-n proof: when a quadrant avoids both full local"
          " last-contact endpoints, it forms a STRICTLY SMALLER crossed"
          " original-order pair and remains doubly covering")
    print("LIMIT: no all-width crossed-tree example constructed or excluded")
    print("LIMIT: minimal deranged four-hub case remains OPEN")
    print("LIMIT: global original-half forest and 2n-3 spanner OPEN")


if __name__=="__main__":
    main()
