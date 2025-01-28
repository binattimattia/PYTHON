righe = int(input("Quante righe vuoi che io stampi? : "))
numero = 1

for i in range(righe):
    for _ in range(i + 1):
        print(numero, end=" ")
        numero += 1
    print()
