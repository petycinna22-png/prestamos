from django.shortcuts import render, get_object_or_404

from django.views.generic import CreateView
from django.urls import reverse
from .models import Pago
from .forms import PagoForm

from prestamos_app.models import Prestamo
# Create your views here.

class PagoCreateView(CreateView):
    model = Pago
    form_class = PagoForm
    template_name = 'pagos/crear.html'

    def dispatch(self, request, *args, **kwargs):
        self.prestamo = get_object_or_404(
            Prestamo,
            pk=self.kwargs['prestamo_id']
        )
        print(f"DEBUG: Obteniendo prestamo con ID: {self.prestamo.id}")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.prestamo = self.prestamo
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        try:
            prestamo = self.prestamo
        except AttributeError:
            prestamo = None
        if prestamo is not None:
            if not kwargs.get('instance'):
                kwargs['instance'] = Pago(prestamo=prestamo)
        return kwargs

    def get_success_url(self):
        return reverse(
            'prestamos:prestamo_detalle',
            kwargs={'pk': self.object.prestamo_id}
        )
    