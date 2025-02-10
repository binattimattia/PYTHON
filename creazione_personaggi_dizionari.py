# Name: Mattia
# Partner: 👤
# Date: 10/02/2025
# Class: 3AINFO

# ***ISTRUZIONI***
# Crea una tua copia di questo codice. Segui le istruzioni per completare gli step indicati.
# Scrivi tutto il codice tra le linee di asterischi per ogni esercizio.

import random

print('\n#1: CREAZIONE DEL PERSONAGGIO\n')
# 1. Crea un dizionario inserendo al suo interno:
# 	 - Un nome scelto a caso dalla lista di nomi
#    - Chiedi all'utente di inserire una classe per il proprio personaggio a scelta tra Guerriero, Mago, Chierico, Ladro
#    Memorizza queste informazioni in un dizionario chiamato 'character'.
nomi = ["Drakar", "Lirael", "Thalas", "Eldorin", "Lyndra", "Kaelith", "Sylas", "Faelan", "Mirabelle", "Zephyr", "Isolde", "Thorn", "Elysia", "Varian", "Aeris", "Nerys", "Gwynn", "Eldira", "Soren", "Lirion"]

# ****************************************
letter = "n"
name = random.choice(nomi)

while letter != "a" and letter != "b" and letter != "c" and letter != "d":
	print(f"Choose a class from:\nA) Warrior \nB) Mage \nC) Cleric \nD) Thief.")
	letter = input().lower()
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
	
character = {name, character_class}
print(character[name])
# ****************************************

print('\n#2: ATTRIBUTI DEL PERSONAGGIO\n')
# 2. Aggiungi al dizionario i seguenti attributi generati casualmente:
#    - Punti vita tra 80 e 100
#    - Armatura tra 5 e 10
#    - Tipo di dado d'attacco (es. "1d6") scelto dall'utente

# ****************************************

## SCRIVI QUI

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

## SCRIVI QUI

# ****************************************

print('\n#3: STAMPA DEL PERSONAGGIO\n')
# 3. Stampa a video tutte le informazioni del personaggio, una per riga.

# ****************************************

## SCRIVI QUI

# ****************************************
	

print('\n#4: FUNZIONI - CREAZIONE PERSONAGGIO\n')
# 4. Trasforma il codice della creazione di un personaggio in una funzione chiamata 'create_character'.
#    La funzione deve restituire un dizionario con i dati del personaggio.

# ****************************************
def create_character():
	pass
	
	## SCRIVI QUI
	
# ****************************************

print('\n#5: FUNZIONI - CREAZIONE PARTY\n')
# 5. Trasforma il codice della creazione di un party in una funzione chiamata 'create_party'.
#    La funzione deve restituire una lista di personaggi (lista di dizionari).

# ****************************************
def create_party():
	pass
	
	## SCRIVI QUI
	
# ****************************************

print('\n#6: FUNZIONI - STAMPA PARTY\n')
# 6. Trasforma il codice della stampa del party in una funzione chiamata 'print_party'.
#    La funzione deve ricevere una lista di dizionari come parametro e stampare i dati di ogni personaggio.

# ****************************************
def print_party(party):
	pass
	
	## SCRIVI QUI
	
# ****************************************
			
print('\nFUNZIONE PRINCIPALE\n')
# La funzione main qui sotto deve essere compatibile con il tuo codice

# ****************************************
def main():
	party = create_party()
	print_party(party)
	
main()
# ****************************************