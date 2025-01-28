# Servono ad inserire più cose all'interno di un'unica variabile;
# Non hanno un ordine, non hanno un indice;
# Non ci possono essere duplicati
# Possiamo aggiungere e rimuovere elementi
print("SET")
set = {"banana", "mela", "cocco"} 
set.add("pera")
set.remove("banana")

print(set)


# Servono ad inserire più cose all'interno di un'unica variabile
# Hanno un indice
# È immutabile
# Usate se i dati sono costanti o devono essere protetti da modifiche.
print("TUPLA")
tupla = ("banana", "mela", "cocco", "banana")
print(tupla.index("mela"))
print(tupla.count("banana"))
