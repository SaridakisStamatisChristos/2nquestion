"""Independent source-by-source reachability and metamorphic verification for v0.8.

Run: python research/v0.8/independent_verify_v08.py
Does not import v0.5 or v0.8 solver code.
"""
from __future__ import annotations
import itertools,json,random
from pathlib import Path

HERE=Path(__file__).resolve().parent

def check(n,seq,indices):
    selected=set(indices)
    if len(seq)!=n*(n-1)//2:raise AssertionError('not a clique schedule')
    if {tuple(sorted(e)) for e in seq}!={tuple(e) for e in itertools.combinations(range(n),2)}:raise AssertionError('bad edges')
    for s in range(n):
        seen={s}
        for j,(a,b) in enumerate(seq,1):
            if j not in selected:continue
            if a in seen or b in seen:
                seen.add(a);seen.add(b)
        if len(seen)!=n:return False
    return True

def pivot_by_earliest_arrivals(n,seq):
    # For each edge e, verify that all sources reach at least one endpoint BEFORE e,
    # and the two endpoints jointly reach all vertices using only edges AFTER e.
    possible=[]
    for i,(a,b) in enumerate(seq):
        everyone=True
        for s in range(n):
            seen={s}
            for x,y in seq[:i]:
                if x in seen or y in seen:
                    seen.update((x,y))
            if not ({a,b}&seen):everyone=False;break
        if not everyone:continue
        reached={a,b}
        for x,y in seq[i+1:]:
            if x in reached or y in reached:reached.update((x,y))
        if len(reached)==n:possible.append(i+1)
    return possible

def main():
    archive=json.loads((HERE/'certificates_pod9.json').read_text())['cases']
    assert len(archive)==14
    for c in archive:
        seq=[tuple(e) for e in c['chronological_edges']]
        assert c['pivot_contact_1based'] is None
        assert pivot_by_earliest_arrivals(9,seq)==[],c['case']
        chosen=c['selected_contacts_1based']
        assert len(chosen)==14 and check(9,seq,chosen),c['case']
        # Reversal duality: reversing all edge labels and retaining reversed
        # chronological positions preserves all ordered reachabilities.
        m=len(seq);dual=[m+1-t for t in chosen]
        assert check(9,seq[::-1],dual)
        # Vertex relabelling invariance.
        perm=list(range(9));random.Random(c['case']+20261025).shuffle(perm)
        newseq=[(perm[a],perm[b]) for a,b in seq]
        assert check(9,newseq,chosen)
    adv=json.loads((HERE/'adversarial_certificate.json').read_text())
    assert adv['pivot_contact'] is None
    assert not pivot_by_earliest_arrivals(9,[tuple(e) for e in adv['sequence']])
    assert len(adv['greedy_witness_indices_1based'])==14
    assert check(9,[tuple(e) for e in adv['sequence']],adv['greedy_witness_indices_1based'])
    # Exhaustive differential check against bitset information propagation
    # on all K4 chronologies and all 64 selected-edge subsets.
    def info_checker(n,seq,ids):
        I=[1<<i for i in range(n)]
        for j,(a,b) in enumerate(seq,1):
            if j in ids:
                z=I[a]|I[b];I[a]=I[b]=z
        return all(x==(1<<n)-1 for x in I)
    edges=list(itertools.combinations(range(4),2));cases=0
    for order in itertools.permutations(edges):
        for mask in range(1<<len(edges)):
            ids=[j+1 for j in range(len(edges)) if mask>>j&1]
            assert check(4,order,ids)==info_checker(4,order,ids)
            cases+=1
    print('PASS: 14/14 n9 certificates, independent non-pivot tests, reversal and relabelling')
    print('PASS: adversarial instance refuted by 14-edge witness')
    print('PASS: exhaustive 46,080 K4 (ordering,edge-subset) differential checks')
    print('TOTAL independent differential checks:',cases)
if __name__=='__main__':main()
