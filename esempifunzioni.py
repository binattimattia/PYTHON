import random

def salutare(nome):
    print(f"Ciao {nome}!")

salutare("mattia")

def lancio_dado(facce):
    valore_dado = random.randint(1, facce)
    print(f"DADO ESTRATTO = {valore_dado}")

def lancia_dadi(numero_dadi, facce ):
    for _ in range(numero_dadi):
        valore += random.randint(1, facce)
    return valore

facce = int(input("Inserisci il numero di facce del dado: "))
lancio_dado(facce)
lancio_dado(int(input("Inserisci il numero di facce del dado: ")))
lancio_dado(int(input("Inserisci il numero di facce del dado: ")))
