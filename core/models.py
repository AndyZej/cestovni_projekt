

from django.db import models

class Zeme(models.Model):
    nazev = models.CharField(max_length=100, unique=True, verbose_name="Název země")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL slug")
    hlavni_foto = models.ImageField(upload_to='zeme_foto/', blank=True, null=True, verbose_name="Hlavní fotografie")
    popis = models.TextField(blank=True, verbose_name="Popis země")

    def __str__(self):
        return self.nazev
# Create your models here.
