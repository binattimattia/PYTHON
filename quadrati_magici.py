import funzionidadi
import random

def genera_matrice(n: int) -> list[list]:
    """Genera una matrice n x n con numeri casuali."""
    lista_numeri = []
    matrice = []
    for i in range(1, n**2 + 1):
        lista_numeri.append(i)

    for riga in range(n):
        matrice_interna = []
        for colonna in range(n):
            numerocasuale = random.choice(lista_numeri)
            lista_numeri.remove(numerocasuale)
            matrice_interna.append(numerocasuale)
        matrice.append(matrice_interna)

    return matrice

"""Verifica se la matrice è un quadrato magico."""
matrice = genera_matrice(3)
somma_righe = 0
somma_colonne = 0
# somma tra le righe
for riga in matrice:
    for numero in riga:
        somma_righe += numero
for i in range(len(matrice)**len(matrice)):
    somma_colonne += matrice[i][i]
print(somma_righe, somma_colonne)

#def stampa_matrice(matrice, costante_magica=None):
#    """Stampa la matrice in un formato leggibile, aggiungendo la costante se è  disponibile."""
#    pass
#
#def main():
#    """Funzione principale che genera e verifica quadrati magici."""
#    for i in range(3, 11):
#	    while True:
#	        matrice = genera_matrice(n)
#	        verifica, costante_magica = verifica_quadrato_magico(matrice)
#	        if verifica:
#	            break
#	    stampa_matrice(matrice, costante_magica)
#
#if __name__ == "__main__":
#    main()