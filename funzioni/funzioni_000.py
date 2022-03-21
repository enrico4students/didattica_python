
# definizione della funzione
def nome_fissato():
    return "Mario"

# chiamiamo/eseguiamo la funzione
valore_ritornato_dalla_funzione = nome_fissato()
print(valore_ritornato_dalla_funzione)


def saluta(nome):
    valore_da_ritornare = "ciao"+ " " + nome
    return valore_da_ritornare

valore_ritornato_dalla_funzione = saluta("Mario")
print(valore_ritornato_dalla_funzione)


def voto_equivalente_0_9(punti_fino_a_100):
    voto_fino_a_9_con_parte_decimale = punti_fino_a_100/100 * 9
    # +0.99 modo "artigianale" per arrotondare per eccesso, es 7.02 -> 8.0.1 -> 8
    voto_fino_a_9_intero = int(voto_fino_a_9_con_parte_decimale+0.99) 
    return voto_fino_a_9_intero

punti_presi = 90
voto_0_9 = voto_equivalente_0_9(punti_fino_a_100 = punti_presi)
print("voto 0-9 equivalente a {} punti e' {} (arrotondato verso l'alto)".format(punti_presi, voto_0_9))


def voto_equivalente_0_max(punti_fino_a_100, max_voto = 9):
    # prende come parametri, cioe' in input 
    # - punti fra 0 e 100 
    # - il voto massimo possibile
    # ritorna il voto corrispondente fra 0 e il valore del parametro max_voto 
    voto_fino_a_9_con_parte_decimale = punti_fino_a_100/100 * max_voto
    # +0.99 modo "artigianale" per arrotondare per eccesso, es 7.02 -> 8.0.1 -> 8
    voto_fino_a_9_intero = int(voto_fino_a_9_con_parte_decimale+0.99) 
    return voto_fino_a_9_intero

punti_presi = 90
max = 30
voto_0_30 = voto_equivalente_0_max(punti_fino_a_100 = punti_presi, max_voto = max)
print("se max voto e' {} il voto equivalente a {} punti e' {}".format(max, punti_presi, voto_0_30))


def area_quadrato(lato):
    return lato*lato   # non dobbiamo creare variabili dedicate per  il valore di ritorno
    # nei casi precedenti sono state create per comodita' didattica


def ritorna_tupla():
    return "Mario", "Rossi", 33

tupla_ritornata_dalla_funzione = ritorna_tupla()

print("primo valore ritornato = ",   tupla_ritornata_dalla_funzione[0])
print("secondo valore ritornato = ", tupla_ritornata_dalla_funzione[1])
print("terzo valore ritornato = ",   tupla_ritornata_dalla_funzione[2])