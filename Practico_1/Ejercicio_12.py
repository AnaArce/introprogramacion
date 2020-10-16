#Programa que debe mostrar la malabra mas larga y la mas corta
n = int(input("Indique cuantas palabras ingresara: "))
palabra_mas_larga = ""
palabra_mas_corta = "-1"
for i in range(1,n+1):
    palabra_actual = input(f"Ingrese palabras: ")
    if len(palabra_actual) >= len(palabra_mas_larga):
        palabra_mas_larga = palabra_actual
    if len(palabra_actual) <= len(palabra_mas_corta):
            palabra_mas_corta = palabra_actual
print(f"La palabra mas larga es {palabra_mas_larga} y la palabra mas corta es {palabra_mas_corta}")