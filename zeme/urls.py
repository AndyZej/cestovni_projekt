

from django.urls import path
from . import views

urlpatterns = [
    path('', views.vyber_zeme, name='vyber_zeme'),
    path('<slug:slug>/', views.detail_zeme, name='detail_zeme'),
]