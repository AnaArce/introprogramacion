#Crea una aplicación que pida un numero por teclado y después comprobaremos si el numero introducido es capicua,
#es decir, que se lee igual sin importar la dirección. Por ejemplo, si introducimos 30303 es capicua, si introducimos
#30430 no es capicua. Piensa como puedes dar la vuelta al número. Una forma es dividiendolo entre 10 y sacando unidad por unidad.
#Otra es pasarlo a String y revisar posición por posición.

num=int(input("Ingrese un número: "))
ns=str(num)
numeroArmado=""
inicioFor=len(ns)-1
stopFor=-1

for pos in range(inicioFor,stopFor,-1):
    numA=numA+ns[pos]
print (numA)
if(numA==ns):
    print("El número es capicua")
else:
    print("El número no es capicua")