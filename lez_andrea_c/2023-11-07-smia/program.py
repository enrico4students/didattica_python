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
      anagrammi = set()
      stringa_l = list(stringa)
      for first in range(len(stringa_l)):
          for second in range(first+1,len(stringa_l)):
              anagramma_corr = stringa_l.copy()
              temp = anagramma_corr[first]
              anagramma_corr[first] = anagramma_corr[second]
              anagramma_corr[second] = temp
              anagramma_corr = "".join(anagramma_corr)
              print(f"scambio {first} {second}\n{stringa}\n{anagramma_corr}")
              if anagramma_corr not in anagrammi:
                anagrammi.add(anagramma_corr)
              else:
                  print(f"{anagramma_corr} già presente")
      # for i, anagramma in enumerate(anagrammi):
      #     print(f"anagramma {i+1:>2}: {anagramma}")
      anaDict[stringa] = (anagrammi, len(anagrammi))
  return anaDict




# ----------------------------------- Esercizio 2: subDict ----------------------------------- #
"""
Es. 2: 
"""

# funzione che ritorna subDict; NON rinominatela
def ex2(inputList):
  
  subDict = {}
  for stringa in inputList:
    sottostringhe = set()
    for len_substr in range(2, len(stringa)):
      for start in range(0,len(stringa)-len_substr+1):
          cur_substr = stringa[start:start+len_substr]
          print(f"len substr: {len_substr} start: {start} substr: {cur_substr}")
          sottostringhe.add(cur_substr)
  
    subDict[stringa] =(sottostringhe, len(sottostringhe))
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

  palDict = { True: (palindrome, len(palindrome)),
              False: (non_palindrome, len(non_palindrome))  }
  return palDict



if __name__ == "__main__":
    print(ex1(["enrico"]))
    print(ex2(["enrico"]))
    print(ex3(["aba", "ert", "bab", "carlo"]))