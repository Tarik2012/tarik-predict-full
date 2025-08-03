from django.views.generic import TemplateView
from .utils import load_data
from collections import Counter
import pandas as pd


class HomeView(TemplateView):
    template_name = 'core/home.html'


class AnalysisView(TemplateView):
    template_name = "core/analysis.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Cargar datos del CSV como DataFrame
        df = load_data()

        # Total de participantes (número de filas)
        context["total_participants"] = len(df)

        # Salario promedio (eliminando valores nulos)
        context["average_salary"] = round(df["ConvertedCompYearly"].dropna().mean(), 2)

        # Tipos de desarrollador (DevType puede tener varios por persona separados por ;)
        roles_series = df["DevType"].dropna()  # Quitamos nulos
        roles = []
        for entry in roles_series:
            roles.extend(entry.split(";"))  # Separar por ";"

        # Contamos los más comunes (limpiando espacios) y guardamos el top 5
        top_roles = Counter([r.strip() for r in roles]).most_common(5)
        context["top_roles"] = top_roles

        # Top 5 niveles educativos
        top_education = df["EdLevel"].value_counts().head(5)
        context["top_education"] = top_education.items()


        return context
    
class FilterView(TemplateView):
    template_name = "core/filters.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        df = load_data()

        # ----------------------------
        # Preparar listas únicas para los filtros
        # ----------------------------
        context["countries"] = sorted(df["Country"].dropna().unique())
        context["devtypes"] = sorted(set(dev.strip() for devlist in df["DevType"].dropna().str.split(";") for dev in devlist))
        context["edlevels"] = sorted(df["EdLevel"].dropna().unique())
        context["experiences"] = sorted(df["YearsCodePro"].dropna().unique(), key=lambda x: str(x))

        # ----------------------------
        # Aplicar filtros GET si existen
        # ----------------------------
        country = self.request.GET.get("country")
        devtype = self.request.GET.get("devtype")
        edlevel = self.request.GET.get("edlevel")
        experience = self.request.GET.get("experience")

        if country:
            df = df[df["Country"] == country]

        if devtype:
            df = df[df["DevType"].notna() & df["DevType"].str.contains(devtype, na=False)]


        if edlevel:
            df = df[df["EdLevel"] == edlevel]

        if experience:
            df = df[df["YearsCodePro"] == experience]

        # ----------------------------
        # Resultados filtrados
        # ----------------------------
        context["total"] = len(df)
        context["average_salary"] = df["ConvertedCompYearly"].dropna().mean()

        return context    
