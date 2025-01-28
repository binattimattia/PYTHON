import random

while True:
    numero_segreto = ""
    scelta = ""
    tentativi_rimasti = 5

    for i in range(4):
        numero_casuale = random.randint(1,9)
        numero_segreto += str(numero_casuale)

    while scelta != numero_segreto:
        print(f"Hai {tentativi_rimasti} tentativi per indovinare il numero segreto! (4 CIFRE!)")
        scelta = input("Inserisci il numero : ")
        tentativi_rimasti -= 1
        if tentativi_rimasti == 0:
            print(f"Hai esaurito i tentativi! Il numero segreto era: {numero_segreto}")
            scelta = input("Vuoi riavviare la partita? (SI / NO) : ")
            if scelta.lower() != "si":
                quit(0)
            else:
                tentativi_rimasti = 5

    print(f"Hai indovinato il numero segreto ({numero_segreto}), hai vinto!")
    