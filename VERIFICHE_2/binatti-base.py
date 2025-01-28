from random import randint

'''
Cognome: Binatti          Nome: Mattia
Classe: 3A INFO            Data: 18/12/2024
Livello: Base
'''

lista_base = ["Tony Stark", "Steve Rogers", "Thor Odinson", "Henry Pym", "Bruce Banner", "Clint Barton", "Wanda Maximoff", "T'Challa", "Natasha Romanoff", "Henry McCoy", "Susan Carol", "Monica Rambeau"]

lista_dare = []
lista_ricevere = []

print("---- LIVELLO BASE ----")
for i in lista_base:
    lista_dare.append(i)
    lista_ricevere.append(i)

while len(lista_dare) > 0 and len(lista_ricevere) > 0:

    conta_lista_dare = len(lista_dare) - 1
    conta_lista_ricevere = len(lista_ricevere) - 1

    prima_persona = 0
    seconda_persona = 0

    if conta_lista_dare > 0 and conta_lista_ricevere > 0:
        while prima_persona == seconda_persona:
            prima_persona = randint(0, conta_lista_dare)
            seconda_persona = randint(0, conta_lista_ricevere)
    else:
        prima_persona = 0
        seconda_persona = 0

    partecipante_1 = lista_dare[prima_persona]
    partecipante_2 = lista_ricevere[seconda_persona]

    print(f"Il partecipante {partecipante_1} dà il regalo al partecipante {partecipante_2}.")
    lista_dare.remove(partecipante_1)
    lista_ricevere.remove(partecipante_2)

print("-----------------------")
