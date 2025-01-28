n = int(input("Dammi un numero : "))
m = int(input("Dammi un numero : "))

contatore = 0

for i in range(m):
    contatore += n

print(f"La moltiplicazione tra questi 2 numeri senza usare la moltiplicazione è : {contatore}")
