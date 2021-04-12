def calcular(a = 3,b= 4):
    suma = a + b
    resta= a - b
    multi= a * b
    return (suma, resta, multi, a / b , a**b)

def main():
    suma,resta,multi,divi,expo = calcular(b = 7)
    print(suma,resta,multi,divi,expo)



main()
