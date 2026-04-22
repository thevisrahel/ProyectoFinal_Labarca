from django.urls import path
# from . import views
from .views import SubirFotoView, EliminarFotoView
app_name = 'fotos'

urlpatterns = [
    path('subir/<int:viaje_id>/', SubirFotoView.as_view(), name='subir'),
    path('eliminar/<int:id_foto>/', EliminarFotoView.as_view(), name='eliminar_foto'),
]