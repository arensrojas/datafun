# librarium/urls.py

from django.urls import path
from . import views
from . import views

urlpatterns = [
    path('', views.v_index, name='v_index'),
    path('data-analitica', views.v_data_analitica, name='v_data_analitica'),
    path('data_frame', views.v_data_frame, name='v_data_frame'),
    path('servicios', views.v_servicios, name='v_servicios'),# Vista principal
    path('download_pdf', views.v_reporte_pdf, name='download_pdf'),  # Descarga del archivo PDF
]
