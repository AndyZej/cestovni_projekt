from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse


class Zeme(models.Model):
    nazev = models.CharField(max_length=100, verbose_name="Název země")
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text="Identifikátor v URL a pro šablonu (např. tunisko, turecko, kapverdy, egypt)",
        verbose_name="URL slug",
    )
    seznameni = models.TextField(verbose_name="Seznámení se zemí", blank=True)
    zajimavosti = models.TextField(verbose_name="Zajímavosti", blank=True)
    itinerar = models.TextField(verbose_name="Harmonogram / Itinerář", blank=True)

    hlavni_foto = models.ImageField(
        upload_to="fotky_zemi/",
        blank=True,
        null=True,
        verbose_name="Hlavní fotografie",
    )

    class Meta:
        verbose_name = "Země"
        verbose_name_plural = "Země"

    def __str__(self):
        return self.nazev

    def get_absolute_url(self):
        return reverse("detail_zeme", kwargs={"slug": self.slug})