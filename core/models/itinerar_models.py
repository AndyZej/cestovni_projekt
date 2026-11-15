

from django.db import models
from .zeme_models import Zeme  # Můžete propojit se zemí


class Itinerar(models.Model):
    nazev = models.CharField(max_length=150, verbose_name="Název itineráře")
    zeme = models.ForeignKey(Zeme, on_delete=models.CASCADE, related_name='itinerare', verbose_name="Země")
    popis = models.TextField(verbose_name="Program / Popis")
    pocet_dni = models.PositiveIntegerField(verbose_name="Počet dní")

    class Meta:
        verbose_name = "Itinerář"
        verbose_name_plural = "Itineráře"

    def __str__(self):
        return f"{self.nazev} ({self.zeme.nazev})"