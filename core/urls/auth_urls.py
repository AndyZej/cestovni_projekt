


from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    # ... vaše ostatní URL ...
    path('zmena-hesla/', auth_views.PasswordChangeView.as_view(template_name='core/password_change.html'), name='password_change'),
    path('zmena-hesla/hotovo/', auth_views.PasswordChangeDoneView.as_view(template_name='core/password_change_done.html'), name='password_change_done'),
]