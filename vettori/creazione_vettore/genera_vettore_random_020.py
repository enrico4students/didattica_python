
from random import random

def genera_vettore_interi(nr_elementi = 10):

    vettore = []

    for i in range(nr_elementi):
        valore = random()*100
        valore = int(valore)
        print("genero {}-esimo elemento, e' {}".format(i, valore))
        vettore.append(valore)

vettore = genera_vettore_interi()
vettore = genera_vettore_interi()