from django.urls import path

from .views import VehiculoDetailView, VehiculoListCreateView

urlpatterns = [
    path("", VehiculoListCreateView.as_view(), name="vehiculo-list-create"),
    path("<int:pk>/", VehiculoDetailView.as_view(), name="vehiculo-detail"),
]
