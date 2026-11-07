from django.db import models

# Create your models here.

from django.db import models

class Zeme(models.Model):
    nazev = models.CharField(max_length=100)
    popis = models.TextField()
    itinerar = models.TextField()

    def __str__(self):
        return self.nazev
