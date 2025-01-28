from random import randint
import funzionidadi

# Binatti
# Singolo
# 3A INFO


scelta = input("C | Armate con numero casuale\nT | Scegli tu i valori delle armate\nSCELTA: ").lower()

turno = 1

if scelta == "c":
    armate_attaccante = randint(7, 12)
    armate_difensore = randint(7, 12)
    print(f"\nArmate iniziali dell'attacco: {armate_attaccante}")
    print(f"Armate iniziali della difesa: {armate_difensore}")
    dado_rosso = []
    dado_azzurro = []
    while armate_difensore > 0 or armate_difensore > 0:
        scelta_armate_attaccante = 0
        scelta_armate_difensore = 0

        print(f"\nTurno #{turno}")
        turno += 1

        while scelta_armate_attaccante <= 0 or scelta_armate_attaccante > 3:
            print(f"Quante armate vuole usare l'attaccante? (MAX 3) (Armate rimanenti: {armate_attaccante})")
            scelta_armate_attaccante = int(input())
            if scelta_armate_attaccante <= 0 or scelta_armate_attaccante > 3:
                print(f"ERRORE!")

        while scelta_armate_difensore <= 0 or scelta_armate_difensore > 3:
            print(f"Quante armate vuole usare il difensore? (MAX 3) (Armate rimanenti: {armate_difensore})")
            scelta_armate_difensore = int(input())
            if scelta_armate_difensore <= 0 or scelta_armate_difensore > 3:
                print(f"ERRORE!")

        for i in range(scelta_armate_attaccante):
            dado_rosso.append(funzionidadi.tiroDado(6))
        
        dado_rosso.sort(reverse = True)
        print(f"Dadi attaccante: {dado_rosso}")

        for i in range(scelta_armate_difensore):
            dado_azzurro.append(funzionidadi.tiroDado(6))

        dado_azzurro.sort(reverse = True)
        print(f"Dadi difensore: {dado_azzurro}")

        for i in range(min(scelta_armate_attaccante, scelta_armate_difensore)):
            if max(dado_rosso) > max(dado_azzurro):
                armate_difensore -= 1
                print(f"Il difensore ha perso il confronto #{i + 1}, perciò ha perso un'armata")
            elif max(dado_rosso) == max(dado_azzurro):
                armate_attaccante -= 1
                print(f"I dadi hanno valori uguali nel confronto #{i + 1}, perciò l'attaccante perde un'armata")
            else:
                armate_attaccante -= 1
                print(f"L'attaccante ha perso il confronto #{i + 1}, perciò ha perso un'armata")
            dado_rosso.remove(max(dado_rosso))
            dado_azzurro.remove(max(dado_azzurro))
        
        if armate_attaccante < 0:
            armate_attaccante = 0
        if armate_difensore < 0:
            armate_difensore = 0

        print(f"Armate attacco: {armate_attaccante}\nArmate difensore: {armate_difensore}")
    
        if armate_attaccante == 0 and armate_difensore > 0:
            print(f"\nIl Difensore ha vinto con {armate_difensore} rimanenti!")
            break
            
        if armate_attaccante == 0 and armate_difensore == 0:
            print(f"\nEntrambe le armate sono state completamente distrutte, PAREGGIO!")
            break

        if armate_attaccante > 0 and armate_difensore == 0:
            print(f"\nL'Attaccante ha vinto con {armate_attaccante} rimanenti!")
            break

if scelta == "t":
    armate_attaccante = 0
    armate_difensore = 0

    while armate_attaccante < 7 or armate_attaccante > 12:
        armate_attaccante = int(input("Armate attaccante (MIN 7 | MAX12): "))
        if armate_attaccante < 7 or armate_attaccante > 12:
            print("ERRORE!")

    while armate_difensore < 7 or armate_difensore > 12:
        armate_difensore = int(input("Armate difensore (MIN 7 | MAX12): "))
        if armate_difensore < 7 or armate_difensore > 12:
            print("ERRORE!")

    print(f"\nArmate iniziali dell'attacco: {armate_attaccante}")
    print(f"Armate iniziali della difesa: {armate_difensore}")
    dado_rosso = []
    dado_azzurro = []
    while armate_difensore > 0 or armate_difensore > 0:
        scelta_armate_attaccante = 0
        scelta_armate_difensore = 0
        print(f"\nTurno #{turno}")
        turno += 1

        while scelta_armate_attaccante <= 0 or scelta_armate_attaccante > 3:
            print(f"Quante armate vuole usare l'attaccante? (MAX 3) (Armate rimanenti: {armate_attaccante})")
            scelta_armate_attaccante = int(input())
            if scelta_armate_attaccante <= 0 or scelta_armate_attaccante > 3:
                print(f"ERRORE!")

        while scelta_armate_difensore <= 0 or scelta_armate_difensore > 3:
            print(f"Quante armate vuole usare il difensore? (MAX 3) (Armate rimanenti: {armate_difensore})")
            scelta_armate_difensore = int(input())
            if scelta_armate_difensore <= 0 or scelta_armate_difensore > 3:
                print(f"ERRORE!")

        for i in range(scelta_armate_attaccante):
            dado_rosso.append(funzionidadi.tiroDado(6))
        
        dado_rosso.sort(reverse = True)
        print(f"Dadi attaccante: {dado_rosso}")

        for i in range(scelta_armate_difensore):
            dado_azzurro.append(funzionidadi.tiroDado(6))

        dado_azzurro.sort(reverse = True)
        print(f"Dadi difensore: {dado_azzurro}")

        for i in range(min(scelta_armate_attaccante, scelta_armate_difensore)):
            if max(dado_rosso) > max(dado_azzurro):
                armate_difensore -= 1
                print(f"Il difensore ha perso il confronto #{i + 1}, perciò ha perso un'armata")
            elif max(dado_rosso) == max(dado_azzurro):
                armate_attaccante -= 1
                print(f"I dadi hanno valori uguali nel confronto #{i + 1}, perciò l'attaccante perde un'armata")
            else:
                armate_attaccante -= 1
                print(f"L'attaccante ha perso il confronto #{i + 1}, perciò ha perso un'armata")
            dado_rosso.remove(max(dado_rosso))
            dado_azzurro.remove(max(dado_azzurro))
        
        if armate_attaccante < 0:
            armate_attaccante = 0
        if armate_difensore < 0:
            armate_difensore = 0

        print(f"Armate attacco: {armate_attaccante}\nArmate difensore: {armate_difensore}")
    
        if armate_attaccante == 0 and armate_difensore > 0:
            print(f"\nIl Difensore ha vinto con {armate_difensore} armate rimanenti!")
            break
            
        if armate_attaccante == 0 and armate_difensore == 0:
            print(f"\nEntrambe le armate sono state completamente distrutte, PAREGGIO!")
            break

        if armate_attaccante > 0 and armate_difensore == 0:
            print(f"\nL'Attaccante ha vinto con {armate_attaccante} armate rimanenti!")
            break
