from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import InfoExtra
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].label = "Usuario"
        self.fields["password"].label = "Contraseña"

        self.fields["username"].help_text = ""
        self.fields["password"].help_text = ""

        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Introduce tu usuario"
        })

        self.fields["password"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Introduce tu contraseña"
        })

class CreacionUsuario(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        labels = {
            "username": "Nombre de usuario",
            "first_name": "Nombre",
            "last_name": "Apellido",
            "email": "Email",
            "password1": "Contraseña",
            "password2": "Repetir contraseña",
        }

        for field, label in labels.items():
            self.fields[field].label = label
            self.fields[field].help_text = ""
            self.fields[field].widget.attrs.update({
                "class": "form-control"
            })


class ActualizarUsuario(forms.ModelForm):

    fecha_nacimiento = forms.DateField(
        required=False,
        label="Fecha de nacimiento",
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control"
        })
    )

    avatar = forms.ImageField(
        required=False,
        label="Avatar",
        widget=forms.FileInput(attrs={
            "class": "form-control"
        })
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.get("instance")
        super().__init__(*args, **kwargs)

        labels = {
            "first_name": "Nombre",
            "last_name": "Apellido",
            "email": "Email",
        }

        for field, label in labels.items():
            self.fields[field].label = label
            self.fields[field].help_text = ""
            self.fields[field].widget.attrs.update({
                "class": "form-control"
            })

        if user:
            info, _ = InfoExtra.objects.get_or_create(user=user)
            self.fields["fecha_nacimiento"].initial = info.fecha_nacimiento
            self.fields["avatar"].initial = info.avatar

    def save(self, commit=True):
        user = super().save(commit=False)

        fecha = self.cleaned_data.get("fecha_nacimiento")
        avatar = self.cleaned_data.get("avatar")

        if commit:
            user.save()

        info, _ = InfoExtra.objects.get_or_create(user=user)
        info.fecha_nacimiento = fecha

        if avatar:
            info.avatar = avatar

        if commit:
            info.save()

        return user

class CambiarPassword(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        labels = {
            "old_password": "Contraseña actual",
            "new_password1": "Nueva contraseña",
            "new_password2": "Confirmar nueva contraseña",
        }

        for field, label in labels.items():
            self.fields[field].label = label
            self.fields[field].help_text = ""
            self.fields[field].widget.attrs.update({
                "class": "form-control"
            })