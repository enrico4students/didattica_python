import csv
import re


lista_persone = []
fname = 'lista_persone.csv'

def aggiungi_persona(lista, nome, cognome, telefono, email, citta):
    persona = {'Nome': nome, 'Cognome': cognome, 'Telefono': telefono, 'Email': email, 'Città': citta}
    lista.append(persona)


def salva_su_file(lista, nome_file):
    with open(nome_file, 'w', newline='') as file_csv:
        campo_nomi = ['Nome', 'Cognome', 'Telefono', 'Email', 'Città']
        writer = csv.DictWriter(file_csv, fieldnames=campo_nomi, delimiter='\t')
        
        writer.writeheader()
        for persona in lista:
            writer.writerow(persona)


def leggi_da_file(nome_file):

    global lista_persone
    lista_letti = []

    with open(nome_file, 'r', newline='') as file_csv:
        campo_nomi = ['Nome', 'Cognome', 'Telefono', 'Email', 'Città']
        # reader = csv.DictReader(file_csv, fieldnames=campo_nomi, delimiter = "\t")
        reader = csv.DictReader(file_csv, delimiter = "\t")
        # for row in reader:
        #     lista_letti.append(row) 
        lista_letti.extend(reader)

    return lista_letti


def ricerca_persona(lista, campo, valore):
    risultati = []
    for persona in lista:
        if re.search(valore, persona[campo], re.IGNORECASE):
            risultati.append(persona)
    return risultati


def visualizza_lista_paginata(lista, dimensione_pagina):

    for i, persona in enumerate(lista):
        print(persona)
        if (i % dimensione_pagina == 0 and i > 0):
            scelta = input("premere return per continuare a stampare, u per uscire ")
            if scelta in ['u', 'U']:
                break


def main():

    global lista_persone

    dimensione_pagina = 2  # Imposta il numero di persone da visualizzare per pagina

    lista_persone = leggi_da_file(fname)

    while True:
        print("\nMenu:")
        print("1. Inserisci una nuova persona")
        print("2. Ricerca")
        print("3. Visualizza lista pagina per pagina")
        print("0. Esci")

        scelta = input("Inserisci il numero corrispondente all'opzione desiderata: ")

        if scelta == '1':
            # Inserisci una nuova persona
            nome = input("Nome: ")
            cognome = input("Cognome: ")
            telefono = input("Telefono: ")
            email = input("Email: ")
            citta = input("Città: ")
            aggiungi_persona(lista_persone, nome, cognome, telefono, email, citta)
            salva_su_file(lista_persone, fname)

        elif scelta == '2':
            # Ricerca
            campo_ricerca = input("Inserisci il campo su cui vuoi effettuare la ricerca (Nome, Cognome, Telefono, Email, Città): ")
            valore_ricerca = input("Inserisci il valore da cercare (può essere una regex): ")
            risultati_ricerca = ricerca_persona(lista_persone, campo_ricerca, valore_ricerca)

            if risultati_ricerca:
                print("\nRisultati della ricerca:")
                for persona in risultati_ricerca:
                    print(persona)
            else:
                print("\nNessun risultato trovato.")

        elif scelta == '3':
            # Visualizza lista pagina per pagina
            visualizza_lista_paginata(lista_persone, dimensione_pagina)

        elif scelta == '0':
            # Esci
            break

        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
