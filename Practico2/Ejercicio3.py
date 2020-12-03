x=int(input("X: "))
y=int(input("Y: "))

sd=0
d=0

r=-1

while(r!=0):
    r=float(input("Radio: "))
    diametro=r*2
    s=sd+diametro
    if(diametro>d):
        d=diametro

if(sd<=x and d<=y):
    print("Entran")
elif (sd<=y and d<=x):
    print("Entran")
else:
    print("No entran")
