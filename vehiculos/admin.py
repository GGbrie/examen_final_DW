from django.contrib import admin

from .models import Vehiculo


@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    list_display = ("id", "marca", "modelo", "anio", "color", "created_at")
    search_fields = ("marca", "modelo", "color")
