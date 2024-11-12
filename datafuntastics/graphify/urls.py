# graphify/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.v_index, name='graphify_index'),  # Vista principal
    path('download_png', views.v_reporte_png, name='download_png'),  # Descarga del gráfico PNG
]