from django.db import models

class Contratista (models.Model):
    NombreContratista = models.CharField(max_length=200)
    IdentificacionContratista = models.CharField(max_length=20, unique = True)
    DireccionContratista = models.CharField(max_length=200)
    TelefonoContratista = models.CharField(max_length=20)

    def __str__(self):
        return self.NombreContratista 

