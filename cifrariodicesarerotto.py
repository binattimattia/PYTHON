testo_cifrato = input("Qual è la frase da decifrare? \n")
testo_cifrato = testo_cifrato.upper()
for key in range (1, 25):
    testo_decifrato = ""
    for letter in testo_cifrato:
        ASCII = ord(letter)
        if ASCII == 32:
            ASCII = ASCII
        else:
            ASCII = ASCII - key
            if ASCII <= 64:
                ASCII = ASCII + 26
        carattere = chr(ASCII)
        testo_decifrato = testo_decifrato + carattere
    print(testo_decifrato)
    