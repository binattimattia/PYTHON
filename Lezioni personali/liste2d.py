frutta = ["mela", "banana", "pera"]
verdura = ["melanzane", "spinaci", "patate"]
dolci = ["tiramisù", "pasticcini", "gelato"]

dispensa = [frutta, verdura, dolci]

for sezione in dispensa:                    # per ogni lista nella dispensa
    for cibo in sezione:                    # per ogni cibo nella lista della dispensa
        print(cibo, end=" ")

print()
print(dispensa[0][1])               # Accedo prima alla lista, e poi all'elemento all'interno della lista