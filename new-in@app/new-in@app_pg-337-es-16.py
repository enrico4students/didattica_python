# new in@app pg 337 es 16
# Partizionamento con pivot · Scrivi un programma che, dopo aver riempito con numeri casuali 
# un vettore di NUMELE elementi (per esempio NUMELE = 15) 
# con valori compresi tra MIN e MAX (per esempio MIN = 2 e MAX = 20)
# 5217128152141211894313
# 01234567891011121314
# estragga una posizione a caso all’interno del vettore (PIVOT) (per esempio indice = 9) 
# e riorganizzi i dati spostando gli elementi più piccoli a sinistra di pivot e quelli più grandi a destra
# 5234892811121415121713senza effettuare l’ordinamento del vettore.


import random

NUMELE = random.randint(3,25)
print("il vettore avrà {} elementi random".format(NUMELE))

MIN = random.randint(-1000,1000)
MAX = random.randint(MIN,MIN+1000)
print("i valori saranno fra {} e {}".format(MIN, MAX))


v = [0]*NUMELE # questo evita l'append, forse è piu' veloce
for i in range(NUMELE):
    v[i] = random.randint(MIN,MAX)
print(v)

PIVOT = random.randint(1, NUMELE-1)
valore_pivot = v[PIVOT]
print("la posizione PIVOT è {} il valore pivot è {}".format(PIVOT, valore_pivot))

nr_maggiori = 0
nr_minori = 0
nr_uguali = 0
for e in v:
    if e < valore_pivot:
        nr_minori += 1
    elif e == valore_pivot:
        nr_uguali += 1
    else:
        nr_maggiori += 1

v2 = [0]*NUMELE
cur_pos_left  = 0
cur_pos_equal = nr_minori
cur_pos_right = cur_pos_equal+nr_uguali
print("la nuova posizione PIVOT sarà {} (il valore pivot è {})".format(nr_minori, valore_pivot))

for e in v:
    print("valore {} posizioni min {} uguale {} magg {}".format(e, cur_pos_left, cur_pos_equal, cur_pos_right))
    if e < valore_pivot:
        v2[cur_pos_left] = e
        cur_pos_left += 1
    elif e == valore_pivot:
        v2[cur_pos_equal] = e
        cur_pos_equal += 1
    else:
        v2[cur_pos_right] = e
        cur_pos_right += 1
    print(v2)

