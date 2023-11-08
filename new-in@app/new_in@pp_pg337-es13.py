# new in@app
# pg 337
# es.13
# Ribaltamento vettore · 
# Scrivi un programma che, 
# dopo aver riempito con numeri casuali un vettore di NUMELE elementi (per esempio NUMELE = 15) 
# con valori compresi tra MIN e MAX (per esempio MIN = 2 e MAX = 20), 
# lo visualizzi e successivamente lo ribalti
#
# Come tutti gli esercizi fatto in modo didattico, di solito esistono modi migliori
# ma non utili a livello didattico in questa fase
#

import random

vettore = []
NUMELE = int(input("inserire numero di elementi del  vettore: "))
for i in range(NUMELE):
    valore_random_real = random.random()*100
    valore_random_int = int(valore_random_real)
    vettore.append(valore_random_int)

print("stampa elementi vettore")
for elemento_vettore in vettore:
    print(elemento_vettore)

# print("stampa elementi vettore con l'indice")
# for i, elemento_vettore in vettore.items():
#    print("elemento in posizione {} e': {}}".format(i,elemento_vettore))

# invertiamo il vettore
vettore_invertito = [None] * NUMELE # creiamo il vettore dove copiare
# gli elementi del nostro vettore in ordine inverso
for i in range(len(vettore)):
    posizione_invertita = (NUMELE-1) -i #  (NUMELE -1) perchè gli elementi vanno da 0 a NUMELE-1
    print("copio il valore in posizione "+str(i)+" nel vettore invertito in posizione "+str(posizione_invertita))
    vettore_invertito[posizione_invertita] = vettore[i]

print("stampa elementi del nuovo con contenuti invertiti")
for elemento_vettore in vettore_invertito:
    print(elemento_vettore)

print(vettore)
print(vettore_invertito)

