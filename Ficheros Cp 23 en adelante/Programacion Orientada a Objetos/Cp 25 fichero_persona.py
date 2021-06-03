"""
    class nombre_clase:
        def __init__(self [,posibles parametros]):
            implementacion del constructor
        def metodo_1 (self [,posibles parametros]):
            implementacion_1
        def metodo_n (self [,posibles parametros]):
            implementacion_n
"""
class empleado:
    def __init__(self, nombre):
        self.nombre=         nombre
        self.antiguedad =    None
        self.cualificacion = None # 1 malo, hasta 5 exelente
        self.CI = None
    def sueldo(self):
        return (1000 + self.antiguedad * 25 + self.cualificacion*100 )

def main():
    empleado_1 = empleado(None)
    empleado_1.nombre = "Pepe"
    empleado_1.CI = 5234875
    empleado_1.antiguedad = 6
    empleado_1.cualificacion = 3
    print (empleado_1)
    print("El empleado", empleado_1.nombre , "con CI: ", empleado_1.CI)
    print("Lleva trabajando : ", empleado_1.antiguedad, "años en la empresa y su calificacion es: ", empleado_1.cualificacion, " estrellas")
    print("El sueldo que corresponde a ", empleado_1.nombre , "es :", empleado_1.sueldo())
main()