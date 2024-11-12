# librarium/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.v_index, name='librarium_index'),  # Vista principal
    path('download_pdf', views.v_reporte_pdf, name='download_pdf'),  # Descarga del archivo PDF
]
