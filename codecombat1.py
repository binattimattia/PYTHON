import funzionidadi

hp = int(input("Inserisci la vita del personaggio: "))
turni = 0

print(f"Vita Iniziale: {hp}.")

while hp > 0:
    hit = funzionidadi.tiroDado(6)
    hp -= hit
    turni += 1
    print(f"Danni inflitti: {hit}.")
    if hp < 0:
        hp = 0
    print(f"Vita rimanente: {hp}.")

print("Il personaggio è stato sconfitto.")
print(f"Turni giocati: {turni}.")