

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Administrace
    path('admin/', admin.site.urls),

    # Hlavní rozcestník (app core)
    path('', include('core.urls')),

    # Aplikace zeme (zahrnuje cesty pro země, galerie i itineráře)
    path('', include('zeme.urls')),

    # Sekce Zprávy
    path('zpravy/', include('zpravy.urls')),

    # Přihlášení a odhlášení
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
