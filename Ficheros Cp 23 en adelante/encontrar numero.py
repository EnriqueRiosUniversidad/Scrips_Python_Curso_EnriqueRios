

def recursion(numero, contador):
    if (numero < 1 ):
        return (contador)
    else:
        return recursion(numero / 2, contador + 1)

    #return 0


def main():
    print(recursion(1000000,0))
main()