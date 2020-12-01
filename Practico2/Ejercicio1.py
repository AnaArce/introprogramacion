vi=int(input("Numero inicial: "))
vf=int(input("Numero final: "))

valores=list(range(vi,vf+1))
print(valores)

def pares (numeros):
    pares= []
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
    return pares

valores2= pares(valores)
print(valores2)

def sumar (numeros):
    suma =0
    for n in numeros:
        suma+= n
    return suma

print(sumar(valores2))

def impares (numeros):
    impares=[]
    for n in numeros:
        if n %2 !=0:
            impares.append(n)
    return impares

valores3=impares(valores)
print(valores3)
print(sumar(valores3))







