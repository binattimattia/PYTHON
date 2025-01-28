# Binatti 
# 👤
# 3A INFO

from random import randint

def genera_sequenza_segreta(dimensione, minimo, massimo): 
    sequenza_segreta = []

    while len(sequenza_segreta) < dimensione:
        numero = randint(minimo, massimo)
        if numero not in sequenza_segreta:
            sequenza_segreta.append(numero)

    return sequenza_segreta

def leggi_sequenza_utente(dimensione):
    tentativo = []
    while len(tentativo) < dimensione:
        numero_tentativo = 0
        while numero_tentativo != 1 and numero_tentativo != 2 and numero_tentativo != 3 and numero_tentativo != 4 and numero_tentativo != 5 and numero_tentativo != 6:
            numero_tentativo = int(input(f"Inserisci un numero (INSERISCI NUMERI DIVERSI!) : "))
            # Controllo che il numero sia tra 1 e 6
            if numero_tentativo != 1 and numero_tentativo != 2 and numero_tentativo != 3 and numero_tentativo != 4 and numero_tentativo != 5 and numero_tentativo != 6:
                print("ERRORE! Inserisci un numero tra 1 e 6")
            # Controllo che il numero non sia già stato scritto
            while numero_tentativo in tentativo:
                print(f"ERRORE! Il numero {numero_tentativo} è già stato scritto, scegline un altro :", end=" ")
                numero_tentativo = int(input())

        tentativo.append(numero_tentativo)

    print(" --- RESOCONTO ---")

    return tentativo

def calcola_feedback(sequenza_segreta, tentativo):
    posto_giusto = 0
    posto_sbagliato = 0
    for i in range(len(tentativo)):
        if tentativo[i] == sequenza_segreta[i]:
            posto_giusto += 1
        else:
            if tentativo[i] in sequenza_segreta:
                posto_sbagliato += 1
    # Resoconto dei posti
    print(f"I numeri corretti ma che si trovano al posto sbagliato sono {posto_sbagliato}.")
    print(f"I numeri corretti che si trovano al posto corretto sono {posto_giusto}.")
    print(" -----------------")

    return posto_sbagliato, posto_giusto

def scegli_difficoltà():
    scelta = "z"
    while scelta != "A" and scelta != "B" and scelta != "C":
        print("  --- DIFFICOLTÀ ---")
        difficoltà_tentativi = {"Facile": 15,"Intermedio": 10, "Difficile": 7}

        lettere = ("A)", "B)", "C)")
        index = 0
        for tentativo in difficoltà_tentativi:
            print(f"{lettere[index]} {tentativo}: {difficoltà_tentativi[tentativo]} TENTATIVI")
            index += 1

        scelta = input("SCELTA: ").upper()
        if scelta == "A":
            n_tentativi = 15
            print("  ------------------")
        elif scelta == "B":
            n_tentativi = 10
            print("  ------------------")
        elif scelta == "C":
            n_tentativi = 7
            print("  ------------------")
        else:
            print("ERRORE! SCELTA NON VALIDA!")

    return n_tentativi
        
def gioca_partita(max_tentativi):

    sequenza_segreta = genera_sequenza_segreta(4, 1, 6)

    for i in range(max_tentativi):
        print(f"TENTATIVO N.{i + 1}")
        posti = calcola_feedback(sequenza_segreta, leggi_sequenza_utente(4))
        # Se i numeri si trovano tutti al posto corretto vinci
        if posti[1] == 4:
            print()
            print(" --- VITTORIA! ---")
            print("Hai indovinato la sequenza segreta! 😊")
            break
    # Tentativi finiti, se i numeri non si trovano al posto corretto perdi
    if posti[1] != 4:
        print()
        print(" --- SCONFITTA ---")
        print("Non sei riuscito ad indovinare le sequenza segreta!")
        print("Sequenza:", end=" ")
        for i in sequenza_segreta:
            print(i, end=" ")

        print()

def main():
    print("----- MASTERMIND -----")
    print("OBIETTIVO: Indovinare la sequenza segreta")

    #SCELTA DIFFICOLTà
    max_tentativi = scegli_difficoltà()

    #AVVIA LA PARTITA
    gioca_partita(max_tentativi)

    print()
    print("Grazie per aver giocato! 😉")
    print(" -----------------")

main()    
