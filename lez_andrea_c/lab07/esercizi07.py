# Ignorare le righe fino alla 31
from typing import Any, Callable, List, Tuple, Dict, Union
import sys
from unittest import result
import images

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Esegue un test e controlla il risultato
def check_test(func: Callable, expected: Any, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        expected_str = repr(expected)
        test_outcome = "succeeded" if (result == expected) else "failed"
        color = bcolors.OKGREEN if (result == expected) else bcolors.FAIL
        print(f'{color}Test on {func_str} on input {args_str} {test_outcome}. Output: {result_str} Expected: {expected_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERROR: {func_str}({args_str}) => {error_str}')


# Scrivere una funzione che data una matrice di interi, restituisce la matrice trasposta
# Ad esempio:
# 5 2 9    ->  5 3
# 3 1 0        2 1
#              9 0
def transpose(m : List[List[int]]) -> List[List[int]]:

    # Ottieni il numero di righe e colonne della matrice
    nr_righe = len(m)    # elementi più esterni
    nr_colonne = len(m[0])  # elementi interni a una riga, quindi a m[i]

    # Inizializza una nuova matrice vuota per la trasposta
    # le colonne sono interne alle righe quindi nidificate
    trasposta_matrice = [[0 for _ in range(nr_righe)] for _ in range(nr_colonne)]

    # Calcola la trasposta
    for i in range(nr_righe):
        for j in range(nr_colonne):
            trasposta_matrice[j][i] = m[i][j] # semplicemente invertiamo gli indici

    return trasposta_matrice


# Scrivere una funzione che date due matrici, restituisca una matrice
# equivalente alla somma fra le due matrici.
# Esempio:
#     1 0 1        1 2 1       2 2 2
#     2 1 1   +    2 3 1   =   4 4 2
#     0 1 1        4 2 2       4 3 3
#     1 1 2        1 2 3       2 3 5
# Restituire None se le due matrici non possono essere sommate.
def matrix_matrix_sum(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

    assert(len(A) == len(B) and len(A[0]) == len(B[0]))

    # liste più interne (righe) hanno nr-di-colonne elementi
    
    # ERRATO
    empty_row = [None] * len(A[0])
    empty_matrix = [ empty_row ] * len(A)

    for i in range(len(empty_matrix)):
        print(id(empty_matrix[i]))
        for j in range(len(empty_matrix[0])):
            print("     "+ str(id(empty_matrix[i][j])), end = ", ")
        print()


    for i in range(len(A)):
        for j in range(len(A[0])):
            empty_matrix[i][j] = i*10+j

    for r in empty_matrix:
        for c in r:
            print(c, end = ", ")
        print()



    return empty_matrix


x = matrix_matrix_sum([ [0,1], [2,3], [4,5]], [ [10, 11], [12, 13], [14, 15] ])
print(x)
print(x)


# Scrivere una funzione che date due matrici, restituisca una matrice
# equivalente al prodotto fra le due matrici.
# Esempio:
#     1 0 1        1 2 1       5  4 3
#     2 1 1   x    2 3 1   =   8  9 5
#     0 1 1        4 2 2       6  5 3
#     1 1 2                    11 9 6
# Restituire None se le due matrici non possono essere moltiplicate.
def matrix_matrix_mul(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    pass

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola l'immagine rotata di 90 gradi a destra e invertita rispetto l'asse verticale.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione 
# (non vengono effettuati test automatici)
def img_rotate_right_and_flip_v(img_in: str, img_out : str):
    # Leggere!!!!
    #im = images.load(img_in)  # legge l'immagine del file img_in e la pone nella matrice im
    # im_out = <scrivete il vostro codice>
    #images.save(im_out, img_out)  # salva l'immagine im_out nel file img_out
    pass


# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola l'immagine con i canali rosso e blu invertiti.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione 
# (non vengono effettuati test automatici)
def img_invert_channels(img_in: str, img_out : str):
    pass

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola un'immagine in cui ognuno dei 3 canali è quantizzato su 128 possibili valori 
# (cioè, ogni canale può solo assumere 128 valori anzichè 256).
# Ad esempio, (21, 126, 3) diventa (10, 63, 2)
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione 
# (non vengono effettuati test automatici)
def img_quantize(img_in: str, img_out : str):
    pass

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola un'immagine in cui la metà destra dell'immagine è scambiata con la metà sinistra.
# (Cioè, le colonne nel range [0, N/2] diventano le colonne [N/2, N] nella nuova immagine,
# e le colonne [N, N/2] nella vecchia immagine diventano le colonne [0, N/2] nella nuova immagine).
# Si può assumere che l'immagine abbia un numero di colonne divisibile per 2.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione 
# (non vengono effettuati test automatici)
def img_invert_half(img_in: str, img_out : str):
    pass

# Test funzioni
check_test(transpose, [[5, 3], [2, 1]], [[5, 2], [3, 1]])
check_test(transpose, [[5, 3], [2, 1], [9, 0]], [[5, 2, 9], [3, 1, 0]])
check_test(transpose, [[5, 3]], [[5], [3]])
check_test(transpose, [[5], [3]], [[5, 3]])
check_test(matrix_matrix_sum, [[2, 2, 2], [4, 4, 2], [4, 3, 3], [2, 3, 5]], [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1], [4, 2, 2], [1, 2, 3]])
check_test(matrix_matrix_sum, None, [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2], [2, 3], [4, 2], [1, 2]])
check_test(matrix_matrix_sum, None, [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1], [4, 2, 2]])
check_test(matrix_matrix_mul, [[5, 4, 3], [8, 9, 5], [6, 5, 3], [11, 9, 6]], [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1], [4, 2, 2]])
check_test(matrix_matrix_mul, [[5], [8], [6], [11]], [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1], [2], [4]])
check_test(matrix_matrix_mul, None, [[1, 0, 1], [2, 1, 1], [0, 1, 1], [1, 1, 2]], [[1, 2, 1], [2, 3, 1]])
img_rotate_right_and_flip_v("img.png", "img_rotate_flip.png")
img_invert_channels("img.png", "img_invert_channels.png")
img_quantize("img.png", "img_quantized.png")
img_invert_half("img.png", "img_inverted_half.png")