import math

def divisori(numero_positivo):
    lista_divisori = []
    for i in range(1, numero_positivo + 1):
        if numero_positivo % i == 0:
            lista_divisori.append(i)
    return lista_divisori

def Primo(numero_positivo):
    divisori = []
    for i in range(1, numero_positivo + 1):
        if numero_positivo % i == 0:
            divisori.append(i)
    if len(divisori) == 2:
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
