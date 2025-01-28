import math

def divisori(numero_positivo):
    lista_divisori = []
    for i in range(1, numero_positivo + 1):
        if numero_positivo % i == 0:
            lista_divisori.append(i)
    return lista_divisori

def Primo(numero_positivo):
    if numero_positivo == 1:
        return False  # Il numero 1 non è primo
    if numero_positivo <= 3:
        return True  # 2 e 3 sono numeri primi
    if numero_positivo % 2 == 0 or numero_positivo % 3 == 0:
        return False  # Esclude multipli di 2 e 3
    
    i = 5
    while i * i <= numero_positivo:  # Controlla solo fino alla radice quadrata del numero
        if numero_positivo % i == 0 or numero_positivo % (i + 2) == 0:
            return False
        i += 6  # Salta i multipli di 2 e 3
    return True
    
def Primi_piccoli(numero_positivo):
    lista_primi = []
    for i in range(2, numero_positivo):
        if Primo(i):
            lista_primi.append(i)

    return lista_primi

def Coprimi(numero_positivo1, numero_positivo2):
    mcd = math.gcd(numero_positivo1, numero_positivo2)
    if mcd == 1:
        return True

def Eulero(numero_positivo):
    lista_minori = []
    lista_minori_coprimi = []
    for i in range(1, numero_positivo):
        lista_minori.append(i)
    for i in lista_minori:
        if Coprimi(numero_positivo, i):
            lista_minori_coprimi.append(i)
    eulero = len(lista_minori_coprimi)
    return eulero
