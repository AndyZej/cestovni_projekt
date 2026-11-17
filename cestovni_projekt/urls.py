
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Hlavní stránka a core funkce
    path('', include('core.urls')),

    # Aplikace zeme (zde máte schované i vše ostatní)
    path('', include('zeme.urls')),

    # Zprávy / Podpora
    path('zpravy/', include('zpravy.urls')),

    # Přihlášení a odhlášení
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]