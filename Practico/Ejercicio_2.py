#Diseñar un programa que lea como entrada dos vectores de tamaño 5 y devuelva el vector suma.
#Ejemplo: si tenemos los vectores V1 = (a1, a2, …, a5) y V2 = (b1, b2, …, b5) el vector suma se define como el vector obtenido
#de sumar componente a componente: V1 + V2 = (a1+ b1, a2+ b2, …, a5+ b5).

vector1=[]
vector2=[]
for i in range (0,5):
    vect1=int(input("Ingrese un numero para vector 1: "))
    vector1.append(vect1)
for i in range (0,5):
    vect2=int(input("Ingrese un numero para vector 2: "))
    vector2.append(vect2)
vector=[]
for i in range (0,5):
    suma=vector2[i]+vector1[i]
    vector.append(suma)
print(vector1)
print(vector2)
print(vector)
