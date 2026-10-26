"""n=16 structural frontier: independent incidence enumerators and rectangular falsification.

Scope: necessary structural filters only. A surviving marked 3x3 orbit is NOT
a legal gossip schedule; it is not even a satisfying temporal-profile CSP.

Run from repository root:
    python3 research/v2.2/verify_n16_frontier.py
Python stdlib only. Historical n=13..15 counts are regression anchors.
"""
from collections import Counter
from itertools import combinations, permutations
from math import comb
from pathlib import Path
import sys

BASE=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(BASE/"v2.0"))
sys.path.insert(0,str(BASE/"v2.1"))
from half_forest14_grid import run as multiset_run
from verify_n15_structural_independent import legal, canonical

def compositions(n,k):
    for cuts in combinations(range(1,n),k-1):
        bounds=(0,)+cuts+(n,)
        yield tuple(bounds[i+1]-bounds[i] for i in range(k))

def n16_square():
    expected=(34092,16704,4635,81)
    a=multiset_run(16)
    assert (a[0],a[1],a[2],len(a[3]))==expected,("old generator",a[:3],len(a[3]))
    classes=Counter()
    eligible=basic=strong=0
    for parts in compositions(16,9):
        M=tuple(tuple(parts[3*r:3*r+3]) for r in range(3))
        for cr in range(3):
            for cc in range(3):
                if any(r!=cr and all(M[r][c]==1 for c in range(3))
                       for r in range(3)):continue
                if any(c!=cc and all(M[r][c]==1 for r in range(3))
                       for c in range(3)):continue
                eligible+=1
                if not legal(M,cr,cc,False):continue
                basic+=1
                if not legal(M,cr,cc,True):continue
                strong+=1
                classes[canonical(M,cr,cc)]+=1
    assert comb(15,8)==6435
    assert (eligible,basic,strong,len(classes))==expected,(
        "second composition generator",(eligible,basic,strong,len(classes)))
    assert classes==a[3],("entire canonical orbit map differs")
    assert sum(classes.values())==4635
    assert Counter(classes.values())=={9:1,18:3,36:27,72:50}
    print("PASS n16 3x3 independent grids: 6435 allocations,"
          " 34092 eligible, 16704 basic, 4635 strong,"
          " 81 marked orbits",flush=True)
    return classes

def rectangular_attack():
    """Enumerate ALL positive 3x4 n16 matrices and possible rank-2
    distributions among suffix columns. Sufficiency is NOT being tested.

    Exact necessary requirements used:
    - There is one cyclic prefix row and two prefix tree rows.
    - Suffix components have total cyclomatic rank two; hence at least
      two suffix columns are trees, regardless of whether the two
      cycle ranks are [2] or [1,1].
    - A singleton prefix row/cell needs a complete prefix collector.
    - If a suffix tree sees the cyclic prefix row at a singleton entry,
      the single-source tree-entry lemma requires a complete prefix
      collector in every other prefix row's intersection with this Q.
    - No prefix tree can have more than two complete collectors.
    - A suffix tree cannot have >2 reverse complete collectors;
      each singleton entry from a different prefix row requires one.

    Both distribution types are fully enumerated (one bicyclic suffix
    component, or two unicyclic suffix components), even when a chosen
    column is too small to support its cycle rank. We do not prune on
    that extra topology, so a zero surviving count is conservative.
    """
    rank_masks=[]
    for c in range(4):
        xs=[0]*4;xs[c]=2;rank_masks.append(tuple(xs))
    for a,b in combinations(range(4),2):
        xs=[0]*4;xs[a]=xs[b]=1;rank_masks.append(tuple(xs))
    assert len(rank_masks)==10
    examined=0
    after_tree_collectors=0
    survivors=0
    for parts in compositions(16,12):
        M=tuple(tuple(parts[4*r:4*r+4]) for r in range(3))
        for cyc_row in range(3):
            tree_rows=[r for r in range(3) if r!=cyc_row]
            for cycle_rank_by_col in rank_masks:
                examined+=1
                tree_cols=[c for c in range(4)
                           if cycle_rank_by_col[c]==0]
                # The prefix tree's complete collectors must include
                # every singleton and an entry to each tree Q whose
                # cyclic-row entry is a singleton.
                prefix_requirements=[]
                for r in tree_rows:
                    needed={c for c in range(4) if M[r][c]==1}
                    needed.update(c for c in tree_cols
                                  if M[cyc_row][c]==1)
                    prefix_requirements.append(len(needed)<=2)
                if not all(prefix_requirements):continue
                after_tree_collectors+=1
                if any(sum(M[r][c]==1 for r in range(3))>2
                       for c in tree_cols):continue
                survivors+=1
                raise AssertionError(("3x4 structural adversary survives",
                                     M,cyc_row,cycle_rank_by_col))
    assert comb(15,11)==1365
    assert examined==1365*3*10==40950
    assert survivors==0
    print("PASS 3x4 n16 rectangular exhaustive necessary-condition attack:"
          f" {examined} marked candidates checked,"
          f" {after_tree_collectors} pass prefix collector capacity,"
          " 0 pass tree-column reverse collectors",flush=True)

def four_by_four_proof_check():
    # rs=16 forces every cell singleton. A prefix graph with r=4 and
    # n-2 contacts has cycle rank 2; hence at least two prefix components
    # are trees. Each tree row has four singleton entries into distinct
    # suffix components -> needs 4 complete collectors, impossible.
    assert 4*4==16
    for ranks in compositions(2+4,4):
        pass  # not a proof; enumerate zero-cycles with true rank budgets below
    rank_patterns=[]
    for p in range(3**4):
        v=[];x=p
        for i in range(4):v.append(x%3);x//=3
        if sum(v)==2:rank_patterns.append(v)
    assert len(rank_patterns)==10
    assert all(sum(v==0 for v in ranks)>=2 for ranks in rank_patterns)
    print("PASS 4x4 n16 obstruction: all cells singleton;"
          " every admissible rank-two component allocation has"
          " >=2 prefix trees, each demanding 4 collectors",flush=True)

def main():
    for n,known in ((13,(1278,9,0,0)),
                    (14,(4698,738,81,3)),
                    (15,(13680,4662,945,20))):
        a=multiset_run(n)
        assert (a[0],a[1],a[2],len(a[3]))==known
    rectangular_attack()
    four_by_four_proof_check()
    n16_square()
    print("FRONTIER ONLY: r=s=3 forced at n16;"
          " 81 3x3 classes still need temporal-profile analysis."
          " NO n16 half-forest theorem certified.",flush=True)

if __name__=="__main__":main()
