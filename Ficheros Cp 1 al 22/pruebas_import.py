import math as m
# X^8 + 2*SENO(X) + X!
X = 5
resultado = m.pow(X, 8) + ( 2 * m.sin(X)) + m.factorial(X)
print(resultado)
print ("la variable era ", X)
