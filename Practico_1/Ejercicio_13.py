#Desarolle un programa para estimar el valor de pi, la entrada del programa debe se un numero n entero que indique cuantos terminos de la suma se untilizara
numero = int(input("n: "))
suma = 0
for nta in range(1, numero + 1):
    if nta % 2 == 0:
        signo = -1
    else:
        signo = 1
    valor = signo / (1 + 2*(nta - 1))
    suma += valor
pi = 4 * suma
print(pi)


