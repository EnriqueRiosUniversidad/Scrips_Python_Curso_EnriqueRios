from CalculadoraAreas import CalculadoraAreas
from CalculadoraVolumen import CalculadoraVolumen

import math

class Calculador_Fisica (CalculadoraAreas, CalculadoraVolumen):
    def __init__(self):
        #CalculadoraAreas.__init__(self)
        #CalculadoraVolumen.__init__(self)
        super().__init__()
    def calcular_Fuerza(self, masa : float):
        fuerza = masa* self.G
        return round (fuerza, 2)
    def pitagoras_hipotenusa(self, cateto1, cateto2):
        temp = math.pow(cateto1 , 2) + math.pow(cateto2,2)
        temp = math.sqrt(temp)
        return round (temp, 2)

def main():
    Areas = CalculadoraAreas ()
    Volumen = CalculadoraVolumen()

    print(Areas.PI)
    print(Volumen.G)

    herencia= Calculador_Fisica()
    print(herencia.area_Circulo(5))
    print(herencia.volumen_Esfera(5))

    print()
    print("¿la masa de una pelota es 5kg y se deja caer, que fuerza tiene?", herencia.calcular_Fuerza(5))
    print("La hipotenusa del triangulo con catetos 3 y 4 es", herencia.pitagoras_hipotenusa(4,3))


main()