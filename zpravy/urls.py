

from django.urls import path
from . import views

urlpatterns = [
    path('', views.komunita_rozcestnik, name='seznam_zprav'),
    path('zeme/<slug:slug>/', views.diskuze_zeme, name='diskuze_zeme'),
    path('admin-chat/', views.chat_admin, name='chat_admin'),
]