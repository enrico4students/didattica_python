import random
minValore = 10
maxValore = 20
mioVettore = []       # definisco una variabile lista
# riempio un vettore di numeri casuali
x = 0
while x < 12:
  mioVettore.append(random.randint(minValore, maxValore))
  x = x + 1

#visualizza il vettore posizione alla volta

x = 00
while x < len(mioVettore):
  print (mioVettore[11-x])
  x = x + 1
  
#visualizzo il vettore completo 
print (mioVettore)  
