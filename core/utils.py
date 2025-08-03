import pandas as pd

def load_data():
    """Carga el archivo CSV principal, ignorando líneas corruptas."""
    df = pd.read_csv("data/survey_results_public.csv", on_bad_lines='skip')
    return df
