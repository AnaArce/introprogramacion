#Diseñar un programa que almacene en  un vector llamado FACT, el factorial de los primeros 20 números naturales. FACT = {1!, 2!, 3!, … 20!}
#Debe diseñar una función que calcule el factorial de un número, por lo tanto, esta función tiene un parámetro y DEVUELVE (o retorna) un valor.

num_f=1
FACT=[]
for num in range(1,21):
    num_f = num*num_f
    FACT.append(num_f)

print(FACT)


