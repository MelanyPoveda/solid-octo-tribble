# Datos iniciales

unidades_vendidas = [15,16,85,92,3,54,13]
dias = ["lunes", "martes", "miercoles", "miercoles", "jueves", "viernes", "sabado", "domingo"]
PRECIO_UNITARIO = 1200

# Reporte diario

for dia, unidades in zip(dias, unidades_vendidas):
    ingreso = unidades * PRECIO_UNITARIO
    print(dia + ":", unidades,  "unidaes - Ingreso " + str(ingreso))

# Alertas condicionales

    if ingreso < 10000:
        print("¡Revisar ventas!")
    if ingreso == 0:
        print("Producto no se vendió!")
    if ingreso > 20:
        print("¡Día excelente!")

# Resumesen semanal

total_unidades = sum(unidades_vendidas)
ingreso_total = total_unidades * PRECIO_UNITARIO
promedio_diario = round(ingreso_total / len(unidades_vendidas), 2)
print("total unidades vendidas: ", total_unidades)
print("ingreso total: ", ingreso_total)
print("promedio de unidades: ", promedio_diario)

# Analsis con while

contador = 0
indice = 0

while indice < len(unidades_vendidas):
    if unidades_vendidas[indice] < 10:
        contador += 1
    indice += 1

print("Dias con menos de 10 unidades vendidas: ", contador)