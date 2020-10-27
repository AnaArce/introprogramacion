#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
#devuelve False.
def vocal(letra):
    if letra in ("a","e","i","o","u") or ("A","E","I","O","U"):
        return "True"
    else:
        return "False"

p = input("Ingrese un caracter: ")
print(vocal(p))
