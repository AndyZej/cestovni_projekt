

# core/urls/dashboard_uctu.py
from core.views.dashboard_uctu import dashboard_uctu
from core.views.upravit_oblibene_view import upravit_oblibene_view
from django.urls import path

urlpatterns = [
    # Cesta pro samotný dashboard účtu
    path(
        'uctu/',
        dashboard_uctu,
        name='dashboard_uctu'
    ),

    # Cesta pro formulář výběru a úpravy oblíbených částí
    path(
        'uctu/oblibene/upravit/',
        upravit_oblibene_view,
        name='upravit_oblibene'
    ),
]

