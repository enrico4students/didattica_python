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

def dump_matrix_ids(m):
    for i in range(len(m)):
        print(id(m[i]))
        for j in range(len(m[0])):
            print("     "+ str(id(m[i][j])), end = ", ")


def matrix_matrix_sum(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None

    # approccio semplice
    # result_matrix = A.copy() # non necessario inizializzarla
                               # verrà comunque totalmente sovrascritta
    # approccio complesso a fini di pratica didattica
    result_matrix = [ [0 for c in range(len(A[0])) ] for r in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A[0])):
            result_matrix[i][j] = A[i][j]+B[i][j]

    return result_matrix

if False:
    x = matrix_matrix_sum([ [0,1], [2,3], [4,5]], 
                        [ [10, 11], [12, 13], [14, 15] ])
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
    
    nr_cols_A = len(A[0])
    nr_rows_B = len(B)
    if nr_cols_A != nr_rows_B:
        print(f"moltiplicazione non possible nr cols A {nr_cols_A} diverso da nr righe B {nr_rows_B}")
        return None

    result_matrix = [[ 0 for _ in B[0] ] for _ in A]


    for idx_row_A in range(len(A)):
        for idx_col_B in range(len(B[0])):
            # print(f"moltiplico riga {idx_row_A} di A con col {idx_col_B} di B")
            ris_molt = 0
            for idx_molt in range(nr_cols_A):
                ris_molt += A[idx_row_A][idx_molt] * B [idx_molt][idx_col_B]
            result_matrix[idx_row_A][idx_col_B] = ris_molt

    return result_matrix

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola l'immagine rotata di 90 gradi a destra e invertita rispetto l'asse verticale.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione 
# (non vengono effettuati test automatici)
def img_rotate_right_and_flip_v(img_in: str, img_out : str):
    # Leggere!!!!
    im = images.load(img_in)  # legge l'immagine del file img_in e la pone nella matrice im

    # mio codice
    print(f"type(im): {type(im)} {len(im)}x{len(im[0])}" )

    im = im[::-1]
    im = transpose(im)
    im = im[::-1]

    im_out = im
    
    images.save(im_out, img_out)  # salva l'immagine im_out nel file img_out


# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola l'immagine con i canali rosso e blu invertiti.
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione 
# (non vengono effettuati test automatici)
def img_invert_channels(img_in: str, img_out : str):

    import copy

    im = images.load(img_in)  # legge l'immagine del file img_in e la pone nella matrice im

    # mio codice
    im_out = copy.deepcopy(im)

    for i in range(len(im)):
        for j in range(len(im[0])):
            r, g, b = im[i][j]
            im_out[i][j] = b, g, r
            # if r != b:
            #     print(f"{im[i][j]}\n{im_out[i][j]}\n")            
            #     print("")

    images.save(im_out, img_out)  # salva l'immagine im_out nel file img_out

# Definire una funzione che dato il nome di un file (img_in) contenente un'immagine,
# calcola un'immagine in cui ognuno dei 3 canali è quantizzato su 128 possibili valori 
# (cioè, ogni canale può solo assumere 128 valori anzichè 256).
# Ad esempio, (21, 126, 3) diventa (10, 63, 2)
# L'immagine risultante viene salvata nel file con nome indicato come parametro (img_out)
# Per leggere/scrivere l'immagine usare i comandi load/save del modulo "images" visto a lezione.
# Controllare il file risultante per verificare la correttezza della funzione 
# (non vengono effettuati test automatici)
def img_quantize(img_in: str, img_out : str):

    im = images.load(img_in)  # legge l'immagine del file img_in e la pone nella matrice im

    # mio codice
    for i in range(len(im)):
        for j in range(len(im[0])):
            r, g, b = im[i][j]
            im[i][j] = r//2, g//2, b//2

    images.save(im, img_out)  # salva l'immagine im_out nel file img_out

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

    import copy

    im = images.load(img_in)  # legge l'immagine del file img_in e la pone nella matrice im

    im_out = copy.deepcopy(im)

    for row_idx in range(len(im)):
        for col_idx in range(len(im[0])):
            im_out[row_idx][col_idx] = im[row_idx][-col_idx]

    images.save(im_out, img_out)  # salva l'immagine im_out nel file img_out


# Test funzioni
if True:
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
    img_rotate_right_and_flip_v("./lez_andrea_c/lab07/img.png", "./lez_andrea_c/lab07/img_rotate_flip.png")
    img_invert_channels("./lez_andrea_c/lab07/img.png", "./lez_andrea_c/lab07/img_invert_channels.png")
    img_quantize("./lez_andrea_c/lab07/img.png", "./lez_andrea_c/lab07/img_quantized.png")
    img_invert_half("./lez_andrea_c/lab07/img.png", "./lez_andrea_c/lab07/img_inverted_half.png")