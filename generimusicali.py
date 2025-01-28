# Binatti
# Mezzadri
# 19 / 11 / 2024
# 3A INFO

index_artisti = 0

print('\n#1: GENERI MUSICALI PREFERITI\n')
generi_musicali = []

for i in range(4):
    generi_musicali.append(input("Dimmi un genere musicale:\n"))

print(f"I generi musicali da te scritti sono:")

for i in generi_musicali:
    print(i, end=" ")

print("\n\n#2: ARTISTI PREFERITI + #3: STAMPA ARTISTI E GENERI\n")

artisti_preferiti = []

for generi in generi_musicali:
    print(f"Qual è il tuo cantante preferito / band per il genere {generi}?")
    artisti_preferiti.append(input())
    print(f"{generi}: {artisti_preferiti[index_artisti]}")
    index_artisti += 1

print("\n\n#4: QUANTE PERMUTAZIONI + #5: LOOP ANNIDATO - DIVERSE PERMUTAZIONI\n")

lettere = ["A", "B", "C", "D"]
numeri = [1, 2, 3, 4]

index_lettere = 0

for generi in generi_musicali:
    index_numeri = 0
    for artisti in artisti_preferiti:
        print(f"{lettere[index_lettere]}{numeri[index_numeri]} {generi}: {artisti}")
        index_numeri += 1
    index_lettere += 1
    