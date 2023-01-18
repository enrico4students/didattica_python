from random import random

def genera_vettore_interi(nr_elementi = 10):
    """ genera un vettore di interi con valori casuali"""
    vettore = [int(random()*100) for i in range(nr_elementi)]
    return vettore

vettore = genera_vettore_interi()
print(vettore)
