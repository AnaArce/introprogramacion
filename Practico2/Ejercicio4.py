import math

ax=int(input("Ax: "))
ay=int(input("Ay: "))
bx=int(input("Bx: "))
by=int(input("By: "))
cx=int(input("Cx: "))
cy=int(input("Cy: "))

altura=(by-ay)
base=(cx-ax)
hipo= math.sqrt(altura*altura+base+base)

area=(altura*hipo)/2
perimetro=altura+base+hipo

print("Perimetro:",perimetro)
print("Area: ", area)

