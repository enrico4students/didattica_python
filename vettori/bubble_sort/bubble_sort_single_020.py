

def bubble_sort(vettore):

    debbo_controllare_vettore = True # almeno un controllo dobbiamo farlo

    while debbo_controllare_vettore:
        debbo_controllare_vettore = False # relativo alla prossima iterazione/controllo in questa siamo gia' entrati 
        for i in range(len(vettore)-1):
            if vettore[i] > vettore[i+1]: # ordine non desiderato, dobbiamo scambiarli 
                # Python fa lo scambio senza costringerci a creare una variabile di appoggio
                # la crea lui dietro le quinte. 
                vettore[i], vettore[i+1] = vettore[i+1], vettore[i] # scambio
                debbo_controllare_vettore = True 

vettore = [9, 1, 8, 2, 7, 3, 6, 4, 5]
bubble_sort(vettore)
print(vettore)
