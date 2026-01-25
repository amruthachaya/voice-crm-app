from django.urls import path
from .views import ExtractDataAPIView, EvaluationAPIView, EvaluationExcelAPIView

urlpatterns = [
    path("extract/", ExtractDataAPIView.as_view(), name="extract"),
    path("evals/", EvaluationAPIView.as_view(), name="evals"),
    path("evals/excel/", EvaluationExcelAPIView.as_view(), name="evals_excel"),
]
