from django.db import models

# Create your zeme_views here.

from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User
from zeme.models import Zeme  # uprav název modelu, pokud se u tebe jmenuje jinak

class ZpravaAdminovi(models.Model):
    uzivatel = models.ForeignKey(User, on_delete=models.CASCADE)
    zprava = models.TextField()
    cas_odeslani = models.DateTimeField(auto_now_add=True)

class KomunitniZprava(models.Model):
    zeme = models.ForeignKey(Zeme, on_delete=models.CASCADE, related_name='komunitni_zpravy')
    uzivatel = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    cas_odeslani = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uzivatel.username} - {self.zeme.nazev}"