#DESARROLLAR UN ALGORITMO QUE PIDA AL USUARIO PUEDA INGRESAR UN NÚMERO "N" Y ÉSTE SEA LA ALTURA Y ANCHO DE UN
#TRIÁNGULO RECTÁNGULO FORMADO POR ASTERISCOS (*) DONDE EL ÁNGULO RECTO SE APOYE AL LADO DERECHO. POR EJEMPLO:
#INGRESE N

N=int(input("Ingrese un numero para la altura y ancho del triangulo rectangulo: "))
for i in range(N+1):
    espacios=N-i
    print(" "*espacios+"*"*i)