# core/train_model.py

import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Cargar el dataset ya codificado
df = pd.read_csv("data/datos_limpios_modelo.csv")

# Dividir en features (X) y target (y)
X = df.drop("ConvertedCompYearly", axis=1)
y = df["ConvertedCompYearly"]

# Dividir en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
modelo = RandomForestRegressor(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Guardar modelo y columnas
joblib.dump(modelo, "modelos/random_forest.pkl")
joblib.dump(X_train.columns.tolist(), "modelos/columnas_entrenamiento.pkl")

print("✅ Modelo entrenado y guardado con éxito.")
