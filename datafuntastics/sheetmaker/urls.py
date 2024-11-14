# sheetmaker/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.v_index, name='v_index'),  # Vista principal
    path("macros", views.v_macros, name="macros"),
    path("powerbi", views.v_powerbi, name="powerbi"),
    path("analitica", views.v_analitica, name="analitica"),
    path('reporte_xls', views.v_reporte_xls, name='v_reporte_xls'),  # Descarga del archivo XLS
]
