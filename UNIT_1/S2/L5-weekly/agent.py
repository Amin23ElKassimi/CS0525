# Il programma simula un assistente virtuale che risponde a comandi specifici dell'utente.

# qui si importa il modulo datetime per lavorare con date e orari
import datetime


# Il programma chiede all'utente di inserire un comando.
# Se l'utente digita "esci", il programma stampa "Arrivederci!" e termina.
# Altrimenti, il programma chiama la funzione assistente_virtuale con il comando dell'utente.


# c'era Errore nel ciclo while era scritto male
# Qui definisce con l'istruzione "def" la funzione assistente_virtuale che prende l'argomento "comando" ovver
def assistente_virtuale(comando):

# - Se il comando è "Qual è la data di oggi?",
# salva la data odierna in una variabile usando il modulo date time.
# dopo di che salva la risposta concatenando la stringa "La data di oggi è " con la data formattata con il metodo strftime.
# che formatta la data nel formato giorno/mese/anno.
    if comando == "Qual è la data di oggi?":
        oggi = datetime.datetoday()
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")

# - Se il comando è "Che ore sono?",
# salva l'ora attuale in una variabile usando il modulo date time.
# dopo di che salva la risposta concatenando la stringa "L'ora attuale è " con l'ora formattata con il metodo strftime.
# che formatta l'ora nel formato ore:minuti.
    elif comando == "Che ore sono?":
        ora_attuale = datetime.datetime.now().time()
        risposta = "L'ora attuale è " + ora_attuale.strftime("%H:%M")

# - Se il comando è "Come ti chiami?",
# salva la risposta con la stringa "Mi chiamo Assistente Virtuale".
    elif comando == "Come ti chiami?":
        risposta = "Mi chiamo Assistente Virtuale"

# - Se il comando non corrisponde a nessuno di quelli sopra,
# salva la risposta con la stringa "Non ho capito la tua domanda.".
    else:
        risposta = "Non ho capito la tua domanda."

# Returna la risposta salvata. "return" e' usato per restituire un valore da una funzione in Python.
    return risposta



while True:
    comando_utente = input("Cosa vuoi sapere? ")
    if comando_utente == "esci":
        print("Arrivederci!")
        break
    else:
        print(assistente_virtuale(comando_utente))
