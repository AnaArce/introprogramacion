#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena
#"estoy probando" debería devolver la cadena "odnaborp yotse"

def invertir_cadena(palabra):
    resultado = ""

    for i in range(len(palabra)-1,-1,-1):
        resultado += palabra[i]
    return resultado

frase = input("Ingrese una palabra: ")
print(invertir_cadena(frase))