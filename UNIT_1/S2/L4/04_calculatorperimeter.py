# Traccia: Si scriva un programma in Python che in base alla scelta dellʼutente permetta di calcolare il perimetro di diverse figure geometriche (scegliete pure quelle che volete voi).

# Per la risoluzione dellʼesercizio abbiamo scelto:
# ● Quadrato (perimetro = lato*4).
# ● Cerchio (circonferenza = 2*pi greco*r).
# ● Rettangolo (perimetro= base*2 + altezza*2.

import math

#Scegliere la figura geometrica
input_figure = int(input("Scegli la figura geometrica per calcolare il perimetro:\n1. Quadrato\n2. Cerchio\n3. Rettangolo\nInserisci il numero corrispondente alla tua scelta: "))

# Funzione per calcolare il perimetro del quadrato
if input_figure == 1:
    lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
    perimetro_quadrato = lato * 4
    print(f"Il perimetro del quadrato è: {perimetro_quadrato}")

# Funzione per calcolare la circonferenza del cerchio
elif input_figure == 2:
    raggio = float(input("Inserisci il raggio del cerchio: "))
    circonferenza_cerchio = 2 * math.pi * raggio
    print(f"La circonferenza del cerchio è: {circonferenza_cerchio}")

#Funzione per calcolare il perimetro del rettangolo
elif input_figure == 3:
    base = float(input("Inserisci la lunghezza della base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    perimetro_rettangolo = 2 * (base + altezza)
    print(f"Il perimetro del rettangolo è: {perimetro_rettangolo}")

# Questo codice usa il metodo che in programmazione viene chiamato "struttura condizionale multipla" per eseguire diverse sezioni di codice in base alla scelta dell'utente.
