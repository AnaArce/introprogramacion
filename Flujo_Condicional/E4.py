W = "Elija un partido: "
P1 = "MAS"
P2 = "JUNTOS"
print(W, P1, P2)
voto = input("selecccione un partido: ")
if voto == P1 :
    print("Usted voto por: MAS ")
elif voto ==  P2 :
    print(f"Usted voto por: JUNTOS")
else:
    print("Voto invalido")