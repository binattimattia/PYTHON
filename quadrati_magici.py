import random
from math import inf

def genera_matrice(n: int) -> list[list]:
    """Genera una matrice n x n con numeri casuali."""
    lista_numeri = []
    matrice = []
    for i in range(1, n**2 + 1):
        lista_numeri.append(i)

    for riga in range(n):
        matrice_interna = []
        for colonna in range(n):
            numerocasuale = random.choice(lista_numeri)
            lista_numeri.remove(numerocasuale)
            matrice_interna.append(numerocasuale)
        matrice.append(matrice_interna)

    return matrice

def righe_magiche(matrice: list[list]) -> bool:
    riga_precedente = inf
    for riga in matrice:
        riga_attuale = sum(riga)
        if riga_precedente == inf:
            riga_precedente = riga_attuale
        else:
            if riga_precedente != riga_attuale:
                return False
    return True

def colonne_magiche(matrice: list[list]) -> bool:
    colonna_precedente = inf
    lista_colonna = []
    numero = 0
    for colonna in matrice:
        for numero_colonna in range(len(matrice)):
            lista_colonna.append(matrice[numero_colonna][numero])
        colonna_attuale = sum(lista_colonna)
        if colonna_precedente == inf:
            colonna_precedente = colonna_attuale
        else:
            if colonna_precedente != colonna_attuale:
                return False
        numero += 1

    return True

def diagonali_magiche(matrice: list[list]) -> bool:
    diagonale_1 = []
    diagonale_2 = []

    for numero_diagonale in range(len(matrice)):
        diagonale_1.append(matrice[numero_diagonale][numero_diagonale])
    somma_diagonale_1 = sum(diagonale_1)

    for numero_diagonale in range(len(matrice)):
        diagonale_2.append(matrice[numero_diagonale][len(matrice) - 1 - numero_diagonale])
    somma_diagonale_2 = sum(diagonale_2)

    return True if somma_diagonale_1 == somma_diagonale_2 else False

def verifica_quadrato_magico(matrice) -> tuple[bool, int]:
    """Verifica se la matrice è un quadrato magico."""
    controllo_righe = righe_magiche(matrice)
    controllo_colonne = colonne_magiche(matrice)
    controllo_diagonali = diagonali_magiche(matrice)

    if controllo_righe and controllo_colonne and controllo_diagonali:
        return True, sum(matrice[0])
    else:
        return False, None

def stampa_matrice(matrice, costante_magica) -> None:
    """Stampa la matrice in un formato leggibile, aggiungendo la costante se è disponibile."""
    for riga in matrice:
        print(riga)

    if costante_magica is not None:
        print(f"Costante magica: {costante_magica}")

def main():
    """Funzione principale che genera e verifica quadrati magici."""
    verifica = False
    while not verifica:
        matrice = genera_matrice(3)
        verifica, costante_magica = verifica_quadrato_magico(matrice)
    stampa_matrice(matrice, costante_magica)

main()