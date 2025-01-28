messaggioCifrato = ""
print("Quale messaggio vuoi cifrare?")
message = input()
print("Qual è la chiave?")
key = int(input())
lunghezza = len(message)
print("La lunghezza del messaggio che hai inserito è " + str(lunghezza))
for i in range(0, lunghezza - 1 + 1, 1):
    carattere = message[i]
    if carattere != " ":
        aSCII = ord(carattere)
        aSCIIcifrato = aSCII + key
        if aSCIIcifrato > ord("Z"):
            aSCIIcifrato = aSCIIcifrato - 26
        carattereCifrato = chr(aSCIIcifrato)
        print(carattere + " è " + str(aSCII) + " in ASCII e viene cifrato in " + carattereCifrato)
    else:
        carattereCifrato = " "
    messaggioCifrato = messaggioCifrato + carattereCifrato
print("Il messaggio cifrato è " + messaggioCifrato)
