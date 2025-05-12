import random

BOMBA = '💣'
CELLA_NASCOSTA = '◼​'

def genera_griglia(dimensione, numero_mine):
    griglia = [['' for _ in range(dimensione)] for _ in range(dimensione)]
    posiziona_mine(griglia, numero_mine)
    calcola_numeri(griglia)
    return griglia

def posiziona_mine(griglia, numero_mine):
    dimensione = len(griglia)
    mine_posizionate = 0
    while mine_posizionate < numero_mine:
        riga = random.randint(0, dimensione - 1)
        colonna = random.randint(0, dimensione - 1)
        if griglia[riga][colonna] != BOMBA:
            griglia[riga][colonna] = BOMBA
            mine_posizionate += 1

def calcola_numeri(griglia):
    dimensione = len(griglia)
    for r in range(dimensione):
        for c in range(dimensione):
            if griglia[r][c] == BOMBA:
                continue
            conta = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < dimensione and 0 <= nc < dimensione:
                        if griglia[nr][nc] == BOMBA:
                            conta += 1
            griglia[r][c] = ' ' if conta == 0 else str(conta)

def rivela_cella(griglia, riga, colonna, celle_rivelate):
    if [riga, colonna] in celle_rivelate:
        return False

    celle_rivelate.append([riga, colonna])

    if griglia[riga][colonna] == BOMBA:
        return True

    if griglia[riga][colonna] == ' ':
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = riga + dr, colonna + dc
                if 0 <= nr < len(griglia) and 0 <= nc < len(griglia):
                    if [nr, nc] not in celle_rivelate:
                        rivela_cella(griglia, nr, nc, celle_rivelate)

    return False

def visualizza_griglia(griglia, celle_rivelate):
    dimensione = len(griglia)
    print("   " + " ".join(str(i) for i in range(dimensione)))
    for r in range(dimensione):
        riga_str = f"{r}  "
        for c in range(dimensione):
            if [r, c] in celle_rivelate:
                riga_str += griglia[r][c] + " "
            else:
                riga_str += CELLA_NASCOSTA + " "
        print(riga_str)

def gioco_finito(griglia, celle_rivelate):
    for r in range(len(griglia)):
        for c in range(len(griglia)):
            if griglia[r][c] != BOMBA and [r, c] not in celle_rivelate:
                return False
    return True

def main():
    print("- CAMPO MINATO 💣 -")
    dimensione = int(input("Inserisci la dimensione della griglia: "))
    numero_mine = int(dimensione * dimensione * 0.15)

    griglia = genera_griglia(dimensione, numero_mine)
    celle_rivelate = []

    while True:
        visualizza_griglia(griglia, celle_rivelate)

        try:
            riga = int(input("Inserisci la riga: "))
            colonna = int(input("Inserisci la colonna: "))
        except ValueError:
            print("Inserisci numeri validi.")
            continue

        if not (0 <= riga < dimensione and 0 <= colonna < dimensione):
            print("Coordinate fuori dalla griglia.")
            continue

        esplosa = rivela_cella(griglia, riga, colonna, celle_rivelate)

        if esplosa:
            print("BOOM! Hai colpito una mina.")
            for r in range(dimensione):
                for c in range(dimensione):
                    if griglia[r][c] == BOMBA and [r, c] not in celle_rivelate:
                        celle_rivelate.append([r, c])
            visualizza_griglia(griglia, celle_rivelate)
            break

        if gioco_finito(griglia, celle_rivelate):
            print("Complimenti! Hai vinto!")
            visualizza_griglia(griglia, celle_rivelate)
            break

if __name__ == "__main__":
    main()
