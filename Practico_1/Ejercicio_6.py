N1 = int(input("Ingrese numero: "))
N2 = int(input("Ingrese numero: "))
N3 = int(input("Ingrese numero: "))
min = min(N1, N2, N3)
max = max(N1, N2, N3)
md =(N1 + N2 +N3) -min -max
print(min, "   ", md, "   ", max)
if N1 == N2 and N1 == N3:
    print("Los nuemeros son iguales")