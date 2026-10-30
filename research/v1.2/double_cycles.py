import itertools, collections,time,sys

def find_case(extra,cycrow=0,cyccol=0,verbose=False):
    V=[(r,c,0) for r in range(3) for c in range(3)]+[(r,c,k+1) for k,(r,c) in enumerate(extra)]
    n=len(V);R=[[v for v,(r,c,_) in enumerate(V) if r==i] for i in range(3)];C=[[v for v,(r,c,_) in enumerate(V) if c==i] for i in range(3)]
    # if duplicates in same cell unique label index still good
    @functools_cache
    def seqs(tuplegroup,numedges):
      group=tuplegroup;m=len(group);ed=list(itertools.combinations(group,2));
      ret=[]
      for choose in itertools.combinations(ed,numedges):
       for seq in itertools.permutations(choose):
        p={v:v for v in group}
        def root(v):
         while p[v]!=v:v=p[v]
         return v
        for a,b in seq:
         ra=root(a);rb=root(b);p[ra]=rb
        if len({root(v) for v in group})!=1:continue
        inf={v:1<<v for v in group}
        for a,b in seq:inf[a]=inf[b]=inf[a]|inf[b]
        ret.append((seq,inf))
      return ret
    def foptions(groups, other_group_id, special, backwards=False):
      arr=[]
      for i,grp in enumerate(groups):
        seq=seqs(tuple(grp),len(grp) if i==special else len(grp)-1)
        full=sum(1<<v for v in grp)
        sing=[v for v in grp if sum(1 for w in grp if V[w][other_group_id]==V[v][other_group_id])==1]
        def filt(item):
          s=item[0]
          info={v:1<<v for v in grp}
          for a,b in (reversed(s) if backwards else s):info[a]=info[b]=info[a]|info[b]
          return all(info[v]==full for v in sing)
        arr.append([item[0] for item in seq if filt(item)])
      return arr
    rowopts=foptions(R,1,cycrow)
    colopts=foptions(C,0,cyccol,True)
    if verbose:print('layout',extra,R,C,'options',list(map(len,rowopts)),list(map(len,colopts)),flush=True)
    if not all(map(bool,rowopts+colopts)):return None
    full=(1<<n)-1
    for rowcombo in itertools.product(*rowopts):
      inf={v:1<<v for v in range(n)}
      used=set()
      for seq in rowcombo:
       for a,b in seq:inf[a]=inf[b]=inf[a]|inf[b];used.add((min(a,b),max(a,b)))
      chosen=[]
      for c in sorted(range(3),key=lambda c:len(colopts[c])):
       col=C[c]
       success=False
       for seq in colopts[c]:
        if any((min(a,b),max(a,b)) in used for a,b in seq):continue
        state={v:inf[v] for v in col}
        for a,b in seq:state[a]=state[b]=state[a]|state[b]
        if all(state[v]==full for v in col):
          success=True;chosen.append(seq);break
       if not success:break
      if len(chosen)==3:return {'V':V,'R':R,'C':C,'rows':rowcombo,'cols':chosen}
    return None

def functools_cache(f):
    return __import__('functools').lru_cache(None)(f)

if __name__=='__main__':
  t=time.time()
  for row in range(3):
   for col in range(3):
    result=find_case([(0,0),(1,1),(2,2)],row,col,True)
    print('attempt',row,col,'found',bool(result),'elapsed',round(time.time()-t,2),flush=True)
    if result:
      print(result);quit()
