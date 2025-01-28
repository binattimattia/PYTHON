import time                         # Importo la libreria del tempo

tempo = int(input("Inserisci il tempo in secondi: "))

for i in range(tempo, 0, -1):   # Il ciclo inizia dal valore massimo (tempo), arriva fino a 1, e decrementa di 1 (-1) ogni volta
    secondi = i % 60            # Usa il resto della divisione (%) per ottenere i secondi rimanenti che non formano un minuto intero.
    minuti = int(i / 60) % 60   # Divide i per 60 per calcolare il numero totale di minuti, poi calcola il resto (% 60) per ottenere i minuti rimanenti che non formano un'ora intera.
    ore = int(i / 3600)         # Divide i per 3600 per calcolare il numero totale di ore (senza resto).
    print(f"{ore:02}:{minuti:02}:{secondi:02}")
    time.sleep(1)

print("Il tempo è scaduto!")
