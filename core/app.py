import joblib
import pandas as pd

# Cargar modelo y columnas
modelo = joblib.load("modelos/random_forest.pkl")
columnas = joblib.load("modelos/columnas_entrenamiento.pkl")

# Crear base con ceros
datos = {col: 0 for col in columnas}

# Perfil fijo
perfil_fijo = {
    'YearsCodePro': 5,
    'EdLevel_Master': 1,
    'Employment_Employed, full-time': 1,
    'DevType_Developer, full-stack': 1,
    'RemoteWork_Remote': 1,
    'OrgSize_100 to 499 employees': 1,
    'AISelect_Yes, I use AI tools regularly': 1,
}

# Aplicar el perfil fijo solo si la clave está en columnas
for clave, valor in perfil_fijo.items():
    if clave in datos:
        datos[clave] = valor

# Lista de países a comparar (solo si están en las columnas)
paises = {
    "United States of America": "Country_United States of America",
    "Algeria": "Country_Algeria",
    "Spain": "Country_Spain",
    "India": "Country_India",
}

for nombre, columna_pais in paises.items():
    if columna_pais in columnas:
        datos_pais = datos.copy()
        datos_pais[columna_pais] = 1
        salario = modelo.predict([pd.Series(datos_pais)])[0]
        print(f"💰 {nombre}: ${salario:,.2f}")
    else:
        print(f"⚠️ {nombre} no fue usado en el modelo (columna ausente).")
