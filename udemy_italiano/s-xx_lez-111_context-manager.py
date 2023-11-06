import os.path

path = os.path.join(".","udemy_italiano","risorse")
fname = "isolamisteriosa.txt"
pathname = os.path.join(path,fname)


print(f"in {os.getcwd()} provo ad aprire {pathname}")

file_obj = open(pathname)
print(f"file_obj è di tipo {type(file_obj)} l'encoding è {file_obj.encoding}")
file_obj.close()

with open(pathname) as file_obj:
    print(f"file_obj è di tipo {type(file_obj)} l'encoding è {file_obj.encoding}")
    print("il context manager chiuderà automaticamente il file")


# -------------------------------------------------------------------
with open(pathname, "rt") as file_obj: # rt = read, text
    contenuti = file_obj.read() # senza parametri legge l'intero file
    print(f"\n\ncontenuti è di tipo {type(contenuti)} ed è:\n{contenuti}")

print("\n"*3+"-"*10+".readline()"+"-"*10)
with open(pathname, "rt") as file_obj: # rt = read, text
    line = file_obj.readline()
    print(f".readline() -> {line}")


print("\n"*3+"-"*10+"files di testo sono iterabili"+"-"*10)
with open(pathname, "rt") as file_obj: # rt = read, text
    for i, line in enumerate(file_obj):
        print(f"{i+1:>3}: {line.strip()}")


print("\n"*3+"-"*10+".readlines*()"+"-"*10)
with open(pathname, "rt") as file_obj: # rt = read, text
    lines = file_obj.readlines()
    print(f"tipo oggetto ritornato da my_file.readlines() {type(lines)}")
    for line in lines:
        print(f"{i+1:>3}: {line.strip()}")
