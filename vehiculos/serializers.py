from rest_framework import serializers

from .models import Vehiculo


class VehiculoSerializer(serializers.ModelSerializer):
    """Convierte Vehiculo a JSON y valida los datos que llegan del cliente."""

    class Meta:
        model = Vehiculo
        fields = [
            "id",
            "marca",
            "modelo",
            "anio",
            "color",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def validate_marca(self, valor):
        if not valor.strip():
            raise serializers.ValidationError("La marca no puede estar vacía.")
        return valor.strip()

    def validate_modelo(self, valor):
        if not valor.strip():
            raise serializers.ValidationError("El modelo no puede estar vacío.")
        return valor.strip()

    def validate_color(self, valor):
        if not valor.strip():
            raise serializers.ValidationError("El color no puede estar vacío.")
        return valor.strip()

    def validate_anio(self, valor):
        if valor < 1886:
            raise serializers.ValidationError(
                "El año debe ser 1886 o posterior (año del primer automóvil)."
            )
        return valor
