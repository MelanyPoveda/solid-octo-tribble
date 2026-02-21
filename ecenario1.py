# Definicionde datos

gastos = [100000.0, 87700.0, 500000.0, 78000.0, 187000.0, 485990.0, 15000.0]
dias = ["lunes", "martes", "miercoles", "Jueves", "viernes", "sabado", "domingo"]

# Manejo deestructuras basicas

total_gastos = sum(gastos)
promedio_diario = total_gastos / len(gastos)
for gasto in gastos:
    if gasto > 20000:
        print("Alerta sobrepaso los 20000")
        break

# Interacion y control

print("Gasto por dia:")
for dia, gasto in zip(dias, gastos):
    print(f"{dia}: {gasto}")

print("Dias con gastos menor que 10000:")
for dia, gasto in zip(dias, gastos):
    if gasto < 10000:
        print(dia, ":", gasto)

print("Numeracion de dias con gastos:")
for dia, gasto in enumerate(gastos, start=1):
    print(dia, ":", gasto)

# Optimizacion con colecciones

total_gastos = sum(gastos for gastos in gastos)
print("Gastos usados en total:", total_gastos)
gastos_unicos = set(gastos)
print("Gastos unicos en la semana:", gastos_unicos)
gastos_pordia = dict(zip(dias, gastos))
print("Gastos pordia en la semana:", gastos_pordia)

# Iterador sobre la lista de gastos

iterador_de_gastos = iter(gastos)
print(next(iterador_de_gastos))
print(next(iterador_de_gastos))
print(next(iterador_de_gastos))
