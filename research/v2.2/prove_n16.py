"""Complete n=16 finite original-half-forest research certificate.

Proof obligations:
  - n16 rectangular 3x4/4x3 and 4x4 are impossible by collector lemmas;
  - 3x3 structural grids exhaust to 81 marked symmetry orbits / 4635 placements;
  - the primary C++ program yields sound exact/optimistic local domains;
  - both eight-vertex residual local types are replaced by independent EXACT
    Python side-chronology oracles;
  - the independent Stage-3 C++ enumerator reproduces ALL exact n16 domains;
  - a second Python global CSP checks EVERY orbit UNSAT.

Reproduces and audits; never infer n>=17 or mathematical novelty.
"""
from collections import Counter
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile

HERE=Path(__file__).resolve().parent
V21=HERE.parent/"v2.1"
sys.path.insert(0,str(HERE.parent/"v2.0"))
sys.path.insert(0,str(V21))
from verify_n16_frontier import n16_square,rectangular_attack,four_by_four_proof_check
from verify_n15_independent import parse,requirements,compatible
from exclude_n16_orbit10 import exact_profiles as tree8
from exclude_n16_orbit11 import exact_profiles as cycle8

def compile_cpp(path,executable):
    subprocess.run(["g++","-O3","-std=c++17","-Wall","-Wextra",
                    str(path),"-o",str(executable)],check=True)

def key_sets(M,cr,cc):
    forward,backward=requirements(M,cr,cc)
    rowkeys=[]
    colkeys=[]
    for r in range(3):
        grp=tuple(M[r])
        cyc=int(r==cr)
        n=sum(grp)
        opt=int((n>=7 and not cyc) or (n>=8 and cyc))
        rowkeys.append((grp,tuple(forward[r]),cyc,opt))
    for c in range(3):
        grp=tuple(M[r][c] for r in range(3))
        cyc=int(c==cc)
        n=sum(grp)
        opt=int((n>=7 and not cyc) or (n>=8 and cyc))
        colkeys.append((grp,tuple(backward[r][c] for r in range(3)),cyc,opt))
    return rowkeys,colkeys

