# test_countries.py

import joblib
import numpy as np
import pandas as pd

# Cargar el modelo y columnas
modelo = joblib.load("modelos/random_forest.pkl")
columnas = joblib.load("modelos/columnas_entrenamiento.pkl")

# Crear diccionario con valores base (0 para todos)
ejemplo = {col: 0 for col in columnas}

# Asignamos valores para un perfil técnico
ejemplo['YearsCodePro'] = 5
ejemplo['EdLevel_Master'] = 1
ejemplo['DevType_Developer, full-stack'] = 1
ejemplo['RemoteWork_Remote'] = 1

# País 1: Estados Unidos
ejemplo['Country_United States of America'] = 1
x_usa = pd.DataFrame([ejemplo])
salario_usa = modelo.predict(x_usa)[0]

# Cambiamos solo el país a Argelia
ejemplo['Country_United States of America'] = 0
ejemplo['Country_Algeria'] = 1
x_argelia = np.array([list(ejemplo.values())])
salario_argelia = modelo.predict(x_argelia)[0]

# Mostrar resultados
print("📊 Comparativa de salarios por país (mismo perfil):")
print(f"🇺🇸 USA:     ${salario_usa:,.2f}")
print(f"🇩🇿 Argelia: ${salario_argelia:,.2f}")
