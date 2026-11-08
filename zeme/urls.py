

from django.urls import path
from . import views

urlpatterns = [
    # Hlavní stránka / Domů
    path('', views.domovsky_view, name='domovsky'),

    # Seznamy
    path('země/', views.seznam_zemi_view, name='seznam_zemi'),
    path('itinerare/', views.seznam_itineraru_view, name='seznam_itineraru'),

    # Detail jednotlivých zemí
    path('zeme/<slug:slug>/', views.detail_zeme_view, name='detail_zeme'),

    # Itineráře zemí (detail)
    path('itinerare/<slug:slug>/', views.detail_itineraru_view, name='detail_itineraru'),

    # Samostatné galerie jednotlivých zemí (sekce Země)
    path('galerie/kapverdy/', views.kapverdy_galerie_view, name='kapverdy_galerie'),
    path('galerie/egypt/', views.egypt_galerie_view, name='egypt_galerie'),
    path('galerie/tunisko/', views.tunisko_galerie_view, name='tunisko_galerie'),
    path('galerie/turecko/', views.turecko_galerie_view, name='turecko_galerie'),

    # Samostatné galerie jednotlivých itinerářů (sekce Itinerář)
    path('itinerare/galerie/kapverdy/', views.kapverdy_itinerar_galerie_view, name='kapverdy_itinerar_galerie'),
    path('itinerare/galerie/egypt/', views.egypt_itinerar_galerie_view, name='egypt_itinerar_galerie'),
    path('itinerare/galerie/tunisko/', views.tunisko_itinerar_galerie_view, name='tunisko_itinerar_galerie'),
    path('itinerare/galerie/turecko/', views.turecko_itinerar_galerie_view, name='turecko_itinerar_galerie'),
]