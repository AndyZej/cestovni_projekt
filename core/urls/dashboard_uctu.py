

from django.urls import path
from core.views import dashboard_views  # <-- Toto tam chybělo

urlpatterns = [
    path('uctu/', dashboard_views.dashboard_uctu, name='dashboard_uctu'),
]