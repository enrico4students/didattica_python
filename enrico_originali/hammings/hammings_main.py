

import random
import math

import hammings_utils as hutil

LUNG_MESSAGGI = 8


pos_bits_mesg_l = [] # indici dei bits del messaggio
pos_bits_ctrl_l = [] # indici dei bits di controllo


def inizializzazioni():

    for i in range(1, 256):
        log2_i = math.log2(i)
        if log2_i == int(log2_i):
            pos_bits_ctrl_l.append(i-1)
        else:
            pos_bits_mesg_l.append(i-1)

    print(f"indici bits controllo {pos_bits_ctrl_l}")
    print(f"indici bits messaggio {pos_bits_mesg_l}")
    print()


def genera_messaggio(lung):

    messaggio = []
    for i in range(lung):
        temp = random.randint(0, 1)
        # print(f"temp: {temp}")
        messaggio.append(temp)
    return messaggio


def crea_codeword(messaggio):
    
    codeword = [9]*64 # andrebbe calcolata matematicamente
    
    # --- copia i bits del messaggio nella codeword
    pos_bit_msg = 0
    for pos_bit_msg_in_cword in pos_bits_mesg_l:

        if pos_bit_msg_in_cword >= len(codeword):
            print(f"errore interno, eccceduta lunghezza codeword")
            exit(1)
            break
        codeword[pos_bit_msg_in_cword] = messaggio[pos_bit_msg]
        pos_bit_msg += 1
        if pos_bit_msg >= len(messaggio): # raggiunta fine messaggio
            break


    # --- avvalora i bits di controllo, usa parità pari

    for pos_ctrl in pos_bits_ctrl_l:

        print(f"calcolo valore parita bit controllo(rettificato): {pos_ctrl+1}")        
        parita_trovata = 0 
        for i in range(len(codeword)):
            bin_digits_posizione = hutil.bindigits_list_from_num(i)
            if bin_digits_posizione[pos_ctrl] != 1:
                continue # ignoro, non è nel dominio di parità di questo bit di controllo 

            print(f"--- esamino bit codeword (rettificato): {i+1}: {codeword[i+1]}")        
            parita_trovata += bin_digits_posizione[pos_ctrl]

        print(f"paritaà trovata: {parita_trovata}")
        valore_bit_controllo = 0 if (parita_trovata%2 == 0) else 1
        codeword[pos_ctrl] = valore_bit_controllo

    return codeword


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