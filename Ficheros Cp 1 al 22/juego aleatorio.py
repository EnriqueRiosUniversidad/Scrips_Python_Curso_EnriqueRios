import random

numero = random.randint(1,10)
print ("Introduzca un numero, entre el 1 y el 10")
respuesta = eval(input())
intentos = 1


while respuesta != numero:
    intentos += 1
    if respuesta > numero:
        print("Su numero es mayor al buscado")
    else:
        print("Su numero es menor al buscado")

    print("Se ha equivocado de numero, por favor introduzca uno nuevo")
    respuesta = eval(input())

print("Ha hacertado, el numero era",respuesta, "numero de intentos: ", intentos,  sep= ":: ")