
def media_mobile(lista, n):
    medie = []
    
    for i in range(len(lista)): #Qui stai dicendo: scorri tutti gli indici della lista.
        
        finestra = lista[:i+1][-n:]    # ultimi n elementi
        
        media = sum(finestra) / len(finestra)

        # un array che mi contiene tutte le medie mobili
        medie.append(media) 
    
    return medie

# Argomenti passati per testare la funzione 
print(media_mobile([10, 20, 30, 50, 60], 3))
# The function will return the moving averages of the list with a window size of 3.

