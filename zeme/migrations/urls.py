
from django.urls import path
from . import views

urlpatterns = [
    path('', views.vyber_zeme, name='vyber_zeme'),
    path('itinerar/<int:zeme_id>/', views.detail_itineraru, name='itinerar'),
]
