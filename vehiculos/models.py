from django.core.exceptions import ValidationError
from django.db import models


def validar_texto_no_vacio(valor):
    """Rechaza cadenas vacías o formadas solo por espacios."""
    if not valor or not valor.strip():
        raise ValidationError("Este campo no puede estar vacío.")


class Vehiculo(models.Model):
    marca = models.CharField(
        max_length=100,
        validators=[validar_texto_no_vacio],
        help_text="Marca del vehículo (obligatoria).",
    )
    modelo = models.CharField(
        max_length=100,
        validators=[validar_texto_no_vacio],
        help_text="Modelo del vehículo (obligatorio).",
    )
    anio = models.IntegerField(
        help_text="Año de fabricación del vehículo (obligatorio).",
    )
    color = models.CharField(
        max_length=50,
        validators=[validar_texto_no_vacio],
        help_text="Color del vehículo (obligatorio).",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "vehiculos"
        ordering = ["-created_at"]
        verbose_name = "Vehículo"
        verbose_name_plural = "Vehículos"

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"
