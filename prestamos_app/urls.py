from django.urls import path
from .views import PrestamoDetailView, PrestamoCreateView

urlpatterns = [
    path('<int:pk>/', PrestamoDetailView.as_view(), name='prestamo_detalle'),
    path("crear/<int:cliente_id>/", PrestamoCreateView.as_view(), name="prestamo_crear"),
]
