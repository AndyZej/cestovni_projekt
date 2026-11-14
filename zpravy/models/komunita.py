

from django.db import models
from django.contrib.auth.models import User
from zeme.models import Zeme

class KomunitniZprava(models.Model):
    zeme = models.ForeignKey(
        Zeme,
        on_delete=models.CASCADE,
        related_name='komunitni_zpravy'
    )
    uzivatel = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    cas_odeslani = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uzivatel.username} - {self.zeme.nazev} ({self.cas_odeslani.strftime('%d.%m.%Y %H:%M')})"