


from django.db import models
from django.contrib.auth.models import User

class UzivatelskaObdobnaCast(models.Model):
    uzivatel = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Uživatel")
    # Identifikátor nebo název vybrané části (např. 'seznam_zemi', 'seznam_itineraru', 'zpravy' atd.)
    nazev_casti = models.CharField(max_length=100, verbose_name="Název části")
    url_name = models.CharField(max_length=100, verbose_name="Django URL název")
    ikona = models.CharField(max_length=50, default="🌍", verbose_name="Ikona")
    poradi = models.PositiveIntegerField(default=1, verbose_name="Pořadí (1-4)")

    class Meta:
        ordering = ['poradi']
        verbose_name = "Oblíbená část uživatele"
        verbose_name_plural = "Oblíbené části uživatele"

    def __str__(self):
        return f"{self.uzivatel.username} - {self.nazev_casti}"