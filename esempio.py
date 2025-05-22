#!/usr/bin/env python3

import json

def leggi_file_json(nome_file: str) -> list[dict]:
    with open(nome_file, "r", encoding="utf-8") as file:
        dati_videogiochi = json.load(file)
    return dati_videogiochi


def scrivi_risultato(nome_file: str, titolo: str, punteggio: int) -> None:
    with open(nome_file, "w", encoding="utf-8") as file:
        file.write(f"Titolo: {titolo}, punteggio: {punteggio}")
    print("Report scritto correttamente su file.")


def elabora_dati(dati_videogiochi: list[dict]) -> tuple:
    gioco_punteggio_massimo = None
    punteggio_massimo = -1
    for gioco in dati_videogiochi:
        titolo = gioco["titolo"]
        punteggio = gioco["punteggio"]

        if punteggio > punteggio_massimo:
            punteggio_massimo = punteggio
            gioco_punteggio_massimo = titolo

    return gioco_punteggio_massimo, punteggio_massimo
    

def main():
    dati = leggi_file_json("esempio.json")
    titolo, punteggio = elabora_dati(dati)
    scrivi_risultato("report.txt", titolo, punteggio)

if __name__ == "__main__":
    main()
