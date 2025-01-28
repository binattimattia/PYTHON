height = float(input("Qual è la tua altezza? (Utilizza i metri)\n"))
weight = float(input("Qual è il tuo peso? (Utilizza i KG)\n"))
bmi = weight / (height * height)
print("Il tuo BMI è " + str(bmi) + " kg/m²")
if bmi < 16:
    print("Grave magrezza")
else:
    if bmi < 18.4:
        print("Magrezza")
    else:
        if bmi < 24.9:
            print("Normopeso")
        else:
            if bmi < 29.9:
                print("Sovrappeso")
            else:
                if bmi < 34.9:
                    print("Obesità")
                else:
                    if bmi < 39.9:
                        print("Obesità grave")
                    else:
                        if bmi < 49.9:
                            print("Obesità patologica")
                        else:
                            print("Super obesità")
