


# views/__init__.py

# Importy z modulu komunita
from .komunita import diskuze_zeme, komunita_rozcestnik

# Importy z administrátorské sekce
from zpravy.views.administrator.administrator import (
    admin_chat_dashboard_view,
    chat_admin,
)

# Import JSON API endpointu
from .json import odeslat_zpravu_api