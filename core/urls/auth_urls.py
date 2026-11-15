


from django.urls import path
from core.views import registrace

urlpatterns = [
    path('registrace/', registrace, name='registrace'),
]