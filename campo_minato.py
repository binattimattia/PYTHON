import random

BOMBA = '💣'

def genera_griglia(dimensione: int) -> list[list[str]]:
    """
    Genera una griglia di gioco con mine posizionate casualmente.

    Args:
        dimensione (int): La dimensione della griglia (N x N).

    Returns:
        list: La griglia di gioco.
    """
    griglia = []
    for _ in range(dimensione):
        griglia.append(['🌼'] * dimensione)

    return griglia

def posiziona_mine(griglia: list[list[str]], numero_mine: int) -> None:
    """
    Posiziona le mine nella griglia di gioco.

    Args:
        griglia (list): La griglia di gioco.
        numero_mine (int): Il numero di mine da posizionare.
    """
    dimensione = len(griglia)

    for _ in range(numero_mine):
        numeroRiga = random.randint(0, dimensione - 1)
        numeroColonna = random.randint(0, dimensione - 1)
        if not griglia[numeroRiga][numeroColonna] == '💣':
            griglia[numeroRiga][numeroColonna] = '💣'
        else:
            while griglia[numeroRiga][numeroColonna] == '💣':
                numeroRiga = random.randint(0, dimensione - 1)
                numeroColonna = random.randint(0, dimensione - 1)
            griglia[numeroRiga][numeroColonna] = '💣'

def calcola_numeri(griglia):
    """
    Calcola il numero di mine adiacenti per ogni cella.

    Args:
        griglia (list): La griglia di gioco.
    """
    pass

def rivela_cella(griglia, riga, colonna):
    """
    Rivela il contenuto di una cella.

    Args:
        griglia (list): La griglia di gioco.
        riga (int): La riga della cella.
        colonna (int): La colonna della cella.

    Returns:
        bool: True se la cella contiene una mina, False altrimenti.
    """
    pass

def visualizza_griglia(griglia, celle_rivelate):
    """
    Visualizza la griglia di gioco.

    Args:
        griglia (list): La griglia di gioco.
        celle_rivelate (set): L'insieme delle celle rivelate.
    """
    pass

def gioco_finito(griglia, celle_rivelate):
    """
    Verifica se il gioco è finito.

    Args:
        griglia (list): La griglia di gioco.
        celle_rivelate (set): L'insieme delle celle rivelate.

    Returns:
        bool: True se il gioco è finito, False altrimenti.
    """
    pass

def main():
    """
    Funzione principale del programma.
    """
    print("- CAMPO MINATO 💣 -")
    dimensione = int(input("Inserisci la dimensione della griglia: "))
    numero_mine = int(input("Inserisci il numero di mine: "))
    griglia = genera_griglia(dimensione)
    posiziona_mine(griglia, numero_mine)
    for riga in griglia:
        print(" ".join(riga))

if __name__ == "__main__":
    main()