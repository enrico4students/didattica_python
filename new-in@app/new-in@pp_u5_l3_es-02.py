

massimo = -32767 # dovremmo cercare il min numero reale, 
                 # non abbiamo tempo, prendiamo il classico minimo intero

num_numeri_da_inserire = int(input('Quanti numeri vuoi inseire? '))

for i in range(0,num_numeri_da_inserire):
    current_num = int(input('inserisci un numero: '))
    print("hai inserito {}".format(current_num))
    if current_num > massimo:
        massimo = current_num

print("il massimo dei numeri inseriti e': {}".format(massimo))



