
import joblib
columnas = joblib.load("modelos/columnas_entrenamiento.pkl")
print("Country" in columnas)
print([col for col in columnas if "Country" in col])