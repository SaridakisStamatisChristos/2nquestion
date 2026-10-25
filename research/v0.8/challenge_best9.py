"""Verify the adversarial schedule with independent greedy deletion and exact MILP feasibility.
Statuses UNKNOWN on timeouts are not counterexamples. Absolute contact order is significant.
"""
from __future__ import annotations
import argparse,importlib.util,json,random
from pathlib import Path
from certify_pod9 import frontier,pivot_index,greedy

def main():
 p=argparse.ArgumentParser();p.add_argument('--greedy-starts',type=int,default=50000);p.add_argument('--seconds',type=float,default=35);a=p.parse_args()
 here=Path(__file__).resolve().parent
 rows=here.joinpath('adversarial_best9.txt').read_text().splitlines()
 seq=[tuple(map(int,s.split())) for s in rows[1:]]
 assert len(seq)==36 and {tuple(sorted(e)) for e in seq}==set(frontier.complete_edges(9))
 piv=pivot_index(9,seq)
 best=36;witness=None;winning_seed=None
 for seed in range(a.greedy_starts):
  mask=greedy(9,seq,seed)
  if mask.bit_count()<best:
   best=mask.bit_count();witness=mask;winning_seed=seed
  if best==14:break
 assert frontier.is_connected(9,seq,witness)
 print('greedy_best',best,'seed',winning_seed,'pivot',piv,flush=True)
 sol=None
 if best>14:
  sol=frontier.solve(9,seq,upper=14,time_limit=a.seconds,max_rounds=250,verbose=False)
  print('MILP', {k:v for k,v in sol.items() if k!='mask'},flush=True)
  if sol['mask'] is not None:
   assert frontier.is_connected(9,seq,sol['mask'])
 result={'n':9,'sequence':seq,'pivot_contact':piv,'greedy_starts':a.greedy_starts,
   'best_greedy_size':best,'greedy_seed':winning_seed,
   'greedy_witness_indices_1based':[i+1 for i in range(36) if witness>>i&1],
   'milp':{k:v for k,v in sol.items() if k!='mask'} if sol else None,
   'milp_witness_indices_1based':[i+1 for i in range(36) if sol and sol['mask'] is not None and sol['mask']>>i&1]}
 here.joinpath('adversarial_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
 print('certificate recorded; 14-edge existence status', 'YES' if best==14 or (sol and sol['mask'] is not None) else 'UNKNOWN' if not sol or sol['status']!='PROVED_INFEASIBLE' else 'NO_CERTIFIED',flush=True)
if __name__=='__main__':main()
