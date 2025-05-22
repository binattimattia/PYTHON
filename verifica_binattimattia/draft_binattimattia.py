# Binatti Mattia
# 3A INFO
# 20/05/2025

import random
import json

def load_cards(file_path: str) -> list[dict[str, any]]:
    """
    Carica i dati delle carte dal file JSON.
    (Per il livello base, se non implementata, si può usare una lista hardcoded)
    Restituisce una lista di dizionari, ognuno rappresentante una carta.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        dati_carte = json.load(file)
    return dati_carte

def get_random_card_pair(available_cards: list[dict[str, any]]) -> tuple[dict[str, any], dict[str, any]]:
    """
    Seleziona due carte casuali DISTINTE dalla lista 'available_cards',
    assicurandosi che NESSUNA delle due sia già presente.
    Restituisce una tupla contenente i dizionari delle due carte.
    """
    carta1 = random.choice(available_cards)
    carta2 = carta1
    while carta2 == carta1:
        carta2 = random.choice(available_cards)
    available_cards.remove(carta1)
    available_cards.remove(carta2)

    return carta1, carta2

def display_card_options(card1: dict[str, any], card2: dict[str, any]) -> None:
    """
    Visualizza le informazioni essenziali delle due carte proposte per la scelta.
    Formato suggerito:
    Opzione 1: NomeCarta1 (Elisir: X, Tipo: Y, Rarità: Z)
               Descrizione: ...
    Opzione 2: NomeCarta2 (Elisir: A, Tipo: B, Rarità: C)
               Descrizione: ...
    """
    print("\n--- Scelta 1 di 8 ---")
    print(f"Opzione 1: {card1['name']} (Elisir: {card1['elixir']}, Tipo: {card1['type']}, Rarità: {card1['rarity']})")
    print(f"            Descrizione: {card1['description']}")
    print(f"Opzione 2: {card2['name']} (Elisir: {card2['elixir']}, Tipo: {card2['type']}, Rarità: {card2['rarity']})")
    print(f"            Descrizione: {card2['description']}")

def get_user_choice() -> int:
    """
    Chiede all'utente di scegliere una delle due carte (inserendo '1' o '2').
    Continua a chiedere finché l'input non è valido.
    Restituisce la scelta dell'utente (1 o 2).
    """
    input_utente = 999
    while input_utente != 1 and input_utente != 2:
        input_utente = int(input("\nScelta (1 | 2): "))
        if input_utente != 1 and input_utente != 2:
            print("Scelta non valida, riprova")

    return input_utente

def display_deck(current_deck: list[dict[str, any]]) -> None:
    """
    Visualizza le carte attualmente selezionate nel mazzo.
    Formato suggerito:
    --- Il Tuo Mazzo Attuale ---
    1. NomeCarta1 (Elisir: X)
    2. NomeCarta2 (Elisir: Y)
    ...
    --------------------------
    """
    numero = 0
    print("\n--- Il Tuo Mazzo Attuale ---")
    for carta in current_deck:
        numero += 1
        print(f"{numero}. {carta['name']} (Elisir: {carta['elixir']})")
    print("--------------------------")

def generate_draft_report(final_deck: list[dict[str, any]]) -> None:
    """
    Genera e visualizza un report finale del mazzo draftato.
    Per ogni carta, mostra: Nome, Elisir, Tipo, Rarità.
    """
    numero = 0
    print("\n=============================")
    print("=== Report Mazzo Draftato ===")
    print("=============================")
    for carta in final_deck:
        numero += 1
        print(f"{numero}. {carta['name']}               [Elisir: {carta['elixir']}, Tipo: {carta['type']}, Rarità: {carta['rarity']}]")
    print("=============================")

def simulate_base_draft() -> list[dict[str, any]]:
    """
    Funzione principale per simulare il draft di livello base.
    Deve gestire il ciclo di 8 scelte, chiamando le altre funzioni.
    Restituisce la lista delle carte del mazzo finale.
    """
    mazzo = []
    dati_carte = load_cards("cards.json")
    carte_disponibili = dati_carte
    for _ in range(8):
        carta_1, carta_2 = get_random_card_pair(carte_disponibili)
        display_card_options(carta_1, carta_2)
        scelta = get_user_choice()
        if scelta == 1:
            mazzo.append(carta_1)
        else:
            mazzo.append(carta_2)
        display_deck(mazzo)
    
    return mazzo

def main():
    print("Benvenuto al Clash Royale Draft Simulator!")
    mazzo = simulate_base_draft()
    generate_draft_report(mazzo)
    

if __name__ == "__main__":
    main()