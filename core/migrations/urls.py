from django.urls import path
from . import views

urlpatterns = [
    path('', views.domovska_stranka, name='domov'),
]
