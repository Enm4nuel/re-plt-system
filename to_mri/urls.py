from django.urls import path

from . import views

urlpatterns = [
    path('', views.formatear_data, name='formatear_data'),
]