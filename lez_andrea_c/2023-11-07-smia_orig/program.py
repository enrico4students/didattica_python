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

nome        = "NOME"
cognome     = "COGNOME"
matricola   = "MATRICOLA"

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
def ex1(inputList):
    

    anaDict = {}

    for stringa in inputList:
        # print(stringa)
        # for carattere in stringa:
        #     print(carattere)
        anagrammi_di_una_stringa = set()
        string_as_char_list = list(stringa)
        for pos_primo in range(len(string_as_char_list)):
            for pos_secondo in range(pos_primo+1,len(string_as_char_list)):
                # print(pos_primo, pos_secondo, string_as_char_list[pos_primo], string_as_char_list[pos_secondo])
                temp = string_as_char_list[pos_primo] # salviamo perchè l'assegnamento seguente lo sovraschiverà
                string_as_char_list[pos_primo] = string_as_char_list[pos_secondo]
                string_as_char_list[pos_secondo] = temp
                anagramma = "".join(string_as_char_list)
                # print(anagramma)
                anagrammi_di_una_stringa.add(anagramma)
        # print(anagrammi_di_una_stringa)
        tupla2 = (anagrammi_di_una_stringa, len(anagrammi_di_una_stringa)) 
        anaDict[stringa] = tupla2
    
    return anaDict

# ----------------------------------- Esercizio 2: subDict ----------------------------------- #
"""
Es. 2: 
"""

# funzione che ritorna subDict; NON rinominatela
def ex2(inputList):
    pass



# ----------------------------------- Esercizio 3: palDict ----------------------------------- #
"""
Es. 3: 10 punti
"""

# funzione che ritorna palDict; NON rinominatela
def ex3(inputList):
    pass

if __name__ == "__main__":
    lista_parole = ["forza", "Sinner", "sei", "numero 4", "del mondo"]
    lista_parole = ["01234"]
    lista_parole = ["enrico", "andrea"]
    x = ex1(lista_parole)
    print(x)