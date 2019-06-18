from django.db import models

class  auditoria (models.Model):
    FechaAccion = models.DateField(unique=True)

    def __str__(self):
        return self.FechaAccion 