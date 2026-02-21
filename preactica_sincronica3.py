# Iteracion con for

for numero in range(2, 21, 2):
    print(numero)

for i in range(1, 11):
    print(7 * i)

nombres = ["Ana", "Luis", "Maria"]
for nombre in nombres:
    print(nombre)

numeros = [3, 7, 2, 9, 5]
suma = 0
for numero in numeros:
    suma += numero
print(suma)

for numero in range(10, 0, -1):
    print(numero)

# Uso de enumerate

colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print(indice, color)

palabra = ["Escriba una palabra: "]
for indice, palabra in enumerate(palabra):
    print(indice, palabra)

numeros = [4, 7, 10, 13, 16]
for indice, numero in enumerate(numeros):
    if numero % 2 == 0:
        print(indice, numero, "es par")
    else:
        print(indice, numero, "es impar")

frutas = ["manzana", "pera", "uva", "sandia"]
for indice, fruta in enumerate(frutas, start=1):
    print(indice, fruta)

lista = [5, 10, 15, 20, 25]
for indice, valor in enumerate(lista):
    if indice % 2 == 0:
        print(valor)

# Uso de zip

nombre = ["Ana", "Luis", "Maria"]
edades = [18, 20, 19]
for nombre, edad in zip(nombre, edades):
    print(nombre, "tiene", edad)

numeros = [1, 2, 3, 4, 5]
cuadrados = [1, 4, 9, 16, 25]
for numero, cuadrada in zip(numeros, cuadrados):
    print(numero, cuadrada)

lista1 = [10, 20., 30]
lista2 = [15, 25, 35]
for a, b in zip(lista1, lista2):
    if a > b:
        print(a)
    else:
        print(b)

letras = ["a", "b", "c"]
numeros = [1, 2, 3]
for par in zip(letras, numeros):
    print(par)

lista1 = ["sol", "luna", "estrella"]
lista2 = [1, 2, 3]
lista3 = ["dia", "noche", "cielo"]
for a, b, c in zip(lista1, lista2, lista3):
    print(a, b, c)

# Iteradores iter, next

numeros = [1, 2, 3, 4, 5]
it = iter(numeros)
print(next(it))
print(next(it))
print(next(it))

palabra = input("Ingrese una palabra: ")
it = iter(palabra)
print(next(it))
print(next(it))

lista = [10, 20, 30]
it = iter(lista)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

it = iter(range(1,6))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

lista = [100, "Python", 3.14]
it = iter(lista)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

# Generator Expressions

generador = (n ** 2 for n in range(1,10) if n % 2 == 0)
for valor in generador:
    print(valor)

palabras = ["hola", "python", "enumrate"]
generador = (len(palabras) for palabra in palabras)
for longitud in generador:
    print(longitud)

numeros = [1, 4, 6, 8, 3, 9]
generador = (numero for numero in numeros if numero > 5)
for numero in generador:
    print(numero)

palabra = input("Ingrese una palabra: ")
generador = (letra.upper() for letra in palabra)
for letra in generador:
    print(letra)

total = sum(numero for numero in range(1, 100))
print(total)

# Composiones

cuadrados = [numeros ** 2 for numeros in range(1, 10)]
print(cuadrados)

palabra = input("Ingrese una palabra: ")
letras = {letra for letra in palabra}
print(letras)

generador = (numero ** 2 for numero in range(1, 10))
lista = [numero ** 2 for numero in range(1, 10)]
print(list(generador))
print(lista)
