from django.contrib import admin

from .models import auditoria

@admin.register(auditoria)
class auditoriaAdmin(admin.ModelAdmin):
    pass
