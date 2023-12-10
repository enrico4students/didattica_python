
def input_numerico(prompt: str):

    while True:
        stringa_inserita = input(prompt)
        try:
            numero_inserito = float(stringa_inserita)
        except:
            print(f"input non accettabile come numero: {stringa_inserita}")
        else:
            return numero_inserito


def input_numerico2(prompt: str, minimo=None, massimo=None):

    if minimo is not None:
        prompt += f" (maggiore di {minimo}) "
    if massimo is not None:
        prompt += f" (minore di {massimo}) "

    while True:
        numero = input_numerico(prompt)
        if minimo is not None and numero < minimo:
            print(f"{numero} non è >= {minimo}")
            continue
        if massimo is not None and numero > massimo:
            print(f"{numero} non è <= {massimo}")
            continue

        break # esci dal while True


    return numero


x = input_numerico2("inserisci un numero: ", 2, 10)
