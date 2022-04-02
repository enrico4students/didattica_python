
from random import random


vettore = [] # vettori python in realta' sono liste, non vettori

nr_elementi = int(input("quanti elementi deve avere il vettore? "))

for i in range(nr_elementi):
    valore = random()*100
    valore = int(valore)
    print("genero {}-esimo elemento, e' {}".format(i, valore))
    vettore.append(valore)    

print(vettore)