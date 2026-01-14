from django.urls import path
from .views import (
    ClienteListView,
    ClienteDetailView,
    ReporteDeudasView,
    EstadoCuentaClienteView,
    ClienteCreateView
)

urlpatterns = [
    path("", ClienteListView.as_view(), name='cliente_lista'),
    path("crear/", ClienteCreateView.as_view(), name="cliente_crear"),
    path('<int:pk>/', ClienteDetailView.as_view(), name='cliente_detalle'),
    path('reporte/deudas/', ReporteDeudasView.as_view(), name='reporte_deudas'),
    path('<int:pk>/estado-cuenta', EstadoCuentaClienteView.as_view(), name='estado_cuenta')
]
