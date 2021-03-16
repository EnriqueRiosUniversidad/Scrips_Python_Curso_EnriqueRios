#import funcion_suma
"""
    Sumar dos numeros
        Dividirlos y sumarle 5
            Repetir esto 3 veces
"""


def suma1():
    a = eval(input("Introduzca un numero"))
    b = eval(input("Introduzca un otro"))
    respuesta= ((a+b)/2)+5
    print("El primer numero fue: ", a)
    print("El segundo numero fue: ", b)
    print("La respuesta es", respuesta)


def main():
    for i in range(0,3):
        suma1()
        #funcion_suma.suma1()
    print(i)
main()





