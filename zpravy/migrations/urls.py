
from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_admin, name='chat_admin'),
]
