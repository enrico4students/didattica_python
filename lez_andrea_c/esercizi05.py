# Ignorare le righe fino alla 35
from typing import Any, Callable, List, Tuple
import sys
from unittest import result


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


verbose = True
verbose = False 

def log(msg: str):
    global verbose
    if verbose:
        print(msg)

# I numeri di Tribonacci sono come i numeri di Fibonacci, ma ogni numero è funzione dei tre numeri
# di Tribonacci precedenti (anziché solo dei due precedenti come in Fibonacci).
# Ad esempio, tribonacci(n) = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3).
# tribonacci(0) = tribonacci(1) = 0
# tribonacci(2) = 1
# Scrivere una funzione ricorsiva che dato n, restituisca l'n-esimo numero di Tribonacci
def tribonacci(n: int):
    
    if n < 0:
        log(f"errore, valore negativo: {n}")
        exit(1)
    elif n in range(0,2): # 0 o 1, estremo superiore di range non è incluso, 
        # si poteva scrivere èoù semplicemente 
        # n in [0, 1]
        risultato = 0
    elif n == 2:
        risultato = 1
    else:
        risultato = tribonacci(n-1)+tribonacci(n-2)+tribonacci(n-3) 

    log(f"risultato di tribonacci({n}) = {risultato}")

    return risultato


def massimo_ric_calcolo(max_corrente, lista):

    log(f"entro: max corrente: {max_corrente} lista {lista}")

    if len(lista) == 1:
        max_corrente = max(max_corrente, lista[0])
    else:
        lista_tranne_primo_elemento = lista[1::]
        max_corrente = max(max_corrente, massimo_ric_calcolo(lista[0], lista_tranne_primo_elemento))

    log(f"esco: max corrente: {max_corrente} lista {lista}")

    return max_corrente


# Scrivere una funzione ricorsiva che data una lista di interi, restituisca il massimo
# Non usare cicli for/while
def max_recursive(l: List[int]) -> int:

    if l is None or len(l) <= 0:
        log(f"lista è None o vuota: {l}, esco")
        exit(0)

    massimo_corrente = l[0]

    risultato = massimo_ric_calcolo(massimo_corrente, l[1:])

    return risultato



# lista = [1000, 10, 5, 4, 999, 100]
# # lista = []
# print("-"*50+f"\nmassimo {lista} = {max_recursive(lista)}")
# exit(0)


# Scrivere una funzione ricorsive che calcola la somma dei numeri da 0 a n (incluso)
def sum_recursive(n: int) -> int:

    if n < 0:
        print(f"numero = {n} numeri negativi non ammessi")
        exit(1)

    if n == 0:
        risultato = 0
    else:
        risultato = n+sum_recursive(n-1)

    return risultato

# numero = 5
# print("-"*50+f"\nsum_recursive({numero}) = {sum_recursive(numero)}")
# exit(0)


# Scrivere una funzione ricorsiva che calcoli la potenza di un numero,
# utilizzando la seguente formula: power_recursive(base, exp) = base * power_recursive(b, exp-1)
# Non potete usare pow(...) o l'operatore **
def power_recursive(base: int, exp: int) -> int:
    
    if exp < 0:
        print(f"esponente = {n} esponenti negativi non ammessi")
        exit(1)

    if exp == 0:
        risultato = 1
    elif exp == 1:
        risultato = base
    else:
        risultato = base * power_recursive(base, exp-1)

    return risultato



# Scrivere una funzione ricorsiva che prende in input una stringe e restituisce
# la stringa invertita (ad esempio, "ciao" - > "oaic").
# Le uniche operazioni su stringhe permesse sono la concatenazione fra stringhe e lo slicing.

def reverse_recursive(s: str) -> str:
    
    if len(s) == 0:
        risultato = ""
    else:
        risultato = reverse_recursive(s[1:])+s[:1]

    return risultato

# stringa = "ciao"
# print(f"reverse_recursive({stringa}) = {reverse_recursive(stringa)}")
# exit(0)

# Scrivere una funzione ricorsiva che controlla se un numero è un numero primo
# (controllando che non sia divisibile per tutti i numeri precedenti ad esso).
# La funzione prende in input il numero n da controllare, ed un divisore d (all'inizio d==2)
def is_prime_recursive(n: int, d=2) -> bool:

    if n == 1: # 1 nella matematica moderna è primo, in quella non moderna no
        return False

    if d >= n: # se non ci sono divisori d < n è primo
        return True

    if n % d == 0:
        log(f"{n} è divisibile per {d}")
        return False

    return is_prime_recursive(n, d+1)

