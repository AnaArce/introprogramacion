#Programa que pida al usuario dos numeros enteros y luego entregue la suma de todos los numeros que estan entre ellos
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
suma = 0
for i in range(num1+1, num2):
    suma = suma + i
print("La suma es: ", suma)