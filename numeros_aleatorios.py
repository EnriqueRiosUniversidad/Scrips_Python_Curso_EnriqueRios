import random as r

"""
Numeros enteros
"""
for i in range(10):
    print(r.randint(10, 20), end=" | ")

print()

for i in range(10):
    print(r.randrange(10, 20, 2), end=" | ")

print()


""""
Numeros Reales
"""

for i in range(10):
    print(r.random(), end=" | ")
print()

for i in range(10):
    print(r.uniform(0.5,20), end=" | ")
print()

"""
# Caracteres
# """
for i in range(10):
    print(r.choice("hola que 551654 hace"), end=" | ")