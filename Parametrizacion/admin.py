from django.contrib import admin

from .models import Parametrizacion_multa

@admin.register(Parametrizacion_multa)
class Parametrizacion_multaAdmin(admin.ModelAdmin):
    pass
