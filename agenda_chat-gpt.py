import csv
import re

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

def ricerca_persona(lista, campo, valore):
    risultati = []
    for persona in lista:
        if re.search(valore, persona[campo], re.IGNORECASE):
            risultati.append(persona)
    return risultati

def visualizza_lista_paginata(lista, pagina_corrente, dimensione_pagina):
    inizio = (pagina_corrente - 1) * dimensione_pagina
    fine = inizio + dimensione_pagina
    for persona in lista[inizio:fine]:
        print(persona)

def main():
    lista_persone = []
    dimensione_pagina = 2  # Imposta il numero di persone da visualizzare per pagina
    pagina_corrente = 1

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
            salva_su_file(lista_persone, 'lista_persone.csv')

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
            visualizza_lista_paginata(lista_persone, pagina_corrente, dimensione_pagina)
            pagina_corrente += 1

        elif scelta == '0':
            # Esci
            break

        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
