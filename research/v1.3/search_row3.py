from itertools import combinations,permutations
import argparse,time,json,sys

def search(extra,cc,limit_sec=65):
 V=[(r,c) for r in range(3) for c in range(3)]+extra;N=len(V)
 rows=[tuple(i for i,(r,c) in enumerate(V) if r==p) for p in range(3)]
 cols=[tuple(i for i,(r,c) in enumerate(V) if c==p) for p in range(3)]
 def connected(group,edges):
  p={v:v for v in group}
  def rt(a):
   while p[a]!=a:a=p[a]
   return a
  for a,b in edges:p[rt(a)]=rt(b)
  return len({rt(v) for v in group})==1
 def prop(seq,src):
  d=list(src)
  for a,b in seq:d[a]=d[b]=d[a]|d[b]
  return d
 def opts(group,m,required=()):
  ed=list(combinations(group,2));full=sum(1<<v for v in group);arr=[]
  for chosen in combinations(ed,m):
   if not connected(group,chosen):continue
   for order in permutations(chosen):
    if required:
     q=[0]*N
     for v in group:q[v]=1<<v
     q=prop(order,q)
     if any(q[v]!=full for v in required):continue
    arr.append(order)
  return arr
 t=time.time()
 row=[opts(rows[i],len(rows[i]) if i==2 else len(rows[i])-1,tuple(v for v in rows[i] if i!=2 and sum(V[w][1]==V[v][1] for w in rows[i])==1)) for i in range(3)]
 col=[opts(cols[i],len(cols[i]) if i==cc else len(cols[i])-1) for i in range(3)]
 print('extra',extra,'cc',cc,'row lengths',list(map(len,row)),'col lengths',list(map(len,col)),flush=True)
 # triangle row2 full info irrespective of its chronology (need ensure)
 assert len(rows[2])==3
 tri_info=prop(row[2][0],[1<<i for i in range(N)])
 assert all(tri_info[v]==sum(1<<w for w in rows[2]) for v in rows[2])
 d={}
 for c in sorted(range(3),key=lambda k:len(col[k])):
  req2=sum(1<<v for v in rows[2]);q=[0]*N
  for v in rows[2]:q[v]=tri_info[v]&req2
  idx2=0
  for j,seq in enumerate(col[c]):
   s=prop(seq,q)
   if all(s[v]==req2 for v in cols[c]):idx2|=1<<j
  print('col',c,'src2 options',idx2.bit_count(),flush=True)
  if not idx2:return None
  for r in [0,1]:
   goal=sum(1<<v for v in rows[r]);d[r,c]=[]
   for order in row[r]:
    q=[0]*N
    for v in rows[r]:q[v]=1<<v
    q=prop(order,q)
    preedges=set(order)
    mask=0
    for j,seq in enumerate(col[c]):
     if not (idx2>>j)&1:continue
     if any(e in preedges for e in seq):continue
     post=prop(seq,q)
     if all(post[v]==goal for v in cols[c]):mask|=1<<j
    d[r,c].append(mask)
   print('built',r,c,'surviving',sum(bool(z) for z in d[r,c]),'secs',round(time.time()-t,2),flush=True)
   if not any(d[r,c]): print('PRUNED: no eligible suffix for row source',r,c);return None
  if time.time()-t>limit_sec:print('time limit intermediate');return None
 for i in range(len(row[0])):
  if not all(d[0,c][i] for c in range(3)):continue
  for j in range(len(row[1])):
   hit=[d[0,c][i]&d[1,c][j] for c in range(3)]
   if all(hit):
    chosen=[col[c][(hit[c]&-hit[c]).bit_length()-1] for c in range(3)]
    schedule=list(row[0][i])+list(row[1][j])+list(row[2][0])+sum([list(z) for z in chosen],[])
    q=[1<<k for k in range(N)];q=prop(schedule,q)
    good=all(v==(1<<N)-1 for v in q)
    print('FOUND',good,'unique',len(set(schedule))==len(schedule),'time',round(time.time()-t,2),flush=True)
    obj={'vertices':N,'grid':V,'extra':extra,'cycle_column':cc,'schedule':schedule,'valid':good}
    with open(str(__import__('pathlib').Path(__file__).with_name('success.json')),'w') as f:json.dump(obj,f,indent=2)
    return obj
 print('NONE layout',extra,'col cycle',cc,'secs',round(time.time()-t,2),flush=True)
 return None
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--pattern',type=int,default=0);ap.add_argument('--cc',type=int,default=2)
 a=ap.parse_args(); patterns=[[(0,0),(0,0),(1,1),(1,1)],[(0,0),(0,0),(1,1),(1,2)],[(0,0),(0,1),(1,0),(1,1)],[(0,0),(0,1),(1,0),(1,2)]]
 search(patterns[a.pattern],a.cc)
