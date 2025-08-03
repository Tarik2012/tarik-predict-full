import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Cargar modelo y columnas
modelo = joblib.load("modelos/random_forest.pkl")
columnas_finales = joblib.load("modelos/columnas_entrenamiento.pkl")

# 🔁 Función para evaluación general del modelo (no formulario)
def predecir_salarios():
    df = pd.read_csv("data/datos_limpios_modelo.csv")
    X = df.drop("ConvertedCompYearly", axis=1)
    y = df["ConvertedCompYearly"]

    y_pred = modelo.predict(X)
    mae = mean_absolute_error(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)

    return {
        "sample_size": len(df),
        "mae": round(mae, 2),
        "mse": round(mse, 2),
        "r2": round(r2, 4),
        "modelo": "Random Forest Regressor"
    }

# 🔮 Función para predecir desde formulario (ya transformado con get_dummies)
def predecir_salario_desde_formulario(datos):
    print("🌍 País recibido:", datos.get("Country"))

    # Crear DataFrame
    df = pd.DataFrame([datos])
    print("🌍 País recibido:", df["Country"].values[0])  # Debug

    

    # Validar YearsCodePro
    try:
        df["YearsCodePro"] = float(df["YearsCodePro"].values[0])
    except:
        df["YearsCodePro"] = 0.0

    # Codificar con get_dummies
    df_encoded = pd.get_dummies(df)

    # 🔧 Agregar columnas faltantes con 0 (versión rápida y sin warning)
    columnas_faltantes = [col for col in columnas_finales if col not in df_encoded.columns]
    df_extra = pd.DataFrame(0, index=df_encoded.index, columns=columnas_faltantes)
    df_encoded = pd.concat([df_encoded, df_extra], axis=1)

    # Ordenar columnas
    df_encoded = df_encoded[columnas_finales]

    # ✅ Verificar si la columna del país está activa
    columna_pais = f"Country_{df['Country'].values[0]}"
    if columna_pais in df_encoded.columns:
        print(f"✅ '{columna_pais}' ACTIVADA con valor: {df_encoded[columna_pais].values[0]}")
    else:
        print(f"❌ '{columna_pais}' NO está en las columnas codificadas")

    # 🔎 Ver columnas activadas del país
    print("🔎 Columnas de país activadas:")
    print(df_encoded[[col for col in df_encoded.columns if "Country" in col]].T)

    # Predicción
    prediccion = modelo.predict(df_encoded)[0]
    return round(prediccion, 2)
