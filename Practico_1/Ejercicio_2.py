#Escriba un programa que muestrela tabla de multiplicar del 1 al 10 del numero ingresado por el usuario
num = int(input("Ingrese un numero: "))
for i in range(1, 11):
    print(num, "por", i, "=", num*i)
