import random
TANTI = 15        
maxValore = 99   
numeri = []     
trovato = False
posizionibrutte= []

for  x in range (0,TANTI): 
  numeri.append(random.randint(1, maxValore))
  if x % 2 != numeri[x]%2==0:
          posizionibrutte.append(x)

out = ""
for x, numero in enumerate(numeri):
    out += "bad pos:"+str(x)+" " if x in posizionibrutte else ""
    out += str(numero)+", "
print(out)