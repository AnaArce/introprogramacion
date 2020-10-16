#Programa que pida al usuario dos palabras, y que indique cual de ellas es la mas larga y por cuantas letras
P1 = input("Palabra 1: ")
P2 = input("Palabra 2: ")
long_P1 = len(P1)
long_P2 = len(P2)
if long_P1 > long_P2:
    print(f"La palabra {P1} tiene {long_P1 - long_P2} letras mas que {P2}")
elif long_P1 == long_P2:
    print(f"La palabra {P1} tiene el mismo numero de letras que {P2}")
else:
    print(f"La palabra {P2} tiene {long_P2 - long_P1} letras mas que {P1}")
