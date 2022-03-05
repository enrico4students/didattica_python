
vettore = [9, 1, 8, 2, 7, 3, 6, 4, 5]


debbo_controllare_vettore = True # almeno un controllo dobbiamo farlo

while debbo_controllare_vettore:
    debbo_controllare_vettore = False # relativo alla prossima 
                                    # iterazione/controllo
                                    # in questa siamo gia' entrati 
    fatto_scambio = False
    for i in range(len(vettore)-1):

        if vettore[i] > vettore[i+1]:    
            # ordine non desiderato, dobbiamo scambiarli 
            var_per_scambio = vettore[i] # salviamo altrimenti viene sovrascritto
            vettore[i]      = vettore[i+1]# salviamo altrimenti viene sovrascritto
            vettore[i+1]    = var_per_scambio # completato scambio
            fatto_scambio = True
            debbo_controllare_vettore = fatto_scambio 

print(vettore)
