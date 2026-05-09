Analisis de Ventas con Python

Script de analisis de ventas usando pandas y matplotlib a partir del archivo ventas.csv.

Que hace este proyecto

El script analisis_ventas.py realiza:

Carga del CSV con parseo de fechas (parse_dates=["fecha"])
Calculo de ventas por mes (cantidad * precio)
Identificacion de:
Producto mas vendido por unidades
Producto con mayor ingreso total
Generacion de 2 graficos:
ventas_por_mes.png (barras de ingresos por mes)
top5_productos.png (top 5 productos por ingreso)

Estructura

analisis_ventas.py: script principal
ventas.csv: datos de ventas de entrada
ventas_por_mes.png: grafico generado por el script
top5_productos.png: grafico generado por el script

Requisitos

Python 3.9+
pandas
matplotlib

Instalacion de dependencias:
pip install pandas matplotlib

Como ejecutarlo

python analisis_ventas.py
Al ejecutar, veras en consola:

Ventas por mes
Producto mas vendido en unidades
Producto con mayor ingreso
Y se guardaran los graficos en la misma carpeta del proyecto.

Notas de datos

El CSV debe contener al menos estas columnas:

fecha
producto
cantidad
precio
Formato esperado de fecha: YYYY-MM-DD (ejemplo: 2026-03-23).

Autor
Daniela Caraballo
