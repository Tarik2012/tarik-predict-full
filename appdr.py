import pandas as pd
import sys

# Cargar un archivo CSV (reemplaza con tu archivo real)
# Asegúrate de que el archivo 'datos.csv' esté en la misma carpeta
data = pd.read_csv("datos.csv")

# Mostrar tipo de variable
print("📌 Tipo de variable:")
print(type(data))

# Mostrar forma (filas, columnas)
print("\n📏 Tamaño (filas, columnas):")
print(data.shape)

# Mostrar nombres de columnas
print("\n🧩 Columnas:")
print(data.columns.tolist())

# Mostrar los primeros datos
print("\n📄 Primeras 5 filas:")
print(data.head())

# Mostrar resumen completo
print("\n📊 Información general:")
data.info()

# Mostrar el tamaño en memoria aproximado (en bytes)
print("\n💾 Tamaño en memoria (bytes):")
print(sys.getsizeof(data))