# La Torre di Hanoi (anche conosciuta come Torre di Lucas dal nome del suo inventore)
# è un rompicapo matematico composto da tre paletti e un certo numero di dischi di
# grandezza decrescente, che possono essere infilati in uno qualsiasi dei paletti.
# Il gioco inizia con tutti i dischi incolonnati su un paletto in ordine decrescente,
# in modo da formare un cono. Lo scopo del gioco è portare tutti i dischi su un paletto diverso,
# potendo spostare solo un disco alla volta e potendo mettere un disco solo su un altro disco più grande,
# mai su uno più piccolo.
# La soluzione base del gioco della torre di Hanoi si formula in modo ricorsivo.
#
# Siano i paletti etichettati con A, B e C, e i dischi numerati da 1 (il più piccolo) a n (il più grande).
# L’algoritmo si esprime come segue:
#
# Sposta i primi n-1 dischi da A a B. (Questo lascia il disco n da solo sul paletto A)
# Sposta il disco n da A a C
# Sposta n-1 dischi da B a C
#
# Scrivere una funziona che calcola il numero minimo di mosse necessarie per spostare
# gli n dischi da uno paletto all’altro.

def print_move(n: int, da: str, a: str, msg = ""):
    log(f"muovo disco {n} da {da} a {a}")

def sposta_disco(n: int, da: str, a: str, appoggio: str, nr_mosse: int):


    if n <= 1:
        nr_mosse +=1
        print_move(n, da, a, "COMPLETATO   ")
        return nr_mosse
    
    nr_mosse = sposta_disco(n-1, da, appoggio, a, nr_mosse)
    print_move(n, da, a)
    nr_mosse = sposta_disco(n-1, appoggio, a, da, nr_mosse)

    nr_mosse +=1

    return nr_mosse


def hanoi_moves(n: int) -> int:
    # https://www.youtube.com/watch?v=rf6uf3jNjbo

    nr_mosse = sposta_disco(n, "A", "C", "B", 0)

    return nr_mosse


# Nota: esercizio difficile
# Scrivere una funzione che risolve il problema dello zaino.
# Dato una lista di tuple l=[(w0, v0), (w1, v1), ...], dove wi è
# il peso in kg dell'oggetto i-esimo, e vi è il suo valore in euro,
# scrivere una funzione che prenda in input la lista l, e un peso massimo W.
# La funzione deve restituire la somma dei valori degli oggetti in una lista
# r=[(wk, vk), (wj, vj), ...] contenente un sottoinsieme delle tuple di input,
# tale che la somma dei pesi sia minore o uguale a W e il valore totale (in euro)
# sia il massimo possibile
def knapsack(l: List[Tuple[int, int]], W: int) -> int:
    # https://www.youtube.com/watch?v=gu2HEn15h-c
    # 
    pass


# numero = 10
# print("-"*50+f"\ntribonacci di {numero} = {tribonacci(numero)}")
# exit(0)


# Test funzioni
# check_test(tribonacci, 0, 0)
# check_test(tribonacci, 0, 1)
# check_test(tribonacci, 1, 2)
# check_test(tribonacci, 66012, 21)
# check_test(max_recursive, 100, [0, 1, 2, 100, 3, 4, 7])
# check_test(max_recursive, 200, [200, 1, 2, 100, 3, 4, 7])
# check_test(max_recursive, 337, [0, 1, 2, 100, 3, 4, 337])

# for t in range(10):
#     check_test(sum_recursive, sum(range(t+1)), t)

# for base in range(3):
#     for exp in range(3):
#         check_test(power_recursive, base**exp, base, exp)
# check_test(reverse_recursive, "oaic", "ciao")
# check_test(reverse_recursive, "itopinonavevanonipoti", "itopinonavevanonipoti")
# check_test(is_prime_recursive, False, 1)
# check_test(is_prime_recursive, True, 2)
# check_test(is_prime_recursive, True, 3)
# check_test(is_prime_recursive, False, 4)
# check_test(is_prime_recursive, True, 5)
# check_test(is_prime_recursive, False, 6)
# check_test(is_prime_recursive, False, 35)
# check_test(is_prime_recursive, True, 89)

for n in range(1, 20):
    check_test(hanoi_moves, 2**n - 1, n)

exit(0)
check_test(knapsack, 220, [(10, 60), (20, 100), (30, 120)], 50)
check_test(knapsack, 90, [(5, 10), (4, 40), (6, 30), (3, 50)], 10)
# values = [
#        360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
#        78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
#        87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
#        312]
# weights = [
#        7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
#        42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
#        3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13]
#long_l = []
# for i in range(len(values)):
#    long_l += [(weights[i], values[i])]
#check_test(knapsack, 7534, long_l, 850)
