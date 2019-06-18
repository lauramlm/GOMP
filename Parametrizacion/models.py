from django.db import models

class  Parametrizacion_multa (models.Model):
    DesfaseTiempo1 = models.IntegerField(default = 0.5)
    DesfaseTiempo2 = models.IntegerField(default = 0.2)
    ValorTotalMulta = models.IntegerField(default = 0)

    def __str__(self):
        return self.ValorTotalMulta 