
import json
from openpyxl import Workbook
from core import get_jobs


def save_to_json(data, filename):
    # Guardar en un archivo JSON
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def save_to_excel(data, filename):
    # Crear un nuevo libro de trabajo y seleccionar la hoja activa
    wb = Workbook()
    ws = wb.active
    ws.title = "Trabajos"

    # Escribir la fila de encabezados
    headers = ['Título', 'Empresa', 'Ubicación', 'Fecha de publicación', 'Enlace', 'Imagen', 'Tiempo específico']
    ws.append(headers)

    # Escribir los datos
    for job in data:
        ws.append([job['Título'], job['Empresa'], job['Ubicación'], job['Fecha de publicación'], job['Enlace'], job['Imagen'], job['Tiempo específico']])

    # Guardar el archivo Excel
    wb.save(filename)

# Obtener los trabajos
jobs = get_jobs("desarrollador de software empleos")

# Guardar los trabajos en un archivo JSON
save_to_json(jobs, 'trabajos.json')

# Guardar los trabajos en un archivo Excel
save_to_excel(jobs, 'trabajos.xlsx')

print("Datos guardados en 'trabajos.json' y 'trabajos.xlsx'.")
