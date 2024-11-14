# graphify/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.v_index, name='graphify_index'),  # Vista principal
    path('download_png', views.v_reporte_png, name='download_png'),  # Descarga del gráfico PNG
    path("lista_reportes", views.v_lista_reportes, name="lista_reportes"),
    path("lista_imagenes", views.v_lista_imagenes, name="lista_imagenes")
]