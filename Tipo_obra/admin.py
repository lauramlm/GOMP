from django.contrib import admin

from .models import tipo_obra

@admin.register(tipo_obra)
class tipo_obraAdmin(admin.ModelAdmin):
    pass
