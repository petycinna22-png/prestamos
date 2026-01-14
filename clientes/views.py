from django.shortcuts import render

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm
# Create your views here.

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'clientes/form.html'
    success_url = reverse_lazy('clientes:cliente_lista')

class ModelUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/form.html"
    success_url = reverse_lazy('clientes:cliente_lista')


class ClienteListView(ListView):
    model = Cliente
    template_name = 'clientes/lista.html'
    context_object_name = 'clientes'

class ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'clientes/detalle.html'
    context_object_name = 'cliente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prestamos'] = (
            self.object.prestamos.prefetch_related('pagos')
        )

        return context

class ReporteDeudasView(ListView):
    model = Cliente
    template_engine = 'clientes/reporte_deudas.html'
    context_object_name = 'clientes'

class EstadoCuentaClienteView(DetailView):
    model = Cliente
    template_name = 'clientes/estado_cuenta.html'
    context_object_name = 'cliente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prestamos'] = (
            self.object.prestamos.prefetch_related('pagos')
        )

        return context
    