from django.urls import path
from . import views

app_name = 'fotos'

urlpatterns = [
    path('subir/<int:viaje_id>/', views.subir_foto, name='subir'),
    path('eliminar/<int:id_foto>/', views.eliminar_foto, name='eliminar_foto'),
]