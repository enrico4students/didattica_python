
from pathlib import Path

# percorso relativo
# path = Path("c:","windows", "win.ini")
# Errno 2] No such file or directory: 'c:windows\\win.ini'

win_ini_path = Path("c:\\","windows", "win.ini")
print(f"win_ini_path is {win_ini_path}")

# modalitù naive
file_obj = open(win_ini_path)
file_obj.close()

# percorso assoluto
home_path = Path.home()
print(f"home is {home_path}")

try:
    non_esiste = Path("c:\\","sdfsddfs", "hsrsr.ini")
    file_obj = open(non_esiste)
except FileNotFoundError as exc:
    print(f"eccezione di classe {type(exc)}: {exc}")

