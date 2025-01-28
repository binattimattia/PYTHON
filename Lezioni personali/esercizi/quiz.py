domande = (("Qual è la radice quadrata di 9?"),
           ("Come si chiama l'azienda che produce gli Iphone?"),
           ("Qual è il linguaggio utilizzato per creare pagine WEB?"),
           ("Chi scoprì l'America?"),
           ("Qual è il pianeta più caldo del sistema solare?"))

opzioni = (("A) 7", "B) 9", "C) 3"),
           ("A) ACER", "B) APPLE", "C) HP"),
           ("A) HTML", "B) PYTHON", "C) REACT"),
           ("A) CRISTOFORO COLOMBO", "B) ALBERT EINSTEIN", "C) GALILEO GALILEI"),
           ("A) MERCURIO", "B) VENERE", "C) SATURNO"))

risposte = ("C", "B", "A", "A", "B")

index_opzioni = 0
index_risposte = 0
risposte_corrette = 0
risposte_input = []

for domanda in domande:
    print("------------------")
    print(domanda)
    for opzione in opzioni[index_opzioni]:
        print(opzione)
    risposta = input("RISPOSTA: ").upper()
    risposte_input.append(risposta)
    if risposta == risposte[index_risposte]:
        print(f"LA RISPOSTA {risposte[index_risposte]} È CORRETTA!")
        risposte_corrette += 1
    else:
        print(f"LA RISPOSTA È SBAGLIATA! LA RISPOSTA CORRETTA ERA: {risposte[index_risposte]}")
        
    index_opzioni += 1
    index_risposte += 1

print("------------------")
print("     RISULTATO    ")
print("------------------")

print("RISPOSTE CORRETTE: ", end="")
for risposta in risposte:
    print(risposta, end=" ")

print()
print("LE TUE RISPOSTE: ", end="")
for risposta in risposte_input:
    print(risposta, end=" ")

print()
print(f"PUNTEGGIO:\n{(risposte_corrette * 100) / 5:.0f}%")
