def genera_tabula_recta() -> list[list[str]]:
    """Genera e restituisce la tabula recta, una matrice 26x26 di alfabeti traslati."""
    tabula_recta = []
    for i in range(26):
        riga = []
        for j in range(i, i + 26):
            numero_ascii = (j % 26) + 65
            lettera = chr(numero_ascii)
            riga.append(lettera)
        tabula_recta.append(riga)

    return tabula_recta


def cifra(messaggio: str, chiave: str, tabula_recta: list[list[str]]) -> str:
    """Cifra un messaggio con il cifrario di Vigenère usando la tabula recta.
    
    Args:
        messaggio: Il testo da cifrare (solo lettere A-Z, senza spazi o caratteri speciali).
        chiave: La parola chiave usata per la cifratura.
        tabula_recta: La tabula recta pre-generata.
    
    Returns:
        Il testo cifrato.
    """
    chiave_ripetuta = estendi_chiave(chiave, len(messaggio))
    testo_cifrato = ""
    for i in range(len(messaggio)):
        riga = ord(chiave_ripetuta[i]) - 65
        colonna = ord(messaggio[i]) - 65
        testo_cifrato += tabula_recta[riga][colonna]
    return testo_cifrato


def decifra(messaggio_cifrato: str, chiave: str, tabula_recta: list[list[str]]) -> str:
    """Decifra un messaggio cifrato con il cifrario di Vigenère usando la tabula recta.
    
    Args:
        messaggio_cifrato: Il testo cifrato.
        chiave: La parola chiave usata per la cifratura.
        tabula_recta: La tabula recta pre-generata.
    
    Returns:
        Il testo decifrato.
    """
    chiave_ripetuta = estendi_chiave(chiave, len(messaggio_cifrato))
    testo_decifrato = ""
    for i in range(len(messaggio_cifrato)):
        riga = ord(chiave_ripetuta[i]) - 65
        colonna = tabula_recta[riga].index(messaggio_cifrato[i])
        testo_decifrato += chr(colonna + 65)
    return testo_decifrato


def normalizza_testo(testo: str) -> str:
    """Rimuove caratteri non alfabetici e converte tutto in maiuscolo per garantire compatibilità con la cifratura.
    
    Args:
        testo: Il testo di input.
    
    Returns:
        Il testo pulito e in maiuscolo.
    """
    testo_pulito = ""
    for carattere in testo:
        if carattere.isalpha():
            testo_pulito += carattere.upper()
    return testo_pulito


def estendi_chiave(chiave: str, lunghezza: int) -> str:
    """Espande la chiave fino alla lunghezza richiesta ripetendola ciclicamente.
    
    Args:
        chiave: La parola chiave originale.
        lunghezza: La lunghezza del testo da cifrare/decifrare.
    
    Returns:
        La chiave estesa.
    """
    return (chiave * (lunghezza // len(chiave)) + chiave[:lunghezza % len(chiave)]).upper()


def main():
    """Funzione principale che gestisce l'interazione con l'utente."""
    print("Cifrario di Vigenère")
    
    tabula_recta = genera_tabula_recta()

    scelta = input("Vuoi cifrare (C) o decifrare (D)? ").strip().upper()

    if scelta == "C":
        messaggio = input("Inserisci il messaggio da cifrare: ")
        chiave = input("Inserisci la chiave: ")
        messaggio = normalizza_testo(messaggio)
        chiave = normalizza_testo(chiave)
        testo_cifrato = cifra(messaggio, chiave, tabula_recta)
        print(f"Testo cifrato: {testo_cifrato}")

    elif scelta == "D":
        messaggio_cifrato = input("Inserisci il messaggio cifrato: ")
        chiave = input("Inserisci la chiave: ")
        messaggio_cifrato = normalizza_testo(messaggio_cifrato)
        chiave = normalizza_testo(chiave)
        testo_decifrato = decifra(messaggio_cifrato, chiave, tabula_recta)
        print(f"Testo decifrato: {testo_decifrato}")

    else:
        print("Scelta non valida.")


if __name__ == "__main__":
    main()