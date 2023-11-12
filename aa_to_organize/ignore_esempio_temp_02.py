

import random

# i commenti li usiamo per scrivere siegazioni e gli interpreti e compilatori
# ignorano quello che e' scritto nei commenti
# for i in range(5,10):
#     print(i)

# ITERAZIONE INDETERMINATA
print("eseguo un'iterazione indeterminata")
valore = -1 # un valore  a caso
while valore < 50:
    print("eseguo le istruzioni dentro il loop/iterazione")
    valore = random.randint(0,99)
    print("adesso la variabile 'valore' contiene il valore generato in modo random: ", valore)

print("sono fuori dal tunned del divertimetnto (Capareza)")


# ITERAZIONE ETERMINATA
print("\neseguo un'altra iterazione (ciclo for con lista)")
vettore_in_realta_lista = [1, "forza roma", 4.5]
for elemento_corrent in vettore_in_realta_lista:
     print(elemento_corrent)

print("\neseguo un'altra iterazione (ciclo for con funzione range(start, stop))")
for elemento_corrent in range(4,8):
     print(elemento_corrent)




exit(0)

squadara_persona_incontrata1 = "romanista"

squadara_persona_incontrata2 = "laziale"


if squadara_persona_incontrata2 == "romanista":
    print("sciao frate'!")


eta = 18
if eta < 18:
    print("non puoi guidare la macchina legalmente")
else:
    print("vai piano")



print("fine")
