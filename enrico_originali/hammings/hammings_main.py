

import random
import math

import hammings_utils as hutil

LUNG_MESSAGGI = 8


pos_bits_mesg = [] # indici dei bits del messaggio
pos_bits_ctrl = [] # indici dei bits di controllo


def inizializzazioni():

    for i in range(1,256):
        log2_i = math.log2(i)
        if log2_i == int(log2_i):
            pos_bits_ctrl.append(i)
        else:
            pos_bits_mesg.append(i)

    print(f"indici bits controllo {pos_bits_ctrl}")
    print(f"indici bits messaggio {pos_bits_mesg}")


def genera_messaggio(lung):

    messaggio = []
    for i in range(lung):
        temp = random.randint(0, 1)
        # print(f"temp: {temp}")
        messaggio.append(temp)
    return messaggio


def crea_codeword(messaggio):
    # 
    
    return messaggio + [9,9,9]


def trasmetti_codeword(codeword):
    # ritorna la codeword, eventualmente corrotta
    return "111111111111111111111111"

def analizza_codeword_ricevuta(codeword):
    
    # if ....
    print(f"codeword: {codeword} è corretta")
    print(f"codeword contiene un errore, codeword corretta: {codeword} ")


def main():

    NUMERO_MESSAGGI_TEST = 6

    inizializzazioni()

    for i in range(6):
        
        messaggio = genera_messaggio(LUNG_MESSAGGI)
        print(f"messaggio: {messaggio}")

        codeword_tx = crea_codeword(messaggio)
        print(f"codeword: {codeword_tx}")


        codeword_rx = trasmetti_codeword(codeword_tx)

        analizza_codeword_ricevuta(codeword_rx)


if __name__ == "__main__":
    main()