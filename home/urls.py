from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('csv_download/', views.csv_download, name='csv_download'),
    path('csv_upload/', views.csv_upload, name='csv_upload'),
    path('csv_upload/confirm/', views.csv_upload_confirm, name='csv_upload_confirm'),
    path('csv_upload/confirm/cc/<str:bldgid>', views.csv_upload_confirm_cc, name='csv_upload_confirm_cc'), # guardar cambios 
    path('csv_upload/confirm/dc/<str:bldgid>', views.csv_upload_confirm_dc, name='csv_upload_confirm_dc'), # deshacer cambios
    path('data_validate/', views.data_validate, name='data_validate'),
    path('data_validate/confirm/<int:id>', views.data_validate_confirm, name='data_validate_confirm'),
    path('data_post/', views.data_post, name='data_post')
]