from django.contrib import admin

from .models import Contratista

@admin.register(Contratista)
class ContratistaAdmin(admin.ModelAdmin):
    pass
