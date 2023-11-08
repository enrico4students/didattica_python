import random
print("\nTemperature giornaliere")
TANTI = 24
minValore = -10  # valore minimo
maxValore = 25   # massimo valore
minima = maxValore
massima = minValore
mioVettore = []  # definisco una lista
trovato = False
somma  = 0       # init accumulatore
# riempio un vettore di numeri casuali
x = 0
while x < TANTI:
  numero = random.randint(minValore, maxValore)
  mioVettore.append(numero)
  x = x + 1
# effettuo la ricerca 
x = 0
while x < len(mioVettore):
  if (minima > mioVettore[x]):
    minima = mioVettore[x]
    oraMin = x
  if (massima < mioVettore[x]):
    massima = mioVettore[x]
    oraMax = x
  x = x + 1
# comunico i risultati 
print("la temp minima e' stata ", minima, " alle ore ", oraMin)
print("la temp massima e' stata", massima, " alle ore ", oraMax)

#visualizzo il vettore completo 
print (mioVettore)


