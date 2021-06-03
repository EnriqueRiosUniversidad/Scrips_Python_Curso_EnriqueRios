

class Persona():
    def __init__(self, nombre:str, edad : int):
        self.nombre = nombre
        self.__edad = edad

    def get_datos(self):
        return "Nombre: " + self.nombre + " Edad " + str(self.__edad)
    def getEdad(self):
        return self.__edad

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


main()