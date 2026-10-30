"""Exploratory n16 local/profile CSP scan using the established n15 C++ oracle.

IMPORTANT: This is NOT a full n16 verifier. Exact components of size >7
are deliberately skipped (the existing oracle cannot enumerate them).
Tree components of size >=7 are conservatively *optimistic*, so UNSAT is
sound for a scanned orbit under the established mathematical reductions;
RELAXED_SAT is not a legal schedule/counterexample.

Outputs an inspectable JSON report + concise stdout per orbit.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
V20=HERE.parent/"v2.0"
V21=HERE.parent/"v2.1"
sys.path.insert(0,str(V20))
from half_forest14_grid import run

def main():
    eligible,basic,strong,orbits=run(16)
    assert (eligible,basic,strong,len(orbits))==(34092,16704,4635,81)
    all_cases=list(sorted(orbits.items()))
    selected=[]
    deferred=[]
    for index,((M,cr,cc),mult) in enumerate(all_cases):
        rc=sum(M[cr])
        ccsize=sum(M[r][cc] for r in range(3))
        record={"orbit":index,"matrix":[list(row) for row in M],
                "cyclic_row":cr,"cyclic_column":cc,
                "multiplicity":mult,"cyclic_sizes":[rc,ccsize]}
        if rc>7 or ccsize>7:
            record["status"]="UNTESTED_OVERSIZED_CYCLE"
            deferred.append(record)
        else:
            selected.append(record)
    assert sum(x["multiplicity"] for x in selected+deferred)==4635
    lines=[]
    for item in selected:
        M=item["matrix"]
        args=[item["orbit"],item["multiplicity"],
              item["cyclic_row"],item["cyclic_column"]]
        args.extend(v for row in M for v in row)
        lines.append(" ".join(map(str,args)))
    data="\n".join(lines)+"\n"
    print("N16_CSP_START selected=",len(selected),
          "deferred_large_cycle=",len(deferred),flush=True)
    with tempfile.TemporaryDirectory(prefix="n16_profile_") as folder:
        executable=Path(folder)/"oracle"
        subprocess.run(["g++","-O3","-std=c++17","-Wall","-Wextra",
                        str(V21/"profile_oracle.cpp"),"-o",str(executable)],
                       check=True)
        results=subprocess.run([str(executable),"1"],input=data,
                               text=True,capture_output=True,
                               check=True,timeout=1050)
    outcomes={}
    for line in results.stdout.splitlines():
        assert line.startswith("CASE "),line
        tokens=line.split()
        ix=int(tokens[1])
        status=[x.removeprefix("status=") for x in tokens
                if x.startswith("status=")]
        assert len(status)==1
        assert status[0] in ("LOCAL_UNSAT","PROFILE_UNSAT","RELAXED_SAT")
        assert ix not in outcomes
        outcomes[ix]=status[0]
        print("N16_PROFILE",line,flush=True)
    assert len(outcomes)==len(selected),("missing orbit result",len(outcomes))
    for item in selected:item["status"]=outcomes[item["orbit"]]
    ordered=sorted(selected+deferred,key=lambda d:d["orbit"])
    tally={}
    for item in ordered:tally[item["status"]]=tally.get(item["status"],0)+1
    report={"claim":"EXPLORATORY 3x3 n16 profile necessary-condition scan",
            "caveat":"Large cycles >7 deferred; optimistic tree domains; SAT is NOT an actual gossip schedule",
            "structural":{"eligible":eligible,"basic":basic,
                          "strong":strong,"orbits":len(orbits)},
            "counts":tally,"orbits":ordered}
    print("N16_PROFILE_COUNTS",json.dumps(tally,sort_keys=True),flush=True)
    print("N16_PROFILE_REPORT_JSON",json.dumps(report,separators=(",",":")),flush=True)
    print("N16_CSP_DONE: NEVER infer full n16 theorem without"
          " checking RELAXED_SAT and untested oversized-cycle classes.",flush=True)
if __name__=="__main__":main()
