import random

lista = []


lista.append(56)
print(lista)
numero = int(input("Ingrese unnnumero: "))
lista.append(numero)
print(lista)
for i in range(0,100):
    aleat = random.randint(0,100)
    lista.append(aleat)

print(lista)
    