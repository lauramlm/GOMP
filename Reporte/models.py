from django.db import models

class reporte (models.Model):
    FechaReporte = models.DateField(unique=True)

    def __str__(self):
        return self.FechaReporte 