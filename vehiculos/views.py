from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Vehiculo
from .serializers import VehiculoSerializer


class VehiculoListCreateView(generics.ListCreateAPIView):
    """GET /api/vehiculos/ (listar) y POST /api/vehiculos/ (crear)."""

    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [AllowAny]


class VehiculoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """GET, PUT, PATCH y DELETE sobre /api/vehiculos/<id>/."""

    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [AllowAny]
