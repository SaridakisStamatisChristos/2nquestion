"""Exact separable feasibility for a specified 3x3 intersection grid of a shortest gossip schedule.
Each half has n-2 contacts, each grid row/col forms one connected component.
Two tree components of size 5 and one triangle in each half (n=13).
"""
from itertools import combinations, permutations
from functools import lru_cache
import json,time

EXTRAS=((0,0),(0,1),(1,0),(1,1))
V=[(r,c) for r in range(3) for c in range(3)]+list(EXTRAS)
N=len(V)
ROW=[tuple(i for i,(r,c) in enumerate(V) if r==a) for a in range(3)]
COL=[tuple(i for i,(r,c) in enumerate(V) if c==a) for a in range(3)]

def connected(vertices,edges):
 p={v:v for v in vertices}
 def find(a):
  while p[a]!=a: a=p[a]
  return a
 for a,b in edges:p[find(a)]=find(b)
 return len({find(v) for v in vertices})==1

def transfer(seq,init):
 info=list(init)
 for a,b in seq:info[a]=info[b]=info[a]|info[b]
 return info

def opts(group,m,filter_node=None):
 edges=list(combinations(group,2))
 ret=[]
 for chosen in combinations(edges,m):
  if not connected(group,chosen):continue
  for order in permutations(chosen):
   if filter_node is not None:
    arr=[0]*N
    for v in group:arr[v]=1<<v
    state=transfer(order,arr)
    if state[filter_node]!=sum(1<<v for v in group):continue
   ret.append(order)
 return ret

def collisions(opt1,opt2):
 s=set(tuple(sorted(e)) for e in opt1)
 return any(tuple(sorted(e)) in s for e in opt2)

def bitset_for(rowidx, colidx, rowoptions, coloptions):
 target=COL[colidx]
 full=sum(1<<v for v in ROW[rowidx]); out=[]
 for ro in rowoptions:
  arr=[0]*N
  for v in ROW[rowidx]: arr[v]=1<<v
  pre=transfer(ro,arr)
  bits=0
  for j,co in enumerate(coloptions):
   if collisions(ro,co):continue
   post=transfer(co,pre)
   if all(post[v]==full for v in target):bits|=1<<j
  out.append(bits)
 return out

def run():
 t=time.time();prefix=[];suffix=[]
 for r in range(3):
  group=ROW[r]; sing=[v for v in group if sum(1 for w in group if V[w][1]==V[v][1])==1]
  # for this grid, tree rows have exactly one singleton in col2; triangle all full
  prefix.append(opts(group,len(group) if r==2 else len(group)-1,sing[0] if r!=2 else None))
 for c in range(3):suffix.append(opts(COL[c],len(COL[c]) if c==2 else len(COL[c])-1))
 print('N',N,'prefix options',list(map(len,prefix)),'suffix options',list(map(len,suffix)),flush=True)
 bits={}
 for c in (0,1):
  # C_c constraint broadcast of all row2 info from singleton source
  eligible=bitset_for(2,c,[prefix[2][0]],suffix[c])[0]
  for r in (0,1):
   bits[r,c]=[k & eligible for k in bitset_for(r,c,prefix[r],suffix[c])]
   print('built',r,c,'nonzero',sum(bool(k) for k in bits[r,c]),'elapsed',round(time.time()-t,2),flush=True)
 result=None
 for i in range(len(prefix[0])):
  if not bits[0,0][i] or not bits[0,1][i]:continue
  for j in range(len(prefix[1])):
   a=bits[0,0][i]&bits[1,0][j]
   if not a:continue
   b=bits[0,1][i]&bits[1,1][j]
   if b:
    s0=(a & -a).bit_length()-1;s1=(b & -b).bit_length()-1
    result={'n':N,'grid':V,'prefix':list(prefix[0][i])+list(prefix[1][j])+list(prefix[2][0]),'suffix':list(suffix[0][s0])+list(suffix[1][s1])+list(suffix[2][0]),'indices':[i,j,s0,s1]}
    break
  if result:break
 print('search_done',bool(result),'elapsed',round(time.time()-t,2),flush=True)
 if result:
  result['calls']=result['prefix']+result['suffix']
  # Direct information test independent of row splitting
  state=[1<<i for i in range(N)]
  for a,b in result['calls']:state[a]=state[b]=state[a]|state[b]
  result['all_gossip']=all(s==(1<<N)-1 for s in state)
  result['unique_edges']=len({tuple(sorted(e)) for e in result['calls']})==len(result['calls'])
  print('verifier',result['all_gossip'],result['unique_edges'],len(result['calls']))
  with open(str(__import__('pathlib').Path(__file__).with_name('candidate.json')),'w') as f:json.dump(result,f,indent=2)
 return result
if __name__=='__main__':run()
