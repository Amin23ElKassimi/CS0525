# Traccia: Si scriva un programma in Python che in base alla scelta dellʼutente permetta di calcolare il perimetro di diverse figure geometriche (scegliete pure quelle che volete voi).

# Per la risoluzione dellʼesercizio abbiamo scelto:
# ● Quadrato (perimetro = lato*4).
# ● Cerchio (circonferenza = 2*pi greco*r).
# ● Rettangolo (perimetro= base*2 + altezza*2.

import math

#Scegliere la figura geometrica
input_figure = input("Scegli la figura geometrica (quadrato, cerchio, rettangolo): ").lower()

# Funzione per calcolare il perimetro del quadrato
if input_figure == "quadrato":
    lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
    perimetro_quadrato = lato * 4
    print(f"Il perimetro del quadrato è: {perimetro_quadrato}")


# Funzione per calcolare il perimetro del cerchio

# Funzione per calcolare il perimetro del rettangolo
