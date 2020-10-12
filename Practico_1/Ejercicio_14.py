peso = int(input("Ingrese su peso en Kg: "))
altura = float(input("Ingrese su altura en m: "))
edad = int(input("Ingrese su edad: "))
masa_muscular = peso / altura**2
print("Tu masa muscular es: ", masa_muscular)
if masa_muscular < 22.0 and edad < 45:
    print("Tu indice es bajo")
elif masa_muscular >= 22.0 and edad < 45:
    print("Tu indice es medio")
elif masa_muscular < 22.0 and edad >= 45:
    print("Tu indice es medio")
elif masa_muscular >= 22.0 and edad >= 45:
    print("Tu indice es alto")
else:
    print("Revice bien los datos e intente de nuevo")