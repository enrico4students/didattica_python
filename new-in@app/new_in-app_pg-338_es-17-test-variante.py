# new-in@app pg 338 es 17 
# Ordinamento per conteggio · 
# Effettua l’ordinamento di un vettore (con elementi tutti diversi)
# mediante l’algoritmo di seguito descritto (algoritmo counting-sort): 
# conoscendo il valore massimo degli elementi presenti in un vettore, 
# per ogni elemento conta quanti altri elementi presenti nel vettore hanno valore minore; 
# posiziona quindi l’elemento che stai analizzando in un nuovo vettore 
# dopo aver lasciato tanti spazi vuoti quanti sono gli elementi calcolati in precedenza.

import random


NUMELE, MIN, MAX = 15, 2, 20
vettore = [None] *NUMELE
vettoreSort = [0]*NUMELE

# generazione vettore casuale
# costretti a usare il while a causa del requisito
# (con elementi tutti diversi)

i = 0
while i < NUMELE:
	n = random.randint(MIN, MAX)
	if not vettore.__contains__(n):
		vettore[i] = n
		i += 1

# --- non corrisponde  a quanto richiesto ---
pos = NUMELE-1
for i in range(MAX+1, 0, -1):
	if vettore.__contains__(i):
		vettoreSort[pos] = i
		pos -= 1


# --- provo a fare come richiesto ---
vett_nr_minori  = [0]*NUMELE
for i in range(NUMELE):
    nr_numeri_minori = 0
    for v in vettore:
        if v < vettore[i]:
            nr_numeri_minori += 1 # icrementa nr num minori di v[i]
    vett_nr_minori[i] = nr_numeri_minori # in posizione i
    vettoreSort[vett_nr_minori[i]] = vettore[i]

print("vettore prima del sort\t", vettore)
print("vettore dopo il sort\t", vettoreSort)
