
positivi, negativi, nulli = 0, 0, 0

while True:
    numero_inserito = int(input("Inserire un numero (numero negativo per terminare): "))
    if numero_inserito > 0:
        positivi += 1
    elif numero_inserito == 0:
        nulli += 1
    else:
        negativi += 1
        break

print("I numeri inseriti erano\n{} positivi \n{} nulli\n{} negativi ".format(positivi, nulli, negativi))

