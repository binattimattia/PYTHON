import random

def tiroDado(facce: int):
    """
    Tira un singolo dado.
    :parametro facce: Numero di facce del dado.
    :return: Un numero casuale tra 1 e il numero delle facce.
    """
    return random.randint(1, facce)

def listaRisultati(facce: int):
    """
    Tira quanti dadi vuoi.
    :parametro facce: Numero di facce del dado.
    :return: Lista dei risultati di n dadi da m facce
    """
    index = 1
    lista_risultati = []
    for i in range(int(input("Quanti dadi vuoi tirare?\n"))):
        lista_risultati.append(random.randint(1, facce))
    for i in lista_risultati:
        print(f"Dado #{index}: {i}")
        index += 1
    return lista_risultati

def sommaLanci(facce: int):
    """
    Tira quanti dadi vuoi.
    :parametro facce: Numero di facce del dado.
    :return: Somma tra la facce dei dadi.
    """
    somma = 0
    risultato = 0

    for i in range(int(input("Quanti dadi vuoi tirare?\n"))):
        risultato = random.randint(1, facce)
        print(f"Il risultato del lancio del Dado #{i + 1} è: {risultato}")
        somma += risultato

    print(f"La somma tra i lanci dei dadi è: {somma}")

    return somma

def somma_ndm():
    """
    Tira quanti dadi vuoi.
    :return: Somma tra la facce dei dadi.
    """
    lanci = input("Quanti dadi vuoi tirare e da quante facce? (es. formato: 4 dadi da 4 facce)\n")
    dadi_split = lanci.split(" dadi da ")
    facce_split = dadi_split[1].split(" facce")
    dadi = dadi_split[0]
    facce = facce_split[0]
    somma = 0

    for i in range(int(dadi)):
        risultato = random.randint(1, int(facce))
        print(f"Il risultato del lancio del Dado #{i + 1} è: {risultato}")
        somma += risultato

    print(f"La somma tra i lanci dei dadi è: {somma}")

    return somma

def lancio_con_vantaggio():
    """
    Tira quanti dadi vuoi.
    :return: Lancio con vantaggio tra n dadi da m facce.
    """
    lanci = int(input("Quanti dadi vuoi lanciare?\n"))
    facce = int(input("Da quante facce vuoi i dadi?\n"))
    lista_valori = []

    for i in range(lanci):
        dado = random.randint(1, facce)
        print(f"Dado #{i + 1}: {dado}")
        lista_valori.append(dado)
    dado_massimo = max(lista_valori)

    print(f"Il risultato tra {lanci} lanci di dadi da {facce} facce, dice che il valore maggiore è: {dado_massimo}")

    return dado_massimo

def lista_dadi_con_vantaggio():
    """
    Fa quanti lanci vuoi.
    Tira quanti dadi vuoi.
    :return: Lista dei valori dei dadi con valori maggiori.
    """
    lanci = int(input("Quanti lanci vuoi fare?\n"))
    lista_valori = []

    for i in range(int(lanci)):
        print(f"Lancio #{i + 1}:")
        risultati = []
        ndm = input("Quanti dadi vuoi tirare e da quante facce? (es. formato: 4 dadi da 4 facce)\n")
        dadi_split = ndm.split(" dadi da ")
        facce_split = dadi_split[1].split(" facce")
        dadi = dadi_split[0]
        facce = int(facce_split[0])
        for j in range(int(dadi)):
            dado = random.randint(1, facce)
            print(f"Dado #{j + 1}: {dado}")
            risultati.append(dado)
        print(f"Il risultato tra {dadi} dadi da {facce} facce, dice che il valore maggiore è: {max(risultati)}")
        lista_valori.append(max(risultati))

    print(f"Ecco a te la lista dei risultati maggiori: {lista_valori}")

    return lista_valori


def somma_con_vantaggio():
    """
    Fa quanti lanci vuoi.
    Tira quanti dadi vuoi.
    :return: Somma dei lanci tra i dadi con vantaggio
    """
    lanci = int(input("Quanti lanci vuoi fare?\n"))
    lista_valori = []
    somma = 0

    for i in range(int(lanci)):
        print(f"Lancio #{i + 1}:")
        risultati = []
        ndm = input("Quanti dadi vuoi tirare e da quante facce? (es. formato: 4 dadi da 4 facce)\n")
        dadi_split = ndm.split(" dadi da ")
        facce_split = dadi_split[1].split(" facce")
        dadi = dadi_split[0]
        facce = int(facce_split[0])
        for j in range(int(dadi)):
            dado = random.randint(1, facce)
            print(f"Dado #{j + 1}: {dado}")
            risultati.append(dado)
        print(f"Il risultato tra {dadi} dadi da {facce} facce, dice che il valore maggiore è: {max(risultati)}")
        lista_valori.append(max(risultati))

    for valori in lista_valori:
        somma += valori

    print(f"La somma tra i valori dei lanci con vantaggio è di: {somma}")

    return somma
