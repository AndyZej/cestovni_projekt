

from django.contrib.auth.models import User
from django.db import models


class UzivatelskePreference(models.Model):
  # Propojení 1:1 s vestavěným Django uživatelem
  uzivatel = models.OneToOneField(
      User, on_delete=models.CASCADE, related_name='preferovane_sekce'
  )

  # Uloží seznam vybraných hodnot, např. ['seznam_zemi', 'egypt_detail', ...]
  vybrane_sekce = models.JSONField(default=list, blank=True)

  def __str__(self):
    return f'Oblíbené sekce pro: {self.uzivatel.username}'