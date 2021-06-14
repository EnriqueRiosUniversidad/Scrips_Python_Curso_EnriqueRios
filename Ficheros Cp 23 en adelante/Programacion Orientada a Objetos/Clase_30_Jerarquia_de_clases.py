

class Persona():
    def __init__(self, nombre:str, edad : int):
        self.nombre = nombre
        self.__edad = edad

    def get_datos(self):
        return "Nombre: " + self.nombre + " Edad " + str(self.__edad)
    def getEdad(self):
        return self.__edad
    #def __eq__(self,objeto):
    #    return self.nombre == objeto.nombre


class Empleado(Persona):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
        self.calificacion= "*"
        self.salario = 55.45
    def get_datos(self):
        return "Empleado: " + self.nombre + " Edad " + str(self.getEdad()) + " Tiene la calificacion: " + self.calificacion

def main():
    Pepe = Persona ("Pepe", 55)
    print(Pepe.get_datos())
    Juan = Empleado ("Juan", 65)
    print(Juan.get_datos())

    print(Pepe.__str__())
    print(Pepe.nombre.__eq__(Juan.nombre))
    #print(Pepe.__eq__(Juan))

    print(Pepe.__sizeof__())
    print(Juan.__sizeof__())

    print(Pepe.nombre.__lt__(Juan.nombre))
    print(Pepe.nombre.__gt__(Juan.nombre))

    print(Pepe.getEdad().__le__(Juan.getEdad()))

main()