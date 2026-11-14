



from django.urls import path, include

urlpatterns = [
    # Všechny cesty pro itineráře budou mít předponu 'itinerare/'
    path('itinerare/', include('zeme.urls.urls_itinerar')),

    # Všechny ostatní cesty spravuje urls_zeme
    path('', include('zeme.urls.urls_zeme')),
]