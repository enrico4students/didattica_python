
from random import random

def genera_vettore_interi(nr_elementi = 10):
    """ genera un vettore di interi con valori casuali"""
    vettore = []
    for i in range(nr_elementi):
        valore = random()*100
        valore = int(valore)
        print("genero {}-esimo elemento, e' {}".format(i, valore))
        vettore.append(valore)

    return vettore

vettore = genera_vettore_interi()
print(vettore)
