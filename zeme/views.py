
from django.shortcuts import render
from django.http import Http404
from .models import Zeme

# Centrální slovník pro galerie jednotlivých zemí
STRUKTURA_CEST = {
    'egypt': {'nazev': 'Egypt'},
    'kapverdy': {'nazev': 'Kapverdy'},
    'tunisko': {'nazev': 'Tunisko'},
    'turecko': {'nazev': 'Turecko'},
}

def domovsky_view(request):
    """Úvodní domovská stránka"""
    return render(request, 'zeme/domovsky.html')

def galerie_view(request):
    """Stránka hlavní fotogalerie"""
    return render(request, 'zeme/galerie.html')

def seznam_zemi_view(request):
    """Seznam všech zemí z databáze"""
    zemes = Zeme.objects.all()
    return render(request, 'zeme/seznam_zemi.html', {'zemes': zemes})

def detail_zeme_view(request, slug):
    """Dynamicky otevře HTML šablonu země podle slugu"""
    template_map = {
        'turecko': 'zeme/turecko.html',
        'kapverdy': 'zeme/Kapverdy.html',
        'tunisko': 'zeme/tunisko.html',
        'egypt': 'zeme/egypt.html',
    }

    template_name = template_map.get(slug)
    if not template_name:
        raise Http404("Země nebyla nalezena")

    return render(request, template_name)

def seznam_itineraru_view(request):
    """Stránka se seznamem itinerářů s ručně definovanými kartami"""
    itinerare = [
        {'nazev': 'Turecko', 'slug': 'turecko'},
        {'nazev': 'Kapverdy', 'slug': 'kapverdy'},
        {'nazev': 'Tunisko', 'slug': 'tunisko'},
        {'nazev': 'Egypt', 'slug': 'egypt'},
    ]
    return render(request, 'itinerar/domovsky.html', {'itinerare': itinerare})

def detail_itineraru_view(request, slug):
    """Dynamicky otevře HTML šablonu pro itinerář podle slugu"""
    template_map = {
        'turecko': 'itinerar/turecko.html',
        'kapverdy': 'itinerar/Kapverdy.html',
        'tunisko': 'itinerar/tunisko.html',
        'egypt': 'itinerar/egypt.html',
    }

    template_name = template_map.get(slug)
    if not template_name:
        raise Http404("Itinerář nebyl nalezen")

    return render(request, template_name)

def galerie_zeme(request, slug):
    """Dynamická fotogalerie pro konkrétní zemi (načítá šablony z templates/zeme/galerie/)"""
    zeme_data = STRUKTURA_CEST.get(slug)
    if not zeme_data:
        raise Http404("Galerie neexistuje")

    # Cesta k šabloně odpovídající umístění v templates/zeme/galerie/[slug].html
    template_name = f"zeme/galerie/{slug}.html"
    return render(request, template_name, {'zvolena_zeme': zeme_data})