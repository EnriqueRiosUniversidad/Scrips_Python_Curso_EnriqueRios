def imprimir (num_1,num_2,num_3):
    print("El primer numero: ", num_1)
    print("El Segundo numero: ", num_2)
    print("El Tercer numero: ", num_3)
def main ():
    print("Argumentos posicionales")
    imprimir (5,7,9)
    print()
    print("Argumentos nombrados")
    imprimir(num_1=5, num_2=7,num_3= 9)
    print()
    print("Argumentos nombrados en desorden")
    imprimir(num_2=5, num_3=7,num_1= 9)
    print("Argumentos mezclados")
    imprimir(num_1=9, num_3=7, 5)

main()