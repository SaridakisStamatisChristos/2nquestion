"""Reproducible, adversarial n=9 POD check. No timeout is a refutation.

Input: v0.2/hard_seeds9.txt (length-prefixed list of edge sequences).
Requires scipy. Emits JSON with machine-checkable selected edges.
"""
import argparse
import importlib.util
import json
import random
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/'v0.5'/'frontier_solver_v05.py'
spec=importlib.util.spec_from_file_location('frontier',SRC)
frontier=importlib.util.module_from_spec(spec)
spec.loader.exec_module(frontier)

def read_seeds(path):
    lines=path.read_text().splitlines(); pos=0; out=[]
    while pos<len(lines):
        n_cases=int(lines[pos]);pos+=1
        for _ in range(n_cases):
            seq=[tuple(map(int,lines[i].split())) for i in range(pos,pos+36)]
            pos+=36
            assert len(set(seq))==36
            assert {tuple(sorted(p)) for p in seq}==set(frontier.complete_edges(9))
            out.append(seq)
        assert pos==len(lines)
    return out

def pivot_index(n,seq):
    state=[1<<i for i in range(n)];full=(1<<n)-1
    for t,(u,v) in enumerate(seq):
        if (state[u]|state[v])==full:
            reach=(1<<u)|(1<<v)
            for a,b in seq[t+1:]:
                if reach&(1<<a|1<<b):reach|=1<<a|1<<b
            if reach==full:return t
        both=state[u]|state[v];state[u]=state[v]=both
    return None

def greedy(n,seq,seed):
    rnd=random.Random(seed);order=list(range(len(seq)));rnd.shuffle(order)
    m=(1<<len(seq))-1
    for j in order:
        k=m&~(1<<j)
        if frontier.is_connected(n,seq,k):m=k
    return m

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-cases',type=int,default=4)
    parser.add_argument('--starts',type=int,default=1000)
    parser.add_argument('--seconds',type=float,default=8)
    args=parser.parse_args()
    cases=read_seeds(ROOT/'v0.2'/'hard_seeds9.txt')[:args.max_cases]
    records=[]
    for idx,seq in enumerate(cases):
        piv=pivot_index(9,seq)
        best=(37,None,None)
        for seed in range(args.starts):
            mask=greedy(9,seq,seed)
            if mask.bit_count()<best[0]:best=(mask.bit_count(),mask,seed)
            if best[0]==14:break
        status='WITNESS_14' if best[0]==14 else 'UNKNOWN'
        sol=None
        if status=='UNKNOWN':
            sol=frontier.solve(9,seq,upper=14,time_limit=args.seconds,max_rounds=300)
            if sol['mask'] is not None and sol['best_size']<=14:
                best=(sol['best_size'],sol['mask'],None);status='WITNESS_14'
            elif sol['status']=='PROVED_INFEASIBLE':status='CERTIFIED_NO_14'
        mask=best[1]
        assert mask is not None and frontier.is_connected(9,seq,mask)
        record={'case':idx,'pivot_contact_1based':piv+1 if piv is not None else None,
                'status':status, 'best_witness_size':best[0],
                'greedy_seed':best[2],
                'selected_contacts_1based':[j+1 for j in range(36) if mask>>j&1],
                'chronological_edges':seq,
                'solver':{k:v for k,v in sol.items() if k!='mask'} if sol else None}
        records.append(record)
        print(json.dumps({k:v for k,v in record.items() if k not in ('chronological_edges',)},sort_keys=True),flush=True)
    out=Path(__file__).with_name('certificates_pod9.json')
    out.write_text(json.dumps({'model':'distinct times, strictly increasing temporal paths', 'cases':records},indent=2)+'\n')
    print('WROTE',out,flush=True)
if __name__=='__main__':main()
