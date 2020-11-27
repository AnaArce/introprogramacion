#Crea un array de números de un tamaño pasado por teclado, el array contendrá números aleatorios entre 1 y 300
#y mostrar aquellos números que acaben en un dígito que nosotros le indiquemos por teclado (debes controlar que
#se introduce un numero correcto), estos deben guardarse en un nuevo array.
#Por ejemplo, en un array de 10 posiciones e indicamos mostrar los números acabados en 5, podría salir 155, 25, etc

import random
def VectorRandom(tam):
    vector=[]
    for i in range(1,tam+1):
        vector.append(random.randint(1,300))
    return vector

tam=int(input("Ingrese el tamaño del vector: "))
VNA=VectorRandom(tam)
VNE=[]
print(VNA)
digito=int(input("Ingrese el último dígito a verificar: "))
for pos in range(0,tam):
    valor=VNA[pos]
    residuo=valor%10
    if(residuo==digito):
        VNE.append(valor)
print(VNE)


