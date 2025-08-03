# tune_model.py

import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# 1. Cargar datos limpios
df = pd.read_csv("data/datos_limpios_modelo.csv")
X = df.drop("ConvertedCompYearly", axis=1)
y = df["ConvertedCompYearly"]

# 2. Dividir en train y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Definir modelo base
modelo = RandomForestRegressor(random_state=42)

# 4. Definir grid de hiperparámetros (más rápido que GridSearch)
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'bootstrap': [True, False]
}

# 5. RandomizedSearchCV
busqueda = RandomizedSearchCV(
    estimator=modelo,
    param_distributions=param_grid,
    n_iter=20,
    cv=3,
    verbose=2,
    n_jobs=-1,
    random_state=42
)

# 6. Entrenar búsqueda
busqueda.fit(X_train, y_train)

# 7. Evaluar el mejor modelo
mejor_modelo = busqueda.best_estimator_
y_pred = mejor_modelo.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("✅ Mejor modelo encontrado:")
print(busqueda.best_params_)
print(f"📉 MSE: {mse:.2f}")
print(f"📈 RMSE: {rmse:.2f}")

# 8. Guardar el modelo y columnas
os.makedirs("modelos", exist_ok=True)
joblib.dump(mejor_modelo, "modelos/mejor_modelo.pkl")
joblib.dump(X_train.columns.tolist(), "modelos/columnas_entrenamiento.pkl")

print("✅ Modelo optimizado guardado en: modelos/mejor_modelo.pkl")
