# sheetmaker/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.v_index, name='sheetmaker_index'),  # Vista principal
    path('download_xls', views.v_reporte_xls, name='download_xls'),  # Descarga del archivo XLS
]
