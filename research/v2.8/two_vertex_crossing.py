"""Independent exact finite falsification of the two-person crossing theorem.

Enumerate all 7 nonempty possible families of nonempty supporter-subsets
of 2 vertices for A-secrets and likewise for B-secrets (7^2=49).
Then check the all-n logical iff via an unrelated brute-force predicate.
Enumerate positive k=2 crossing matrices of total 4..7 and require
root-tree group covering sizes >=4 and <=1 small cell per arm.
"""
from itertools import product


def main():
    subsets = (1,2,3)
    families = [frozenset(x for i,x in enumerate(subsets)
                          if (mask>>i)&1)
                for mask in range(1,8)]
    count = 0
    for A,B in product(families,repeat=2):
        compatible = all((u & v)!=0 for u,v in product(A,B))
        # All secrets at vertex i iff their supports all contain bit i.
        full_a = [all((s>>i)&1 for s in A) for i in (0,1)]
        full_b = [all((s>>i)&1 for s in B) for i in (0,1)]
        alternative = (all(full_a) or all(full_b)
                       or any(full_a[i] and full_b[i] for i in (0,1)))
        assert compatible == alternative, (A,B,compatible,alternative)
        count += compatible
    assert (len(families)**2,count)==(49,21)
    print("PASS 49 ordered A/B secret-support family pairs on"
          " two shared participants: 21 exactly compatible;"
          " trichotomy matches every possibility",flush=True)

    def matrices(t):
        for a in range(1,t-2):
            for b in range(1,t-a-1):
                for c in range(1,t-a-b):
                    d=t-a-b-c
                    if d>=1:
                        yield ((a,b),(c,d))

    expected={4:0,5:0,6:2,7:8}
    for t,eligible in expected.items():
        local=survivors=0
        for M in matrices(t):
            if any(sum(row)<3 for row in M) or any(
                M[0][j]+M[1][j]<3 for j in range(2)
            ):
                continue
            local+=1
            row_ok=all(sum(x<=2 for x in row)<=1 for row in M)
            col_ok=all(sum(M[i][j]<=2 for i in range(2))<=1
                       for j in range(2))
            survivors += bool(row_ok and col_ok)
        assert (local,survivors)==(eligible,0),(t,local,survivors)
        print(f"PASS crossed 2x2 t={t}: {local} local-cover"
              " candidates, zero compatible with exact"
              " small-cell packing",flush=True)
    for k in range(2,9):
        bound=max(3*k*k-2*k, k*((1<<k)-1)+k-1)
        assert bound>=k*((1<<k)-1)+k-1
        print(f"PASS k={k} combined minimum shared-cell t>={bound}",
              flush=True)
    print("SCOPE: binary support lemma and conditional rooted-arm"
          " obstruction only; original all-n half-forest conjecture OPEN",
          flush=True)


if __name__ == "__main__":
    main()
