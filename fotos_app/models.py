from django.db import models
from viajes_app.models import Viaje

class Foto(models.Model):
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return f"Foto {self.id}"