
# Errori
# Iniziate a prendere familiarità con i messaggi di errore che Python vi da. Provate ad introdurre di
# proposito degli errori e a vedere quale messaggio di errore ottenete. Meglio fare errori ora e di
# proposito (e capirli), piuttosto che accidentalmente in seguito e non riuscire a capire dov'è l'errore. Ad
# esempio:
# Cosa succede se dimenticate gli apici alla fine di una stringa?

nome = "enrico" # ok, corretto
# se scriviamo
# nome = "enrico
# l'errore è
#   File "d:\00_data\08-dev\08-didattica-pers\corrieri\esercizi01.py", line 8
#     nome = "enrico
#                   ^
# SyntaxError: EOL while scanning string literal

# apici singoli sono identici ad apici doppi
nome = 'mario'
# causiamo l'errore
# nome = 'mario
#   File "d:\00_data\08-dev\08-didattica-pers\corrieri\esercizi01.py", line 20
#     nome = 'mario
#                  ^
# SyntaxError: EOL while scanning string literal
# EOL mè l'abbreviazione di end of line

nome = """
enrico continuiamo 
a capo
"""
print(nome)

# quanto segue causerebbe errore
# nome = """
#  enrico continuiamo 
# a capo
# File "d:\00_data\08-dev\08-didattica-pers\corrieri\esercizi01.py", line 56
#     # se mettiamo un punto e virgola alla fine di un'istruzione Python? E se mettiamo un punto?
#                                                                                                ^
# SyntaxError: EOF while scanning triple-quoted string literal
# EOF è l'abbreviazione di end of file


# Cosa succede se dividete un numero per 0?
# x = 3/0
# se eseguiamo l'istruzione sopra otteniamo l'errore
# Traceback (most recent call last):
#   File "d:\00_data\08-dev\08-didattica-pers\corrieri\esercizi01.py", line 46, in <module>
#     x = 3/0
# ZeroDivisionError: division by zero


# Cosa succede se in una istruzione di stampa (print) dimenticate una o entrambe le parentesi?
# print3)
# da' errore
#  File "d:\00_data\08-dev\08-didattica-pers\corrieri\esercizi01.py", line 55
#     print3)
#           ^
# SyntaxError: unmatched ')'

# print(3
# causa
#  File "d:\00_data\08-dev\08-didattica-pers\corrieri\esercizi01.py", line 75

#     ^
# SyntaxError: unexpected EOF while parsing

# Per esprimere un numero negativo, si antepone il segno meno (ad esempio, -2). Cosa succede
# se anteponete il segno +? e se fate 2++2?
-2 # ok
x = -2 # ok
z = 2++2
print(z)



# Nella notazione matematica, gli 0 iniziali sono ammessi (ad esempio, 02). Cosa succede in
# Python?
# x = 05
#   File "d:\00_data\08-dev\08-didattica-pers\corrieri\esercizi01.py", line 80
#     x = 05
#          ^
# SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
# literal = valori espliciti, x. 123  "forza roma"   2.42
# c++ const int ETA_MAGG = 18; // ETA_MAGG è una costante simbolica, 18 costante/valore interi literal 


# Nella notazione matematica, possiamo omettere il simbolo di moltiplicazione. Ad esempio x*y
# può essere scritto come xy. E' permesso anche in Python?
x = 1
y = 2
# print(xy)
#   File "d:\00_data\08-dev\08-didattica-pers\corrieri\esercizi01.py", line 93, in <module>
#     print(xy)
# NameError: name 'xy' is not defined
# prende xy come un identificatore di variabile, tale variabile non è stata creata/definita, quindi errore


# In Python possiamo assegnare un numero ad una variabile, ad esempio: n=42. Cosa succede
# se facciamo 42=n?
# 42=n
#  File "d:\00_data\08-dev\08-didattica-pers\corrieri\esercizi01.py", line 102
#     42=n
#     ^
# SyntaxError: cannot assign to literal
# ci dice che non può assegnare valori ad un valore esplicito (literal)

# Cosa succede con x=y=1?
x=y=z=1
print(x,y,z)
print(f"x={x} Y={y} z={z}") # f immediatamente prima " rende possibile linterpolazione
print("x={x} Y={y} z={z}") # manca la f quindi NON avviente l'interpolazione


