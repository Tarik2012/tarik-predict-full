import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# ======================
# 1. Cargar dataset
# ======================
data = load_iris()
# ✅ Usar DataFrame con nombres de columnas y todo en float64 (evita warnings)
X = pd.DataFrame(data.data, columns=data.feature_names).astype("float64")
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ======================
# 2. Definir modelos
# ======================
experiments = [
    ("Logistic Regression", LogisticRegression(max_iter=1000)),
    ("Random Forest", RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)),
    ("SVM", SVC(kernel="rbf", C=1, gamma="scale"))
]

# Ejemplo de input para MLflow (1 fila de entrenamiento)
example = X_train.iloc[:1]

# ======================
# 3. Ejecutar experimentos
# ======================
for model_name, model in experiments:
    with mlflow.start_run(run_name=model_name):
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        # Calcular métricas
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, average="macro")
        rec = recall_score(y_test, y_pred, average="macro")
        f1 = f1_score(y_test, y_pred, average="macro")

        # Guardar parámetros y métricas
        mlflow.log_param("model", model_name)
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("precision", prec)
        mlflow.log_metric("recall", rec)
        mlflow.log_metric("f1_score", f1)

        # Guardar modelo en MLflow con input_example
        mlflow.sklearn.log_model(
            sk_model=model,
            name=f"{model_name}_model",
            input_example=example
        )

        print(f"✅ {model_name} registrado con Accuracy={acc:.2f}, F1={f1:.2f}")
