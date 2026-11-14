


from django.urls import path  # <--- TENTO IMPORT VÁM TAM CHYBÍ
from zpravy.views.administrator.administrator import (
    admin_chat_dashboard_view,
    chat_admin,
)

urlpatterns = [
    path('chat/', chat_admin, name='chat_admin'),
    path('admin-dashboard/', admin_chat_dashboard_view, name='admin_chat_dashboard'),
]