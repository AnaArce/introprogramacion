inicio = int(input("Escribir un numero: "))
if inicio != 0:
    if inicio < 0:
        print("El numero es negativo")
    else:
        print("El numero es positivo")
else:
    print("El numero es cero")