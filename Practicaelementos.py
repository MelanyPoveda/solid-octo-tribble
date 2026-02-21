# Entarada de datos

resenas = [
    {
        "nombre": "Maria",
        "calificacion": 1,
        "comentario": "No me gusto para nada"
    },
    {
        "nombre": "Luis",
        "calificacion": 5,
        "comentario": "Excelente calidad, muy recomendado."
    },
    {
        "nombre": "Ana",
        "calificacion": 3,
        "comentario": "Está bien, pero puede mejorar."
    },
    {
        "nombre": "Pedro",
        "calificacion": 2,
        "comentario": "No cumplió con mis expectativas."
    },
    {
        "nombre": "Sofía",
        "calificacion": 5,
        "comentario": "Me encantó, compraría de nuevo."
    }
]

# Extraccion y estadisticas basicas
total_resenas = len(resenas)
suma_calificaciones = 0
redenas_positvas = 0
resenas_negativas = 0
for resena in resenas:
    suma_calificaciones += resena["calificacion"]
    if resena["calificacion"] == 5:
        redenas_positvas += 1
    if resena["calificacion"] <= 3:
        resenas_negativas += 1
promedio_calificacion = suma_calificaciones / total_resenas
print("Total de resenas: ", total_resenas)
print("Promedio: ", promedio_calificacion)
print("Resenas con 5 estrellas: ", redenas_positvas)
print("Resenas con 3 o menos estrellas: ", resenas_negativas)

# Procesamiento de texto
for resena in resenas:
    comentario = resena["comentario"]
    comentario = comentario.lower()
    comentario = comentario.replace("producto", "articulo")
    print(comentario)

# Acceso a datos
print("Primer cliente: ", resenas[0]["nombre"])
print("Ultimo comentario", resenas[-1]["comentario"])