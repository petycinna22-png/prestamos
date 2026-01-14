from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView
from .models import Prestamo
from .forms import PrestamoForm

from clientes.models import Cliente
# Create your views here.

class PrestamoCreateView(CreateView):
    model = Prestamo
    form_class = PrestamoForm
    template_name = 'prestamos/form.html'

    def dispatch(self, request, *args, **kwargs):
        self.cliente = get_object_or_404(
            Cliente,
            pk=self.kwargs['cliente_id']
        )
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.cliente = self.cliente
        return super().form_valid(form)


    def get_success_url(self):
        return reverse(
            'clientes:cliente_detalle',
            kwargs={'pk': self.object.cliente_id}
        )


class PrestamoDetailView(DetailView):
    model = Prestamo
    template_name = 'prestamos/detalle.html'
    context_object_name = 'prestamo'

    def get_queryset(self):
        return (super()
                .get_queryset()
                .select_related('cliente')
                .prefetch_related('pagos')
        )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pagos'] = (
            self.object.pagos.all()
        )
        return context

