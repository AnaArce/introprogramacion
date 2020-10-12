num = int(input("Ingrese la duracion del tramo: "))
suma = 0
while num > 0:
    suma = suma + num
    num = int(input("ingrese la duracion del tramo: "))
tiempo = suma/60
print(f"El tiempo total de viaje es: {round(tiempo,2)} horas.")
