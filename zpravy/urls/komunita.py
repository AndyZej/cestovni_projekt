
from django.urls import path
from ..views import komunita_rozcestnik, diskuze_zeme

urlpatterns = [
    # Hlavní rozcestník pro zprávy/komunity (adresa: /zpravy/)
    path('', komunita_rozcestnik, name='zpravy'),

    # Detail diskuze pro konkrétní zemi (adresa: /zpravy/zeme/egypt/)
    path('zeme/<slug:slug>/', diskuze_zeme, name='diskuze_zeme'),
]