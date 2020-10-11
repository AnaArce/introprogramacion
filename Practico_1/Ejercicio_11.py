from time import localtime
t = localtime()
año_ac = t.tm_year
mes_ac = t.tm_mon
dia_ac = t.tm_mday
año = int(input("Año: "))
mes = int(input("Mes: "))
dia = int(input("Dia: "))
#año
edad1 = año_ac - año
#mes
edad2 = mes_ac - mes
#dia
edad3 = dia_ac - dia

if edad2 < 0:
    print("Usted tiene", (edad2-1), "años")
else:
    print("Usted tiene", edad1, "años")
