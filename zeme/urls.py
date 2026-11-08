

from django.urls import path
from . import views

urlpatterns = [
    # Hlavní stránka (zde musí být domov_view, protože tak se jmenuje ve views.py)
    path('', views.domov_view, name='domov'),

    # Galerie
    path('galerie/', views.galerie_view, name='galerie'),

    # Sekce Země (seznam + detail)
    path('zeme/', views.seznam_zemi_view, name='seznam_zemi'),
    path('zeme/<slug:slug>/', views.detail_zeme_view, name='detail_zeme'),

    # Sekce Itineráře (seznam + detail)
    path('itinerare/', views.seznam_itineraru_view, name='seznam_itineraru'),
    path('itinerare/<slug:slug>/', views.detail_itineraru_view, name='detail_itineraru'),
]
