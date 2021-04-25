class empleado:
    def __init__(self, nombre):
        self.nombre=   nombre
        self.antiguedad =    None
        self.__cualificacion = None # 1 malo, hasta 5 exelente
        self.CI = None
    def sueldo(self):
        return (1000 + self.antiguedad * 25 + self.__cualificacion*100 )
    def setCualificacion(self,calificacion):
        self.__cualificacion = calificacion
    def getCualificacion(self):
        return self.__cualificacion

def aumentar_antiguedad(objeto, inmutable):
    objeto.antiguedad += 1
    inmutable += 1

def main():
    empleado_1 = empleado("Pepe")
    empleado_1.CI = 5234875
    empleado_1.antiguedad = 3
    inmutable = 3
    print("Objeto: ", empleado_1.antiguedad)
    print("Objeto int: ", inmutable)

    aumentar_antiguedad(empleado_1, inmutable)

    print("Objeto: ", empleado_1.antiguedad)
    print("Objeto int: ", inmutable)



""""
    print (empleado_1)
    print("El empleado", empleado_1.nombre, "con CI: ", empleado_1.CI)
    print("Lleva trabajando : ", empleado_1.antiguedad, "años en la empresa y su calificacion es: ", empleado_1.getCualificacion(), " estrellas")
    print("El sueldo que corresponde a ", empleado_1.nombre , "es :", empleado_1.sueldo())
"""
main()