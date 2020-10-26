#Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que
#python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un
#muy buen ejercicio.
def contadorp (lista):
    contador = 0
    for i in lista:
        contador += 1
    return contador
n = int(input("Ingrese numero de palabras: "))
for i in range(0,n):
    palabras = input("Ingrese la palabra: ")
    print(contadorp(palabras))

