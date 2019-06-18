from django.db import models

from Contratista.models import Contratista

class Obra (models.Model):
    NombreObra = models.CharField(max_length=200, unique =True)
    DireccionObra = models.CharField(max_length=200)
    ValorObra = models.IntegerField()
    FechaInicioObra = models.DateField()
    FechaFinObra = models.DateField()
    MultaObra = models.IntegerField(default = 0)

    Contratista = models.ForeignKey(Contratista, on_delete=models.CASCADE)

    def __str__(self):
        return self.NombreObra 
    


