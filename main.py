# Esto imprime un hola
"""
esto imprime hola en pantalla

"""
print("Hola", "mundo" , end="")
print("Hola", "mundo" ,sep="\n")
print("Hola", "me llamo juan", "esto es orto comentario")
print("Hola\nme llamo juan", "esto es orto")

# Esto funciona para escribir

# Pruebas funcion
edad = 18
precion_producto = 10.99
cancion = "Thee Sacred Souls"
print("precion_producto")
print (edad)
print(f"Su edad es en anos mas es: '{edad + 20}'")
print("cancion")
print (edad + edad)
x = 2
y = 2.9
print(x + y)
print(x*y)
# Practica 1

#Nombre
print("Melany")
# Edad con funcion
edad = 18
print (edad)
# Pais con funcion
pais = "Costa Rica"
print(pais)

#Practica 2

TASA_IVA = 0.13 # Porsentaje de impuesto
precio_base :float = 100.0
precio_final :float = precio_base * ( 1 + TASA_IVA)
print(precio_final)

# Lista
estudiantes :list = [ "Ling", "TK","Farida","Viwe"]
print(estudiantes)
estudiantes.append("Faye")
print(estudiantes)

# Condicion

x = 10
y = 5

if x > y:
    print("x es mayor que y")
print("El programa ha terminado")

a = 10
b = 5

if a == b:
    print("a es igual a b")
print("El programa ha terminado")

edad = 18

if edad >= 18:
    print("Puede votar el domingo")
else :
    print("No puede votar el domingo")

edad = 18

if edad < 18:
    print("es menor de edad")
elif edad < 65:
    print("Es adulto")
elif edad >= 65 :
    print("Es adulto mayor ")
else:
    print("es un alien")

edad = 76
if edad >= 75 and edad <= 80:
    print("Cumple!")

nota = 75
if nota >= 90:
     print("Aprobado")
elif nota >= 70:
     print("Regular")
elif nota >= 60:
     print("Regular")
else:
    print("Reprobado")

numero = -5
resultado = "Positivo" if nota >= 0 else "Negativo"
print(resultado)

persona ={
     "nombre":"Melany",
     "edad":18,
}



# Practica

numero = int(input("Ingrese un número entero: "))
if numero > 100 :
    print("El numero es mayor que 100")
elif numero < 100 :
    print("El numero es menor que 100")
else :
    print("El numero es igual a 100")

edad = int(input("Ingrese edad: "))
if edad >= 18 :
    print("Acceso permitido")
if edad < 18 :
    print("Acceso denegado")

calificacion = int(input("Ingrese calificacion entre 0 y 100: "))
if calificacion >= 90:
    print("Exelente")
elif calificacion >= 60 or calificacion >= 89:
    print("Regular")
elif calificacion < 60:
    print("Insuficiente")
else:
    print("Reprobado")

contador = 1
while contador <= 10:
    print(contador)
    contador += 1
    if contador > 10:
        break

numero = 2
suma = 0

while numero <= 20:
    suma = suma + numero
    numero += 2

print("La suma de los números pares entre 2 y 20 es:", suma)

nombres = ["Luis", "Ana", "Pedro", "Sofia"]
for nombre in nombres:
    if nombre == "Luis":
        print("Hola", nombre)


palabra = "Programacion"
for letra in palabra:
    print(letra)
try:
    numero1 = int(input("Ingrese un numero entero: "))
    numero2 = int(input("Ingrese un numero entero: "))
    resultado = numero1 / numero2
    print(resultado)
except ZeroDivisionError:
    print("No puede ser cero")

try:
    edad = int(input("Ingrese edad: "))
    print("Su edad es", edad)
except ValueError:
    print("Ese numero no es valido")

numero = int(input("Ingrese un numero entero: "))
if numero % 2 == 0 or numero % 3 == 0:
        print("Divisible entre 3 y 2")
else:
        print("No es divisible")
# Ciclo

contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# Para lista
numeros = [1,3,5,7]
for numero in numeros:
    if numero == 4:
        break
else:("No es un numero")

numeros = [1,3,5,7]
for numero in numeros:
    print(numero)

numeros = [1,3,5,7]
indice = 0

print("Con while")
while indice < len(numeros):
    print(numeros[indice], end=" ")
    indice += 1

print("\nCon for")
for numero in numeros:
    print(numero, end=" ")

for i in range(1,11):
    print(i, end=" ")

for i in range(1,6):
    if i == 3:
        continue
    print(i)

# No caer
try:
    numero = int(input("Ingrese un numero entero: "))
    print(numero)
except ValueError:
    print("No es un numero")
