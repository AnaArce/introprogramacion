D = int(input("Ingrese el dia de nacimiento: "))
M = int(input("Ingreseel mes de nacimiento: "))
A = int(input("Ingrese el año de nacimiento: "))
a = int(input("Ingrese año en curso: "))
EDAD = a - A
V = EDAD > 18
print("Tiene o es mayor de 18 años: ", V)