# core/view_predict.py

from django.views import View
from django.shortcuts import render
from .predict_model import predecir_salarios, predecir_salario_desde_formulario

class PredictSalaryView(View):
    template_name = "core/predict_salary.html"

    def get(self, request):
        # Mostrar solo las métricas del modelo
        context = predecir_salarios()
        return render(request, self.template_name, context)

    def post(self, request):
        # Recibir datos del formulario
        datos = {
            'Country': request.POST.get('Country'),
            'EdLevel': request.POST.get('EdLevel'),
            'YearsCodePro': request.POST.get('YearsCodePro'),
            'Employment': request.POST.get('Employment'),
            'RemoteWork': request.POST.get('RemoteWork'),
            'OrgSize': request.POST.get('OrgSize'),
            'DevType': request.POST.get('DevType'),
            'AISelect': request.POST.get('AISelect'),
        }

        salario = predecir_salario_desde_formulario(datos)

        # Mostrar predicción + análisis del modelo
        context = predecir_salarios()
        context["salario"] = round(salario, 2)
        context["datos"] = datos
        return render(request, self.template_name, context)
