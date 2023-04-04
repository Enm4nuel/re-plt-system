from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('descargar_csv/', views.descargar_csv, name='descargar_csv'),
    path('subir_archivo/', views.subir_archivo, name='subir_archivo'),
    path('subir_archivo/confirmar/<str:filename>', views.subir_archivo_confirmar, name='subir_archivo_confirmar'),
    path('subir_archivo/confirmar/cc/', views.subir_archivo_confirmar_cc, name='subir_archivo_confirmar_cc'), # guardar cambios 
    path('subir_archivo/confirmar/dc/', views.subir_archivo_confirmar_dc, name='subir_archivo_confirmar_dc'), # deshacer cambios
    path('validar_datos/', views.validar_datos, name='validar_datos'),
    path('postear_datos/', views.postear_datos, name='postear_datos')
]