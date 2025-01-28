while True:
    scelta = input("PREMI UNO TRA I SEGUENTI TASTI :\n Q | Area di un quadrato\n C | Area di un cerchio\n E | Esci dal programma\nSCELTA : ")
    lato_quadrato = -1
    raggio_cerchio = -1
    scelta = scelta.lower()

    if scelta == "q":
        while lato_quadrato < 0:
            lato_quadrato = float(input("Dammi il lato del quadrato : "))
            if lato_quadrato < 0:
                print("Il lato non può essere negativo!")
        area_quadrato = lato_quadrato * lato_quadrato

        print(f"L'area del quadrato è : {area_quadrato}")

    elif scelta == "c":
        while raggio_cerchio < 0:
            raggio_cerchio = float(input("Dammi il raggio del cerchio : "))
            if raggio_cerchio < 0:
                print("Il raggio non può essere negativo!")
        area_cerchio = 3.14 * raggio_cerchio * raggio_cerchio
        print(f"Il raggio del cerchio è : {area_cerchio}")

    elif scelta == "e":
        print("Grazie per aver usato il programma!")
        quit(0)
    
    else:
        print("Scelta non valida!")
