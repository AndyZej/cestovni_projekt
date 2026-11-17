
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

# Import pohledu pro úpravu oblíbených částí uživatele
from core.views import upravit_oblibene_view

urlpatterns = [
    # Administrace Django
    path('admin/', admin.site.urls),

    # Aplikace core (domovská stránka, uživatelský panel atd.)
    path('', include('core.urls')),

    # Aplikace zeme
    path('', include('zeme.urls')),

    # Zprávy / Podpora
    path('zpravy/', include('zpravy.urls')),

    # Přihlášení a odhlášení
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Správa 4 oblíbených částí v uživatelském panelu
    path('uctu/oblibene/upravit/', upravit_oblibene_view, name='upravit_oblibene'),
]