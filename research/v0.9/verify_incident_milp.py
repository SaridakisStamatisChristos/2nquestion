"""Independent brute-force check of incident-local MILP on complete edge-orderings."""
import itertools,random,json,sys
from pathlib import Path
from incident_milp import solve

def check(n,seq,selected):
    """Independent source-by-source propagation; no bitset implementation reused."""
    for src in range(n):
        reachable={src}
        for t,(u,v) in enumerate(seq):
            if t in selected and (u in reachable or v in reachable):
                reachable.update((u,v))
        if len(reachable)!=n:return False
    return True

def oracle(n,seq):
    m=len(seq)
    for k in range(m+1):
        for choose in itertools.combinations(range(m),k):
            if check(n,seq,set(choose)):
                return k
    raise AssertionError('full clique should connect')

rng=random.Random(20261025)
records=[]
for n,nsamp in [(3,6),(4,720),(5,120)]:
    edges=list(itertools.combinations(range(n),2))
    orders=list(itertools.permutations(edges)) if n<5 else [rng.sample(edges,len(edges)) for _ in range(nsamp)]
    for idx,seq in enumerate(orders):
        expect=oracle(n,seq)
        got=solve(n,seq,seconds=4)
        assert got['status']=='OPTIMAL' and got['cardinality']==expect,(n,idx,got,expect)
        # Exact feasibility at the impossible budget optimum-1, except n=3
        if idx<30:
            failed=solve(n,seq,upper=expect-1,seconds=4)
            assert failed['status']=='INFEASIBLE_SOLVER_CERTIFIED',(n,idx,failed)
        if idx<30:
            admissible=solve(n,seq,upper=expect,seconds=4)
            assert admissible['status']=='OPTIMAL' and admissible['cardinality']==expect,(n,idx,admissible)
    records.append({'n':n,'orders':len(orders),'full_optimum_checks':len(orders),
                    'infeasibility_at_opt_minus_one':min(30,len(orders)),
                    'feasibility_at_optimum':min(30,len(orders))})
    print('PASS',records[-1],flush=True)

p=Path(__file__).with_name('validation_results.json')
p.write_text(json.dumps(records,indent=2)+'\n')
print('WROTE',p)