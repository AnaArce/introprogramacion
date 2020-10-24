#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que
#tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que
#devolver True.
palabra=input("Ingrese una palabra: ")

tam=len(palabra)
tam = tam-1
palabrainv = ""
for indice in range(tam,-1,-1):
    palabrainv = palabrainv + palabra[indice]

if palabrainv == palabra:
    print("True")
else:
    print("False")