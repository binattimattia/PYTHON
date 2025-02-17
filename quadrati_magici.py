import funzionidadi
import random

matrice = []

def genera_matrice(n) -> list:
    """Genera una matrice n x n con numeri casuali."""
    lista_numeri = []
    
    for i in range(1, n + 1):
        lista_numeri.append(i)

    for riga in range(n):
        matrice_interna = []
        for colonna in range(n):
            numerocasuale = random.choice(lista_numeri)
            lista_numeri.remove(numerocasuale)
            matrice_interna.append(numerocasuale)
        matrice.append(matrice_interna)
    return matrice

print(genera_matrice(10))
