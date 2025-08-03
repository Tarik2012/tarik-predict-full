# core/evaluate_model.py

import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

# 1. Cargar modelo optimizado y columnas usadas
modelo = joblib.load("modelos/mejor_modelo.pkl")
columnas = joblib.load("modelos/columnas_entrenamiento.pkl")

# 2. Cargar los datos y dividir en X e y
df = pd.read_csv("data/datos_limpios_modelo.csv")
X = df[columnas]
y = df["ConvertedCompYearly"]

# 3. Dividir en train y test (igual que antes)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Hacer predicciones
y_pred = modelo.predict(X_test)

# 5. Calcular métricas
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)



# 6. Mostrar resultados
print("📊 Resultados del modelo optimizado:")
print(f"🔹 MAE (Mean Absolute Error): ${mae:,.2f}")
print(f"🔹 R² (Coef. de Determinación): {r2:.4f}")
