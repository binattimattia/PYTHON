from random import randint
import funzionidadi

attaccante = randint(5, 8)
difensore = randint(5, 8)
lanci = ["primo", "secondo", "terzo", "quarto", "quinto", "sesto", "settimo", "ottavo", "decimo"]
index = 1

while attaccante > 0 and difensore > 0:
    print(f"\nTurno #{index}")
    index += 1
    print(f"\nARMATE:\nL'attaccante ha {attaccante} armate")
    print(f"Il difensore ha {difensore} armate\n")
    print(f"LANCI:")

    for i in range(3):
        dado_attaccante = funzionidadi.tiroDado(6)
        print(f"L'attaccante ha lanciato {dado_attaccante}")
        dado_difensore = funzionidadi.tiroDado(6)
        print(f"Il difensore ha lanciato {dado_difensore}")
        if dado_attaccante > dado_difensore:
            difensore -= 1
            print(f"Il difensore al lancio {i + 1} perde 1 armata")
        elif dado_attaccante == dado_difensore:
            attaccante -= 1
            print(f"L'attaccante al lancio {i + 1} perde 1 armata")
        else:
            attaccante -= 1
            print(f"L'attaccante al lancio {i + 1} perde 1 armata")

        if attaccante < 0:
            attaccante = 0
        if difensore < 0:
            difensore = 0

    print(f"\nAlla fine del turno l'attaccante è rimasto con {attaccante} armate, il difensore è rimasto con {difensore} armate.")

if attaccante > difensore:
    print(f"\nHa vinto l'attaccante con {attaccante} armate rimaste\n")

elif difensore == attaccante:
    print(f"\nL'attaccante e il difensore hanno pareggiato, siccome l'attaccante è rimasto con {attaccante} armate e il difensore è rimasto con {difensore} armate. \n")

else:
    print(f"\nHa vinto il difensore con {difensore} armate rimaste\n")
