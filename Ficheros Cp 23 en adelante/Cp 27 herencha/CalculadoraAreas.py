

from CalculadoraBasica import CalculadoraBasica
class CalculadoraAreas (CalculadoraBasica):
    def __init__(self):
        super().__init__()
    def area_Cuadrado(self, lado):
        return  lado * lado
    def area_Circulo(self, radio):
        return self.multiplicar(radio, self.PI) * 2

def main():
    v3 = CalculadoraAreas()
    print("El area del cuadrado de lado 3 es -> ",v3.area_Circulo(3))

main()