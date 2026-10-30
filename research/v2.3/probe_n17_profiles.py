"""Exploratory n17 3x3 temporal-profile necessary-condition CSP.

Replicates the same primary C++ local/profile model used for n16, but
on 3x3 orbit types with every row/column component size <=10.
The v2.3 verifier uses fixed 10-vertex C++ arrays and a fail-closed
capacity check, so >10 is NEVER silently processed. Cyclic components of size >=8 and trees of size >=7
are handled by documented *overapproximations*. UNSAT is meaningful
relative to the mathematical soundness of these relaxations; a SAT
assignment is NOT a realizable gossip schedule. Not an n17 proof.

Run: python3 research/v2.3/probe_n17_profiles.py
"""
from collections import Counter
from pathlib import Path
import json
import subprocess
import sys
import tempfile

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/"v2.0"))
from half_forest14_grid import run

def main():
    eligible,basic,strong,orbits=run(17)
    assert (eligible,basic,strong,len(orbits))==(75933,45783,15777,256)
    sorted_orbits=sorted(orbits.items())
    selected=[]
    deferred=[]
    for i,((M,cr,cc),mult) in enumerate(sorted_orbits):
        max_comp=max(*(sum(row) for row in M),
                     *(sum(M[r][c] for r in range(3)) for c in range(3)))
        max_group=max(max(row) for row in M)
        rec={"orbit":i,"matrix":[list(row) for row in M],
             "cyclic_row":cr,"cyclic_column":cc,"multiplicity":mult,
             "max_component":max_comp,"max_cell":max_group}
        if max_comp>10 or max_group>6:
            rec["status"]="DEFERRED_ORACLE_CAPACITY"
            deferred.append(rec)
        else:
            selected.append(rec)
    assert len(selected)+len(deferred)==256
    assert selected and sum(x["multiplicity"] for x in selected+deferred)==15777
    print("N17_START capacity=10 eligible=",eligible,"structural=",strong,
          "orbits=",len(orbits),"selected=",len(selected),
          "deferred=",len(deferred),flush=True)
    data="\n".join(" ".join(map(str,([z["orbit"],z["multiplicity"],
                                     z["cyclic_row"],z["cyclic_column"]]+
                        [t for row in z["matrix"] for t in row])))
                   for z in selected)+"\n"
    with tempfile.TemporaryDirectory() as temp:
        exe=Path(temp)/"n17"
        subprocess.run(["g++","-std=c++17","-O3","-Wall","-Wextra",
                        str(HERE/"profile_oracle17_relaxed.cpp"),
                        "-o",str(exe)],check=True)
        p=subprocess.run([str(exe),"1"],input=data,text=True,
                         stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                         timeout=1040,check=True)
    statuses={}
    for line in p.stdout.splitlines():
        assert line.startswith("CASE "),line
        spl=line.split()
        idx=int(spl[1])
        status=next(v.partition("=")[2] for v in spl
                    if v.startswith("status="))
        assert status in ("LOCAL_UNSAT","PROFILE_UNSAT","RELAXED_SAT")
        assert idx not in statuses
        statuses[idx]=status
    assert len(statuses)==len(selected),("missing C++ cases",
                                         len(statuses),len(selected))
    for z in selected:z["status"]=statuses[z["orbit"]]
    result=sorted(selected+deferred,key=lambda z:z["orbit"])
    counts=dict(Counter(z["status"] for z in result))
    weights={k:sum(z["multiplicity"] for z in result if z["status"]==k)
             for k in counts}
    assert sum(counts.values())==256
    assert sum(weights.values())==15777
    print("N17_COUNTS",json.dumps(counts,sort_keys=True),flush=True)
    print("N17_PLACEMENTS",json.dumps(weights,sort_keys=True),flush=True)
    residual=[z for z in result if z["status"] in
             ("RELAXED_SAT","DEFERRED_ORACLE_CAPACITY")]
    print("N17_RESIDUALS",json.dumps(residual,sort_keys=True),flush=True)
    print("N17_BOUNDARY: exploratory UNSAT classifications only,"
          " no proof that all n17 configurations excluded.",flush=True)

if __name__=="__main__":
    main()
