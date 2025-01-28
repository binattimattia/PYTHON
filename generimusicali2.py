# Binatti
# No Partner
# 24 / 11 / 2024
# 3A INFO

def ottieniGeneri(n_volte):
    print('\n#6: FUNZIONI - GENERI')
    generi_musicali = []

    for i in range(n_volte):
        generi_musicali.append(input("Dimmi un genere musicale:\n"))

    print(f"I generi musicali da te scritti sono:")

    for i in generi_musicali:
        print(i, end=" ")

    return generi_musicali

def ottieniArtisti(generi_musicali):
    print("\n\n#7: FUNZIONI ARTISTI + #8: FUNZIONI PREFERITI\n")

    index_artisti = 0
    artisti_preferiti = []

    for generi in generi_musicali:
        print(f"Qual è il tuo cantante preferito / band per il genere {generi}?")
        artisti_preferiti.append(input())
        stampaPreferiti(generi, artisti_preferiti, index_artisti)
    
    return artisti_preferiti

def stampaPreferiti(generi, artisti_preferiti, index_artisti):
    print(f"{generi}: {artisti_preferiti[index_artisti]}")
    index_artisti += 1

def stampaPermutazioni(generi_musicali, artisti_preferiti):
    print("\n\n#9: FUNZIONI - STAMPA PERMUTAZIONI")

    lettere = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numeri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

    index_lettere = 0

    for generi in generi_musicali:
        index_numeri = 0
        for artisti in artisti_preferiti:
            print(f"{lettere[index_lettere]}{numeri[index_numeri]} {generi}: {artisti}")
            index_numeri += 1
        index_lettere += 1

def parladimusica():

    generi = ottieniGeneri(int(input("Quanti generi vuoi? (MAX 26) \n")))
    print("I generi da te scritti sono: ")
    for i in generi:
        print(i)

    artisti = ottieniArtisti(generi)

    stampaPermutazioni(generi, artisti)

for i in range (2):
    parladimusica()
