# Declaracion de constante

EXELENCIA = 90 # Sirve para declarar un valor

# Uso de varibles

nota1 = 98 # Representa una calificacion
nota2 = 69
nota3 = 35

# Calculo de expreciones

promedio = (nota1 + nota2 + nota3) / 3
print(promedio)

# Operadores logicas

es_aprobado = (
    promedio >= 70 # Condiciones de aprobacion 
    and nota1 >= 50
    and nota2 >= 50
    and nota3 >= 50
)

# Funciones de biblioteca

nota_mayor = max (nota1, nota2, nota3)
nota_menor = min (nota1, nota2, nota3)
promedio_redondeado = round(prmedio, 2)
print("Nota mayor: ", nota_mayor) # Muestra los resultados de las notas
print("Nota menor: ", nota_menor)
print("Promedio redondeado: ", promedio_redondeado)