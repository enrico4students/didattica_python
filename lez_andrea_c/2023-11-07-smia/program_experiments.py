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

nome = "Andrea"
cognome = "Corrieri"
matricola = f"????????"

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

def is_anagram_sorting_sbs(s1: str, s2: str):
    """ didattica, "spreco" di variabili
    """
    if len(s1) != len(s2):
        return False
    else:
        s1_sorted = sorted(s1)
        s2_sorted = sorted(s2)
        if s1_sorted == s2_sorted:
            return True
        else:
            return False

def is_anagram_sorting(s1: str, s2: str):
    """ controlla se due stringhe sono un'anagramma ordinando i loro caratteri e confrontando il risultato """
    return len(s1) == len(s2) and sorted(s1) == sorted(s2)



# funzione che ritorna anaDict; NON rinominatela
def ex1_variante1(inputList):

    if True:
        print("ordino la lista, anche se non richiesto dall'esercizio (ottengo un errore anzichè due)")
        inputList = sorted(inputList)

    anaDict = {}
    gia_anagramma = set()
    for i in range(len(inputList)): # per ogni stringa
        if inputList[i] in gia_anagramma:
            # print(f"'{inputList[i]}' non considerata perchè gia anagramma di altra stringa nella lista "+
            #      "(NB interpretazione esercizio non sicura, incluso questo punto)")
            continue # non consideriamo se già anagramma
        anagrammi = set()
        for j in range(i+1,len(inputList)):
            if is_anagram_sorting(inputList[i], inputList[j]):
                anagrammi.add(inputList[j])
                gia_anagramma.add(inputList[j]) # cos' verrà ignorata "se una stringa è già stata considerata  come anagramma non viene presentata nel dizionario"
        anaDict[inputList[i]] = (anagrammi, len(anagrammi))
    
    anaDict = dict(sorted(anaDict.items(), reverse=True))

    return anaDict


def ex1_variante2(inputList):
    """ Qui consideriamo come anagramma l'elemento precedente nella lista, anzichè il secondo
    come sembrerebbe naturale
    QUESTO APPROCCIO NON SEMBRA FUNZIONARE, la probabile causa è l'approccio disorganico degli indici
    """

    anaDict = {}
    idx_gia_anagramma = set()
    idx_gia_chiave    = set()   # forse non servira, rimnuovere

    for i in range(len(inputList)): # per ogni stringa        
        if i in idx_gia_anagramma or i in idx_gia_chiave:
            continue # non consideriamo se già usata
            pass
        for j in range(len(inputList)):
            # if j in idx_gia_anagramma or j in idx_gia_chiave:
            if i == j:
                continue
            if j in idx_gia_anagramma:
                # continue # se è chiave non lo consideriamo come anagramma di chiave
                pass
            if is_anagram_sorting(inputList[i], inputList[j]):
                idx_gia_chiave.add(j)
                idx_gia_anagramma.add(i)
                if inputList[j] not in anaDict: # crea entry prima volta
                    anaDict[inputList[j]] = (set(),0)
                anaDict[inputList[j]][0].add(inputList[i]) # 
                # tuple invariabili non possiamo aggiornare nr elementi passo passo con: anaDict[inputList[j]][1] += 1

        # alla fine aggiorniamo il nr anagrammi, non potevamo farlo prima perchè tuple read-only
        for k in anaDict:
            insieme = anaDict[k][0]
            anaDict[k] = (insieme, len(insieme))

    return anaDict


def ex1(inputList):
    return ex1_variante2(inputList)


# ----------------------------------- Esercizio 2: subDict ----------------------------------- #
"""
Es. 2: 
"""


def is_substring_sbs(s1: str, s2:str):
    if len(s1) >= len(s2):
        return False
    else:
        return s1 in s2

def is_substring(s1: str, s2:str):
    return len(s1) < len(s2) and s1 in s2

# funzione che ritorna subDict; NON rinominatela
def ex2(inputList):

    subDict = {}
    substrings = set() # usiamo fino a quando non abbiamo verificato che possiamo modificare il set su cui iteriamo
    input_set1 = sorted(list(set(inputList)), key = len, reverse=True) # ignoriamo stringhe uguali - cominciamo dalle più lunghe
    input_set2 = input_set1.copy() #

    for stringa1 in input_set1:
        if stringa1 in substrings:
            # print(f"'{stringa1}' non considerata perchè sottostringa di altra stringa nella lista "+
            #       "(NB interpretazione esercizio non sicura, incluso questo punto)")
            continue #è una sottostringa, non la usiamo come chiave/risultato
        stringa1_substr_set = set()
        for stringa2 in input_set2:
            if is_substring(stringa2, stringa1):
                stringa1_substr_set.add(stringa2)
                substrings.add(stringa2)
        subDict[stringa1] = (stringa1_substr_set, len(stringa1_substr_set))

    return subDict


# ----------------------------------- Esercizio 3: palDict ----------------------------------- #
"""
Es. 3: 10 punti
"""


# funzione che ritorna palDict; NON rinominatela
def ex3(inputList):
    palindrome = set()
    non_palindrome = set()
    for stringa in inputList:
        if stringa == stringa[::-1]:
            palindrome.add(stringa)
        else:
            non_palindrome.add(stringa)

    palDict = {True: (palindrome, len(palindrome)),
               False: (non_palindrome, len(non_palindrome))}
    return palDict


if __name__ == "__main__":

    input_list = ["enrico", "roma", "lazio", "sole", "mela", "pera", "casa", "maro","ziola", "enirco", "ocirne", "omar","olaiz"]
    print("\n\n"+"-"*10+" ex1: anagrammi"+"-"*10)
    print(f"input list:\n{input_list}")
    print("risultato:\n"+str(ex1(input_list)))

    if False:
        input_list = ["enrico", "en", "rico", "la","zio", "roma", "ro", "ma", "lazio"]
        print("\n\n"+"-"*10+" ex2: sottostringhe"+"-"*10)
        print(f"input list:\n{input_list}")
        print("risultato:\n"+str(ex2(input_list)))

        input_list = ["aba", "ert", "bab", "carlo", "yamamay"]
        print("\n\n"+"-"*10+" ex3: palindrome"+"-"*10)
        print(f"input list:\n{input_list}")
        print(ex3(input_list))
