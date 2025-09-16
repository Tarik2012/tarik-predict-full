# TariPredict – Tech Salary Prediction App 💼📈

**TariPredict** is a professional-grade web application that predicts the expected salary of a developer based on their profile, using real-world data and a trained machine learning model.

---

## 🌍 Overview

This project uses data from the **Stack Overflow Developer Survey 2024** to build a machine learning model that predicts annual compensation based on variables such as:

- Country
- Education level
- Years of professional experience
- Developer type
- Work hours
- Company size
- Remote work status

The application is powered by **Django** on the backend and integrates a trained **Random Forest Regressor** model for inference.

---

## 🚀 Technologies Used

- Python 3.12+
- Pandas, NumPy, Scikit-learn, Joblib
- Django (for web interface)
- HTML / CSS (for frontend)
- VS Code (development)
- Railway (deployment)
- Git & GitHub

---

## 🧠 Machine Learning Model

- Type: Random Forest Regressor
- Training data: Cleaned Stack Overflow dataset
- Encoding: One-Hot Encoding (pd.get_dummies)
- Saved using: `joblib`
- Input features: Based on selected categorical + numerical columns
- Model files:
  - `modelo_entrenado.pkl`
  - `columnas_entrenamiento.pkl`

---

## 🧾 Web App Features

- 🌐 Simple form interface to enter developer data
- 📥 Real-time salary prediction using the trained model
- ✅ Encodes categorical variables and fills missing columns
- 🔍 Country influence is verified in the pipeline

---

## 📂 Project Structure

```
TariPredict/
├── core/
│   ├── predict_model.py          # ML prediction logic
│   ├── templates/
│   │   └── predict_salary.html   # Form template
│   └── modelos/
│       ├── modelo_entrenado.pkl
│       └── columnas_entrenamiento.pkl
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🛠️ How to Run

1. Clone this repo:

```bash
git clone https://github.com/Tarik2012/tarik-predict.git
cd TariPredict
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python manage.py runserver
```

Then open `http://127.0.0.1:8000/predict-salary/` in your browser.

---

## 📸 Screenshots

_(Optional – you can add screenshots later here)_

---

## 📜 License

This project is licensed under the MIT License. You are free to use, modify and distribute it.

---

## 🙌 Credits

Developed by **Tarek Errochdi** as part of a professional Data Science portfolio.
