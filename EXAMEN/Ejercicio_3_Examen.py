#DESARROLLAR UN ALGORITMO DONDE EL USUARIO INGRESE X CANTIDAD DE NÚMEROS COMPRENDIDOS ENTRE EL 1 AL 10, UNA VEZ INGRESADO
#EL NRO 0, SE MOSTRARÁ POR PANTALLA TODOS LOS NÚMEROS INGRESADOS HASTA ESE MOMENTO, ADICIONALMENTE DEBERÁN MOSTRAR LA
#FRECUENCIA DE TODOS LOS INGRESOS, MOSTRANDO EL NÚMERO Y CANTIDAD DE REPETICIONES PERO EN ASTERISCOS (*).

numero=1
lista=[]
while numero > 0:
    numero = int(input("Introduce un numero: "))
    lista.append(numero)

l1= lista.count(1)
l2= lista.count(2)
l3= lista.count(3)
l4= lista.count(4)
l5= lista.count(5)
l6= lista.count(6)
l7= lista.count(7)
l8= lista.count(8)
l9= lista.count(9)
l10= lista.count(10)
print("1","=",l1*"*")
print("2","=",l2*"*")
print("3","=",l3*"*")
print("4","=",l4*"*")
print("5","=",l5*"*")
print("6","=",l6*"*")
print("7","=",l7*"*")
print("8","=",l8*"*")
print("9","=",l9*"*")
print("10","=",l10*"*")