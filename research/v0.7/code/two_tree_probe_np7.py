import itertools
N=7
TIMELINE=[(3,6),(5,6),(4,6),(3,4),(1,4),(0,6),(2,3),(3,5),(0,3),(2,5),(2,4),(1,6),(4,5),(0,5),(1,3),(1,5),(0,4),(2,6),(0,1),(1,2),(0,2)]
EDGES=list(itertools.combinations(range(N),2))
TIDX={e:i for i,e in enumerate(EDGES)}

def connected(mask):
  info=[1<<i for i in range(N)]
  for a,b in TIMELINE:
    if mask>>TIDX[min(a,b),max(a,b)]&1:
      new=info[a]|info[b];info[a]=info[b]=new
  return all(x==(1<<N)-1 for x in info)

# Construct 2trees in a completely separate Python enumerator.
out=set()
for init in itertools.combinations(range(N),3):
  base={tuple(sorted(x)) for x in itertools.combinations(init,2)}
  remaining=tuple(v for v in range(N) if v not in init)
  for order in itertools.permutations(remaining):
    states={frozenset(base)}
    for v in order:
      next_states=set()
      for state in states:
        for a,b in state:
          next_states.add(state|{tuple(sorted((v,a))),tuple(sorted((v,b)))})
      states=next_states
    for state in states:
      mask=sum(1<<TIDX[e] for e in state)
      out.add(mask)
print('2trees',len(out),'temporal spanners',sum(connected(mask) for mask in out))
