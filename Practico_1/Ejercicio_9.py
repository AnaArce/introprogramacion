#Calculadora
print("Operaciones: suma(+), resta(-), multiplicacion(*), divicion(/), potenciacion(**)")
N1 = int(input("Operando: "))
N2 = (input("Operador: "))
N3 = int(input("Operando: "))
if N2 == "+" :
    res = N1 + N3
    print(N1, "+", N3, "=", res)
elif N2 == "-" :
    res = N1 - N3
    print(N1, "-", N3, "=", res)
elif N2 == "*" :
    res = N1 * N3
    print(N1, "*", N3, "=", res)
elif N2 == "/" :
    res = N1 / N3
    print(N1, "/", N3, "=", res)
elif N2 == "**" :
    res = N1 ** N3
    print(N1, "**", N3, "=", res)
else:
    print("Operacion invalida")