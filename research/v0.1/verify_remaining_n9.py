"""Reproduce hard n9 certificates via increased deterministic greedy starts."""
import json
from temporal_lab import greedy, is_spanner
p='nonpivot_survey.json'
data=json.load(open(p))
nine=next(x for x in data if x['n']==9)
for case in nine['hard']:
    seq=case['sequence']
    result=None
    for seed in range(2000):
        mask=greedy(9,seq,seed)
        if mask.bit_count()<=14:
            assert is_spanner(9,seq,mask)
            result=(seed,[i for i in range(len(seq)) if mask>>i&1]);break
    assert result is not None, ('unresolved',case['trial'])
    print('trial',case['trial'],'seed',result[0],'selected positions',result[1])
print('all',len(nine['hard']),'n9 initially hard cases yield <=14-edge witnesses')
