#Definir una función que tome como argumento dos números y devuelva el mayor de ellos.
#(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es
#un muy buen ejercicio.

def numero_mayor(num1,num2):
    if num1 > num2:
        print("El numero mayor es: ",num1)
    else:
        print("El numero mayor es: ",num2)
    return num1, num2
n1=int(input("Ingrese un numero: "))
n2=int(input("Ingrese otro numero: "))
m=numero_mayor(n1,n2)