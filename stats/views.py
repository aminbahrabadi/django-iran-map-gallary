from django.views.generic import TemplateView

from .models import State


class GeoStatsTemplateView(TemplateView):
    template_name = 'states/geo_stats.html'

    def get_context_data(self, **kwargs):
        context = super(GeoStatsTemplateView, self).get_context_data(**kwargs)

        context['states'] = State.objects.all()

        return context
