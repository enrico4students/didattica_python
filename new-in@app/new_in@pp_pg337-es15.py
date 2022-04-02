# new in@app
# pg 337
# es.15
# Shift a destra e sinistra · 
# Scrivi un programma che, 
# dopo aver riempito con numeri casuali un vettore di NUMELE elementi (per esempio NUMELE = 15) 
# con valori compresi tra MIN e MAX (per esempio MIN = 10 e MAX = 20)
# estragga una sequenza di numeri casuali terminante con 0 con range di valori (0-6):
# a) nel caso di numeri dispari, gli elementi del vettore devono essere traslati di x posizioni a destra 
# b) nel caso di numero pari, gli elementi del vettore devono essere traslati di x posizioni a sinistra

import random

MIN = 10
MAX = 20

NUMELE = int(input("inserire numero di elementi del vettore: "))

vettore = []
for i in range(NUMELE):
    valore = MIN+random.random()*(MAX - MIN)
    valore = int(valore)
    # print("genero {}-esimo elemento, e' {}".format(i, valore))
    vettore.append(valore)    

continua = True
while continua:
    
    numero_casuale_real = random.random()*6.99
    numero_casuale_int = int(numero_casuale_real) # togliamo la parte decimale
    
    if numero_casuale_int == 0:
        print("generato 0 - esco")
        break
    
    if numero_casuale_int % 2 == 0: # e' pari?
        numero_casuale_int = numero_casuale_int*-1 # se pari ruotiamo verso sinistra
    
    nuovo_vettore_ruotato = [None] * NUMELE # il nuovo vettore in cui mettiamo gli elementi spostati
    for i in range(NUMELE):
        i_dest = (i+numero_casuale_int) % NUMELE # rotazione
        nuovo_vettore_ruotato[i_dest] = vettore[i]
    print("---------------------")
    print("vettore originario", vettore)
    print("sposto di {} posizioni".format(numero_casuale_int))
    print("vettore ruotato: ", nuovo_vettore_ruotato)