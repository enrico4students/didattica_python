#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consideriamo la codifica posizionale di un numero in base B.
Date le N cifre:      a_{N-1} .... a_1 a_0
Il valore del numero si ottiene sommando, per ogni indice i
da 0 ad N-1, i valori a_i*B^i .

Esempio: se la base B=6  e il numero è     (52103)_6
Il suo valore sarà    5*6^4 + 2*6^3 + 1*6^2 + 0*6^1 + 3*6^0 = (6951)_10

Generalizziamo questa notazione per usare basi diverse per ciascuna
posizione: avremo quindi una lista "bases" formata da N basi e un
numero formato da N cifre contenute in una lista di nome "digits".
Per l'esempio sopra avremo: bases = [6, 6, 6, 6, 6] digits = [5, 2, 1,
0, 3]. Le cifre sono tali che ciascuna sia minore della base nella
stessa posizione.  Il valore del numero in base 10 si ottiene come
nella conversione iniziale, usando per la potenza i-esima la base
i-esima della lista.

NOTA: per comodità useremo nel codice delle liste di cifre e di basi
in cui l'esponente della potenza corrisponde all'indice nelle liste.
Quindi ciascuna lista conterrà basi e cifre a partire dalle unita'.

NOTA: Il numero di basi N e' maggiore stretto di 1. I valori delle
basi anche esse sono maggiori di 1.

In base a quanto detto, data in ingresso una lista "bases",
un obiettivo dell'HW e' genera la lista di tutte le possibili
combinazioni valide di cifre rappresentabili con quelle basi.

Esempio: se in ingresso bases vale [2, 5], tutte le combinazioni sono:
[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]

infatti:
- nella prima cifra ci sono solo valori fra [0, 1] perche' la base e' 2
- nella seconda cifra ci sono solo valori fra [0, 4] perche' la base e' 5.

Ciascuna combinazione rappresenta un intero che va convertito da lista
a intero secondo la base specificata in "bases". Una volta che tutte
le possibili combinazioni sono state convertite in un intero e'
necessario trovare quali interi hanno piu di una rappresentazione
nelle basi date.

Esempio: Se in ingresso bases vale [4, 3, 2] allora gli interi che 
ammetto piu di una rappresentazione sono {3, 4, 5, 6, 7, 8, 9, 10}

Infatti, ad esempio il numero 10 con queste basi ha le due rappresentazioni 
    [3, 1, 1] -> 3*4^0 + 1*3^1 + 1*2^2 = 10
    [0, 2, 1] -> 0*4^0 + 2*3^1 + 1*2^2 = 10

Il problema e' gia' stato diviso in sottoproblemi e dovete realizzate
quindi le funzioni che seguono:
 - decode_digits, e' la funzione piu semplice e basilare che riceve
   una lista di basi e una lista di digits e la converte in intero.
 - generate_digits, e' la funzione che fa la maggior parte del lavoro
   che data una lista di basi, calcola tutte le combinazioni.
 - find_doubles, e' l'ultima funzione che date le combinazioni trova i
   corrispettivi interi che hanno piu di una rappresentazione.

Il Timeout applicato è 0.5 secondi.

