
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
    def get_salario(self):
        return "El salario de " + self.nombre + " Es_ : " + str(self.salario)



class Maquina():
    def __init__(self):
        self.__edad = None
    def setEdad(self,edad : int):
        self.__edad = edad
    def get_datos(self):
        return "La edad de la maquina es: " + str(self.__edad) + " años"

def obtenerDatos(objeto):
    print(objeto.get_datos() )
    if(isinstance(objeto, Empleado)):
        obtener_Salario(objeto)
    print()

def obtener_Salario(objeto):
    print(objeto.get_salario())
    print()

def main():
    pepe = Persona ("Pepe", 55)
    juan = Empleado ("Juan", 65)
    tito = Maquina()
    tito.setEdad(15)

    obtenerDatos(pepe)
    obtenerDatos(juan)

    if (isinstance(tito, Maquina)):
        print("Tito es una Maquina ")
    obtenerDatos(tito)

    if(issubclass(Empleado, Persona)):
        print("Empleado es una sub clase de Persona")

    if(issubclass(Persona, Persona)):
        print("Persona es una Persona")
main()