# In alcuni linguaggi, come il C, ogni istruzione termina con un punto e virgola (;). Cosa succede
# se mettiamo un punto e virgola alla fine di un'istruzione Python? E se mettiamo un punto?
x = 1; y = 2

if x > 0: x = 11; y = 12 # molto inusuale
print(x,y)

y = 2.           # considera y float
print(type(y))
y = 2            # considera y intero
print(type(y)) 


# if x > 0:
#    print().
#   File "d:\00_data\08-dev\08-didattica-pers\corrieri\esercizi01.py", line 129
#     print().
#             ^
# SyntaxError: invalid syntax
# for i in range(5):
#     print(i)
#     .

# Calcoli
# Scrivete una espressione che calcoli il numero di secondi che ci sono in 42 minuti e 42 secondi.
print("in 42 minuti e 42 secondi ci sono",42*60+42)

# Scrivete una espressione che calcoli il numero di miglia che ci sono in 10 chilometri. (1 miglio = 1.61
# km).
print(10*1.61)

# Scrivete una espressione che calcoli la velocità media e la cadenza media (tempo per miglio, in minuti
# e secondi) di un corridore che corre una gara di 10 chilometri in 42 minuti e 42 secondi.
tempo_tot_secondi = 42*60+42
distanza_in_miglia = 10/1.61
print(f"distanza in miglia = {distanza_in_miglia}")
velocita_miglia_sec = distanza_in_miglia/tempo_tot_secondi
print(f"miglia/sec = {velocita_miglia_sec}")
print(f"miglia/ora = {velocita_miglia_sec/3600}")


# Import math Library
import math
from math import pi

# Il volume di una sfera di raggio r è 4/3 * PI * r^3. Scrivere una espressione che calcoli il volume
# di una sfera di raggio 5.
raggio = 5
volume = 4/3 * math.pi * raggio**3
volume = 4/3 * pi * raggio**3 # possiamo scriverlo grazia a: from math import pi
print(f"volume vera di raggio {raggio} = {volume}")

# Il prezzo di copertina di un libro è 24.95, ma una liberia ottiene il 40% di sconto. I costi di spedizione
# sono 3 euro per la prima copia, e 75 centesimi per ogni copia aggiuntiva. Qual'è il costo totale di 60
# copie?
NR_COPIE = 60 # cerchiamo di scrivere codice generale come se questo valore potesse essere qualunque intero >=1
assert(NR_COPIE >= 1)
costo_libri = (24.95*0.6) *NR_COPIE
costi_sped = 3 if NR_COPIE == 1 else 3+(NR_COPIE-1)*0.75


# Se uscite di casa alle 6:52 di mattina e correte un miglio a ritmo blando (8 minuti e 15 secondi al
# miglio), e poi 3 miglia a ritmo moderato (7 minuti e 12 secondi al miglio), e infine un altro miglio a ritmo
# blando (9 minuti e 45 secondi al miglio), a che ora sarete tornati a casa?
# in pyton ci sono moduli che fanno questi calcoli in modo semplice 
# https://www.geeksforgeeks.org/python-datetime-timedelta-function/

tempo_tratta1_1miglio_sec = 1*(8*60+15)
tempo_tratta2_3miglia_sec = 3*(7*60+12)
tempo_tratta3_1miglio_sec = 1*(9*60+45)
tempo_totale_sec = tempo_tratta1_1miglio_sec+tempo_tratta2_3miglia_sec+tempo_tratta3_1miglio_sec
tempo_minuti = tempo_totale_sec//60
tempo_sec_restanti = tempo_totale_sec%60
print(f"tempo totale in secondi: {tempo_totale_sec} = {tempo_minuti} minuti + {tempo_sec_restanti} secondi (check {tempo_minuti*60+tempo_sec_restanti})")
ora_arrivo_ora = 6 + (52+tempo_minuti)//60
ora_arrivo_minuti = (52+tempo_minuti)%60
print(f"ora arrivo {ora_arrivo_ora}:{ora_arrivo_minuti}")

# Stringhe
# Avete una stringa di 5 caratteri. Ogni carattere è una cifra decimale. Ad esempio, s="85721".
# Stampate la somma delle cifre contenute nella stringa.

