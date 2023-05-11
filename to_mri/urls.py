from django.urls import path

from . import views

urlpatterns = [
    #path("", views.formatear_data, name="formatear_data"),
    path("export", views.export_excel, name="export_excel"),
]
