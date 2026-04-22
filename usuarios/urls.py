from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from usuarios.views import CambioDePass


app_name = 'usuarios'

urlpatterns = [
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', LogoutView.as_view(template_name='usuarios/cerrar_sesion.html'), name='cerrar_sesion'),  
    path('registro/', views.registrarse, name='registro'),    
    path('perfil/', views.perfil, name='perfil'), 
    path('perfil/actualizar', views.actualizar_perfil, name='actualizar_perfil'), 
    path('perfil/eliminar-avatar/', views.eliminar_avatar, name='eliminar_avatar'),
    path('perfil/actualizar/password/', CambioDePass.as_view(), name='actualizar_password'),
    
]