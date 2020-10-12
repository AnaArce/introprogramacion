lista = []
p = int(input("Ingrese el numero de palabras: "))
mayor = 0
menor = 0
i = 1

while (p > 0):
    palabra = input("Palabra " + str(i) + ": ")
    lista.append(palabra)
    i = i + 1
    p = p - 1
print(lista)
mas_corta = min(lista)
mas_larga = max(lista)
for i in range(0,p):
        if len(mas_corta) < len(p[i]):
         mas_corta = p[i]
        elif len(mas_larga) > len(p[i]):
         mas_larga = p[i]
print("La palabra mas larga es:", mas_larga, "y la palabra mas corta es:", mas_corta)

