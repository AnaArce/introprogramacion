#Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el
#mayor de ellos.

def numero_mayor(num1,num2,num3):
    if num1 > num2 and num3 < num1:
        print("El numero mayor es: ",num1)
    elif num2 > num1 and num3 < num2:
        print("El numero mayor es: ",num2)
    elif num3 > num1 and num2 < num3:
        print("El numero mayor es: ",num3)

n1= int(input("Ingrese un numero: "))
n2= int(input("Ingrese un numero: "))
n3= int(input("Ingrese un numero: "))
r= numero_mayor(n1,n2,n3)
