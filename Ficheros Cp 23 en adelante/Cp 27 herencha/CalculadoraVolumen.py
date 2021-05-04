"""
Volumen de una esfera. v = 4/3 x π x r^3, donde r es el radio.

Volumen de un cubo. v = L*L*L, donde a es el lado del cubo, o a x a x a.


Fuente: https://concepto.de/volumen/#ixzz6tjmzPEme
"""
from CalculadoraBasica import CalculadoraBasica
class CalculadoraVolumen(CalculadoraBasica):
    def __init__(self):
        super().__init__()
    def volumen_Cubo(self,lado):
        return lado**3
    def volumen_Esfera(self, radio):
        return self.division(3,4) * self.PI * radio**3
def main():
    v2 = CalculadoraVolumen()
    print("El volumen de la esfera de Radio 5 es--> ", v2.volumen_Esfera(5))
main()

