from random import randint

'''
Cognome: Binatti          Nome: Mattia
Classe: 3A INFO            Data: 18/12/2024
Livello: Intermedio
'''

lista_intermedio = ["Victor Von Doom", "Norman Osborn", "Otto Octavius", "Erik Magnus", "William Baker", "Quentin Beck", "Loki"]

def genera_abbinamenti(lista_intermedio):
    conta_lista = len(lista_intermedio) - 1
    prima_persona = 0
    seconda_persona = 0
    while prima_persona == seconda_persona:
        prima_persona = randint(0, conta_lista)
        seconda_persona = randint(0, conta_lista)
    partecipante_1 = lista_intermedio[prima_persona]
    partecipante_2 = lista_intermedio[seconda_persona]

    lista_partecipanti = [partecipante_1, partecipante_2]

    return lista_partecipanti


def visualizza_abbinamenti(partecipante_1, partecipante_2, lista_intermedio):
    print(f"Il partecipante {partecipante_1} dà il regalo al partecipante {partecipante_2}.")
    lista_intermedio.remove(partecipante_1)
    lista_intermedio.remove(partecipante_2)

print("---- LIVELLO INTERMEDIO ----")

while True:
    if len(lista_intermedio) > 0: 
        print("-------")
        lista = genera_abbinamenti(lista_intermedio)
        visualizza_abbinamenti(lista[0], lista[1], lista_intermedio)
    else:
        break

print("-----------------------")
