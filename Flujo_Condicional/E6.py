año = int(input("¿en que año te encuentras? "))
if año%4 == 0:
    if año%100 == 0:
        if año%400 ==0:
            print("El año que elegiste es un año bisisesto")
        else:
            print("El año no es bisiesto")
    else:
        print("El año es bisiesto")
else:
    print("El añlo no es bisiesto")