s="85721" # la variabile s non è necessaria, si poteva inserire la stringa literal nel for
accumulatore_somma= 0
for carattere in s: # in Python iterare usando indici numerici non sempre ma spesso è cattivo uso del linguaggio
    numero = int(carattere)
    print(f"ad accumulatore_somma che è {accumulatore_somma} aggiungo {numero}")
    accumulatore_somma += numero # a += b è un modo abbreviato di scrivere a = a + b
print(f"la somma delle cifre contenute nella stringa è: {accumulatore_somma}")

# Scrivete una espressione che a partire da una stringa di 5 caratteri, rappresentante un numero binario,
# stampi la sua rappresentazione decimale. Ad esempio, s="00101" -> 5.

# in Python ci sono moduli che fanno la conversazione, qui
# si implementa manualmente come se non esistessero questi moduli a fini didattici
# approccio primitivo
print("questo codice fallisce con stringhe che non contengono solo 0 o 1 COME CARATTERI")
print("se la differenza fra i carattere 0 e il numero 0 non è chiara dobbiamo chiarirla")
s="00101"
accumulatore_valore = 0
for pos, bit in enumerate(s[::-1]): # s[::-1] inverte la stringa usando un meccanismo non ancora visto (slicing, step)
    cifra_num = int(bit)
    peso = 2**pos
    valore = cifra_num*peso
    accumulatore_valore += valore
print(f"la stringa {s} considerando i caratteri come cifre binarie ha valore (in decimale) {accumulatore_valore}")

# usando una funzione

def valore_stringabinaria(stringa: str):
    accumulatore_valore = 0
    for pos, bit in enumerate(s[::-1]): # s[::-1] inverte la stringa usando un meccanismo non ancora visto (slicing, step)
        cifra_num = int(bit)
        peso = 2**pos
        valore = cifra_num*peso
        accumulatore_valore += valore

    return accumulatore_valore

# concetti non ancora visti
for s in ["11111111", "10000000", "10101010"]:
    valore = valore_stringabinaria(s)
    print(f"la stringa {s} considerando i caratteri come cifre binarie ha valore (in decimale) {valore}")


# Avete una stringa di 5 caratteri. Il carattere centrale è il punto decimale ('.'). Ad esempio, s="52.29".
# Stampare il numero decimale rappresentato dalla stringa (stamparlo come numero, non come stringa).
s = "52.29"
# utilizzando le funzioni base di conversione (casting)
valore = float(s) # la variabile valore non è necessaria, si poteva scrivere direttamente float(s) come nella seconda stampa
print(f"la stringa {s} convertita in numero ha valore: {valore}")
print(f"la stringa {s} convertita in numero ha valore: {float(s)}")

# implementazione manuale a fini didattici, 
# NB funziona solo per stringhe con formato identico a quella di esempio

parte_intera, parte_frazionaria = s.split(".")
# print(f"{parte_intera} {parte_frazionaria}")
for pos, cifra in enumerate(parte_intera[::-1]):
    accumulatore_valore += int(cifra)* 10**pos # questa volta più concisi di codice precedente simile (ex. stringa binaria)
for pos, cifra in enumerate(parte_frazionaria):
    accumulatore_valore += int(cifra)* 10**(-1*(pos+1)) # questa volta più concisi di codice precedente simile (ex. stringa binaria)
print(accumulatore_valore)


# Funzioni
# ===================================================================
# Scrivere una funzione che prende un numero in virgola mobile, ne calcola la radice cubica, e la ritorna.

# utilizzando libreria matematica (da installare se non si è in anaconda)
import numpy as np
def cubic_root1(val: float):
    return np.cbrt(val)


def cubic_root2(val: float):
    return val**(1/3)

radice3_27 = cubic_root2(27)
print(f"radice cubica di {27} = {radice3_27}")
radice3_1000 = cubic_root2(1000)
print(f"radice cubica di {1000} = {radice3_1000}")


# Scrivere una funzione che prende tre numeri in virgola mobile (a, b, c) e calcola le radici dell'equazione
# a x^2 + b x + c e ritorna la maggiore. Modificare poi la funzione per ritornare entrambi i valori.
import math

