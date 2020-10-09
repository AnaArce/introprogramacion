P1 = input("ingrese una palabra: ")
P2 = input("Ingrese otra palabra: ")
long_P1 = len(P1)
long_P2 = len(P2)
if long_P1 > long_P2:
    print(f"{P1} tiene {long_P1 - long_P2} letras mas que {P2}")
elif long_P1 == long_P2:
    print(f"{P1} tiene el mismo numero de letras que {P2}")
else:
    print(f"{P2} tiene {long_P2 - long_P1} letras mas que {P1}")
