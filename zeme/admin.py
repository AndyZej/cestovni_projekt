

from django.contrib import admin
from .models import Zeme

@admin.register(Zeme)
class ZemeAdmin(admin.ModelAdmin):
    list_display = ('nazev', 'slug')
    prepopulated_fields = {'slug': ('nazev',)}