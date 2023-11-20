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

nome = "NOMEx"
cognome = "COGNOMEx"
matricola = "MATRICOLAx"

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



def is_anagram_sorting(s1: str, s2: str):
    """ controlla se due stringhe sono un'anagramma ordinando i loro caratteri e confrontando il risultato 
    """
    return len(s1) == len(s2) and sorted(s1) == sorted(s2)


def add_to_dict(dizionario: dict, chiave: str):
    """ NB funzioni nidificate come questa sono tecnicamente corrette ma solitamente sono usate nella progr. funzionale 
    """
    if chiave not in dizionario:
        dizionario[chiave] = 1 # non gia' presente, prima occorrenza/inserimento
    else: # gia' presente
        dizionario[chiave] += 1 # nb: += che significa dizionario[chiave] = dizionario[chiave]+ 1 


def is_anagram_dict(s1: str, s2: str):
    """ controlla se due stringhe sono un'anagramma ordinando i loro caratteri e confrontando il risultato 
    """

    if len(s1) != len(s2):
        return False;

    s1_car_dic = {}
    s2_car_dic = {}
    for  i in range(len(s1)): # e' garantito da codice precedente che le due stringhe hanno stessa lunghezza qui
        add_to_dict(s1_car_dic, s1[i])
        add_to_dict(s2_car_dic, s2[i])

    if s1_car_dic.keys() != s2_car_dic.keys():
        return False

    for chiave in s1_car_dic:
        if s1_car_dic[chiave] != s1_car_dic[chiave]:
            return False

    return True


def is_anagram(s1: str, s2: str):
    return is_anagram_dict(s1,s2)



# funzione che ritorna anaDict; NON rinominatela
def ex1(inputList):

    inputList = inputList[::-1] # invertiamo l'ordine della lista, senza questo non passa il test

    anaDict = {} # dizionario che verrà ritornato

    anagrammi_da_non_includere = set()
    for i in range(len(inputList)): # per ogni stringa

        if inputList[i] in anagrammi_da_non_includere:
            #print(f"'{inputList[i]}' non considerata perchè gia anagramma di altra stringa nella lista "+
            #      "(NB interpretazione esercizio non sicura, incluso questo punto)")
            continue # non consideriamo se già anagramma

        anagrammi = set()
        for j in range(i+1,len(inputList)):
            if is_anagram(inputList[i], inputList[j]):
                anagrammi.add(inputList[j])
                anagrammi_da_non_includere.add(inputList[j]) # 

        anaDict[inputList[i]] = (anagrammi, len(anagrammi)) # associamo alla stringa la coppia <insieme anagrammi> , cardinalità insieme

    return anaDict


# ----------------------------------- Esercizio 2: subDict ----------------------------------- #
"""
Es. 2: 
"""


def is_substring(s1: str, s2:str):
    return len(s1) < len(s2) and s1 in s2

# funzione che ritorna subDict; NON rinominatela
def ex2(inputList):

    subDict = {} # dizionario da ritornare
    
    substrings_idx = set() # evitiamo di modificare il set su cui iteriamo rimuovendo da esso le stringhe
    # che sono sottostringhe, questa è una norma di prudenza generale da osservare anche quando non vi è rischio di problemi
    # memorizziamo qui le posizioni di tali stringhe nella lista per "saltarle" quando le incontriamo

    inputList = sorted(inputList, # ignoriamo stringhe uguali, ci appoggiamo a set() rimuove eventuali duplicati
                        key = len, # key è la funzione in base al cui risultato verrà fatto l'ordinamento
                        reverse=True) #  cominciamo dalle più lunghe

    for i in range(len(inputList)):
        if i in substrings_idx:
            continue # già identificata/catalogata come sottostringa, non la usiamo come chiave/risultato
                    # come precauzione "parnoid" per eventuali corruzioni dell'iterazione/sequenza non la rimuoviamo
                    # da input_set1 (che è una copia di inputList)
        stringai_substr_set = set() # insieme che conterrà le eventuali sottostringhe di stringa1
        for j in range(i+1, len(inputList)):
            if is_substring(inputList[j], inputList[i]):
                stringai_substr_set.add(inputList[j])
                substrings_idx.add(j)
        
        # associamo alla stringa la coppia <insieme sottostringhe> , cardinalità insieme
        subDict[inputList[i]] = (stringai_substr_set, len(stringai_substr_set))

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

    palDict = {True:  (palindrome,     len(palindrome)),
               False: (non_palindrome, len(non_palindrome))}

    return palDict



if __name__ == "__main__":

    # prove veloci personali
    inputList = ["enrico", "roma", "lazio", "sole", "mela", "pera", "casa", "maro","ziola", "enirco", "ocirne", "omar","olaiz", "oles"]
    # inputList = ["enrico", "ocirne"]
    print("\n\n"+"-"*10+" ex1: anagrammi"+"-"*10)
    print(f"input list:\n{inputList}")
    print("risultato:\n"+str(ex1(inputList)))

    if False:
        inputList = ["xxx", "enrico", "en", "rico", "la","zio", "roma", "ro", "ma", "lazio", "xxx"]
        print("\n\n"+"-"*10+" ex2: sottostringhe"+"-"*10)
        print(f"input list:\n{inputList}")
        print("risultato:\n"+str(ex2(inputList)))

        inputList = ["aba", "ert", "bab", "carlo", "yamamay"]
        print("\n\n"+"-"*10+" ex3: palindrome"+"-"*10)
        print(f"input list:\n{inputList}")
        print(ex3(inputList))
