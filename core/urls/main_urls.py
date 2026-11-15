


from core.views import domovska_stranka, kontakt, odhlaseni, prihlaseni, registrace
from django.urls import include, path  # Zde je důležitý import include a path

urlpatterns = [
    path('', domovska_stranka, name='domov'),
    path('kontakt/', kontakt, name='kontakt'),
    path('registrace/', registrace, name='registrace'),
    path('prihlaseni/', prihlaseni, name='prihlaseni'),
    path('odhlaseni/', odhlaseni, name='odhlaseni'),
    # případně další vaše URL cesty...
]
