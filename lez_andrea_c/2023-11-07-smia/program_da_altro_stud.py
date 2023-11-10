#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import os

################################################################################

################################################################################

################################################################################


""" Operazioni da svolgere PRIMA DI TUTTO:

 1) Salvare questo file come program.py

 2) Indicare nelle variabili in basso il proprio

    NOME, COGNOME e NUMERO DI MATRICOLA

"""

nome = "ANTONIO"

cognome = "BONITO"

matricola = "152646254"

################################################################################

################################################################################

################################################################################

"""

Esercizi:

    

    Sia dato una lista di elementi. 

    

    Creare dizionari così costruiti:

    - anaDict contiene per ogni stringa nella lista una coppia (insieme di stringhe 

      che la anagrammano, numero di anagrammi) se una stringa è già stata considerata 

      come anagramma non viene presentata nel dizionario;



    - subDict contiene per ogni stringa nella lista una coppia (insieme di sottostringhe 

      proprie, numero di sottostringhe) se una stringa è già stata considerata come 

      sottostringa non viene presentata nel dizionario;



    - palDict contiene come chiavi i valori True e False, e come valori le coppie 

      (insieme di stringhe nell'insieme che sono o non sono palindrome, rispettivamente 

      associate a True e False, dimensione dell'insieme).



    Non si possono usare le funzioni sort, sorted, reverse e reversed, find e index.

"""

################################################################################

################################################################################

################################################################################

# ---------------------------- SUGGERIMENTI PER IL DEBUG --------------------- #

# Per eseguire solo alcuni dei test, si possono commentare le voci con cui la

# lista 'tests' è assegnata alla fine di grade.py

################################################################################


# ----------------------------------- Esercizio 1: anaDict ----------------------------------- #

"""

Es. 1: 

"""


# funzione che ritorna anaDict; NON rinominatela

def is_anagram(string_1, string_2):

        list_string_2 = [l for l in string_2]

        # sottraiamo ogni carattere della string_1 dalla lista dei caratteri della string_2

        # se un carattere della string_1 non è presente nella string_2, allora non sono anagrammi

        for l in string_1:

            try:

                list_string_2.remove(l)

            except:

                return False
        # per essere anagrammi, ogni carattere della string_2 deve appartenere anche alla string_1

        # dunque, dopo l'operazione precedente, dovremmo avere una lista vuota

        if list_string_2 == []:
            return True

        return False


def ex1(inputList):
    # per facilità definiamo prima una funzione che, date due stringhe, ritorna True se sono anagrammi e False in caso contrario

    

    # viene richiesto che una stringa già considerata anagramma non ricompaia nel dizionario, ma non viene specificato quale tra gli anagrammi debba essere la key del dizionario

    # nei test la key del dizionario è l'anagramma con l'index position maggiore, dunque invertiamo la lista per rispettare la condizione

    inputList = inputList[::-1]

    result = {}

    # lista di tutte le stringhe usate com anagrammi

    already_anagrams = []

    for i in range(len(inputList)):

        # inutile, giusto per la readability

        key = inputList[i]

        # se la stringa è già stata considerata, interrompiamo il ciclo

        if key in already_anagrams:
            continue

        # lista degli anagrammi relativi a una specifica key

        anagrams = []

        # testiamo tutte le stringhe successiva a qella in esame (in realtà quelle precedenti, visto che abbiamo invertito la lista)

        for string in inputList[i + 1::]:

            if is_anagram(key, string):
                anagrams.append(string)

                already_anagrams.append(string)

        result[key] = (set(anagrams), len(anagrams))

    return result


# ----------------------------------- Esercizio 2: subDict ----------------------------------- #

"""

Es. 2: 

"""


# funzione che ritorna subDict; NON rinominatela

def ex2(inputList):
    # funzione che ritorna True se string_1 è substring di string_2, False in caso contrario

    def is_substring(string_1, string_2):

        if string_1 == string_2:
            return False

        return string_1 in string_2

    # creiamo un dizionario iniziale con tutte le stringhe come key e una lista vuota come value, a cui aggiungeremo le substrings

    result = {string: [] for string in inputList}

    substrings = set()

    for string_1 in inputList:

        for string_2 in inputList:

            if is_substring(string_1, string_2):
                result[string_2].append(string_1)

                substrings.add(string_1)

    # eliminiamo le stringhe che sono substrings dal dizionario

    for string in substrings:
        del result[string]

    # ritorniamo usubDict a partire da 'result' sfruttando la dictionary comprehension

    return {key: (set(value), len(value)) for key, value in result.items()}


# ----------------------------------- Esercizio 3: palDict ----------------------------------- #

"""

Es. 3: 10 punti

"""


# funzione che ritorna palDict; NON rinominatela

def ex3(inputList):

    palindrome = []
    non_palindrome = []

    for string in inputList:
        if string == string[::-1]:
            palindrome.append(string)
        else:

            non_palindrome.append(string)

    return {True: (set(palindrome), len(palindrome)), False: (set(non_palindrome), len(non_palindrome))}