def find_largest_root(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return max(root1, root2)

def find_both_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None, None
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2

def find_both_roots_alternative(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None, None
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    return root1, root2

a, b, c = 2, -7, 3
largest_root = find_largest_root(a, b, c)
print("La radice più grande è:", largest_root)

roots = find_both_roots(a, b, c)
print("Le radici sono:", roots)


# Scrivere una funzione che prende tre numeri in virgola mobile (a, b, c) e calcola le radici dell'equazione
# a x^2 + b x + c e le ritorna entrambe.
def find_both_roots_alternative(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None, None
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    return root1, root2



# Scrivere una funzione che prende come input cinque numeri e ritorna la somma dei numeri pari meno
# quella dei numeri dispari.

# implementazione goffa
def somma_5_num_vers1(a,b,c,d,e):
    tot_pari = tot_dispari = 0
    if a%2 == 0:
        tot_pari += a
    else:
        tot_dispari +=a
    if b%2 == 0:
        tot_pari += b
    else:
        tot_dispari +=b
    # non vale la pena terminarla

    return tot_pari + tot_dispari


def somma_5_num_vers2(numeri_l: list):
    assert(len(numeri_l) == 5)
    accumul = 0
    for numero in numeri_l:
        accumul += numero if numero%2 == 0 else -1*numero
    return accumul

print(somma_5_num_vers2([10,7,8,7,0]))




# Scrivere una funzione che prende tre valori di input, e ritorna la loro somma se i valori sono punteggi di
# esame validi (0 <= grade <= 30), e altrimenti ritorna -1. 
# probabilmente non è il modo migliore per farla in Python, per ora va bene così
def somma_punteggi(punteggi_l: list):
    accumul_somma = 0
    for punteggio in punteggi_l:
        if punteggio not in range(31):
            return -1
        accumul_somma += punteggio

    return accumul_somma
print(somma_punteggi([10, 10, 10]))
print(somma_punteggi([10, 10, 100]))

# Scriverne poi una variante che legge i valori da terminale con input.
def somma_punteggi_input(numero_punteggi: int = 3): # aggiungiamo la caratteristica non richiesta
                                                    # di passare il numero di input
    punteggi_inseriti = [None] * numero_punteggi
    print(f"ora inseriremo {numero_punteggi} punteggi")
    # fallisce se non inseriamo un numero, per ora ci va bene cosi'
    for i in range(numero_punteggi):
        punteggi_inseriti[i] = int(input(f"inserire un punteggio {i}, valore fra 0 e 30, valori fuori range per abbandonare: "))
        if punteggi_inseriti[i] not in range(31):
            return -1

    return sum(punteggi_inseriti)

#print(somma_punteggi_input(3))



# Scrivere una funzione che prende tre valori (d, m, y) e ritorna se la data è valida o no. Si possono
# ignorare gli anni bisestili. Ad esempio, ritorna False per 30/2/2017 e True per 1/1/1111.
def data_valida(anno, mese, giorno):
    
    valida = anno in range(-752,2050)

    valida = valida and mese in range(12+1)
    
    if mese in [1,3,5,7,8,10,12]:
        valida = valida and giorno in range(31+1)
    elif mese == 2:
        valida = valida and giorno in range(28+1)
    else:
        valida = valida and giorno in range(30+1)
    return valida

print(data_valida(2000, 12, 31))

# Scrivere una funzione che implenta la stessa funzionalità di str.strip().
print("   ciao   ".strip())

# probabilmente inefficiente ma per ora va bene così
def strip2(s):
    
    caratteri_da_saltare = [' ']
    start =  stop = 0
    stato = 0 # 0 eventuali blanks iniziali, 1 non-blanks,
    for i, c in enumerate(s):
        if stato == 0: # forse può essere semplificata
            if c not in caratteri_da_saltare:
                start = i
                stato = 1
        elif stato == 1:
            if c not in caratteri_da_saltare:
                stop = i+1
    
    return s[start:stop]

print(f"-{strip2('  prova  ')}-")
print(f"-{strip2('  prova')}-")
print(f"-{strip2('prova  ')}-")
print(f"-{strip2('prova')}-")
print(f"-{strip2('prova ')}-")
print(f"-{strip2(' prova')}-")
print(f"-{strip2(' ')}-")
print(f"-{strip2('')}-")


# Scrivere una funzione che ritorna una stringa di saluto formata da Ciao , seguito dal nome letto come
# input e poi da Buona giornata!

def ciao_buonagiornata(nome: str):
    return f"Ciao {nome} Buona giornata!"

print(ciao_buonagiornata("Ugo Maria Guidalberto"))