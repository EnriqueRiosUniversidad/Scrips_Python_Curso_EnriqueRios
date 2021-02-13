"""
Hacer una calculadora sensilla que sume los numeros que
que el usuario introduzca hasta que introduzca -1

"""

suma=0
print("introduzca un numero a sumar: ",end="")
respuesta= eval(input())

while respuesta!=-1:
    suma+= respuesta
    print("introduzca otro numero a sumar: ",end="")
    respuesta= eval(input())
print("el resultado es: ", suma)


