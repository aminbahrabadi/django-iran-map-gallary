from django.urls import path

from . import views


app_name = 'stats'

urlpatterns = [
    path('', views.GeoStatsTemplateView.as_view(), name='geo_stats'),
]
