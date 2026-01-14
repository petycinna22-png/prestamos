from django.views.generic import TemplateView
from django.utils.timezone import now

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = now()
        return context