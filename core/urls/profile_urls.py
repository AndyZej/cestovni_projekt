


from core.views import uzivatelsky_profil_view
from django.urls import path

urlpatterns = [
    # URL pro uživatelský profil (kam se uživatel dostane po přihlášení)
    path('', uzivatelsky_profil_view, name='uzivatelsky_profil'),
]