def timeConv (V):
    n = int(input("ingrese el numero de tramos: "))
    for i in range(0,n):
        V = print("duracion del tramo: ")
        m = V % 60
        print(m)
        h = (V - m)/60
        print(h)
        result = str(h) + ":" + str(m)
        print(timeConv (266))
