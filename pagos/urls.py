from django.urls import path
from .views import PagoCreateView

urlpatterns = [
    path('nuevo/<int:prestamo_id>/', PagoCreateView.as_view(), name='pago_crear'),
]
