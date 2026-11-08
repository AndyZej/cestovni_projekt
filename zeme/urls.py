
from django.urls import path
from . import views

urlpatterns = [
    # Hlavní stránka (výběr zemí)
    path('', views.domov_view, name='domov'),

    # Přihlášení
    path('accounts/login/', views.login_view, name='login'),

    # Galerie všech zemí
    path('galerie/', views.galerie_view, name='galerie'),

    # Detaily jednotlivých zemí
    path('egypt/', views.egypt_view, name='egypt'),
    path('turecko/', views.turecko_view, name='turecko'),
    path('kapverdy/', views.kapverdy_view, name='kapverdy'),
    path('tunisko/', views.tunisko_view, name='tunisko'),
]