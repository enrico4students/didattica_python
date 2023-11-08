

"""
SOLO PER I PIU' CURIOSI
Usa qualche idioam (caratteristica specifica) di Python, probabilmente in modo non ottimale,
forse ci sono altri idiomi, non utilizzati, che avrebbero reso il codice più compatto,
(il passaggio dei parametri è un'area in cui cio' è probabile)
"""

dividendo_divisore = ((0,2),(4,2), (10,3), (100,3), (0, 10))


def divisione_tramite_sottrazioni_ripetute(dividendo, divisore, verbose = False):
     rimanente = dividendo

     i = 0
     while rimanente >= divisore:
          rimanente = rimanente - divisore
          i = i+1
          print("iterazione {} sottraggo il divisore {} rimanente {}".format(i, divisore, rimanente))
     quoziente = i # superfluo, solo per leggibilità didattica
     resto = rimanente
     return quoziente, resto


for coppie in dividendo_divisore:
     quoziente, resto = divisione_tramite_sottrazioni_ripetute(coppie[0], coppie[1])
     print("\n\n{} diviso {}".format(coppie[0], coppie[1]))
     print("il risultato e' {} il resto è {}".format(quoziente, resto))