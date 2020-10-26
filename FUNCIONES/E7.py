#Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter
#multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def caracteres(num, caracter):
    carac = (caracter*num)
    print(carac)

caracter = input("Caracter que se repita: ")
num = int(input("Numero de veces que quieres que se repita en el caracter: "))
caracteres(num, caracter)