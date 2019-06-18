from django.db import models

# Create your models here.

class tipo_obra (models.Model):
    ClasificacionObra = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.ClasificacionObra 