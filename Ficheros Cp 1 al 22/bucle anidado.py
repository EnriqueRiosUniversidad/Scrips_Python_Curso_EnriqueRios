""""
realizar un programa que sume todos los numeros dentro de un rango
dado por el usuario. Y que salga del bucle una vez el usuario introduzca
0 0 , luego muestre el resultado de la suma total
"""
inicio = eval(input("introduzca el inicio del bucle: "))
fin = eval(input("introduzca el fin del bucle: "))
suma_total = 0

while inicio != 0 or fin != 0:
    suma_parcial = 0
    for i in range(inicio, fin + 1):
        suma_parcial += i
    inicio = eval(input("introduzca el inicio del bucle: "))
    fin = eval(input("introduzca el fin del bucle: "))
    suma_total += suma_parcial
print("el resultado es: ", suma_total)
