#Programa que genere todas la potencias de 2, desde la 0_esima hasta la ingresada por el usuario
N = int(input("ingrese un numero: "))
for i in range(0,N+1):
    print(2**i)