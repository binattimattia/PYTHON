n = int(input("Dammi un numero : "))
somma = 0
lista_divisori = []

for i in range(1, n):
    if n % i == 0:
        lista_divisori.append(i)
        somma += i

if somma == n:
    print(f"Il numero {n} è perfetto, siccome la somma dei suoi divisori {lista_divisori} è uguale a {somma}")
else:
    print(f"Il numero {n} non è perfetto, siccome la somma dei suoi divisori {lista_divisori} è uguale a {somma}")
