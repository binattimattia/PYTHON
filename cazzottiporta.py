import random
from random import randint

dado = int(input("Da quante facce vuoi il dado? : "))
vita = 100
n_cazzotti = 0

while dado <= 1:
    dado = int(input("ERRORE! Hai inserito un valore on valido per il dado, riprova : "))

while vita > 0:
    danno = randint(1, dado)
    vita = vita - danno
    print(f"Il valore dell'attacco è : {danno} | La vita della porta è di {vita}")            #!formatted string, più comodo
    n_cazzotti = n_cazzotti + 1
print(f"HAI VINTO! Hai tirato {n_cazzotti} cazzotti")
