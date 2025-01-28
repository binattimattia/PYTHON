import random

somma_facce: int = 0

def lancio_dadi(facce_dadi):
    return random.randint(1, facce_dadi)

facce_dadi = int(input("Da quante facce vuoi il dado? ( >= 6 ) | "))

if facce_dadi <= 4:
    print("ERRORE! Numero di facce insufficiente!")
    quit(0)

for _ in range(100000):
    dado1 = lancio_dadi(facce_dadi)
    dado2 = lancio_dadi(facce_dadi)
    controllo_vantaggio = max(dado1, dado2)         #prende il valore più alto
    somma_facce += controllo_vantaggio

print(f"Il valore atteso è: {somma_facce / 100000}")
