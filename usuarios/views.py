from django.shortcuts import render, redirect
from django.contrib.auth import login
from usuarios.forms import CreacionUsuario, ActualizarUsuario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from .forms import CambiarPassword, LoginForm

def iniciar_sesion(request):

    if request.method == "POST":
        formulario = LoginForm(request, data=request.POST)

        if formulario.is_valid():
            user = formulario.get_user()
            login(request, user)
            return redirect("viajes_app:inicio")

    else:
        formulario = LoginForm()

    return render(request, 'usuarios/iniciar_sesion.html', {
        'formulario_iniciar_sesion': formulario
    })
def registrarse(request):
    
    if request.method == "POST":
        formulario = CreacionUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("usuarios:iniciar_sesion")
    else:
        formulario = CreacionUsuario()
        
    return render(request, 'usuarios/registro.html', {'formulario_registro': formulario})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')


@login_required
def actualizar_perfil(request):
    if request.method == "POST":
        print("=== DEBUG ===")
        print("FILES:", request.FILES)
        print("POST:", request.POST)
        
        formulario = ActualizarUsuario(
            request.POST,
            request.FILES, 
            instance=request.user
        )
        
        print("Form valid:", formulario.is_valid())
        print("Form errors:", formulario.errors)
        
        if formulario.is_valid():
            print("cleaned avatar:", formulario.cleaned_data.get("avatar"))
            formulario.save()
            return redirect('usuarios:perfil')
    else:
        formulario = ActualizarUsuario(instance=request.user)

    return render(request, 'usuarios/actualizar_perfil.html', {
        'formulario': formulario
    })
    
@login_required
def eliminar_avatar(request):
    if request.method == "POST":
        info = request.user.info
        if info.avatar:
            info.avatar.delete()
            info.save()
    return redirect('usuarios:perfil')

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

class CambioDePass(PasswordChangeView):
    template_name = 'usuarios/cambio_pass.html'
    form_class = CambiarPassword
    success_url = reverse_lazy('usuarios:perfil')