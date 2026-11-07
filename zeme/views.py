from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template
from django.template import TemplateDoesNotExist
from .models import Zeme


def vyber_zeme(request):
    """Zobrazí seznam všech dostupných zemí z databáze[cite: 1]."""
    vsechny_zeme = Zeme.objects.all()
    return render(request, 'zeme/vyber_zeme.html', {'vsechny_zeme': vsechny_zeme})


def detail_zeme(request, slug):
    """
    Vyhledá zemi podle slugu a dynamicky přiřadí její vlastní šablonu
    (např. tunisko.html, egypt.html atd.) ze složky zeme/zemes/.
    """
    zvolena_zeme = get_object_or_404(Zeme, slug=slug)

    # Sestavení cesty ke specifické šabloně na základě slugu země
    specificka_sablona = f'zeme/zemes/{zvolena_zeme.slug}.html'

    try:
        # Ověření, zda soubor šablony pro danou zemi fyzicky existuje
        get_template(specificka_sablona)
        sablona_k_pouziti = specificka_sablona
    except TemplateDoesNotExist:
        # Pokud šablona neexistuje, použije se univerzální výchozí šablona itineráře
        sablona_k_pouziti = 'zeme/itinerar.html'

    return render(request, sablona_k_pouziti, {'zvolena_zeme': zvolena_zeme})