from django.db import models

# Create your zeme_views here.

from django.db import models
from django.contrib.auth.models import User

class ZpravaAdminovi(models.Model):
    uzivatel = models.ForeignKey(User, on_delete=models.CASCADE)
    zprava = models.TextField()
    cas_odeslani = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Zpráva od {self.uzivatel.username} ({self.cas_odeslani})"
