from django.shortcuts import render
from django.http import HttpResponse
import datetime
from openpyxl import Workbook



static_values = {
    "direccion": "Las flores amarillas 343434 | Concepcion",
    "telefono" : "+56 982020054",
    "email" : "info@lafloresamarillas.cl",
    "whatsapp" : "+56 982020054"
}
# Create your views here.
def  v_index(request):
    return HttpResponse("sheetmaker index")

def  v_macros(request):
    context = {
        "static_values": static_values
    }
    return render(request, "sheetmaker/macros.html", context)

def  v_powerbi(request):
    context = {
        "static_values": static_values
    }
    return render(request, "sheetmaker/powerbi.html", context)

def  v_analitica(request):
    context = {
        "static_values": static_values
    }
    return render(request, "sheetmaker/analitica.html", context)


def v_reporte_xls(request):
    # Crear un libro de Excel
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Reporte de Ejemplo"

    # Agregar encabezados
    encabezados = ["ID", "Nombre", "Fecha"]
    worksheet.append(encabezados)

    # Agregar algunos datos de ejemplo
    datos = [
        [1, "Alice", datetime.date(2023, 11, 5)],
        [2, "Bob", datetime.date(2023, 11, 6)],
        [3, "Charlie", datetime.date(2023, 11, 7)],
    ]

    for fila in datos:
        worksheet.append(fila)

    # Preparar la respuesta HTTP con el archivo Excel
    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = "attachment; filename=reporte.xlsx"

    # Guardar el libro en la respuesta
    workbook.save(response)

    return response