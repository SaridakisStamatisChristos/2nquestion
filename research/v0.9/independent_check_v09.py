"""Independent checker; does not import MILP or historical solver code.
Verifies source reachability and nonpivotability for committed K9/K10 examples.
"""
import json,itertools,random
from pathlib import Path
HERE=Path(__file__).resolve().parent

def connected(n,seq,indices):
    selected=set(indices)
    for s in range(n):
        reach={s}
        for t,(u,v) in enumerate(seq,1):
            if t in selected and (u in reach or v in reach):
                reach.add(u);reach.add(v)
        if len(reach)!=n:return False
    return True

def pivots(n,seq):
    ans=[]
    for t,(a,b) in enumerate(seq):
        if all(any(w in R(s,seq[:t]) for w in (a,b)) for s in range(n)):
            reach={a,b}
            for x,y in seq[t+1:]:
                if x in reach or y in reach:reach.update((x,y))
            if len(reach)==n:ans.append(t+1)
    return ans

def R(s,seq):
    reach={s}
    for x,y in seq:
        if x in reach or y in reach:reach.update((x,y))
    return reach

def assert_chronology(n,seq):
    assert len(seq)==n*(n-1)//2
    assert {tuple(sorted(e)) for e in seq}==set(itertools.combinations(range(n),2))


def main():
    k9=json.loads((HERE/'nine_vertex_results.json').read_text())
    src=json.loads((HERE.parent/'v0.8/certificates_pod9.json').read_text())['cases']
    for case in k9:
        if case['name']=='adversarial':
            seq=json.loads((HERE.parent/'v0.8/adversarial_certificate.json').read_text())['sequence']
        else:
            idx=int(case['name'][4:]);seq=src[idx]['chronological_edges']
        assert_chronology(9,seq)
        assert pivots(9,seq)==[]
        assert len(case['selected_1based'])==14
        assert connected(9,seq,case['selected_1based'])
    print('PASS: 3 independently verified nonpivotable K9 instances with 14-edge witnesses')
    data=json.loads((HERE/'targeted_n10_results.json').read_text())
    assert data['nonpivot']==6
    for rec in data['records']:
        seq=rec['events']; assert_chronology(10,seq)
        assert pivots(10,seq)==[]
        r=rec.get('retry18',rec['result'])
        assert r['selected_1based'] is not None and len(r['selected_1based'])==16
        assert connected(10,seq,r['selected_1based'])
        # Reversing time preserves all-to-all connectivity (direction swaps).
        reverse_ids=[len(seq)+1-t for t in r['selected_1based']]
        assert connected(10,seq[::-1],reverse_ids)
        # Relabel vertices, preserving chronology, and verify again.
        perm=list(range(10));random.Random(1400+rec['attempt']).shuffle(perm)
        assert connected(10,[(perm[u],perm[v]) for u,v in seq],r['selected_1based'])
    print('PASS: 6 nonpivotable K10 chronologies with 16-edge spanners, time reversal and relabeling')
    print('Note: optimum for each instance follows from the external 2n-4 gossip lower bound.')
if __name__=='__main__':main()
