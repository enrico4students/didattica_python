
# 18 Ordinamento per enumerazione · 
# Scrivi un programma che effettui l’ordinamento di un vettore mediante 
# l’algoritmo di seguito descritto (algoritmo per enumerazione): 
# conoscendo il valore massimo degli elementi presenti in un vettore, 
# esegui un ciclo a conteggio con tale valore come estremo superiore e, 
# a ogni iterazione, verifica se il valore corrente dell’indice è presente nel vettore da ordinare; 
# in tal caso, copialo in un nuovo vettore

import random

NUMELE, MIN, MAX = 15, 2, 20
vettore = []
vettore2 = []

for i in range(NUMELE):
	vettore.append(random.randint(MIN, MAX))

massimo = max(vettore)

for i in range(MIN, massimo+1):
	if vettore.__contains__(i):
		vettore2.append(i)
print(vettore)
print(vettore2)
