


from core.views import login_view
from django.urls import path

urlpatterns = [
    # URL pro přihlašovací stránku
    path('prihlaseni/', login_view, name='login'),
]