# Importazione del modulo socket di Python per la gestione delle connessioni di rete
import socket

# definizione dell'indirizzo e della porta del server
SRV_ADDR = "10.0.2.15"
SRV_PORT = 4445


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # questa funzione definisce il tipo di socket, in questo caso il primo argomento indica che si usa IPv4, il secondo argomento indica che si usa TCP
s.bind((SRV_ADDR, SRV_PORT)) # associa l'indirizzo e la porta al socket
s.listen(1) # ascolta una connessione in entrata
print(f"Server listening on {SRV_ADDR}:{SRV_PORT}") # stampa l'indirizzo e la porta del server
connection, client_address = s.accept() # accetta una connessione in entrata
print(f"Connection from {client_address}") # stampa l'indirizzo del client connesso
while True: # ciclo infinito per ricevere dati
    data = connection.recv(8) # riceve fino a 8 byte di dati nel buffer
    if not data:
        break # se non ci sono dati esce dal ciclo
    print(f"Received: {data.decode()}") #decodifica per pulire la stringa
    connection.sendall(data) # invia i dati ricevuti indietro al client
connection.close() # chiude la connessione
