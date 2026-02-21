"""
Triage Hospitalario (script corregido)

Flujo: CSV → Validación → Priorización → Estadística → Gráficas → Reporte PDF

Este script completa las secciones incompletas del notebook original y
añade un CSV de ejemplo con 10 participantes si no existe.
"""

from pathlib import Path
import csv
import json
import statistics
from datetime import datetime
import matplotlib.pyplot as plt

try:
    from reportlab.lib.pagesizes import LETTER
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib import colors
    REPORTLAB_AVAILABLE = True
except Exception:
    REPORTLAB_AVAILABLE = False


# Rutas
base_dir = Path.cwd()
out_dir = base_dir / "salidas_triage"
out_dir.mkdir(exist_ok=True)
csv_in = base_dir / "pacientes_ejemplo.csv"

# Si no hay CSV de entrada, crear uno con 10 participantes (solicitud del usuario)
if not csv_in.exists():
    sample = [
        {"id":1,"nombre":"Juan Perez","edad":45,"frecuencia_cardiaca":85,"sistolica":120,"diastolica":80,"spo2":98,"temperatura":36.5,"dolor_0_10":2,"sintoma_principal":"cefalea","tiempo_espera_min":5},
        {"id":2,"nombre":"Maria Garcia","edad":78,"frecuencia_cardiaca":110,"sistolica":95,"diastolica":60,"spo2":89,"temperatura":38.2,"dolor_0_10":8,"sintoma_principal":"dolor_pecho","tiempo_espera_min":20},
        {"id":3,"nombre":"Carlos Lopez","edad":55,"frecuencia_cardiaca":120,"sistolica":140,"diastolica":90,"spo2":91,"temperatura":39.5,"dolor_0_10":7,"sintoma_principal":"fiebre","tiempo_espera_min":12},
        {"id":4,"nombre":"Ana Martinez","edad":32,"frecuencia_cardiaca":100,"sistolica":125,"diastolica":85,"spo2":95,"temperatura":37.0,"dolor_0_10":5,"sintoma_principal":"dolor_abdominal","tiempo_espera_min":8},
        {"id":5,"nombre":"Roberto Sanchez","edad":68,"frecuencia_cardiaca":130,"sistolica":88,"diastolica":55,"spo2":85,"temperatura":39.8,"dolor_0_10":3,"sintoma_principal":"dificultad_respirar","tiempo_espera_min":18},
        {"id":6,"nombre":"Elena Rodriguez","edad":42,"frecuencia_cardiaca":92,"sistolica":118,"diastolica":76,"spo2":97,"temperatura":36.8,"dolor_0_10":4,"sintoma_principal":"mareos","tiempo_espera_min":6},
        {"id":7,"nombre":"Miguel Torres","edad":81,"frecuencia_cardiaca":115,"sistolica":110,"diastolica":70,"spo2":92,"temperatura":39.2,"dolor_0_10":6,"sintoma_principal":"tos","tiempo_espera_min":25},
        {"id":8,"nombre":"Laura Fuentes","edad":29,"frecuencia_cardiaca":88,"sistolica":122,"diastolica":78,"spo2":99,"temperatura":36.2,"dolor_0_10":1,"sintoma_principal":"control","tiempo_espera_min":3},
        {"id":9,"nombre":"Diego Morales","edad":57,"frecuencia_cardiaca":95,"sistolica":130,"diastolica":85,"spo2":94,"temperatura":37.5,"dolor_0_10":8,"sintoma_principal":"dolor_pecho","tiempo_espera_min":15},
        {"id":10,"nombre":"Patricia Gomez","edad":76,"frecuencia_cardiaca":125,"sistolica":85,"diastolica":52,"spo2":87,"temperatura":40.1,"dolor_0_10":7,"sintoma_principal":"fiebre","tiempo_espera_min":35},
    ]
    campos = ["id","nombre","edad","frecuencia_cardiaca","sistolica","diastolica","spo2","temperatura","dolor_0_10","sintoma_principal","tiempo_espera_min"]
    with open(csv_in, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        w.writeheader()
        for r in sample:
            w.writerow(r)


# 1) Leer datos desde CSV
pacientes = []
errores_lectura = 0
with open(csv_in, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for fila in reader:
        try:
            paciente = {
                "id": int(fila["id"]),
                "nombre": fila["nombre"].strip(),
                "edad": int(fila["edad"]),
                "frecuencia_cardiaca": int(fila["frecuencia_cardiaca"]),
                "sistolica": int(fila["sistolica"]),
                "diastolica": int(fila["diastolica"]),
                "spo2": int(fila["spo2"]),
                "temperatura": float(fila["temperatura"]),
                "dolor_0_10": int(fila["dolor_0_10"]),
                "sintoma_principal": fila.get("sintoma_principal","").strip(),
                "tiempo_espera_min": int(fila["tiempo_espera_min"]),
            }
            pacientes.append(paciente)
        except Exception:
            errores_lectura += 1

print("Pacientes cargados:", len(pacientes))
print("Errores lectura:", errores_lectura)


# 2) Validar datos
errores_validacion = 0
for p in pacientes:
    try:
        if not p["nombre"]:
            raise ValueError("Nombre vacío")
        if p["edad"] < 0 or p["edad"] > 120:
            raise ValueError("Edad fuera de rango")
        if p["frecuencia_cardiaca"] < 30 or p["frecuencia_cardiaca"] > 220:
            raise ValueError("FC fuera de rango")
        if p["sistolica"] < 60 or p["sistolica"] > 250:
            raise ValueError("Sistólica fuera de rango")
        if p["spo2"] < 50 or p["spo2"] > 100:
            raise ValueError("SpO2 fuera de rango")
        if p["temperatura"] < 30 or p["temperatura"] > 43:
            raise ValueError("Temperatura fuera de rango")
        if p["dolor_0_10"] < 0 or p["dolor_0_10"] > 10:
            raise ValueError("Dolor fuera de rango")
        if p["tiempo_espera_min"] < 0:
            raise ValueError("Tiempo espera inválido")
    except Exception as ex:
        errores_validacion += 1
        p["error"] = str(ex)

print("Errores validación:", errores_validacion)


# 3) Priorización (completar TODOs)
for p in pacientes:
    if "error" in p:
        p["prioridad"] = "INVALIDO"
        continue

    # ROJO
    if (
        p["spo2"] <= 89
        or p["sistolica"] <= 90
        or (p["sintoma_principal"] == "dolor_pecho" and p["dolor_0_10"] >= 8)
        or (p["sintoma_principal"] == "dificultad_respirar" and p["frecuencia_cardiaca"] >= 120)
    ):
        p["prioridad"] = "ROJO"
    # AMARILLO
    elif (90 <= p["spo2"] <= 93) or (p["temperatura"] >= 39.0) or (p["dolor_0_10"] >= 6) or (p["edad"] >= 75):
        p["prioridad"] = "AMARILLO"
    else:
        p["prioridad"] = "VERDE"


# 4) Alerta por tiempo de espera
for p in pacientes:
    if p.get("prioridad") in (None, "INVALIDO"):
        p["alerta_espera"] = False
        continue

    if p["prioridad"] == "ROJO" and p["tiempo_espera_min"] > 15:
        p["alerta_espera"] = True
    elif p["prioridad"] == "AMARILLO" and p["tiempo_espera_min"] > 30:
        p["alerta_espera"] = True
    else:
        p["alerta_espera"] = False


# 5) Estadísticas y listas
conteo = {"ROJO": 0, "AMARILLO": 0, "VERDE": 0, "INVALIDO": 0}
for p in pacientes:
    conteo[p["prioridad"]] += 1

espera_rojo = [p["tiempo_espera_min"] for p in pacientes if p.get("prioridad") == "ROJO"]
espera_amarillo = [p["tiempo_espera_min"] for p in pacientes if p.get("prioridad") == "AMARILLO"]
espera_verde = [p["tiempo_espera_min"] for p in pacientes if p.get("prioridad") == "VERDE"]

def safe_mean(lst):
    return round(statistics.mean(lst), 2) if len(lst) else None

print("Espera media ROJO:", safe_mean(espera_rojo))
print("Espera media AMARILLO:", safe_mean(espera_amarillo))
print("Espera media VERDE:", safe_mean(espera_verde))


# 6) Gráficas
labels = ["ROJO", "AMARILLO", "VERDE", "INVALIDO"]
values = [conteo[k] for k in labels]

plt.figure()
plt.bar(labels, values)
plt.title("Conteo de Prioridades (Triage)")
plt.xlabel("Prioridad")
plt.ylabel("Cantidad de pacientes")
graf_prioridades = out_dir / "graf_prioridades.png"
plt.savefig(graf_prioridades, dpi=150, bbox_inches="tight")
plt.close()

# Scatter SpO2 vs sistólica (solo válidos)
x_spo2 = [p["spo2"] for p in pacientes if "error" not in p]
y_sist = [p["sistolica"] for p in pacientes if "error" not in p]
plt.figure()
plt.scatter(x_spo2, y_sist)
plt.title("Relación SpO2 vs Presión Sistólica (Registros válidos)")
plt.xlabel("SpO2")
plt.ylabel("Presión sistólica")
graf_scatter = out_dir / "spo2_vs_sistolica.png"
plt.savefig(graf_scatter, dpi=150, bbox_inches="tight")
plt.close()


# 7) Exportar resultados
csv_out = out_dir / "triage_resultado.csv"
json_out = out_dir / "triage_resultado.json"
campos = [
    "id","nombre","edad","frecuencia_cardiaca","sistolica","diastolica",
    "spo2","temperatura","dolor_0_10","sintoma_principal","tiempo_espera_min",
    "prioridad","alerta_espera"
]

with open(csv_out, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=campos)
    writer.writeheader()
    for p in pacientes:
        writer.writerow({k: p.get(k) for k in campos})

with open(json_out, "w", encoding="utf-8") as f:
    json.dump(pacientes, f, ensure_ascii=False, indent=2)


# 8) Reporte PDF (si reportlab disponible)
pdf_out = out_dir / "Reporte_Triage.pdf"
if REPORTLAB_AVAILABLE:
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(str(pdf_out), pagesize=LETTER)
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    elements = []
    elements.append(Paragraph("Reporte Institucional: Priorización Hospitalaria (Simulación)", styles["Title"]))
    elements.append(Paragraph(f"Fecha de generación: {fecha}", styles["Normal"]))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("Resumen ejecutivo", styles["Heading2"]))
    elements.append(Paragraph(
        f"Se procesaron {len(pacientes)} pacientes. ROJO={conteo['ROJO']}, AMARILLO={conteo['AMARILLO']}, VERDE={conteo['VERDE']}, INVALIDO={conteo['INVALIDO']}.",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 12))
    rojos = [p for p in pacientes if p.get("prioridad") == "ROJO"]
    rojos.sort(key=lambda x: x["tiempo_espera_min"], reverse=True)
    tabla = [["ID","Nombre","SpO2","Sistólica","Síntoma","Espera(min)","Alerta"]]
    for p in rojos[:5]:
        tabla.append([
            p["id"], p["nombre"], p["spo2"], p["sistolica"], p["sintoma_principal"],
            p["tiempo_espera_min"], "SI" if p.get("alerta_espera") else "NO"
        ])
    t = Table(tabla, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
        ("PADDING", (0,0), (-1,-1), 6),
    ]))
    elements.append(Paragraph("Top 5 casos ROJOS por tiempo de espera", styles["Heading2"]))
    elements.append(t)
    elements.append(Spacer(1, 12))
    elements.append(Paragraph("Gráfico", styles["Heading2"]))
    elements.append(Image(str(graf_prioridades), width=420, height=260))
    doc.build(elements)
else:
    print("Aviso: reportlab no está disponible, se omitió la generación de PDF.")

print("Archivos guardados en:", out_dir)
print("Proceso completado!")
