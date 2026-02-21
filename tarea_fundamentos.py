# Temna 1 print

print("Hola mundo")

print("Melany", "18" ,sep="\n")

print("Python" , end=" ")
print("es", end=" ")
print("divertido")

resultado = 25 * 4 - 10
print("El resultado es:", resultado)

print("Producto    Precio")
print("Ensalada    ₡2000")
print("Frijoles    ₡1500")
print("Natillas    ₡2250")

#Tema 2 input

nombre = input("Ingrese su nombre: ")
print("Hola,", nombre + "!")

edad = input("Su edad es (texto): ")
print(" Tu edad es:", edad)

numerouno = int(input("Digite el primer numero: "))
numerodos = int(input("Digite el segundo numero: "))
suma = numerouno + numerodos
print("La suma es:", suma)

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print("La temperatura en fahrenheit es:", fahrenheit)

# Tema 3 variables

x = 10
print("x es:", x)

a = 7
b = 10
print(a + b)
print(a - b)

p = 5
q = 10
print("Antes: ")
print("p =", p)
print("q =", q)
p, q = q, p
print("Despues: ")
print("p =", p)
print("q =", q)

x = 5 # Indica que x es igual a 5
y = x # Indica que y es igual a x osea 5
x = x + 2 # Indica q ahora x es 5 + 2
print(x, y)
# Se imprime "y" como el valor incial pq "x" se cambio hasta despues ya q se aplica de esta misma forma.

saldo_inicial = float(input("Ingrese el saldo inicial: "))
gasto1 = float(input("Ingrese el primer gasto: "))
gasto2 = float(input("Ingrese el segundo gasto: "))
gasto3 = float(input("Ingrese el tercer gasto: "))
saldo_final = saldo_inicial - gasto1 - gasto2 - gasto3
print("El saldo final es:", saldo_final)

# Tema 4 datos

print(42)      # int
print(3.14)    # float
print("42")    # str
print(True)    # bool

numero = input("Ingrese un numero: ")
print("Antes de convertir:", type(numero))
numeroint = int(numero)
print("Despues de convertir:", type(numeroint))

print(10 / 2) # Resultado es 5.0 y el tipo float
print(10 // 2)  # Resultado es 5 y el tipo es int
print(10 // 3)  # Resultado es 3 y el tpo es int
print(10 % 3)   # Resultado es 1 ey el tipi int

precio = float(input("Ingrese el precio: "))
cantidad = int(input("Ingrese la cantidad: "))
total = precio * cantidad
print("Tipo de precio:", type(precio))
print("Tipo de cantidad:", type(cantidad))
print("Tipo del total:", type(total))
print("Total a pagar:", total)

# Tema 5 operaciones arismeticas

print(12+8-5) # El resultado es 15

m = int(input("Ingrese un numero entero: "))
n = int(input("Ingrese un numero entero: "))
print("Suma:", m + n)
print("Resta:", m - n)
print("Multiplicacion:", m * n)
print("Divicion real", m / n)

base = float(input("Ingrese la base del triangulo: "))
altura = float(input("Ingrese la altura del triangulo: "))
print("El area del triangulo es:", base * altura / 2)

# Tema 6 oprciones logicas

print(bool(True and False)) # El resultado false
print(bool(True or False)) #  El resultado true
print(bool(not True)) # El resultado false
