from django.contrib import admin

from .models import Obra

@admin.register(Obra)
class ObraAdmin(admin.ModelAdmin):
    pass