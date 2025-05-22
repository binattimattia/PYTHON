import json

def carica_studenti(nome_file: str) -> list[dict]:
    with open(nome_file, "r") as file:
        studenti = json.load(file)

    return studenti


def calcola_media_materia(studente: dict, materia: str) -> float:
    if materia in studente["voti"]:
        numero_voti = len(studente["voti"][materia])
        somma_voti = sum(studente["voti"][materia])
        return round(somma_voti / numero_voti, 2)
    else:
        return 0.0


def calcola_media_generale(studente: dict) -> float:
    numero_materie = 0
    somma_medie = 0
    for materia in studente["voti"]:
        media_materia = calcola_media_materia(studente, materia)
        somma_medie += media_materia
        numero_materie += 1 if media_materia > 0 else 0

    return round(somma_medie / numero_materie, 2)
            

def aggiungi_voto(lista_studenti: list[dict], id_studente: str, materia: str, voto: int):
    # TODO
    pass

def main():
    studenti = carica_studenti("studenti.json")


if __name__ == "__main__":
    main()