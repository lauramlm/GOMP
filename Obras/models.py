from django.db import models
class Obra (models.Model):
    NombreObra = models.CharField(max_length=200, unique =True)
    DireccionObra = models.CharField(max_length=200)
    ValorObra = models.IntegerField()
    FechaInicioObra = models.DateField()
    FechaFinObra = models.DateField()
    MultaObra = models.IntegerField(default = 0)

    def __str__(self):
        return self.NombreObra 
    


