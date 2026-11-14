


from django.urls import path, include

urlpatterns = [
    path('', include('zpravy.urls.komunita')),
    path('', include('zpravy.urls.administrator')),
]