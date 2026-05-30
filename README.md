# Analisis-ventas-empresa
Trabajo Práctico: Gestión Colaborativa, Control de Versiones y Organización Empresarial (Git, GitHub y Jira)

open("README.md", "w", encoding="utf-8")
contenido_readme = """# Análisis de Ventas - Pequeña Empresa

## Integrantes del Equipo
* Integrante 1 (P1)
* Integrante 2 (P2)
* Integrante 3 (P3)

## Escenario Seleccionado
Escenario B – Análisis de Ventas de una Pequeña Empresa.

## Descripción del Dataset
El archivo datos/dataset.csv registra transacciones comerciales incluyendo: fecha de venta, producto, cantidad vendida y precio unitario.

## Instrucciones de Ejecución
Para replicar el análisis, corre el siguiente comando en la terminal o entorno de ingeniería:
python scripts/analisis_datos.py

El script calculará las métricas clave e imprimirá los resultados, además de guardar una gráfica evolutiva en la carpeta /resultados.
"""

with open("README.md", "w", encoding="utf-8") as archivo:
    archivo.write(contenido_readme)

print("¡Archivo README.md creado y guardado con éxito!")
