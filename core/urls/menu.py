


from django.urls import path
from django.views.generic import TemplateView
from core.views import home_views

urlpatterns = [
    path('', home_views.domovska_stranka, name='domov'),
    # Přidaná cesta pro stránku Menu:
    path('menu/', TemplateView.as_view(template_name='core/menu.html'), name='menu'),
]