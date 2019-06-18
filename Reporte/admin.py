from django.contrib import admin

from .models import reporte

@admin.register(reporte)
class reporteAdmin(admin.ModelAdmin):
    pass
