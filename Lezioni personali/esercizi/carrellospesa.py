cibi = []
prezzi = []
costo_totale = 0


while True:
    cibo = input("Inserisci il prodotto da comprare (q per andare avanti): ").lower()
    if cibo == "q":
        break
    else:
        prezzi.append(float(input(f"Quanto costa il prodotto {cibo}? €")))
        cibi.append(cibo)

print("----- IL TUO CARRELLO -----")

for cibo in cibi:
    print(cibo, end=" ")

for prezzo in prezzi:
    costo_totale += prezzo
    
print()
print(f"Il totale è: €{costo_totale}")