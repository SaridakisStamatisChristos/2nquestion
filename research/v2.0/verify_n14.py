"""Run the full, deterministic n<=14 original half-forest certificate."""
from pathlib import Path
import subprocess,tempfile
from half_forest14_grid import main
from n14_final_cross import run as check_residual

def run():
    classes=main()
    root=Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory() as temp:
        exe=str(Path(temp)/'component')
        subprocess.run(['g++','-O3','-std=c++17',str(root/'local_component_exact.cpp'),'-o',exe],check=True)
        seen=[]
        for (matrix,r,c),multiplicity in sorted(classes.items()):
            if matrix==((1,1,2),(1,1,2),(2,2,2)):
                if (r,c)==(0,0):
                    inp='2 2 2 0 0 2 0\n'
                    expected=[360360,155520,4992,2880,0]
                elif (r,c)==(2,2):
                    inp='2 2 2 1 2 2 0\n'
                    expected=[3603600,2635200,369312,1728,0]
                else:raise AssertionError('Unexpected case')
                out=subprocess.run([exe],input=inp,capture_output=True,text=True,check=True).stdout.split()
                assert out[:3]==['RESULT','6',str(int(r==2))],out
                assert list(map(int,out[3:]))==expected,(out,expected)
                seen.append((matrix,r,c))
                print('PASS local UNSAT:',(r,c),'multiplicity',multiplicity,flush=True)
            else:
                assert (matrix,r,c)==(((1,1,2),(1,2,2),(2,2,1)),2,2)
        assert len(seen)==2
        check_residual()
    print('PASS: complete n14 finite theorem; classic vertex extension gives all 4<=n<=14')
if __name__=='__main__':run()
