

from django.urls import path
from ..views import (
    seznam_itineraru_view,
    detail_itineraru_view,
    kapverdy_itinerar_galerie_view,
    egypt_itinerar_galerie_view,
    tunisko_itinerar_galerie_view,
    turecko_itinerar_galerie_view,
)

urlpatterns = [
    # Seznam itinerářů
    path('', seznam_itineraru_view, name='seznam_itineraru'),

    # 1. SPECIFICKÉ CESTY PRO GALERIE MUSÍ BÝT PRVNÍ:
    path('galerie/kapverdy/', kapverdy_itinerar_galerie_view, name='kapverdy_itinerar_galerie'),
    path('galerie/egypt/', egypt_itinerar_galerie_view, name='egypt_itinerar_galerie'),
    path('galerie/tunisko/', tunisko_itinerar_galerie_view, name='tunisko_itinerar_galerie'),
    path('galerie/turecko/', turecko_itinerar_galerie_view, name='turecko_itinerar_galerie'),

    # 2. OBECNÝ SLUG AŽ NAKONEC:
    path('<slug:slug>/', detail_itineraru_view, name='detail_itineraru'),
]