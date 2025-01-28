# MATTIA BINATTI 3A INFO 13 / 11 / 2024

alfabeto_vocali = ["a", "e", "i", "o", "u", "è", "é", "ò", "à", "ù"]
alfabeto_consonanti = ["q, w, r, t, y, p, s, d, f, g, h, j, k, l, z, x, c, v, b, n, m "]
n_vocali_totali = 0
n_doppie_totali = 0

def scelta(scelta1):
    if scelta1 == "0":
        print(f"Il numero complessivo di vocali è : {n_vocali_totali}")
        print(f"Il numero complessivo di doppie è : {n_doppie_totali}")
        print("Grazie per aver utilizzato il programma :)")
        quit(0)

while True:
    n_vocali = 0
    n_doppie = 0
    index = 1
    scelta1 = input("ESEGUI | 1\nABBANDONA | 0\nSCELTA : ")
    scelta(scelta1)
    parola = str(input("Dimmi una parola : ")).lower()
    lettere_parola = [parola]

    for lettera in alfabeto_vocali:
        for i in range(len(parola)):
            if lettera in parola[i]:
                n_vocali += 1
                n_vocali_totali += 1
    print(f"Il numero di vocali in questa parola è : {n_vocali}")

    for lettera in parola:
        if lettera == parola[index]:
            n_doppie_totali += 1
            n_doppie += 1 
        index += 1
        if index == len(parola) - 1:
            break
    print(f"Il numero di doppie in questa parola è : {n_doppie}")
    