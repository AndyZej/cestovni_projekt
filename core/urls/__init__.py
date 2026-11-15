

# core/urls/__init__.py

from .auth_urls import urlpatterns as auth_patterns
from .login_urls import urlpatterns as login_patterns
from .main_urls import urlpatterns as main_patterns
from .profile_urls import urlpatterns as profile_patterns
from .menu import urlpatterns as menu_patterns  # <-- Přidáno načtení menu

# Zde sesbíráme všechny URL patterny dohromady
urlpatterns = []
urlpatterns += main_patterns
urlpatterns += login_patterns
urlpatterns += profile_patterns
urlpatterns += auth_patterns
urlpatterns += menu_patterns