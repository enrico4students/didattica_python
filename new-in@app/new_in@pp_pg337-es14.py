# new in@app
# pg 337
# es.14
# Numeri primi
# Scrivi un programma che, ricevuto in ingresso un numero, visualizzi un array con tutti 
# i numeri primi minori o uguali a quel numero.
# algoritmo: 
# prendiamo in input un numero e lo dividiamo a mano a mano per numeri minori della sua metà. 
# è scontato che dividendo un numero per valori maggiori della sua metà, il resto della divisione sia diverso da 0.
# dato che tutti i numeri sono divisibili per 1, facciamo senza anche a contarlo come divisore.
# Quindi impostiamo la variabile div a 2 e la incrementiamo di volta in volta fino ad arrivare a numero/2.
# Se il resto della divisione numero%div è uguale a zero, allora conteggiamo i divisori in una variabile contatore 
# count inizializzata a zero.
# Se la variabile count rimane a 0 allora non si trovano divisori e quindi il numero è primo. In caso contrario il numero non è primo.


numeri_primi_l = []
numero_scelto = int(input("inserire numero di elementi del  vettore: "))

for numero in range(2, numero_scelto+1):
    nr_divisori = 0
    for div in range(2, int(numero/2)+1):
        if numero % div == 0:
            nr_divisori += 1
    if nr_divisori == 0:
        numeri_primi_l.append(numero)

print("stampo il vettore di numeri primi minori di {}".format(numero_scelto))
for elemento in numeri_primi_l:
    print(elemento)
