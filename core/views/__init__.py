

# core/views/__init__.py

# Načtení všech pohledů z jednotlivých modulů pomocí hvězdičky
from .admin_dashboard import *
from .auth_views import *
from .dashboard_uctu import *
from .dashboard_views import *
from .home_views import *

# Specifické importy pro jistotu a přehlednost (pokud jsou v souborech výše)
from .login_view import login_view
from .profile_views import uzivatelsky_profil_view

# Pokud máš funkci upravit_oblibene_view v samostatném souboru upravit_oblibene_view.py:
from .upravit_oblibene_view import upravit_oblibene_view