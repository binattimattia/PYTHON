# Name: Mattia
# Partner: 👤
# Date: 10/02/2025
# Class: 3AINFO

# ***ISTRUZIONI***
# Crea una tua copia di questo codice. Segui le istruzioni per completare gli step indicati.
# Scrivi tutto il codice tra le linee di asterischi per ogni esercizio.

import random
import funzionidadi
"""
print('\n#1: CREAZIONE DEL PERSONAGGIO\n')
# 1. Crea un dizionario inserendo al suo interno:
# 	 - Un nome scelto a caso dalla lista di nomi
#    - Chiedi all'utente di inserire una classe per il proprio personaggio a scelta tra Guerriero, Mago, Chierico, Ladro
#    Memorizza queste informazioni in un dizionario chiamato 'character'.
names = ["Drakar", "Lirael", "Thalas", "Eldorin", "Lyndra", "Kaelith", "Sylas", "Faelan", "Mirabelle", "Zephyr", "Isolde", "Thorn", "Elysia", "Varian", "Aeris", "Nerys", "Gwynn", "Eldira", "Soren", "Lirion"]

# ****************************************
letter = "Random words to run the while loop :)"
name = random.choice(names)

while letter != "a" and letter != "b" and letter != "c" and letter != "d":
	print(f"Choose a class from:\nA) Warrior \nB) Mage \nC) Cleric \nD) Thief")
	letter = input("CHOICE: ").lower()
	if letter != "a" and letter != "b" and letter != "c" and letter != "d":
		print(f"The letter {letter} is not valid.")
		
if letter == "a":
	character_class = "Warrior"
elif letter == "b":
	character_class = "Mage"
elif letter == "c":
	character_class = "Cleric"
elif letter == "d":
	character_class = "Thief"
	
character = {name: character_class}
# ****************************************

print('\n#2: ATTRIBUTI DEL PERSONAGGIO\n')
# 2. Aggiungi al dizionario i seguenti attributi generati casualmente:
#    - Punti vita tra 80 e 100
#    - Armatura tra 5 e 10
#    - Tipo di dado d'attacco (es. "1d6") scelto dall'utente

# ****************************************
character["Healt"] = random.randint(80, 100)
character["Armour"] = random.randint(5, 10)
dice = "Random words to run the while loop :)"
while len(dice.split("d")) != 2:
	print("Choose an attack dice (ex. 2d6):") 
	dice = input("Choice: ")
	character["Dice"] = dice
	if len(dice.split("d")) != 2:
		print("Error!")

# ****************************************

print('\n#2.1: AGGIUNTA DELLO ZAINO\n')
# 2.1. Aggiungi al dizionario un nuovo attributo chiamato 'zaino' che sia a sua volta un dizionario contenente:
#      - 'monete': valore casuale tra 20 e 50
#      - 'oggetti': due oggetti casuali estratti dalla lista di oggetti
#      - 'arma': un oggetto casuale estratto dalla lista delle armi

# ****************************************
oggetti = ["Pozione curativa", "Rampino", "Attrezzi da scasso", "Razioni di cibo", "Corda"]
armi = {
	"fisico": ["Spada", "Pugnale", "Arco", "Balestra"],
	"magico": ["Bastone magico", "Bacchetta"]
}
items = []

for i in range(2):
	items.append(random.choice(oggetti))
while items[0] == items[1]:
	items[1] = random.choice(oggetti)

guns_names = ["fisico", "magico"]

character["Backpack"] = {"Coins": random.randint(20, 50),
						 "Items": items,
						 "Gun": random.choice(armi[random.choice(guns_names)])}

# ****************************************

print('\n#3: STAMPA DEL PERSONAGGIO\n')
# 3. Stampa a video tutte le informazioni del personaggio, una per riga.

# ****************************************

print(f"• Name of the character: {name}")
print(f"• Class of the character: {character[name]}")
print(f"• Healt of the character: {character['Healt']}")
print(f"• Armour of the character: {character['Armour']}")
print(f"• Dice of the character: {character['Dice']}")
print(f"• Backpack of the character:")
for item in character['Backpack']:
	print(f"	➝  {item}: {character['Backpack'][item]}")

# ****************************************
	

print('\n#4: FUNZIONI - CREAZIONE PERSONAGGIO\n')
# 4. Trasforma il codice della creazione di un personaggio in una funzione chiamata 'create_character'.
#    La funzione deve restituire un dizionario con i dati del personaggio.
"""
# ****************************************
def create_character(names: list, Items: list, Guns: dict) -> dict:
	letter = "Random words to run the while loop :)"
	name = random.choice(names)

	while letter != "a" and letter != "b" and letter != "c" and letter != "d":
		print(f"Choose a class from:\nA) Warrior \nB) Mage \nC) Cleric \nD) Thief")
		letter = input("CHOICE: ").lower()
		if letter != "a" and letter != "b" and letter != "c" and letter != "d":
			print(f"The letter {letter} is not valid.")
			
	if letter == "a":
		character_class = "Warrior"
	elif letter == "b":
		character_class = "Mage"
	elif letter == "c":
		character_class = "Cleric"
	elif letter == "d":
		character_class = "Thief"
		
	character = {name: character_class}

	character["Healt"] = random.randint(80, 100)
	character["Armour"] = random.randint(5, 10)
	dice = "Random words to run the while loop :)"
	while len(dice.split("d")) != 2:
		print("Choose an attack dice (ex. 2d6):") 
		dice = input("Choice: ")
		character["Dice"] = dice
		if len(dice.split("d")) != 2:
			print("Error!")
	
	items = []

	for i in range(2):
		items.append(random.choice(Items))
	while items[0] == items[1]:
		items[1] = random.choice(Items)

	guns_names = ["fisico", "magico"]

	character["Backpack"] = {"Coins": random.randint(20, 50),
							"Items": items,
							"Gun": random.choice(Guns[random.choice(guns_names)])
							}
	
	print(f"• Name of the character: {name}")
	print(f"• Class of the character: {character[name]}")
	print(f"• Healt of the character: {character['Healt']}")
	print(f"• Armour of the character: {character['Armour']}")
	print(f"• Dice of the character: {character['Dice']}")
	print(f"• Backpack of the character:")
	for item in character['Backpack']:
		print(f"	➝  {item}: {character['Backpack'][item]}")

	return character
	
