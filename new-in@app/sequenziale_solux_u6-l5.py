import random
print("\nRicerca sequenziale in un vettore")
maxValore = 20   # massimo valore 
mioVettore = []  # definisco una lista
trovato = False
# riempio un vettore di numeri casuali
x = 0
while x < 10:
  numero = random.randint(1, maxValore)
  mioVettore.append(numero)
  x = x + 1
# effettuo la ricerca 
voluto = eval(input("numero da cercare: "))
x = 0
while x < len(mioVettore):
  if (voluto == mioVettore[x]):
    trovato = True
    posiz = x
    x = len(mioVettore)
  x = x + 1
# comunico i risultati 
if (trovato == True):
  print("Numero trovato in posizione", posiz)
else:
  print("\nNumero non trovato")  
#visualizzo il vettore completo 
print (mioVettore)  

