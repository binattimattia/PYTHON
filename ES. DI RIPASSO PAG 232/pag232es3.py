n = int(input("Dammi un numero con cui farò il suo fattoriale : "))
fat = 1

for i in range(1, n + 1):
    fat *= i

print(fat)