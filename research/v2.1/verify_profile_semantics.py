"""Independent direct gossip/profile temporal-duality and optimism validation."""
from random import Random

def gossip(steps,m,initial=None):
    state=[1<<i for i in range(m)] if initial is None else list(initial)
    for a,b in steps:
        state[a]=state[b]=state[a]|state[b]
    return state

def sufficiency(state,entries):
    full=(1<<len(state))-1
    output=0
    for mask in range(1<<len(entries)):
        combined=0
        for i,v in enumerate(entries):
            if mask>>i&1:combined|=state[v]
        if combined==full:output|=1<<mask
    return output

def test_semantics():
    rng=Random(20261026)
    for _ in range(3200):
        n=rng.randint(3,7)
        suffix=[tuple(rng.sample(range(n),2)) for _ in range(rng.randint(0,12))]
        prefix=[tuple(rng.sample(range(n),2)) for _ in range(rng.randint(0,8))]
        midpoint=gossip(prefix,n)
        entries=sorted(rng.sample(range(n),rng.randint(1,min(4,n))))
        # The reversed experiment marks all final destinations that can be
        # reached by a given entry in the original suffix order.
        reversed_tokens=gossip(suffix[::-1],n)
        transmitted=gossip(suffix,n,[midpoint[v] if v in entries else 0
                                     for v in range(n)])
        B=sufficiency(midpoint,entries)
        for destination in range(n):
            incoming=sum(1<<i for i,v in enumerate(entries)
                         if reversed_tokens[v]>>destination&1)
            assert bool(B>>incoming&1)==(transmitted[destination]==(1<<n)-1)
    print('PASS: 3,200 direct temporal-gossip/profile differential tests')

    # For a tree chronology, take its actual last edge x-y. Removing it
    # partitions preceding contacts into A and C. Each non-endpoint has seen
    # only secrets from its own side. Giving all side secrets is optimistic.
    for n in (7,8):
        for _ in range(120):
            edges=[(v,rng.randrange(v)) for v in range(1,n)]
            rng.shuffle(edges)
            before=gossip(edges[:-1],n)
            x,y=edges[-1]
            adjacent=[[] for _ in range(n)]
            for a,b in edges[:-1]:
                adjacent[a].append(b);adjacent[b].append(a)
            side={x};todo=[x]
            for a in todo:
                for b in adjacent[a]:
                    if b not in side:side.add(b);todo.append(b)
            sidebits=sum(1<<v for v in side)
            full=(1<<n)-1
            actual=gossip(edges,n)
            optimistic=[full if v in (x,y) else (sidebits if v in side else full^sidebits)
                        for v in range(n)]
            assert all(a&b==a for a,b in zip(actual,optimistic))
    print('PASS: 240 random tree chronologies dominated by optimistic side information')

if __name__=='__main__':
    test_semantics()
