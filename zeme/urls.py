

from django.urls import path
from . import views

urlpatterns = [
    # 1. Hlavní stránka (rozcestník)
    path('', views.domovsky_view, name='domovsky'),

    # 2. Hlavní fotogalerie
    path('galerie/', views.galerie_view, name='galerie'),

    # 3. Sekce Země (seznam + detail)
    path('zeme/', views.seznam_zemi_view, name='seznam_zemi'),
    path('zeme/<slug:slug>/', views.detail_zeme_view, name='detail_zeme'),

    # 4. Samostatná galerie pro konkrétní zemi
    path('zeme/<slug:slug>/galerie/', views.galerie_zeme, name='galerie_zeme'),

    # 5. Sekce Itineráře (seznam + detail)
    path('itinerare/', views.seznam_itineraru_view, name='seznam_itineraru'),
    path('itinerare/<slug:slug>/', views.detail_itineraru_view, name='detail_itineraru'),  # <-- Zde musí být 'detail_itineraru'
]
