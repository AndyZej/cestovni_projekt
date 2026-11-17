
# core/models/oblibene_models.py
from django.contrib.auth.models import User
from django.db import models


class UserFavoriteSection(models.Model):
  user = models.ForeignKey(
      User,
      on_delete=models.CASCADE,
      related_name='favorite_sections',
      verbose_name='Uživatel',
  )
  section_key = models.CharField(
      max_length=100, unique=False, verbose_name='Klíč sekce'
  )
  title = models.CharField(
      max_length=200, blank=True, verbose_name='Nadpis části'
  )
  url_name = models.CharField(
      max_length=100, blank=True, null=True, verbose_name='Django URL název'
  )
  ikona = models.CharField(max_length=50, default='🌍', verbose_name='Ikona')
  poradi = models.PositiveIntegerField(default=1, verbose_name='Pořadí (1-4)')

  class Meta:
    ordering = ['poradi']
    unique_together = ('user', 'section_key')
    verbose_name = 'Oblíbená část uživatele'
    verbose_name_plural = 'Oblíbené části uživatele'

  def __str__(self):
    return (
        f'{self.user.username} -> {self.title or self.section_key} (Pozice:'
        f' {self.poradi})'
    )