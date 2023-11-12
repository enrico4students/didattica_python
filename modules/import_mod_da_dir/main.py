import my_dir.modulo_in_dir
import sys
import os

print(f"in main script, work dir {os.getcwd()}")
for mydir in sorted(sys.path, key=len, reverse=True):
    print(f"import dir> {mydir}")

my_dir.modulo_in_dir.funzione()
