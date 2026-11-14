


from django.urls import path
from ..views import (
    domovsky_view,
    seznam_zemi_view,
    detail_zeme_view,
    kapverdy_galerie_view,
    egypt_galerie_view,
    tunisko_galerie_view,
    turecko_galerie_view,
)

urlpatterns = [
    # Hlavní stránka / Domů
    path('', domovsky_view, name='domovsky'),

    # Seznam zemí
    path('země/', seznam_zemi_view, name='seznam_zemi'),

    # Detail jednotlivých zemí
    path('zeme/<slug:slug>/', detail_zeme_view, name='detail_zeme'),

    # Samostatné galerie jednotlivých zemí
    path('galerie/kapverdy/', kapverdy_galerie_view, name='kapverdy_galerie'),
    path('galerie/egypt/', egypt_galerie_view, name='egypt_galerie'),
    path('galerie/tunisko/', tunisko_galerie_view, name='tunisko_galerie'),
    path('galerie/turecko/', turecko_galerie_view, name='turecko_galerie'),
]
