class fichero_persona():
    def __init__(self):
        self.nombre= None
        self.edad  = None
    def imprimir(self):
        print(self.nombre,self.edad)

def main():
    persona_1 = fichero_persona()
    persona_1.nombre= "Juan"
    persona_1.edad= 45
    persona_1.imprimir()

    print(persona_1)

main()