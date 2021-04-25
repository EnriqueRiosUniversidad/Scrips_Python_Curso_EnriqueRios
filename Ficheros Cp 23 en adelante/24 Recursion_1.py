def factorial(n):
    if (n== 0):
        return 1
    else:
        return n * factorial(n-1)

def main():
    resultado = factorial(4)
    print(resultado)
main()