# Tabla de multiplicar
def tablam(numi):
    for i in range(1, 11):
        print(numi, "x", i, "=", i * numi)


for j in range(1,11):
    print(" ")
    print("Tabla de multiplicar de", j, "es: ")
    tablam(j)