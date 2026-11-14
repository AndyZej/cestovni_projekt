

from django.urls import path
from ..views import komunita_rozcestnik, diskuze_zeme

urlpatterns = [
    path('', komunita_rozcestnik, name='seznam_zprav'),
    path('zeme/<slug:slug>/', diskuze_zeme, name='diskuze_zeme'),
]