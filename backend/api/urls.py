from django.urls import path
from .views import ExtractDataAPIView

urlpatterns = [
    path("extract/", ExtractDataAPIView.as_view(), name="extract"),
]
