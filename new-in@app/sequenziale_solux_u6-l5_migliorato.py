import random
print("\nRicerca sequenziale in un vettore")
maxValore = 10   # massimo valore 
mioVettore = []  # definisco una lista
# trovato = False # non serve
# riempio un vettore di numeri casuali
# x = 0
# while x < 10:
#   numero = random.randint(1, maxValore)
#   mioVettore.append(numero)
#   x = x + 1
for i in range(10):
  mioVettore.append(random.randint(1, maxValore))

# effettuo la ricerca 
# voluto = eval(input("numero da cercare: "))
voluto = int(input("numero da cercare: "))
# x = 0
# while x < len(mioVettore):
#   if (voluto == mioVettore[x]):
#     trovato = True
#     posiz = x
#     x = len(mioVettore)
#   x = x + 1
for i, elemento_corrente_vettore in enumerate(mioVettore):
  if voluto == elemento_corrente_vettore:
      print("Numero trovato in posizione", i)
      print (mioVettore)  
      exit(0)
print("\nNumero non trovato")  
#visualizzo il vettore completo 
print (mioVettore)  

