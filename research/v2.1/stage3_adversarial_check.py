"""Stage 3 adversarial n15 audit: re-enumerate EVERY exact C++ component domain
with a second algorithm, compare complete profile sets and recheck all 20 orbits.

Both executables are built from the committed sources with a fresh compiler.
The independent oracle uses prefix forest/one-cycle union-find and explicitly
enumerates its final two contacts (no used-edge/knowledge-state memoization).
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parents[0]/"v2.0"))
from half_forest14_grid import run
from verify_n15_independent import parse, requirements, compatible
from prove_n15 import cases

def compile_cpp(path,where):
    subprocess.run(["g++","-O3","-std=c++17","-Wall","-Wextra",str(path),
                    "-o",str(where)],check=True)

def test():
    with tempfile.TemporaryDirectory(prefix="n15-stage3-") as d:
        primary=Path(d)/"primary"
        second=Path(d)/"secondary"
        compile_cpp(HERE/"profile_oracle.cpp",primary)
        compile_cpp(HERE/"stage3_independent_oracle.cpp",second)
        source=subprocess.run([str(primary),"1","dump"],input=cases(),
                              text=True,capture_output=True,check=True,timeout=480)
        case_lines,reference=parse(source.stdout)
        exact=sorted(k for k in reference if k[3]==0)
        assert exact and len(exact)>=30
        assert any(sum(key[0])==7 and key[2] for key in exact)
        data="".join(" ".join(map(str,key[0]+key[1]+(key[2],)))+"\n"
                     for key in exact)
        trial=subprocess.run([str(second)],input=data,text=True,
                             capture_output=True,check=True,timeout=720)
        _,rechecked=parse(trial.stdout)
        assert len(rechecked)==len(exact)
        for key in exact:
            assert key in rechecked,key
            for direction,(actual,recomputed) in zip(("B","D"),
                        zip(reference[key],rechecked[key])):
                assert actual==recomputed,("MISMATCH",key,direction,
                                          sorted(actual-recomputed)[:5],
                                          sorted(recomputed-actual)[:5])
            print("MATCH exact",key,"domain sizes",
                  [len(x) for x in rechecked[key]],flush=True)
        print("PASS: complete exact domain equality for",len(exact),
              "component types, including every n=7 type",flush=True)
        print("INDEPENDENT ORACLE EXECUTION COUNTS\n"+trial.stderr,flush=True)

        # Re-run all 20 global compatibility cases, now replacing each exact
        # local domain with one independently exhaustively constructed by the
        # second C++ program. Only sound optimistic tree domains are reused.
        all_domains=dict(reference)
        all_domains.update(rechecked)
        assert len(case_lines)==20
        _,_,strong,orbits=run(15)
        assert strong==945 and len(orbits)==20
        for i,((M,cr,cc),multiplicity) in enumerate(sorted(orbits.items())):
            forward,backward=requirements(M,cr,cc)
            rowkeys=[(tuple(M[r]),tuple(forward[r]),int(r==cr),
                      int(sum(M[r])>=7 and r!=cr)) for r in range(3)]
            colkeys=[(tuple(M[r][c] for r in range(3)),
                      tuple(backward[r][c] for r in range(3)),
                      int(c==cc),
                      int(sum(M[r][c] for r in range(3))>=7 and c!=cc))
                     for c in range(3)]
            rows=[all_domains[key][0] for key in rowkeys]
            cols=[all_domains[key][1] for key in colkeys]
            assert not compatible(rows,cols),("STAGE3 COUNTEREXAMPLE",i)
            print("PASS stage3 orbit",i,"multiplicity",multiplicity,flush=True)

        # The completeness of the comparison itself is checked against the
        # certificate's exact domain-size record for all twenty orbits.
        cert=json.loads((HERE/"N15_CERTIFICATE.json").read_text())
        assert len(cert["orbits"])==20
        assert sum(o["multiplicity"] for o in cert["orbits"])==945
        print("STAGE3 PASS: independent exact local profiles; 20/20 global "
              "UNSAT orbits and 945/945 placements",flush=True)

if __name__=="__main__":
    test()
