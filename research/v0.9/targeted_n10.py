"""Hard nonpivotable K10 search by chronology-preserving extension of K9 seeds.
Any MIP timeout is UNKNOWN. Nonpivotability independently checked.
"""
from pathlib import Path
import json,random,time
from incident_milp import solve,check
HERE=Path(__file__).resolve().parent
cases=json.loads((HERE.parent/'v0.8/certificates_pod9.json').read_text())['cases']

def pivots(n,seq):
    piv=[]
    for t,(a,b) in enumerate(seq):
        for s in range(n):
            r={s}
            for x,y in seq[:t]:
                if x in r or y in r:r.update((x,y))
            if a not in r and b not in r:break
        else:
            r={a,b}
            for x,y in seq[t+1:]:
                if x in r or y in r:r.update((x,y))
            if len(r)==n:piv.append(t)
    return piv

def extension(seq,rng):
    added=[(v,9) for v in range(9)]
    rng.shuffle(added)
    positions=set(rng.sample(range(45),9))
    i=j=0;out=[]
    for t in range(45):
        if t in positions:out.append(added[j]);j+=1
        else:out.append(tuple(seq[i]));i+=1
    return out

def main():
    rng=random.Random(2026102509)
    records=[]; examined=0; nonpivot=0
    for attempt in range(30000):
        original=cases[attempt%len(cases)]['chronological_edges']
        seq=extension(original,rng);examined+=1
        if pivots(10,seq):continue
        nonpivot+=1
        print('EXACT CASE',nonpivot,'from attempt',attempt,flush=True)
        result=solve(10,seq,upper=16,seconds=3)
        records.append({'seed':2026102509,'attempt':attempt,'events':seq,'result':result})
        (HERE/'targeted_n10_results.json').write_text(json.dumps({'sampled':examined,'nonpivot':nonpivot,'records':records},indent=2)+'\n')
        print('RESULT',result['status'],result['cardinality'],result['time_sec'],flush=True)
        if result['status']=='INFEASIBLE_SOLVER_CERTIFIED':
            print('POD POTENTIAL COUNTEREXAMPLE; NEED INDEPENDENT REPRODUCTION',flush=True)
            break
        if nonpivot>=6:break
    payload={'sampled':examined,'nonpivot':nonpivot,'records':records}
    (HERE/'targeted_n10_results.json').write_text(json.dumps(payload,indent=2)+'\n')
    print('SUMMARY',examined,nonpivot,[(c['result']['status'],c['result']['cardinality']) for c in records],flush=True)
if __name__=='__main__':main()
