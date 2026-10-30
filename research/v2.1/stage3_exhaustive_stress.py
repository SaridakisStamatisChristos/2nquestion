"""Independent exhaustive stress tests for the n=15 proof's pruning and duality.

Run as a separate program from the two component oracles; do not import their
code, data structures, or validity predicates.
"""
from itertools import permutations, combinations
from collections import Counter

def connected(n,seq):
    parent=list(range(n))
    def root(a):
        while a!=parent[a]:a=parent[a]
        return a
    for a,b in seq:parent[root(a)]=root(b)
    return len({root(v) for v in range(n)})==1

def propagate(n,seq,initial=None):
    state=list(initial) if initial is not None else [1<<v for v in range(n)]
    for u,v in seq:
        merged=state[u]|state[v]
        state[u]=merged
        state[v]=merged
    return state

def pruning_and_optimism():
    counts=Counter()
    for n in (3,4,5,6):
        edges=tuple(combinations(range(n),2))
        for cyclic in ((False,True) if n<=5 else (False,)):
            length=n-1+int(cyclic)
            for contacts in permutations(edges,length):
                counts[(n,cyclic,"raw")]+=1
                if not connected(n,contacts):continue
                counts[(n,cyclic,"connected")]+=1
                state=propagate(n,contacts)
                full=(1<<n)-1
                last2={p for e in contacts[-2:] for p in e}
                if cyclic:
                    assert all(state[v]!=full for v in range(n) if v not in last2),(
                        "cyclic end-contact pruning counterexample",n,contacts)
                    prefix=propagate(n,contacts[:n-2])
                    assert all(k!=full for k in prefix),(
                        "full knowledge while static graph disconnected",n,contacts)
                else:
                    last=set(contacts[-1])
                    assert all(state[v]!=full for v in range(n) if v not in last),(
                        "tree end-contact pruning counterexample",n,contacts)
                    # Removing the last tree edge splits into disjoint prior
                    # components. Full information at endpoints and own-side
                    # information everywhere else dominates actual knowledge.
                    a,b=contacts[-1]
                    graph=[[] for _ in range(n)]
                    for u,v in contacts[:-1]:
                        graph[u].append(v);graph[v].append(u)
                    side={a};pending=[a]
                    for v in pending:
                        for w in graph[v]:
                            if w not in side:
                                pending.append(w);side.add(w)
                    assert b not in side,("last edge did not bridge",n,contacts)
                    Amask=sum(1<<v for v in side)
                    optimistic=[full if v in last else
                                (Amask if v in side else full^Amask)
                                for v in range(n)]
                    assert all(actual&dominated==actual
                               for actual,dominated in zip(state,optimistic)),(
                        "optimistic tree is not an overapproximation",n,contacts)
    assert counts[(6,False,"raw")]==360360
    assert counts[(6,False,"connected")]==155520
    print("PASS: exhaustive collector/pruning and optimistic-tree containment")
    for n,cy in sorted(set((k[0],k[1]) for k in counts)):
        print("  n=%s cyclic=%s raw=%d connected=%d"%(n,cy,
              counts[(n,cy,"raw")],counts[(n,cy,"connected")]))

def backward_duality():
    # Independent forward propagation with an isolated source, versus backward
    # all-token propagation: all prefix/suffix temporal reachability pairs.
    total=0
    E=tuple(combinations(range(4),2))
    for length in range(5):
        for seq in permutations(E,length):
            reverse=propagate(4,seq[::-1])
            for src in range(4):
                initial=[0]*4
                initial[src]=1<<src
                forward=propagate(4,seq,initial)
                for dst in range(4):
                    assert bool(forward[dst]&(1<<src))==bool(
                        reverse[src]&(1<<dst)),("temporal reverse duality",
                                             seq,src,dst)
            total+=1
    assert total==517
    print("PASS: exhaustive original/reversed temporal reachability "
          "on 517 distinct-edge K4 sequences and 8,272 (source,destination) checks")

if __name__=="__main__":
    pruning_and_optimism()
    backward_duality()
