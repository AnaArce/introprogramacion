from fractions import Fraction
n = int(input("Ingrese el valor de n: "))
ecuacion = Fraction(n*(n+1), 2)
print("Resultado: ", ecuacion)