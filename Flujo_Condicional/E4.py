agua = float(input("Ingrese el consumo de agua en m**3 de la persona: "))
if agua < 100:
    print("La persona debe pagar: ", (agua * 1), "Bs")
elif agua >= 100 and agua <= 499:
    print("La persona debe pagar: ", (agua * 1.20), "Bs")
elif agua >= 500 and agua <= 999:
    print("la persona debe pagar: ", (agua * 1.50), "Bs")
else:
    print("la persona debe pagar: ", (agua * 2), "Bs")