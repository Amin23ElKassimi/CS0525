import datetime
import re

def normalizza_input(testo):
    """Normalizza l'input rimuovendo punteggiatura e convertendo in minuscolo"""
    if not testo or not testo.strip():
        return ""
    testo = testo.lower().strip()
    testo = re.sub(r'[?!.,;:]', '', testo)
    return testo

def assistente_virtuale(comando):
    """Assistente virtuale con gestione flessibile dei comandi"""
    comando_norm = normalizza_input(comando)
    
    # Gestione input vuoto
    if not comando_norm:
        return "Non hai scritto nulla. Digita 'aiuto' per vedere i comandi disponibili."
    
    # Comando data con variazioni
    if any(parola in comando_norm for parola in ['data', 'giorno', 'oggi']):
        try:
            oggi = datetime.date.today()
            return f"La data di oggi è {oggi.strftime('%d/%m/%Y')}"
        except Exception as e:
            return f"Errore nel recupero della data: {e}"
    
    # Comando ora con variazioni
    elif any(parola in comando_norm for parola in ['ora', 'ore', 'orario']):
        try:
            ora_attuale = datetime.datetime.now().time()
            return f"L'ora attuale è {ora_attuale.strftime('%H:%M')}"
        except Exception as e:
            return f"Errore nel recupero dell'ora: {e}"
    
    # Comando nome con variazioni
    elif any(parola in comando_norm for parola in ['chiami', 'nome', 'sei']):
        return "Mi chiamo Assistente Virtuale"
    
    # Comando aiuto
    elif 'aiuto' in comando_norm or 'help' in comando_norm:
        return """Comandi disponibili:
- Chiedi la data (es: "Qual è la data di oggi?")
- Chiedi l'ora (es: "Che ore sono?")
- Chiedi il mio nome (es: "Come ti chiami?")
- Digita "esci" per terminare"""
    
    else:
        return "Non ho capito la tua domanda. Digita 'aiuto' per vedere i comandi disponibili."

# Ciclo principale
def main():
    print("=== Assistente Virtuale ===")
    print("Digita 'aiuto' per vedere i comandi disponibili\n")
    
    try:
        while True:
            comando_utente = input("Cosa vuoi sapere? ")
            
            # Gestione comando esci
            if normalizza_input(comando_utente) == "esci":
                print("Arrivederci!")
                break
            
            # Risposta assistente
            print(assistente_virtuale(comando_utente))
            print()  # Riga vuota per leggibilità
            
    except KeyboardInterrupt:
        print("\n\nInterrotto dall'utente. Arrivederci!")
    except Exception as e:
        print(f"\nErrore imprevisto: {e}")

if __name__ == "__main__":
    main()