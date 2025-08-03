from django.urls import path
from .views import HomeView, AnalysisView, FilterView
from core.views_graphs import GlobalGraphView
from .view_predict import PredictSalaryView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('analysis/', AnalysisView.as_view(), name='analysis'),
    path('filters/', FilterView.as_view(), name='filters'),  # Nueva ruta para explorar por filtros
    path('graphs/', GlobalGraphView.as_view(), name='global_graphs'),
    path("predict-salary/", PredictSalaryView.as_view(), name="predict_salary"),
]
