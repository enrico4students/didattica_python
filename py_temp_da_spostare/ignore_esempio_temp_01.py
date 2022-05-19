
import random

vettore = []
nLenght = 15
nValMin = 3
nValMax = 10

posSbagliate = []
for i in range(nLenght):
    numero = random.randint(nValMin, nValMax)
    vettore.append(numero)
    if i%2 != numero%2:
        posSbagliate.append(i)

print("vettore", vettore)
for i in posSbagliate:
    print("nella posizione/indice {} del vettore il valore è {} {}".format(i, vettore[i]))

