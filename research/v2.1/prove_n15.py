"""Build and execute the n=15 exact/relaxed finite profile certificate.

Run from repository root:
    python3 research/v2.1/prove_n15.py
No SAT/SMT dependencies: Python standard library, g++ with C++17.
"""
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'research'/'v2.0'))
from half_forest14_grid import run

def cases():
    for n,expected in ((13,(1278,9,0,0)),
                       (14,(4698,738,81,3)),
                       (15,(13680,4662,945,20))):
        eligible,basic,strong,orbits=run(n)
        assert (eligible,basic,strong,len(orbits))==expected,(
            n,eligible,basic,strong,len(orbits))
    orbits=run(15)[3]
    assert sum(orbits.values())==945
    lines=[]
    for i,((M,cyclic_row,cyclic_col),multiplicity) in enumerate(sorted(orbits.items())):
        values=[i,multiplicity,cyclic_row,cyclic_col]+[
            value for row in M for value in row]
        lines.append(' '.join(map(str,values)))
    return '\n'.join(lines)+'\n'

def main():
    from verify_n15_independent import audit
    from verify_profile_semantics import test_semantics
    source=HERE/'profile_oracle.cpp'
    with tempfile.TemporaryDirectory() as temp:
        executable=Path(temp)/'profile-oracle'
        subprocess.run(['g++','-O3','-std=c++17','-Wall','-Wextra',
                        str(source),'-o',str(executable)],check=True)
        result=subprocess.run([str(executable),'1','dump'],
                              input=cases(),text=True,capture_output=True,
                              check=True,timeout=480)
        print(result.stderr,flush=True)
        fresh=audit(result.stdout)
        test_semantics()
        recorded=json.loads((HERE/'N15_CERTIFICATE.json').read_text())
        for field in ('structural','orbits'):
            assert fresh[field]==recorded[field],('certificate mismatch',field)
        assert all(item['result'] in ('LOCAL_UNSAT','PROFILE_UNSAT')
                   for item in fresh['orbits'])
        print('PASS: all 20 UNSAT orbits cover 945 placements')
        print('SHA256 source:',hashlib.sha256(source.read_bytes()).hexdigest())
        print('SHA256 domain log:',hashlib.sha256(result.stdout.encode()).hexdigest())

if __name__=='__main__':
    main()
