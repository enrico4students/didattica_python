

dividendo = 3
divisore = 3

rimanente = dividendo

i = 0
while rimanente >= divisore:
     rimanente = rimanente - divisore
     i = i+1
     print("iterazione {} sottraggo il divisore {} rimanente {}".format(i, divisore, rimanente))

print("{} diviso {}".format(dividendo, divisore))
print("il risultato e' {} il resto è {}".format(i, rimanente))