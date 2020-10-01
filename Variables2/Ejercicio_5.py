N = int(input("ingrese el numero: "))
E1 = N == 5
E2 = N == 5.0
E3 = N > 0 and N < 10
E4 = N < 0 and N > 10
E5 = N == 5 and N < 10 or N > 20
print(N, "Es igual a 5: ", E1)
print(N, "Es igual que 5.0: ", E2)
print(N, "Es mayor que 0 y menor que 10: ", E3)
print(N, "Es menor que 0 o mayor que 10: ", E4)
print(N, "Es igual a 5, o en caso de no serlo, si es mayor que 10 y menor que 0: ", E5)