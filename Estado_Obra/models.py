from django.db import models

class estado_obra (models.Model):
    Estado = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Estado 
