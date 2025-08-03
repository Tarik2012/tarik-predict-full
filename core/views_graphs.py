from django.views.generic import TemplateView
from .utils import load_data
import pandas as pd
import numpy as np
import plotly.express as px

class GlobalGraphView(TemplateView):
    template_name = "core/global_graphs.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 1. Cargar datos
        df = load_data()

        # 2. Preparar datos
        df_clean = df[["YearsCodePro", "ConvertedCompYearly"]].dropna()

        def clean_experience(x):
            if x == "Less than 1 year":
                return 0.5
            elif x == "More than 50 years":
                return 51
            try:
                return float(x)
            except:
                return np.nan

        df_clean["YearsCodePro"] = df_clean["YearsCodePro"].apply(clean_experience)
        df_clean = df_clean.dropna()

        # Agrupar y calcular salario medio
        salary_by_experience = df_clean.groupby("YearsCodePro")["ConvertedCompYearly"].mean().reset_index()

        # 3. Crear la gráfica y convertirla a HTML
        fig = px.line(
            salary_by_experience,
            x="YearsCodePro",
            y="ConvertedCompYearly",
            title="Average Salary by Years of Experience",
            labels={
                "YearsCodePro": "Years of Experience",
                "ConvertedCompYearly": "Avg Salary (USD)"
            },
        )
        graph_html = fig.to_html(full_html=False)

        # 4. Pasar el HTML al template
        context["graph_html"] = graph_html
        return context
