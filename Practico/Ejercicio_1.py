#Diseñar un programa que almacene en  un vector llamado FACT, el factorial de los primeros 20 números naturales. FACT = {1!, 2!, 3!, … 20!}
#Debe diseñar una función que calcule el factorial de un número, por lo tanto, esta función tiene un parámetro y DEVUELVE (o retorna) un valor
num = int(input("Ingrese el numero al que quiera sacar factorial: "))
fact = []
for i in range(1,20+1):
    numr= str(i) + "!"
    fact.apped(numr)
print(fact)

mul =1
while num > 1:
    mul= num * mul
    num = num-1
    print("El factorial de ", num, "es:",mul)


