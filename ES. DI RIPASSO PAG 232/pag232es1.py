lettura_numeri = 0
somma = 0
numeri = 1

while numeri != 0:
    numeri = int(input("Dimmi un numero: "))
    lettura_numeri += 1
    somma += numeri

print(f"I numeri totali inseriti sono: {lettura_numeri - 1}")
print(f"La somma dei numeri inseriti è: {somma}")
