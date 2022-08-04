import subprocess
patt = input("path packages : ")
patt = patt.replace("\\", "/")
process = subprocess.Popen(['rm', '-rf', f'{patt}/tess'])
