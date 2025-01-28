import random

alfabeto_noambigui = ["qwertyuipasdfghjkzxcvbnm", "QWERTYUIOPASDFGHJKLZXCVBNM", "23456789", "|\!£$%&/)(=?^'ìèé+*òç@#à°ù-_.:;/"]
alfabeto_ambigui = ["qwertyuipasdfghjkzxcvbnmlo", "QWERTYUIOPASDFGHJKLZXCVBNM", "1234567890", "|\!£$%&/)(=?^'ìèé+*òç@#à°ù-_.:;"]

while True:
    password = ""
    lista_caratteri = []
    lista_password = []
    scelta: str = input("PREMI UNO TRA I SEGUENTI TASTI: \n 1 | OPZIONI DI DEFAULT \n 2 | OPZIONI PERSONALIZZATE \n Q | ESCI \nSCELTA = ")
    if scelta == "1":
        for i in range(3):
            lista_caratteri.append(random.choice(alfabeto_noambigui[0]))
            lista_caratteri.append(random.choice(alfabeto_noambigui[1]))
            lista_caratteri.append(random.choice(alfabeto_noambigui[2]))
            lista_caratteri.append(random.choice(alfabeto_noambigui[3]))
        random.shuffle(lista_caratteri)
        for i in range(12):
            password = password + lista_caratteri[i]
        print(f"PASSWORD = {password}\nGRAZIE PER AVER USATO IL PROGRAMMA, STAY SAFE! :)")
    elif scelta == "2":
        lunghezza = int(input("LUNGHEZZA PASSWORD = "))
        if lunghezza < 8:
            lunghezza = input("LUNGHEZZA TROPPO CORTA, INSERIRE UN VALORE MAGGIORE O UGUALE A 8 = ")
        scelta_cifre = input("VUOI INCLUDERE LE CIFRE? (SI/NO) = ")
        scelta_speciali = input("VUOI INCLUDERE I CARATTERI SPECIALI? (SI/NO) = ")
        scelta_ambigui = input("VUOI USARE I CARATTERI AMBIGUI? (SI/NO) = ")
        if scelta_ambigui.lower() == "si":
            while len(lista_password) < lunghezza:
                lista_caratteri = []
                lista_caratteri.append(random.choice(alfabeto_ambigui[0]))
                lista_caratteri.append(random.choice(alfabeto_ambigui[1]))
                lista_password = lista_password + lista_caratteri
                if scelta_cifre.lower() == "si":
                    lista_cifre = []
                    lista_cifre.append(random.choice(alfabeto_ambigui[2]))
                    lista_password = lista_password + lista_cifre
                if scelta_speciali.lower() == "si":
                    lista_speciali = []
                    lista_speciali.append(random.choice(alfabeto_ambigui[3]))
                    lista_password = lista_password + lista_speciali
            random.shuffle(lista_password)
            for i in range(lunghezza):
                password = password + lista_password[i]
        else:
            while len(lista_password) < lunghezza:
                lista_caratteri = []
                lista_caratteri.append(random.choice(alfabeto_noambigui[0]))
                lista_caratteri.append(random.choice(alfabeto_noambigui[1]))
                lista_password = lista_password + lista_caratteri
                if scelta_cifre.lower() == "si":
                    lista_cifre = []
                    lista_cifre.append(random.choice(alfabeto_noambigui[2]))
                    lista_password = lista_password + lista_cifre
                if scelta_speciali.lower() == "si":
                    lista_speciali = []
                    lista_speciali.append(random.choice(alfabeto_noambigui[3]))
                    lista_password = lista_password + lista_speciali
            random.shuffle(lista_password)
            for i in range(lunghezza):
                password = password + lista_password[i]
        print(f"PASSWORD = {password}\nGRAZIE PER AVER USATO IL PROGRAMMA, STAY SAFE! :)")
    elif scelta == "Q" or scelta == "q":
        print("ARRIVEDERCI, GRAZIE PER AVER USATO IL PROGRAMMA :)")
        quit(0)