def main():
    rectangular_attack()
    four_by_four_proof_check()
    orbits=n16_square()
    total_mult=sum(orbits.values())
    assert total_mult==4635 and len(orbits)==81
    cases=sorted(orbits.items())
    lines=[]
    for i,((M,cr,cc),mult) in enumerate(cases):
        lines.append(" ".join(map(str,[i,mult,cr,cc]+
                                  [v for row in M for v in row])))
    data="\n".join(lines)+"\n"

    # Both residual local solvers are exact; do not replace a real local
    # domain by an optimistic assignment or a merely assumed empty set.
    Tb,Td,tn=tree8()
    Cb,Cd,cn=cycle8()
    assert (Tb,Td,tn)==({(8,14,32768)},{(6,8,278)},48)
    assert (Cb,Cd,cn)==({(14,14,32768)},{(8,8,278)},144)
    special={
        ((2,2,4),(0,2,0),0,1):(Tb,Td),
        ((2,2,4),(2,2,0),1,1):(Cb,Cd),
    }

    with tempfile.TemporaryDirectory(prefix="n16_cert_") as temp:
        original=Path(temp)/"primary"
        independent=Path(temp)/"independent"
        source=HERE/"profile_oracle16_relaxed.cpp"
        compile_cpp(source,original)
        # It emits a fully enumerated domain inventory using the
        # 3x3 local profiles. For cyclic h=8 or tree h>=7 it gives a
        # deliberately optimistic superset, NEVER an incomplete subset.
        first=subprocess.run([str(original),"1","dump"],input=data,
                             text=True,capture_output=True,
                             check=True,timeout=700)
        reports,domains=parse(first.stdout)
        assert len(reports)==81
        # Independently re-enumerate every local EXACT component domain
        # used in this n16 certificate, including any new n7 patterns.
        exact_keys=sorted(k for k in domains if k[3]==0)
        assert exact_keys and all(sum(k[0])<=7 for k in exact_keys)
        compile_cpp(V21/"stage3_independent_oracle.cpp",independent)
        secondary_data="".join(" ".join(map(str,
                           k[0]+k[1]+(k[2],)))+"\n" for k in exact_keys)
        second=subprocess.run([str(independent)],input=secondary_data,
                              text=True,capture_output=True,
                              check=True,timeout=700)
        _,independent_domains=parse(second.stdout)
        assert set(independent_domains)==set(exact_keys)
        for key in exact_keys:
            assert domains[key]==independent_domains[key],(
                "independent n16 local-domain mismatch",key)
        print("PASS n16 second local oracle:",len(exact_keys),
              "complete exact B/D domain pairs independently matched",flush=True)
        print("SHA256 original C++ source:",
              hashlib.sha256(source.read_bytes()).hexdigest(),flush=True)
        print("SHA256 primary domain log:",
              hashlib.sha256(first.stdout.encode()).hexdigest(),flush=True)
        print("SHA256 second oracle domain log:",
              hashlib.sha256(second.stdout.encode()).hexdigest(),flush=True)

        # Substitute the two missing exact 8-vertex domains; repeat
        # all 81 global CSP questions independently of the C++ solver.
        all_domains=dict(domains)
        all_domains.update(special)
        original_counts=Counter()
        status_counts=Counter()
        certificate=[]
        for i,((M,cr,cc),mult) in enumerate(cases):
            rowkeys,colkeys=key_sets(M,cr,cc)
            old_rows=[domains[k][0] for k in rowkeys]
            old_cols=[domains[k][1] for k in colkeys]
            old_bad=any(not d for d in old_rows+old_cols)
            old_status="LOCAL_UNSAT" if old_bad else (
                "RELAXED_SAT" if compatible(old_rows,old_cols)
                else "PROFILE_UNSAT")
            original_counts[old_status]+=1
            assert f"CASE {i} " in reports[i] and (
                f"status={old_status}" in reports[i]),(
                "primary/independent CSP disagree",i,reports[i],old_status)
            rows=[all_domains[k][0] for k in rowkeys]
            cols=[all_domains[k][1] for k in colkeys]
            sat=compatible(rows,cols)
            if sat:
                raise AssertionError(("n16 compatible profile survives",
                                      i,M,cr,cc,mult))
            status=("LOCAL_UNSAT" if any(not d for d in rows+cols)
                    else "PROFILE_UNSAT")
            status_counts[status]+=1
            certificate.append({
                "orbit":i,"matrix":[list(row) for row in M],
                "cyclic_row":cr,"cyclic_column":cc,
                "multiplicity":mult,"original_relaxation":old_status,
                "final_result":status,
                "exact_eight_component_replaced":
                  any(k in special for k in rowkeys+colkeys),
                "row_domain_sizes":[len(x) for x in rows],
                "col_domain_sizes":[len(x) for x in cols],
            })
            print("N16_CERT_CASE",i,status,"mult",mult,
                  "old",old_status,flush=True)
        assert original_counts=={
            "LOCAL_UNSAT":13,"PROFILE_UNSAT":66,"RELAXED_SAT":2
        },original_counts
        assert status_counts=={"LOCAL_UNSAT":13,"PROFILE_UNSAT":68},status_counts
        assert len(certificate)==81
        assert sum(item["multiplicity"] for item in certificate)==4635
        assert [x["orbit"] for x in certificate
                if x["original_relaxation"]=="RELAXED_SAT"]==[10,11]
        print("PASS all 81 n16 marked orbits UNSAT; 4635/4635 placements",
              flush=True)
        print("PASS n16 classification: 13 empty-local and 68 global-profile"
              " exclusions, with exact eight-vertex oracles for orbit 10/11",
              flush=True)
        output={
            "claim":"bounded original chronological half-forest n<=16",
            "scope":"computer-assisted; assumes proved structural/collector lemmas",
            "structural":{"allocations_3x3":6435,"eligible":34092,
                          "basic":16704,"strong":4635,"orbits":81},
            "exact_local_types_independently_checked":len(exact_keys),
            "before_two_residual_refinements":dict(original_counts),
            "final_results":dict(status_counts),"orbits":certificate,
        }
        recorded=json.loads((HERE/"N16_CERTIFICATE.json").read_text())
        assert output==recorded,("stored n16 certificate mismatches freshly executed result")
        print("PASS immutable n16 JSON certificate matches all freshly verified domains, placements and orbit results",flush=True)
        print("N16_COMPLETE_CERTIFICATE_JSON",
              json.dumps(output,separators=(",",":"),sort_keys=True),flush=True)
        print("BOUNDARY: n>=17 and historical novelty remain UNRESOLVED",
              flush=True)

if __name__=="__main__":
    main()
