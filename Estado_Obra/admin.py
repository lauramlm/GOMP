from django.contrib import admin

from .models import estado_obra

@admin.register(estado_obra)
class estado_obraAdmin(admin.ModelAdmin):
    pass
