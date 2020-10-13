num = int(input("Ingrese la duracion del tramo: "))
suma = 0
while num > 0:
    suma = suma + num
    num = int(input("ingrese la duracion del tramo: "))
operacion1 = suma//60
operacion2 = suma % 60
if operacion1 < 10:
    print(f"Tiempo total de viaje: {operacion1}:{operacion2} horas")
else:
    print(f"Tiempo total de viaje: {operacion1}:{operacion2} horas")