ATTENZIONE: è vietato importare altre librerie oltre quelle già presenti.
"""

from typing import List, Set



def decode_digits(digits: List[int], bases: List[int]) -> int:
    '''
    Riceve una lista di cifre ed una lista di basi della stessa lunghezza.
    Calcola il valore intero che corrisponde come spiegato prima.
    Parameters
    digits : List[int]    lista di cifre da convertire
    bases   : List[int]    lista di basi della stessa lunghezza
    Returns
    int                    il valore intero corrispondente

    Esempio: decode_digits( [1, 1, 2], [2, 3, 4] ) -> 36
        infatti   1*2^0 + 1*3^1 + 2*4^2 = 36
    '''
    # SCRIVI QUI IL TUO CODICE
    val = 0
    # for i, base in enumerate(bases): non usiamo questo perche' non troppo chiaro
    assert(len(bases) == len(digits))
    for i in range(len(bases)):
        if bases[i] <= 1:
            print(f"errore: pos. {i}  la base {bases[i]} non e' > 1")
            exit(1)
        if digits[i] >= bases[i]:
            print(f"errore, la base e' {bases[i]}, la cifra {digits[i]} non e' compresa fra 0 e base-1, cioe' {bases[i]-1}")
            exit(1)

        peso = bases[i]**i
        val += digits[i]*peso
        print(f"pos: {i} cifra: {digits[i]} peso: {peso} cifre esaminate finora{digits[:i+1]} val. in decimale: {val}" )

    return val


def generate_digits(bases : List[int] ) -> List[List[int]]:
    '''
    Data una lista di basi, genera la lista di tutte le possibili
    combinazioni di cifre compatibili con le basi date.  Ciascuna
    combinazione è una lista di cifre compatibili.  Ovvero per
    ciascuna posizione che corrisponde a una base B contiene una delle
    possibili cifre in [0..B-1]
    
    Esempio:  generate_digits([2, 5]) produce la lista
    [ [0, 0], [1, 0], [0, 1], [1, 1], [0, 2], [1, 2], [0, 3], [1, 3], [0, 4], [1, 4] ]

    Nota: l'ordine nella lista finale non conta e anche 
    [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]
    è una soluzione valida.
    '''
    # SCRIVI QUI IL TUO CODICE
    
    next_da_riempire = [ [None]*len(bases) ]
    for pos_base, base in enumerate(bases):

        da_riempire = next_da_riempire
        next_da_riempire = []
        for combinazione in da_riempire: # per ogni eelemento dell' insieme di combinazioni riempito fin'ora, fino alla base precedente
            # va creata una variante per ogni cifra della base attuale
            for cifra in range(base):
                cur_comb = combinazione.copy()
                cur_comb[pos_base] = cifra
                next_da_riempire.append(cur_comb)

    return next_da_riempire



def find_doubles(bases : List[int]) -> Set[int]:
    '''
    Data una lista di basi, genera la lista di tutte le possibili
    combinazioni valide di cifre rappresentabili con quelle basi,
    converte ciascuna combinazione nell'intero corrispondente e cerca
    quali interi appaiono più volte.

    Ritorna l'insieme di valori interi che hanno più di una
    rappresentazione nelle basi date.

    Esempio: find_doubles([4, 3, 2]) -> {3, 4, 5, 6, 7, 8, 9, 10}
    Infatti, ad esempio il numero 10 con queste basi ha le due rappresentazioni 
    [3, 1, 1] -> 3*4^0 + 1*3^1 + 1*2^2 = 10
    [0, 2, 1] -> 0*4^0 + 2*3^1 + 1*2^2 = 10
    '''
    numeri_e_rappr = {} # OPZIONALE dizionario per numeri con più di una rappresentazione

    combinazioni_cifre = generate_digits(bases)

    piu_di_una_rappr =      set() # insieme vuoto, conterrà i numeri che hanno più di una rappresentazione
    interi_gia_incontrati = set() # insieme vuoto, verrà riempito con i numeri incontrati per controllare se il numero
                                  # corrispondente alla combinazione attuale + già stato incontrato (già dentro)
    for combinazione_cifre in combinazioni_cifre:
        intero_corrispondente = decode_digits(combinazione_cifre, bases)
        print(f"{intero_corrispondente} = {combinazione_cifre} basi {bases}")
        if intero_corrispondente in interi_gia_incontrati:
            piu_di_una_rappr.add(intero_corrispondente)
        interi_gia_incontrati.add(intero_corrispondente) # se già presente non c'è problema

        # addizionale, non richiesto
        if intero_corrispondente in numeri_e_rappr:
            numeri_e_rappr[intero_corrispondente].append(combinazione_cifre)
        else:
            numeri_e_rappr[intero_corrispondente] = [combinazione_cifre]


    return piu_di_una_rappr, numeri_e_rappr

###################################################################################
if __name__ == '__main__':

    basi_l = [4, 3, 2]
    piu_di_una_rappr, numeri_e_rapp = find_doubles(basi_l)
    print(piu_di_una_rappr)
    for intero in numeri_e_rapp:
        if len(numeri_e_rapp[intero]) > 1:
            print(f"----- intero {intero} con basi {basi_l} ha {len(numeri_e_rapp[intero])} rappresentazioni: ----")
            for rappr in numeri_e_rapp[intero]:
                print(f"     {intero} = {rappr}")

    # inserisci qui i tuoi test
    # se vuoi provare il tuo codice su piccoli dati
    # nota per eseguire questo main devi usare program.py
    # come cliente e non come modulo ossia con python program.py
