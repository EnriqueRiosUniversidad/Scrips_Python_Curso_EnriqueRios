

def suma ():
    global x
    Y = 3
    x = Y + x
    print ("la x de la funcion suma es_: ", x)

def main ():
    global x
    x = 8
    x = x + 10
    suma()
    print("la x del main es: ", x)

main()