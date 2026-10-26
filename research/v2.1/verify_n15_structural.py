"""Necessary-condition n15 structural filter; DOES NOT certify UNSAT of survivors."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"v2.0"))
from half_forest14_grid import run

for n,expected in ((13,(1278,9,0,0)),(14,(4698,738,81,3)),(15,(13680,4662,945,20))):
    eligible,basic,strong,orbits=run(n)
    counts=(eligible,basic,strong,len(orbits))
    print(f"n={n} eligible={eligible} basic={basic} strong={strong} orbits={len(orbits)}",flush=True)
    assert counts==expected,(n,counts,expected)
print("PASS: exact necessary-condition counts; n15 chronology UNSAT NOT verified")
