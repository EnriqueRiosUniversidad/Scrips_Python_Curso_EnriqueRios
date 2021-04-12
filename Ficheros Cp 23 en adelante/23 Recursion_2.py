def funcion_1(n):
    if (n >= 0):
        print(n ,  end= '->')
        funcion_1(n-1)
    else:
        print("Limite 1")

def funcion_2(n):
    if (n >= 0):
        funcion_1(n - 1)
        print(n, end='->')
    else:
        print("Limite 2")

def main():
    funcion_1(5)
    print("-------------------")
    funcion_2(5)
main()