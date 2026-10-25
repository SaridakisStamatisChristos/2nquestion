"""Independent regression check for the refuted v0.3 compulsory-edge bound.

Run with: python check_counter_v03.py
"""
from itertools import combinations
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from essential_poset import compulsory, precedence_matrix, info_at_end

COUNTEREXAMPLE = [(0,1),(1,3),(0,2),(0,3),(1,2),(2,3)]
EXPECTED_FORCED = {(1,3),(0,2),(0,3),(1,2)}


def analyze(n,seq):
    P=precedence_matrix(n,seq)
    minimal=[u for u in range(n) if not any(P[v][u] for v in range(n))]
    maximal=[u for u in range(n) if not any(P[u][v] for v in range(n))]
    forced={tuple(sorted((u,v))) for _,u,v in compulsory(n,seq)}
    bound=max(0, 2*n-len(minimal)-len(maximal)-1)
    return minimal,maximal,forced,bound


if __name__ == '__main__':
    s=COUNTEREXAMPLE
    assert len(s)==len(set(s))==6
    mini,maxi,forced,bound=analyze(4,s)
    assert mini==[0,1] and maxi==[2,3]
    assert forced==EXPECTED_FORCED
    assert len(forced)==4 and bound==3
    # A separate, direct pass through all four temporal events confirms
    # that the four compulsory edges happen to be a temporal spanner.
    forced_sequence=[e for e in s if e in forced]
    assert info_at_end(4,forced_sequence)==[15,15,15,15]
    print('PASS: K4 counterexample to |F| <= 2n-p-q-1')
    print('timestamps:',s)
    print('minima',mini,'maxima',maxi)
    print('forced',sorted(forced),'count',len(forced),'claimed bound',bound)
