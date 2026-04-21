from django import forms
from .models import Foto

class FotoForm(forms.ModelForm):
    imagen = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta:
        model = Foto
        fields = ['imagen']