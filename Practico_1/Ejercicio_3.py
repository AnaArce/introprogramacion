#Programa que pida dos numeros enteros y que calcule la divicion, indicamos si la division es exacta o no
N1 = int(input("Ingrese un mumero: "))
N2 = int(input("Ingrese otro numero: "))
cosiente = N1 // N2
resto = N1 % N2
if resto == 0 :
    print("La division es exacta")
else :
    print("La division no es exacta")
print(f"cociente: {cosiente}")
print(f"resto: {resto}")