# ****************************************

print('\n#5: FUNZIONI - CREAZIONE PARTY\n')
# 5. Trasforma il codice della creazione di un party in una funzione chiamata 'create_party'.
#    La funzione deve restituire una lista di personaggi (lista di dizionari).

# ****************************************

def create_party(number_of_characters: int) -> list:
	party = []
	names = ["Drakar", "Lirael", "Thalas", "Eldorin", "Lyndra", "Kaelith", "Sylas", "Faelan", "Mirabelle", "Zephyr", "Isolde", "Thorn", "Elysia", "Varian", "Aeris", "Nerys", "Gwynn", "Eldira", "Soren", "Lirion"]
	Items = ["Pozione curativa", "Rampino", "Attrezzi da scasso", "Razioni di cibo", "Corda"]
	Guns = {
		"fisico": ["Spada", "Pugnale", "Arco", "Balestra"],
		"magico": ["Bastone magico", "Bacchetta"]
}
	for i in range(number_of_characters):
		party.append(create_character(names, Items, Guns))
	
	return party
	

# ****************************************

print('\n#6: FUNZIONI - STAMPA PARTY\n')
# 6. Trasforma il codice della stampa del party in una funzione chiamata 'print_party'.
#    La funzione deve ricevere una lista di dizionari come parametro e stampare i dati di ogni personaggio.

# ****************************************
def print_party(party):
	pass
	
	## SCRIVI QUI
	
# ****************************************
"""			
print('\nFUNZIONE PRINCIPALE\n')
# La funzione main qui sotto deve essere compatibile con il tuo codice

# ****************************************
def main():
	party = create_party()
	print_party(party)
	
main()
"""
# ****************************************