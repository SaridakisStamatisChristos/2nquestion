"""Stage 6: independently audited original-chronology structural frontier n=17.

Only necessary conditions; NOT an n17 half-forest proof. Tests the n=17
rectangular exclusions and independently enumerates the 3x3 orbit frontier.
The single-source-entry collector requirements are used in BOTH directions.

Usage: python3 research/v2.3/n17_structural.py
"""
from collections import Counter
from itertools import combinations,combinations_with_replacement,product
from pathlib import Path
import sys
BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE/"v2.0"))
sys.path.insert(0,str(BASE/"v2.1"))
sys.path.insert(0,str(BASE/"v2.2"))
from half_forest14_grid import run as original_run
from verify_n15_structural_independent import legal,canonical
from verify_n16_frontier import compositions

def rank_two_column_patterns():
    patterns=[]
    for c in range(4):
        p=[0]*4;p[c]=2;patterns.append(tuple(p))
    for a,b in combinations(range(4),2):
        p=[0]*4;p[a]=p[b]=1;patterns.append(tuple(p))
    assert len(set(patterns))==10
    return tuple(patterns)

def necessary_rectangular(M,cyclic_row,cycle_ranks):
    """Conservative necessary collector capacity with reverse-time obligations.

    Each prefix tree row can have <=2 complete midpoint collectors:
    - a singleton cell requires its sole vertex to be a collector;
    - for a suffix TREE receiving a singleton from any other prefix row,
      the first-bridge entry lemma requires a collector in this row's cell.

    Each suffix TREE has <=2 complete reverse collectors:
    - a singleton cell requires a reverse collector in that row;
    - for a prefix TREE with singleton in a different suffix column,
      reversing time yields a reverse collector in this column/row cell.
    """
    tree_rows=[r for r in range(3) if r!=cyclic_row]
    tree_cols=[c for c in range(4) if cycle_ranks[c]==0]
    for r in tree_rows:
        required={c for c in range(4) if M[r][c]==1}
        for c in tree_cols:
            if any(M[q][c]==1 for q in range(3) if q!=r):
                required.add(c)
        if len(required)>2:return 0
    for c in tree_cols:
        required={r for r in range(3) if M[r][c]==1}
        for r in tree_rows:
            if any(M[r][d]==1 for d in range(4) if d!=c):
                required.add(r)
        if len(required)>2:return 1
    return 2

def rectangular(n,method):
    """Two distinct generation methods: divider compositions vs extras multisets."""
    if method=="dividers":
        mats=(tuple(tuple(p[4*r:4*r+4]) for r in range(3))
              for p in compositions(n,12))
    elif method=="multisets":
        cells=tuple(product(range(3),range(4)))
        def matrix(extra):
            M=[[1]*4 for _ in range(3)]
            for r,c in extra:M[r][c]+=1
            return tuple(tuple(row) for row in M)
        mats=(matrix(e) for e in combinations_with_replacement(cells,n-12))
    else:raise ValueError(method)
    stage=[0,0,0]
    witnesses=[]
    for M in mats:
        for cr in range(3):
            for mask in rank_two_column_patterns():
                stage[0]+=1
                verdict=necessary_rectangular(M,cr,mask)
                if verdict>=1:stage[1]+=1
                if verdict>=2:
                    stage[2]+=1
                    if len(witnesses)<5:witnesses.append((M,cr,mask))
    return tuple(stage),witnesses

def square17():
    eligible,basic,strong,orbits=original_run(17)
    # Regenerate using independent positive integer compositions and a separate
    # strong-collector requirement implementation, compare the FULL orbit map.
    other=Counter()
    neligible=nstrong=0
    for parts in compositions(17,9):
        M=tuple(tuple(parts[3*r:3*r+3]) for r in range(3))
        for cr in range(3):
            for cc in range(3):
                if any(r!=cr and all(M[r][c]==1 for c in range(3))
                       for r in range(3)):continue
                if any(c!=cc and all(M[r][c]==1 for r in range(3))
                       for c in range(3)):continue
                neligible+=1
                if legal(M,cr,cc,True):
                    nstrong+=1
                    other[canonical(M,cr,cc)]+=1
    assert neligible==eligible==75933
    assert nstrong==strong==15777
    assert other==orbits,("orbit-by-orbit discrepancy",len(other),len(orbits))
    assert len(orbits)==256
    assert sum(orbits.values())==15777
    print("PASS n17 3x3 full orbit-map comparison: 75933 marked eligible,"
          f" {basic} basic, 15777 strongly surviving placements,"
          " 256 symmetry classes",flush=True)
    return orbits

def main():
    for n,expected in ((16,(40950,18,0)),(17,(131040,540,0))):
        a,w=rectangular(n,"dividers")
        b,z=rectangular(n,"multisets")
        assert a==b==expected,(n,a,b)
        assert not w and not z
        print(f"PASS 3x4 n={n}: {a[0]} marked assignments,"
              f" {a[1]} pass first collector bound,"
              f" {a[2]} pass both necessary collector bounds;"
              " two generators agree",flush=True)
    # For 4x4 on 17 vertices, only 1 vertex exceeds the 16 singleton
    # intersections. Any prefix TREE has >=3 singleton cells; at least
    # two tree prefix rows exist (total cycle rank 2), impossible.
    assert 17-4*4==1
    print("PASS 4x4 n17: >=2 tree rows, each >=3 singleton cells"
          " but at most two complete collectors",flush=True)
    # r=3,s>=5 needs >=3s+2(s-2)>=21.
    assert 3*5+2*(5-2)==21
    square17()
    print("FRONTIER: n17 both-cyclic requires r=s=3."
          " Surviving 256 classes are STRUCTURAL candidates only,"
          " not counterexamples; n17 full theorem OPEN.",flush=True)

if __name__=="__main__":main()
